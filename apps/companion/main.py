from typing import Dict, Any
from fastapi import FastAPI

app = FastAPI(title="apply-copilot companion")

@app.get("/health")
def health() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "ok"}

@app.post("/click")
def click(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Placeholder click implementation"""
    return {"status": "ok", "rect": payload.get("rect")}

@app.post("/type")
def type_text(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Placeholder type implementation"""
    return {"status": "ok", "text": payload.get("text")}

@app.post("/screenshot")
def screenshot(_: Dict[str, Any] | None = None) -> Dict[str, str]:
    """Return an empty base64 image string"""
    return {"image": ""}
