import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from fastapi.testclient import TestClient
from apps.api.main import app

def sample_payload():
    return {
        "resume_profile_id": "R123",
        "evidence_vault": [
            {"id": "E001", "text": "Built dashboards", "skills": ["SQL"], "year": 2024}
        ],
        "job": {
            "source": "Greenhouse",
            "company": "Acme",
            "title": "Data Analyst",
            "jd_html": "<div>SQL</div>"
        },
        "user_profile": {
            "work_auth": "CA_PR",
            "location": "Vancouver",
            "relocate": True,
            "notice_period": "2w"
        }
    }

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_jtr():
    resp = client.post("/jtr", json=sample_payload())
    assert resp.status_code == 200
    data = resp.json()
    assert "match_score" in data
    assert data["tailored_resume"]["docx_url"]

def test_plan():
    resp = client.post("/plan", json=[{"name": "name", "selector": "#name"}])
    assert resp.status_code == 200
    assert resp.json()["action_plan"]
