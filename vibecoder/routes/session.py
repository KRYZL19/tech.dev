from fastapi import APIRouter, HTTPException
from models.schemas import (
    SessionStart, SessionStartResponse,
    SessionResume, SessionResumeResponse,
    SessionSummaryResponse
)
import uuid
from datetime import datetime
from typing import Dict

router = APIRouter(prefix="/api/v1/session", tags=["session"])

# In-memory session store (use Redis/DB in production)
sessions: Dict = {}


@router.post("/start", response_model=SessionStartResponse)
async def start_session(data: SessionStart):
    session_id = str(uuid.uuid4())
    
    files_summary = ", ".join(data.files) if data.files else "No files"
    context_summary = (
        f"Task: {data.task}\n"
        f"Language: {data.language}\n"
        f"Framework: {data.framework or 'None'}\n"
        f"Files: {files_summary}\n"
        f"Started: {datetime.utcnow().isoformat()}"
    )
    
    sessions[session_id] = {
        "task": data.task,
        "language": data.language,
        "framework": data.framework,
        "files": data.files,
        "context": context_summary,
        "history": [],
        "created_at": datetime.utcnow().isoformat(),
    }
    
    return SessionStartResponse(
        session_id=session_id,
        context_summary=context_summary
    )


@router.post("/resume", response_model=SessionResumeResponse)
async def resume_session(data: SessionResume):
    if data.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[data.session_id]
    session["history"].append(data.new_message)
    
    # Build context window
    context_window = "\n".join(session["history"])
    
    # Injected context from session
    injected_context = (
        f"Previous work: {session['context']}\n"
        f"History ({len(session['history'])} messages):\n{context_window}"
    )
    
    # Simple next step logic
    next_step = f"Continue working on: {session['task']}"
    
    return SessionResumeResponse(
        context_window=context_window,
        injected_context=injected_context,
        next_step=next_step
    )


@router.post("/summary", response_model=SessionSummaryResponse)
async def get_summary(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    
    what_was_built = session.get("task", "Project")
    key_files = session.get("files", [])
    next_steps = [
        "Review and test changes",
        "Add documentation",
        "Run linting/formatting",
    ]
    
    return SessionSummaryResponse(
        what_was_built=what_was_built,
        key_files=key_files,
        next_steps=next_steps
    )
