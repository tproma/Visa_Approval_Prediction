import os
from datetime import date

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL"


PIPELINE_NAME:str = "visa_prediction"
ARTIFACT_DIR:str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "us_visa.csv"
TRAIN_FILE_NAME :str = "train.csv"
TEST_FILE_NAME : str = "test.csv"


"""
Data Ingestion Related Constants 
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR :str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT: float = 0.2


