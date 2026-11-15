1. How many trips?
┌────────┐
│ trips  │
│ int64  │
├────────┤
│ 768705 │
└────────┘

2. What columns are there?
┌────────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│    column_name     │ column_type │  null   │   key   │ default │  extra  │
│      varchar       │   varchar   │ varchar │ varchar │ varchar │ varchar │
├────────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ ride_id            │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ rideable_type      │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ started_at         │ TIMESTAMP   │ YES     │ NULL    │ NULL    │ NULL    │
│ ended_at           │ TIMESTAMP   │ YES     │ NULL    │ NULL    │ NULL    │
│ start_station_name │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ start_station_id   │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ end_station_name   │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ end_station_id     │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ start_lat          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ start_lng          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ end_lat            │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ end_lng            │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ member_casual      │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ month              │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ year               │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
└────────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┘
  15 rows                                                        6 columns

3. First 5 rows
┌─────────────────────┬───────────────┬─────────────────────────┬─────────────────────────┬───┬────────────────────┬───────────────┬───────┬───────┐
│       ride_id       │ rideable_type │       started_at        │        ended_at         │ … │      end_lng       │ member_casual │ month │ year  │
│        int64        │    varchar    │        timestamp        │        timestamp        │ … │       double       │    varchar    │ int64 │ int64 │
├─────────────────────┼───────────────┼─────────────────────────┼─────────────────────────┼───┼────────────────────┼───────────────┼───────┼───────┤
│ 2160132728249199856 │ electric_bike │ 2026-10-03 15:33:39.059 │ 2026-10-03 15:39:35.144 │ … │         -87.627844 │ member        │    10 │  2026 │
│ 6952482780427550594 │ electric_bike │ 2026-10-03 12:14:45.451 │ 2026-10-03 12:30:10.811 │ … │         -87.648384 │ member        │    10 │  2026 │
│ 5304550517524824720 │ electric_bike │ 2026-10-02 21:03:58.733 │ 2026-10-02 21:09:24.288 │ … │         -87.629634 │ member        │    10 │  2026 │
│ 7838143855105179443 │ electric_bike │ 2026-10-03 14:25:50.16  │ 2026-10-03 14:37:06.885 │ … │     -87.6601406209 │ member        │    10 │  2026 │
│ 6615875143606741243 │ electric_bike │ 2026-10-03 10:38:39.63  │ 2026-10-03 10:46:24.44  │ … │ -87.64926373958588 │ member        │    10 │  2026 │
└─────────────────────┴───────────────┴─────────────────────────┴─────────────────────────┴───┴────────────────────┴───────────────┴───────┴───────┘
  5 rows                                                                                                                      15 columns (8 shown)

4. Missing values
┌───────────────────────┬─────────────────────┬──────────────────────┐
│ missing_start_station │ missing_end_station │ missing_end_location │
│         int64         │        int64        │        int64         │
├───────────────────────┼─────────────────────┼──────────────────────┤
│                157299 │              165977 │                  438 │
└───────────────────────┴─────────────────────┴──────────────────────┘

5. Duplicate ride IDs
┌────────────┐
│ duplicates │
│   int64    │
├────────────┤
│          0 │
└────────────┘

6. Weird trips
┌───────────────────┬───────────────────┬────────────────┐
│ ends_before_start │ longer_than_1_day │ under_1_minute │
│      int128       │      int128       │     int128     │
├───────────────────┼───────────────────┼────────────────┤
│                 0 │               430 │          17467 │
└───────────────────┴───────────────────┴────────────────┘

7. Bike types and rider types
┌───────────────┬───────────────┬────────┐
│ rideable_type │ member_casual │ trips  │
│    varchar    │    varchar    │ int64  │
├───────────────┼───────────────┼────────┤
│ electric_bike │ member        │ 363592 │
│ electric_bike │ casual        │ 220362 │
│ classic_bike  │ member        │ 130714 │
│ classic_bike  │ casual        │  54037 │