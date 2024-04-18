from persiancalendar import persian_from_ordinal, ordinal_from_persian
from persiancalendar_fast import (
    persian_fast_from_ordinal,
    ordinal_from_persian_fast,
    SUPPORTED_FIRST_YEAR,
    SUPPORTED_LAST_YEAR,
)

ROUNDTRIP_START_YEAR = 1304
ROUNDTRIP_END_YEAR = 1500


def test_roundtrip_astronomical():
    """Test that the astronomical algorithm roundtrips correctly."""
    start = ordinal_from_persian(ROUNDTRIP_START_YEAR, 1, 1)
    end = ordinal_from_persian(ROUNDTRIP_END_YEAR, 1, 1)

    for ordinal in range(start, end):
        p_date = persian_from_ordinal(ordinal)
        converted_back = ordinal_from_persian(*p_date)
        assert ordinal == converted_back


def test_roundtrip_fast():
    """Test that the fast algorithm roundtrips correctly."""
    start = ordinal_from_persian_fast(ROUNDTRIP_START_YEAR, 1, 1)
    end = ordinal_from_persian_fast(ROUNDTRIP_END_YEAR, 1, 1)

    for ordinal in range(start, end):
        p_date = persian_fast_from_ordinal(ordinal)
        converted_back = ordinal_from_persian_fast(*p_date)
        assert ordinal == converted_back


def test_fast():
    """Test that the results of the fast algorithm matches the results of the astronomical algorithm."""
    start = ordinal_from_persian(SUPPORTED_FIRST_YEAR, 1, 1)
    end = ordinal_from_persian(SUPPORTED_LAST_YEAR + 1, 1, 1)

    for ordinal in range(start, end):
        assert persian_fast_from_ordinal(ordinal) == persian_from_ordinal(ordinal)


if __name__ == "__main__":
    test_roundtrip_astronomical()
    test_roundtrip_fast()
    test_fast()
