# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["APIKey"]


class APIKey(BaseModel):
    id: str

    created_at: datetime

    is_active: bool

    key_prefix: str

    name: str

    rate_limit: int

    scopes: List[Literal["stores:read", "wait_times:read", "queues:read"]]

    expires_at: Optional[datetime] = None

    team_ids: Optional[List[str]] = None
