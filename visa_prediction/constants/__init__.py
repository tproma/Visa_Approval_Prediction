import os
from datetime import date

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "mongodb+srv://tproma2:tproma2@cluster0.rpadq8d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


PIPELINE_NAME:str = "visa_prediction"
ARTIFACT_DIR:str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "us_visa.csv"
TRAIN_FILE_NAME :str = "train.csv"
TEST_FILE_NAME : str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")

"""
Data Ingestion Related Constants 
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR :str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

