from enum import Enum


class OperatingSystem(str, Enum):
    ios = "ios"
    android = "android"


class ColumnType(str, Enum):
    date = "date"
    text = "text"


class MetricsFields(str, Enum):
    date = "date"
    channel = "channel"
    country = "country"
    os = "os"
    impressions = "impressions"
    clicks = "clicks"
    installs = "installs"
    spend = "spend"
    revenue = "revenue"
    cpi = "cpi"


class Operator(str, Enum):
    EQ = "eq"
    GT = "gt"
    LT = "lt"
    LIKE = "like"
    BETWEEN = "between"


class Operations(str, Enum):
    SUM = "sum"
    COUNT = "count"


class SortOrder(str, Enum):
    ASC = "asc"
    DSC = "desc"


