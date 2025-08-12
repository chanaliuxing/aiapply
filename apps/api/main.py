from typing import Dict, Any, List
from fastapi import FastAPI

app = FastAPI(title="apply-copilot API")

@app.get("/health")
def health() -> Dict[str, str]:
    """Simple health check used by tests and CI."""
    return {"status": "ok"}

@app.post("/jtr")
def jtr(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Rule based JTR mock implementation returning placeholder data."""
    return {
        "match_score": 100,
        "must_have_coverage": {"SQL": True},
        "tailored_resume": {
            "docx_url": "/artifacts/resume.docx",
            "pdf_url": "/artifacts/resume.pdf",
            "ats_checks": ["text_ok"],
        },
        "qa_bundle": [
            {
                "q": "Why are you a good fit?",
                "a": "Because",
                "meta": {"evidence_ids": [], "rs_basis": "mock"},
            }
        ],
        "diff_report": [
            {"before": "", "after": "", "reason": "ATS_term_align", "risk_level": "low"}
        ],
        "action_plan": [
            {"selector": "#name", "mode": "dom", "value": "John Doe", "required": True}
        ],
    }

@app.post("/plan")
def plan(fields: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Return trivial action plan for provided fields."""
    steps = [
        {"selector": f.get("selector"), "mode": "dom", "value": "test", "required": True}
        for f in fields
    ]
    return {"action_plan": steps}
