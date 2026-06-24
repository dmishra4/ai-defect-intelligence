import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from app.jira_client import get_all_issues
import json

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def analyze_defect(issue_key):

    issues = get_all_issues()

    issue = next(
        (i for i in issues if i["key"] == issue_key),
        None
    )

    if not issue:
        return {
            "error": "Issue not found"
        }

    prompt = f"""
    You are a Senior QA Architect.

    Analyze the defect.

    Summary:
    {issue['summary']}

    Description:
    {issue['description']}

    Return JSON only.

    {{
        "severity":"",
        "root_cause":"",
        "recommended_tests":[]
    }}
    """

    response = llm.invoke(prompt)

    clean_text = (
    response.content
    .replace("```json", "")
    .replace("```", "")
    .strip()
  )
    print("RAW RESPONSE:")
    print(response.content)
    print("CLEAN RESPONSE:")
    print(clean_text)

    return json.loads(clean_text)


def analyze_release_risk(stats, issues):

    prompt = f"""
    You are a Senior QA Release Manager.

    Analyze the release risk based on open defects.

    Open Defect Statistics:

    {stats}

    Open Defects:

    {issues}

    Return JSON only.


     Rules:

    1. release_risk must be one of:
    - Low
    - Medium
    - High
    - Critical

    2. go_no_go must be one of:
     - Go
     - No Go

     3. risk_score must be between 0 and 100.

     4. reasons must contain business-focused explanations.

     5. recommendations must contain actionable next steps.

     Return JSON in the following format:

    {{
    "release_risk": "Low | Medium | High | Critical",
    "go_no_go": "Go | No Go",
    "risk_score": 0,
    "reasons": [],
    "recommendations": []
     }}
    """
    print("Calling Gemini...")
    response = llm.invoke(prompt)
    print("Gemini Response Received")


    clean_text = (
        response.content
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    print("RAW RESPONSE:")
    print(response.content)

    print("CLEAN RESPONSE:")
    print(clean_text)
    try:
        return json.loads(clean_text)

    except Exception as e:
        print("JSON ERROR:", e)
        print("RAW RESPONSE:", clean_text)
        return {
        "error": str(e),
        "raw_response": clean_text
        }