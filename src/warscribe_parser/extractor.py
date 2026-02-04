"""Transcript extractor stub for WARScribe-Parser."""

from typing import Optional, BinaryIO, Union
from pathlib import Path

from warscribe_parser.models import ExtractionResult, SourceType


class TranscriptExtractor:
    """
    Extracts game transcripts from various sources.
    
    Stub implementation for v0.1.0 foundation.
    """
    
    def __init__(self, model: str = "default") -> None:
        """Initialize extractor with ML model."""
        self.model = model
    
    async def extract_from_image(
        self,
        image: Union[Path, BinaryIO],
    ) -> ExtractionResult:
        """Extract transcript from an image."""
        return ExtractionResult(
            source_type=SourceType.IMAGE,
            source_path=str(image) if isinstance(image, Path) else "stream",
            overall_confidence=0.0,
            warnings=["Stub implementation - no actual extraction"]
        )
    
    async def extract_from_pdf(
        self,
        pdf: Union[Path, BinaryIO],
    ) -> ExtractionResult:
        """Extract transcript from a PDF."""
        return ExtractionResult(
            source_type=SourceType.PDF,
            source_path=str(pdf) if isinstance(pdf, Path) else "stream",
            overall_confidence=0.0,
            warnings=["Stub implementation - no actual extraction"]
        )
