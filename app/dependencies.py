import pandas as pd
from datastore import models
from datastore.database import engine, SessionLocal
from definitions import DATASET_FILE_PATH

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def insert_data():
    df = pd.read_csv(DATASET_FILE_PATH)
    df['date'] = pd.to_datetime(df['date'])
    df['os'] = pd.Categorical(df['os'])
    session = next(get_db())
    session.bulk_insert_mappings(models.PerformanceMetrics, df.to_dict(orient="records"))
    session.commit()
    session.close()
