# GitHub QA Agent

FastAPI + Gemini powered GitHub commit analysis tool.

AI-powered GitHub commit analyzer that automatically reviews the latest code changes in a repository and generates QA-focused test recommendations.

## Features

* Fetches the latest commit from a GitHub repository
* Retrieves commit-level code changes and file diffs
* Uses Google Gemini to analyze code changes
* Generates:

  * Feature summary
  * Change type
  * Risk level
  * Impacted modules
  * Recommended test areas
  * Recommended test types

## Live Demo

https://github-qa-agent-production.up.railway.app/docs

## Tech Stack

- Python 3.12
- FastAPI
- Google Gemini 2.5 Flash
- GitHub REST API
- Railway

## Run Locally

pip install -r requirements.txt

uvicorn app.main:app --reload

## Project Structure

github-qa-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── agent.py
│
├── .gitignore
├── requirements.txt
└── README.md

## Installation

Clone the repository:

git clone https://github.com/<your-username>/github-qa-agent.git

cd github-qa-agent

Create and activate a virtual environment:

Windows:

python -m venv .venv

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Environment Variables

Create a `.env` file:

GOOGLE_API_KEY=your_google_api_key

Optional:

GITHUB_TOKEN=your_github_token

## Run Locally

python -m uvicorn app.main:app --reload --port 8001

Open Swagger UI:

http://localhost:8001/docs

## API Endpoint

POST /analyze

Parameters:

* owner (GitHub repository owner)
* repo (GitHub repository name)

Example:

/analyze?owner=dmishra4&repo=AI-Lab

## Sample Response

{
"feature": "GitHub Commit Diff Fetcher for AI Processing",
"change_type": "new_feature",
"risk_level": "medium",
"impacted_modules": [
"GitHub API Integration",
"Google Gemini API Integration"
],
"test_areas": [
"API validation",
"Error handling"
],
"recommended_test_types": [
"Functional Testing",
"Integration Testing"
]
}

## Future Enhancements

* Analyze pull requests
* Multi-commit analysis
* Jira integration
* Slack notifications
* Test case generation
* CI/CD integration

## License

For learning and demonstration purposes.
