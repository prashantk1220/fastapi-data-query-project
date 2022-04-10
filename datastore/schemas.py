from typing import Optional, List
from datetime import date
from pydantic import BaseModel
from .field_types import MetricsFields, Operator, Operations, SortOrder, OperatingSystem


class SelectColumns(BaseModel):
    column: MetricsFields
    operation: Optional[Operations] = None
    label: Optional[str] = None


class FilterCrtieria(BaseModel):
    column: MetricsFields
    operator: Operator
    values: List


class Disposition(BaseModel):
    start: Optional[int] = 0
    limit: Optional[int] = None
    group_by_columns: Optional[List[MetricsFields]] = None
    sort_on_column: Optional[MetricsFields] = None
    order: Optional[SortOrder] = SortOrder.ASC


class QueryModel(BaseModel):
    display_columns: List[SelectColumns]
    filter: Optional[List[FilterCrtieria]] = None
    disposition: Optional[Disposition] = None


class PerformanceMetrics(BaseModel):
    id: int
    date: date
    channel: str
    country: str
    os: OperatingSystem
    impressions: int
    clicks: int
    installs: int
    spend: float
    revenue: float

    class Config:
        orm_mode = True
