"""Abstract class that all scrapers must inherit and implement"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


class AbstractScraperClass(ABC):
    """All scraper must inherit and implement this class to be detected"""

    @abstractmethod
    def __init__(self, url: str) -> None:
        """Regular initialization method"""

    @classmethod
    @abstractmethod
    def is_valid_show_url(cls, show_url: str) -> bool:
        """Check if a URL is a valid show URL for a specific scraper"""

    @abstractmethod
    def update(
        self, minimum_info_timestamp: Optional[datetime] = None, minimum_modified_timestamp: Optional[datetime] = None
    ) -> None:
        """Update the information for a show"""