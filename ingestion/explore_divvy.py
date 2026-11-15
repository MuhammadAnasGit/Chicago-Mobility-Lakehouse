import duckdb

path = r"C:\lakehouse-data\bronze\divvy\year=2026\month=10\trips.csv"
con = duckdb.connect()
con.sql(f"CREATE VIEW trips AS SELECT * FROM read_csv_auto('{path}')")

print("1. How many trips?")
con.sql("SELECT COUNT(*) AS trips FROM trips").show()

print("2. What columns are there?")
con.sql("DESCRIBE trips").show()

print("3. First 5 rows")
con.sql("SELECT * FROM trips LIMIT 5").show()

print("4. Missing values")
con.sql("""SELECT
  COUNT(*) - COUNT(start_station_name) AS missing_start_station,
  COUNT(*) - COUNT(end_station_name)   AS missing_end_station,
  COUNT(*) - COUNT(end_lat)            AS missing_end_location
FROM trips""").show()

print("5. Duplicate ride IDs")
con.sql("SELECT COUNT(*) - COUNT(DISTINCT ride_id) AS duplicates FROM trips").show()

print("6. Weird trips")
con.sql("""SELECT
  SUM(CASE WHEN ended_at < started_at THEN 1 ELSE 0 END)                    AS ends_before_start,
  SUM(CASE WHEN ended_at - started_at > INTERVAL 1 DAY THEN 1 ELSE 0 END)   AS longer_than_1_day,
  SUM(CASE WHEN ended_at - started_at < INTERVAL 1 MINUTE THEN 1 ELSE 0 END) AS under_1_minute
FROM trips""").show()

print("7. Bike types and rider types")
con.sql("""SELECT rideable_type, member_casual, COUNT(*) AS trips
FROM trips GROUP BY ALL ORDER BY trips DESC""").show()