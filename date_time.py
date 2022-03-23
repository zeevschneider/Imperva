from datetime import datetime


class Solution:
    def __init__(self, date_string, delta, date_format='%d.%m.%Y'):
        try:
            dt = datetime.strptime(date_string, date_format)
            if delta <= 0 or delta > 0:
                self.delta = delta
            else:
                raise ValueError('Received invalid delta')

        except ValueError as e:
            raise f'Received invalid date. The following exception occurred {e}'

        self.day = dt.day
        self.month = dt.month
        self.year = dt.year
        self.DAYS1Y = 365
        self.DAYS4Y = 4 * self.DAYS1Y + 1
        self.DAYS100Y = 25 * self.DAYS4Y - 1
        self.DAYS400Y = 4 * self.DAYS100Y + 1
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def days(self):
        x = self._to_days()
        return self._from_days(x + self.delta)

    @staticmethod
    def _is_leap(y):
        """
        Static method.
        Calculates leap year

        :param y: year to check
        :return:
        """
        if y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False
        else:
            return y % 4 == 0

    def _to_days(self):
        """
        Transforms received date into days
        :return: number of days in the date eg. 1.1.200 = 730486 days
        """
        if self._is_leap(self.year):
            self.days_in_month[2] = 29
        else:
            self.days_in_month[2] = 28

        # calc days in year
        cy = (self.year // 400) * self.DAYS400Y
        self.year %= 400
        cy += (self.year // 100) * self.DAYS100Y
        self.year %= 100
        cy += (self.year // 4) * self.DAYS4Y
        self.year %= 4
        cy += self.year * self.DAYS1Y

        # calc month into days
        cm = 0
        for i in range(1, self.month):
            cm += self.days_in_month[i]

        # add days
        return cy + cm + self.day

    def _from_days(self, x):
        """
        Converts calculated date + delta back to date
        :param x: calculated date + delta
        :return: date
        """
        y = 400 * (x // self.DAYS400Y)
        x %= self.DAYS400Y
        y += 100 * (x // self.DAYS100Y)
        x %= self.DAYS100Y
        y += 4 * (x // self.DAYS4Y)
        x %= self.DAYS4Y
        y += 1 * (x // self.DAYS1Y)
        x %= self.DAYS1Y

        if self._is_leap(y):
            self.days_in_month[2] = 29
        else:
            self.days_in_month[2] = 28

        m = 1
        while self.days_in_month[m] < x:
            x -= self.days_in_month[m]
            m += 1

        return f"{x:02d}.{m:02d}.{y}"


if __name__ == "__main__":
    s1 = Solution('31.1.2000', -29)
    s2 = Solution('31.1.2001', 29)

    print(s1.days())
    print(s2.days())
