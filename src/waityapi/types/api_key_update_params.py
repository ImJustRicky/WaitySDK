# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIKeyUpdateParams"]


class APIKeyUpdateParams(TypedDict, total=False):
    company_id: Required[Annotated[str, PropertyInfo(alias="companyId")]]

    is_active: bool

    name: str

    rate_limit: int
