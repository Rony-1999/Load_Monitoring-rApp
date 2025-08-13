from influxdb_client import InfluxDBClient
from config import *

client = InfluxDBClient(
    url=f"http://{INFLUXDB_HOST}:{INFLUXDB_PORT}",
    username=INFLUXDB_USERNAME,
    password=INFLUXDB_PASSWORD,
    org=INFLUXDB_ORG
)

def fetch_performance_data(query, trigger_func):
    try:
        query_api = client.query_api()
        result = query_api.query(query, org=INFLUXDB_ORG)

        data = []
        for table in result:
            for record in table.records:
                measurement = record.get_measurement()
                field = record.get_field()
                value = record.get_value()
                ric_id = measurement.split(",")[0].replace("ManagedElement=", "")

                data.append({
                    "measurement": measurement,
                    "field": field,
                    "value": value,
                    "ric_id": ric_id
                })

                if field == "DRB.UEThpDl" and value < THROUGHPUT_THRESHOLD:
                    trigger_func(ric_id, field, value)
                elif field == "RRU.PrbDl" and value < PRB_THRESHOLD:
                    trigger_func(ric_id, field, value)

        return data
    except Exception as e:
        print(f"[ERROR] InfluxDB query failed: {e}")
        return []

