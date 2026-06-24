from fastapi import FastAPI
from app.jira_client import (
    get_all_issues,
    get_release_statistics
)

from app.agent import (
    analyze_defect,
    analyze_release_risk
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Defect Intelligence Running"
    }


@app.get("/issues")
def issues():

    return get_all_issues()


@app.get("/analyze/{issue_key}")
def analyze(issue_key: str):

    return analyze_defect(issue_key)

@app.get("/release-risk")
def release_risk():

    stats = get_release_statistics()

    issues = get_all_issues()

    return analyze_release_risk(
        stats,
        issues
    )

# @app.get("/release-risk")
# def release_risk():

#     try:
#         print("STEP 1")

#         stats = get_release_statistics()

#         print("STEP 2")

#         issues = get_all_issues()

#         print("STEP 3")

#         result = analyze_release_risk(
#             stats,
#             issues
#         )

#         print("STEP 4")

#         return result

#     except Exception as e:

#         print("ERROR OCCURRED:")
#         print(type(e))
#         print(str(e))

#         return {
#             "error": str(e)
#         }