CREATE OR REPLACE TABLE sensors_report (
    record_id varchar,
    sensor_id varchar,
    sensor_date date,
    sensor_time time,
    sensor_limit_low numeric,
    sensor_limit_high numeric,
    sensor_temp_low numeric,
    sensor_temp_high numeric,
    sensor_temp_low_prev numeric,
    sensor_temp_high_prev numeric
);