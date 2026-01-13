# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["APIKeyCreateParams"]


class APIKeyCreateParams(TypedDict, total=False):
    name: Required[str]

    scopes: Required[List[Literal["stores:read", "wait_times:read", "queues:read"]]]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional"""

    rate_limit: int
    """Optional; requests per minute"""

    team_ids: SequenceNotStr[str]
    """Optional; restrict key to specific stores"""
