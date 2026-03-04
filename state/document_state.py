from dataclasses import dataclass, field
from typing import Dict, Any
import uuid

@dataclass
class DocumentState:
    document_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: str = ""
    intent: str = ""
    confidence: float = 0.0
    result: Dict[str, Any] = field(default_factory=dict)
    status: str = "STARTED"
    logs: list = field(default_factory=list)
    retries: int = 0