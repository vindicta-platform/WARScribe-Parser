"""Models for WARScribe-Parser."""

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class SourceType(str, Enum):
    """Source types for extraction."""
    IMAGE = "image"
    PDF = "pdf"
    VIDEO = "video"
    TEXT = "text"


class ParsedAction(BaseModel):
    """A parsed action from source material."""
    
    id: UUID = Field(default_factory=uuid4)
    action_type: str
    actor_name: str
    target_name: Optional[str] = None
    
    # Raw extraction
    raw_text: str = ""
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)
    
    # Position in source
    page: Optional[int] = None
    timestamp_seconds: Optional[float] = None


class ExtractionResult(BaseModel):
    """Result of transcript extraction."""
    
    id: UUID = Field(default_factory=uuid4)
    source_type: SourceType
    source_path: str
    
    # Extracted data
    actions: list[ParsedAction] = Field(default_factory=list)
    
    # Quality metrics
    overall_confidence: float = Field(ge=0.0, le=1.0, default=0.0)
    warnings: list[str] = Field(default_factory=list)
    
    # Timing
    extracted_at: datetime = Field(default_factory=datetime.utcnow)
    processing_time_ms: int = 0
