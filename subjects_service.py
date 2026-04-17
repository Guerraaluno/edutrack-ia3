import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

BASE_URL = os.getenv("XANO_BASE_URL", "").rstrip("/")
FALLBACK_FILE = Path(__file__).parent / "subjects_data.json"


def _read_fallback() -> List[Dict[str, Any]]:
    if not FALLBACK_FILE.exists():
        FALLBACK_FILE.write_text("[]", encoding="utf-8")
        return []
    return json.loads(FALLBACK_FILE.read_text(encoding="utf-8"))


def _write_fallback(subjects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    FALLBACK_FILE.write_text(
        json.dumps(subjects, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return subjects


def _api_url(path: str) -> str:
    return f"{BASE_URL.rstrip('/')}/{path.lstrip('/')}"


def _request(method: str, path: str, json_body: Optional[Dict[str, Any]] = None) -> Any:
    url = _api_url(path)
    response = requests.request(method, url, json=json_body, timeout=10)
    response.raise_for_status()
    return response.json()


def get_subjects() -> List[Dict[str, Any]]:
    if BASE_URL:
        try:
            return _request("GET", "subjects")
        except Exception:
            pass
    return _read_fallback()


def create_subject(name: str, description: str = "", active: bool = True) -> Dict[str, Any]:
    if BASE_URL:
        try:
            payload = {
                "name": name,
                "description": description or None,
                "active": active,
            }
            return _request("POST", "subjects", payload)
        except Exception:
            pass

    subjects = _read_fallback()
    next_id = max((s.get("id", 0) for s in subjects), default=0) + 1
    subject = {
        "id": next_id,
        "name": name,
        "description": description,
        "active": active,
    }
    subjects.append(subject)
    _write_fallback(subjects)
    return subject


def update_subject(subject_id: int, name: str, description: str = "", active: bool = True) -> Dict[str, Any]:
    if BASE_URL:
        try:
            payload = {
                "id": subject_id,
                "name": name,
                "description": description or None,
                "active": active,
            }
            return _request("PATCH", "subjects", payload)
        except Exception:
            pass

    subjects = _read_fallback()
    for subject in subjects:
        if subject.get("id") == subject_id:
            subject["name"] = name
            subject["description"] = description
            subject["active"] = active
            _write_fallback(subjects)
            return subject

    raise ValueError("Subject not found")


def delete_subject(subject_id: int) -> bool:
    if BASE_URL:
        try:
            _request("DELETE", "subjects", {"id": subject_id})
            return True
        except Exception:
            pass

    subjects = _read_fallback()
    new_subjects = [s for s in subjects if s.get("id") != subject_id]
    if len(new_subjects) == len(subjects):
        return False
    _write_fallback(new_subjects)
    return True
