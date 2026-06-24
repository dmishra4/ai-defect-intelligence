import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


def fetch_issues_from_jira():

    url = f"{JIRA_URL}/rest/api/3/search/jql"

    headers = {
        "Accept": "application/json"
    }

    auth = HTTPBasicAuth(
        JIRA_EMAIL,
        JIRA_API_TOKEN
    )

    query = {
    "jql": """
        project = SCRUM
        AND issuetype = Bug
        AND resolution = Unresolved
        ORDER BY priority DESC
    """,
    "fields": "summary,description,priority,status"
   }

    response = requests.get(
    url,
    headers=headers,
    params=query,
    auth=auth
    )
    # print("EMAIL =", repr(JIRA_EMAIL))
    # print("TOKEN LENGTH =", len(JIRA_API_TOKEN))
    # print("Status:", response.status_code)
    # print("Headers:", response.headers)
    # print("Body:", repr(response.text))

    return response

def adf_to_text(node):
    """Flatten an Atlassian Document Format field into plain text."""
    if not node:
        return ""

    node_type = node.get("type")

    if node_type == "text":
        return node.get("text", "")

    if node_type == "hardBreak":
        return "\n"

    children_text = "".join(adf_to_text(child) for child in node.get("content", []))

    if node_type == "paragraph":
        return children_text + "\n"

    return children_text


def extract_issues(data):

    issues = []

    for issue in data["issues"]:
        fields = issue["fields"]
        priority = fields.get("priority")
        status = fields.get("status")
        resolution = fields.get("resolution")

        issues.append({
           "key": issue["key"],
            "summary": fields.get("summary"),
             "priority": priority["name"] if priority else None,
             "status": status["name"] if status else None,
             "resolution": resolution["name"] if resolution else "Unresolved",
             "description": adf_to_text(fields.get("description")).strip()
        })

    return issues

def get_all_issues() -> list:
    response = fetch_issues_from_jira().json()
    return extract_issues(response)

def get_release_statistics():

    issues = get_all_issues()

    stats = {
        "total_open": len(issues),
        "highest": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }

    for issue in issues:

        priority = issue["priority"]

        if priority == "Highest":
            stats["highest"] += 1

        elif priority == "High":
            stats["high"] += 1

        elif priority == "Medium":
            stats["medium"] += 1

        elif priority == "Low":
            stats["low"] += 1

    return stats

#print("get_release_statistics :", get_release_statistics())

if __name__ == "__main__":

    issues = get_all_issues()

    for issue in issues:
        pprint(issue)