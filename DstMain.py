/*runs functional time  components returna a time adjusted DST (Day-Light Saving) along with UTC dates*/
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


def convert_local_and_utc(
    dt_string: str, tz_name: str, dt_format: str
) -> dict[str, str]:
    """Parses a naive datetime string, attaches a local timezone (accounting for

    DST), and computes the corresponding UTC time.

    Args:
        dt_string: The date and time text (e.g., "2026-06-01 12:00:00").
        tz_name: IANA timezone string (e.g., "America/New_York").
        dt_format: The format matching dt_string (e.g., "%Y-%m-%d %H:%M:%S").

    Returns:
        A dictionary containing both the localized and UTC formatted strings.
    """
    # 1. Parse the string into a naive datetime object
    naive_dt = datetime.strptime(dt_string, dt_format)

    # 2. Attach the local timezone (ZoneInfo automatically manages DST boundaries)
    local_dt = naive_dt.replace(tzinfo=ZoneInfo(tz_name))

    # 3. Convert to UTC timezone using .astimezone()
    utc_dt = local_dt.astimezone(timezone.utc)

    # 4. Return formatted output strings
    return {
        "local_with_dst": local_dt.strftime(dt_format + " %Z %z"),
        "utc": utc_dt.strftime(dt_format + " %Z"),
    }


# --- Demo: winter vs summer DST ---
if __name__ == "__main__":
    TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOCATION = "America/New_York"

    # Test Case 1: Summer (EDT - Daylight Saving Time active)
    summer_result = convert_local_and_utc(
        "2026-07-01 12:00:00", LOCATION, TIME_FORMAT
    )
    print("Summer:", summer_result)

    # Test Case 2: Winter (EST - Standard Time active)
    winter_result = convert_local_and_utc(
        "2026-12-01 12:00:00", LOCATION, TIME_FORMAT
    )
    print("Winter:", winter_result)
