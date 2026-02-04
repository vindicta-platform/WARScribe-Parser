"""Unit tests for WARScribe-Parser."""

import pytest
from warscribe_parser.models import ParsedAction, ExtractionResult, SourceType


class TestParsedAction:
    def test_action_creation(self):
        action = ParsedAction(action_type="move", actor_name="Squad A", raw_text="moves 6\"")
        assert action.action_type == "move"


class TestExtractionResult:
    def test_result_creation(self):
        result = ExtractionResult(source_type=SourceType.IMAGE, source_path="test.jpg")
        assert result.source_type == SourceType.IMAGE
