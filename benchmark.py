from time import perf_counter
from datetime import date
import gc

from jalali_core import JalaliToGregorian, GregorianToJalali
from gshconverter import gregorian_to_solar_hijri, solar_hijri_to_gregorian
from persiancalendar_fast import ordinal_from_persian_fast, persian_fast_from_ordinal


start = ordinal_from_persian_fast(1300, 1, 1)
end = ordinal_from_persian_fast(1500, 1, 1)

repeat = 10
gc.disable()


def g2j():
    g = date.fromordinal(start)
    assert (
        GregorianToJalali(g.year, g.month, g.day).getJalaliList()
        == persian_fast_from_ordinal(g.toordinal())
        == gregorian_to_solar_hijri(g.year, g.month, g.day)
    )

    t0 = perf_counter()
    for i in range(repeat):
        for ordinal in range(start, end):
            GregorianToJalali(g.year, g.month, g.day).getJalaliList()
    t1 = perf_counter()
    GregorianToJalali_time = t1 - t0

    t0 = perf_counter()
    for i in range(repeat):
        for ordinal in range(start, end):
            persian_fast_from_ordinal(g.toordinal())
    t1 = perf_counter()
    persian_fast_from_ordinal_time = t1 - t0

    t0 = perf_counter()
    for i in range(repeat):
        for ordinal in range(start, end):
            gregorian_to_solar_hijri(g.year, g.month, g.day)
    t1 = perf_counter()
    gregorian_to_solar_hijri_time = t1 - t0

    print(f"{GregorianToJalali_time / persian_fast_from_ordinal_time * 100 - 100 = }")
    print(
        f"{gregorian_to_solar_hijri_time / persian_fast_from_ordinal_time * 100 - 100 = }"
    )


def j2g():
    assert (
        JalaliToGregorian(1300, 1, 1).getGregorianList()
        == date.fromordinal(ordinal_from_persian_fast(1300, 1, 1)).timetuple()[:3]
        == solar_hijri_to_gregorian(1300, 1, 1)
    )

    j_tuples = [persian_fast_from_ordinal(ordinal) for ordinal in range(start, end)]

    t0 = perf_counter()
    for i in range(repeat):
        for j_tuple in j_tuples:
            JalaliToGregorian(*j_tuple).getGregorianList()
    t1 = perf_counter()
    JalaliToGregorian_time = t1 - t0

    t0 = perf_counter()
    for i in range(repeat):
        for j_tuple in j_tuples:
            solar_hijri_to_gregorian(*j_tuple)
    t1 = perf_counter()
    solar_hijri_to_gregorian_time = t1 - t0

    t0 = perf_counter()
    for i in range(repeat):
        for j_tuple in j_tuples:
            date.fromordinal(ordinal_from_persian_fast(*j_tuple)).timetuple()[:3]
    t1 = perf_counter()
    ordinal_from_persian_fast_time = t1 - t0

    print(f"{JalaliToGregorian_time / ordinal_from_persian_fast_time * 100 - 100 = }")
    print(
        f"{solar_hijri_to_gregorian_time / ordinal_from_persian_fast_time * 100 - 100 = }"
    )


g2j()
j2g()
