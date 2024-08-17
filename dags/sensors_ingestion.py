import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from pathlib import Path
from plugins.utils import utils
from plugins.sensors_ingestion.ingestion_runner import IngestionRunner

ENVIRONMENT:                    str = os.getenv("ENVIRONMENT", "dev")
DAG_NAME:                       str = Path(__file__).stem
CONFIG_PATH:                    str = f"/opt/airflow/config/{DAG_NAME}.yaml"
CONFIG:                         str = utils.parse_config(config_path=CONFIG_PATH)
ENDPOINT:                       str = CONFIG.get(ENVIRONMENT)["endpoint"] 
AWS_ACCESS_KEY_ID:              str = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY:          str = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_LOCATION:           str = os.getenv("AWS_DEFAULT_LOCATION")
PSQL_HOST:                      str = os.getenv("PSQL_HOST")
PSQL_PORT:                      str = os.getenv("PSQL_PORT")
PSQL_USER:                      str = os.getenv("PSQL_USER")
PSQL_PASS:                      str = os.getenv("PSQL_PASS")
PSQL_BASE:                      str = os.getenv("PSQL_BASE")
SQL_CREATE_SENSOR_REPORT_STAGE: str = "plugins/sensors_ingestion/sql/create_sensors_report_stage.sql"
SQL_CREATE_SENSOR_REPORT:       str = "plugins/sensors_ingestion/sql/create_sensors_report.sql"

with DAG(DAG_NAME, start_date=datetime(2024, 8, 17)) as dag:

    if all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_LOCATION, PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_BASE]):
        get_sensors_data = PythonOperator(
            task_id='get_sensors_data',
            python_callable=IngestionRunner.run_ingestion,
            provide_context=True,
            op_kwargs={
                "target_environment":             ENVIRONMENT,
                "sql_create_sensor_report":       SQL_CREATE_SENSOR_REPORT,
                "sql_create_sensor_report_stage": SQL_CREATE_SENSOR_REPORT_STAGE,
                "aws_access_key_id":              AWS_ACCESS_KEY_ID,
                "aws_secret_access_key":          AWS_SECRET_ACCESS_KEY,
                "aws_default_location":           AWS_DEFAULT_LOCATION,
                "psql_host":                      PSQL_HOST,
                "psql_port":                      PSQL_PORT,
                "psql_user":                      PSQL_USER,
                "psql_pass":                      PSQL_PASS,
                "psql_base":                      PSQL_BASE
            }
        )

        get_sensors_data

    else:
        return_credentials_error = PythonOperator(
            task_id="return_credentials_error",
            python_callable=lambda: " ... CREDENTIALS ERROR ... ",
            provide_context=True,
        )

        return_credentials_error

