import os, sys
from plugins.sensors_ingestion.api_getter import ApiGetter
from plugins.sensors_ingestion.response_formatter import ResponseFormatter
from plugins.sensors_ingestion.cloud_manager import CloudManager
from plugins.sensors_ingestion.database_manager import DatabaseManager
from plugins.utils.utils import get_dt

class IngestionRunner:

    @staticmethod
    def run_ingestion(
        **kwargs
    ) -> None:
        return "... SUCCESS: LOREM IPSUM ..."
        # database_manager: DatabaseManager = DatabaseManager(
        #     hostname=kwargs.get('psql_host'), 
        #     port=kwargs.get('psql_port'), 
        #     username=kwargs.get('psql_user'), 
        #     password=kwargs.get('psql_pass'), 
        #     database=kwargs.get('psql_base')
        # )
        # database_manager.run_sql_script(kwargs.get('sql_create_sensor_report'))
        # database_manager.run_sql_script(sql_create_sensor_report_stage)
        # cloud_manager = CloudManager(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key) # -> boto3.Session
        # cloud_manager.create_S3_bucket(bucket_location=aws_default_location, bucket_name=f"{target_environment}-sensors-{get_dt()}")
        # api_response_raw: str = ApiGetter.get_endpoint(sys.argv[1])
        # api_response_list: list = ResponseFormatter.format_response(api_response_raw)
        # for item in api_response_list:
        #     print(item)
