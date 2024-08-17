import yaml, time
from datetime import datetime as dt

def parse_config(
        config_path: str
    ) -> dict:
    with open(config_path, "r") as config:
        try:
            return yaml.safe_load(config)
        except yaml.YAMLError as YAMLExc:
            raise YAMLExc
        except Exception as Exc:
            raise Exc

def get_ms() -> str: return str(round(time()*1000))
def get_dt() -> str: return f"{dt.now().year}{dt.now().month}{dt.now().day}"