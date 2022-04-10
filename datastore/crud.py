from sqlalchemy.orm import Session
from sqlalchemy import func
from . import schemas
from .models import PerformanceMetrics as Metrics


def get_performance_metrics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Metrics).offset(skip).limit(limit).all()


def dynamic_filters(criterias):
    filters = []
    for criteria in criterias:
        column = getattr(Metrics, criteria.column, None)
        if not column:
            raise Exception(f'Invalid select column:{criteria.column}')
        if criteria.operator not in [x.value for x in schemas.Operator]:
            raise Exception(f'Invalid operation:{criteria.operator}')
        if not (isinstance(criteria.values, list) and len(criteria.values)):
            raise Exception(f'Invalid values:{criteria.values}')
        if criteria.operator.lower() == schemas.Operator.GT:
            filters.append(column > max(criteria.values))
        elif criteria.operator.lower() == schemas.Operator.LT:
            filters.append(column < min(criteria.values))
        elif criteria.operator.lower() == schemas.Operator.EQ:
            filters.append(column == criteria.values[0])
        elif criteria.operator.lower() == schemas.Operator.BETWEEN:
            filters.append(column.between(criteria.values[0], criteria.values[1]))
        else:
            raise Exception(f'Invalid filter')
    return filters


def dynamic_select(displays):
    columns = []
    for display in displays:
        column = getattr(Metrics, display.column, None)
        if display.operation and display.operation.lower() in [x.value for x in schemas.Operations]:
            op = func.sum if display.operation.lower() == schemas.Operations.SUM else func.count
            column = op(column)
            if display.label:
                column = column.label(display.label)
        columns.append(column)
    return columns


def dynamic_disposition(dynamic_query, disposition):
    if disposition.group_by_columns:
        group_columns = []
        for group_on_column in disposition.group_by_columns:
            column = getattr(Metrics, group_on_column, None)
            group_columns.append(column)
        dynamic_query = dynamic_query.group_by(*group_columns)
    if disposition.sort_on_column:
        sort_column = getattr(Metrics, disposition.sort_on_column, None)
        if disposition.order == schemas.SortOrder.ASC:
            dynamic_query = dynamic_query.order_by(sort_column.asc())
        else:
            dynamic_query = dynamic_query.order_by(sort_column.desc())
    if disposition.limit:
        limit = disposition.limit
        start = disposition.start
        dynamic_query = dynamic_query[start:limit]
    else:
        dynamic_query = dynamic_query.all()
    return dynamic_query


def query_use_case_1(db: Session):
    select_columns = [Metrics.channel, Metrics.country, func.sum(Metrics.impressions).label('impressions'),
                      func.sum(Metrics.clicks).label('clicks')]
    return db.query(*select_columns) \
        .filter(Metrics.date < '2017-056-01') \
        .group_by(Metrics.channel, Metrics.country).order_by(Metrics.clicks.desc())[0:5]


def dynamic_query_performance_metrics(db: Session, query: schemas.QueryModel):
    select_columns = dynamic_select(query.display_columns)
    dynamic_query = db.query(*select_columns)
    if query.filter:
        filters = dynamic_filters(query.filter)
        dynamic_query = dynamic_query.filter(*filters)
    if query.disposition:
        dynamic_query = dynamic_disposition(dynamic_query, query.disposition)

    return dynamic_query
