from date_time import Solution
import datetime


def test_add_date():
    start_date = '31.1.2000'

    s = Solution(start_date, 29)
    s1 = datetime.datetime.strptime(start_date, "%d.%m.%Y") + datetime.timedelta(days=29)

    assert s.days() == s1.strftime("%d.%m.%Y")


def test_subtract_date():
    start_date = '31.1.2000'

    s = Solution(start_date, -29)
    s1 = datetime.datetime.strptime(start_date, "%d.%m.%Y") + datetime.timedelta(days=-29)

    assert s.days() == s1.strftime("%d.%m.%Y")