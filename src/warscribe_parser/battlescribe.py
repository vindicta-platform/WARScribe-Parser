"""
BattleScribe XML parser interface for WARScribe-Parser.

Defines the interface for parsing .ros and .rosz files per Issue #2.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class UnitSelection:
    """A unit selection from BattleScribe."""
    name: str
    points: int
    quantity: int = 1
    wargear: list[str] = field(default_factory=list)
    abilities: list[str] = field(default_factory=list)


@dataclass
class RosterData:
    """Parsed roster data from BattleScribe file."""
    roster_name: str
    faction: str
    total_points: int
    units: list[UnitSelection] = field(default_factory=list)
    detachment: Optional[str] = None


class BattleScribeParser(ABC):
    """Abstract interface for BattleScribe XML parsing."""
    
    @abstractmethod
    def parse_file(self, file_path: str) -> RosterData:
        """Parse a .ros or .rosz file."""
        pass
    
    @abstractmethod
    def parse_xml(self, xml_content: str) -> RosterData:
        """Parse XML content directly."""
        pass
    
    @abstractmethod
    def extract_units(self, xml_content: str) -> list[UnitSelection]:
        """Extract unit selections from XML."""
        pass
