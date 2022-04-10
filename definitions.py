import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCE_DIR = os.path.join(ROOT_DIR, "uresources")
USECASE_DIR = os.path.join(ROOT_DIR, "use-cases")

DATASET_FILE_PATH = os.path.join(RESOURCE_DIR, "dataset.csv")
DATABASE_FILE = os.path.join(RESOURCE_DIR, "datastore.db")

READ_METRICS_RESPONSE = os.path.join(RESOURCE_DIR, "read_metrics_response.json")
RESPONSE_FILE_1 = os.path.join(RESOURCE_DIR, "use_case_1_response.json")
RESPONSE_FILE_2 = os.path.join(RESOURCE_DIR, "use_case_2_response.json")
RESPONSE_FILE_3 = os.path.join(RESOURCE_DIR, "use_case_3_response.json")
RESPONSE_FILE_4 = os.path.join(RESOURCE_DIR, "use_case_4_response.json")
REQUEST_FILE_1 = os.path.join(USECASE_DIR, "use-case1.json")

