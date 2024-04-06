import persiancalendar
import persiancalendar_fast

ROUNDTRIP_START_YEAR = 1304
ROUNDTRIP_END_YEAR = 1500


def test_roundtrip_astronomical():
    """Test that the astronomical algorithm roundtrips correctly."""
    start = persiancalendar.ordinal_from_persian(ROUNDTRIP_START_YEAR, 1, 1)
    end = persiancalendar.ordinal_from_persian(ROUNDTRIP_END_YEAR, 1, 1)

    for date in range(start, end):
        p_date = persiancalendar.persian_from_ordinal(date)
        converted_back = persiancalendar.ordinal_from_persian(*p_date)
        assert (date == converted_back)


def test_roundtrip_fast():
    """Test that the fast algorithm roundtrips correctly."""
    start = persiancalendar_fast.ordinal_from_persian_fast(
        ROUNDTRIP_START_YEAR, 1, 1)
    end = persiancalendar_fast.ordinal_from_persian_fast(
        ROUNDTRIP_END_YEAR, 1, 1)

    for date in range(start, end):
        p_date = persiancalendar_fast.persian_fast_from_ordinal(date)
        converted_back = persiancalendar_fast.ordinal_from_persian_fast(*p_date)
        assert (date == converted_back)


def test_fast():
    """Test that the results of the fast algorithm matches the results of the astronomical algorithm."""
    start = persiancalendar.ordinal_from_persian(
        persiancalendar_fast.SUPPORTED_FIRST_YEAR, 1, 1)
    end = persiancalendar.ordinal_from_persian(
        persiancalendar_fast.SUPPORTED_LAST_YEAR + 1, 1, 1)

    for date in range(start, end):
        fast_p_date = persiancalendar_fast.persian_fast_from_ordinal(date)
        astro_p_date = persiancalendar.persian_from_ordinal(date)
        assert (fast_p_date == astro_p_date)


if __name__ == "__main__":
    test_roundtrip_astronomical()
    test_roundtrip_fast()
    test_fast()
