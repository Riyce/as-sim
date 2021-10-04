from dataclasses import dataclass
from typing import List


@dataclass
class ExtractRequest:
    id: str
    similar_clp: str
    similar_cnt: int
    country: str = 'US'


@dataclass
class ExtractResponse:
    id: str
    similar_apps: List[str]
