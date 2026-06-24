# AI Defect Intelligence Agent

🚀 AI-powered Defect Intelligence Agent that integrates with Jira, analyzes production defects, identifies probable root causes, recommends test coverage, and predicts release risk using Google Gemini and FastAPI.

---

## Features

### Defect Analysis

* Fetches open defects directly from Jira
* Analyzes defect summaries and descriptions
* Identifies probable root causes
* Classifies defect severity
* Generates QA-focused testing recommendations

### Release Risk Assessment

* Calculates release risk based on open defects
* Evaluates defect priorities and volume
* Generates risk score (0-100)
* Provides Go / No-Go recommendation
* Suggests actionable release recommendations

### AI-Powered Insights

* Google Gemini 2.5 Flash Integration
* Intelligent defect analysis
* Root cause prediction
* Release decision support

---

## Architecture

Jira → FastAPI → Gemini AI → Defect Intelligence API

---

## Tech Stack

* Python 3.12
* FastAPI
* Google Gemini 2.5 Flash
* Jira REST API
* LangChain
* AWS EC2
* Systemd

---

## Project Structure

ai-defect-intelligence/

├── app/

│   ├── **init**.py

│   ├── main.py

│   ├── jira_client.py

│   └── agent.py

├── .env

├── .gitignore

├── requirements.txt

└── README.md

---

## Installation

Clone Repository

git clone https://github.com/dmishra4/ai-defect-intelligence.git

cd ai-defect-intelligence

Create Virtual Environment

python3 -m venv venv

source venv/bin/activate

Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file:

GOOGLE_API_KEY=your_google_api_key

JIRA_URL=https://your-domain.atlassian.net

JIRA_EMAIL=[your_email@example.com](mailto:your_email@example.com)

JIRA_API_TOKEN=your_jira_api_token

---

## Run Locally

uvicorn app.main:app --reload --port 8002

Open Swagger UI:

http://localhost:8002/docs

---

## API Endpoints

### Home

GET /

Response:

{
"message": "AI Defect Intelligence Running"
}

### Get All Open Issues

GET /issues

### Analyze Defect

GET /analyze/{issue_key}

Example:

/analyze/SCRUM-5

### Release Risk Assessment

GET /release-risk

---

## Sample Release Risk Response

{
"release_risk": "High",
"go_no_go": "No Go",
"risk_score": 82,
"reasons": [
"Multiple Highest priority defects remain unresolved"
],
"recommendations": [
"Resolve Highest priority defects before release"
]
}

---

## AWS EC2 Deployment

Install Dependencies

sudo apt update

sudo apt install python3-pip python3-venv git -y

Clone Repository

git clone https://github.com/dmishra4/ai-defect-intelligence.git

cd ai-defect-intelligence

Create Virtual Environment

python3 -m venv venv

source venv/bin/activate

Install Requirements

pip install -r requirements.txt

Create Environment File

nano .env

Run Application

uvicorn app.main:app --host 0.0.0.0 --port 8000

Access Swagger

http://<EC2-IP>:8000/docs

---

## Future Enhancements

* Historical defect trend analysis
* AI-based defect clustering
* Automated root cause categorization
* Release quality dashboard
* Slack integration
* Microsoft Teams integration
* Predictive defect leakage analysis

---

## Author

Deepak Kumar

Associate Director |  UBS



---

## License

For learning, demonstration, and portfolio purposes.
