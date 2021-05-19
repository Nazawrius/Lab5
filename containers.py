class Try:
    def __init__(self, name, date, description, percent):
        self._name = name
        self._date = date
        self._description = description
        if 0 <= int(percent) <= 100:
            self._percent = percent
        else:
            raise Exception

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    @property
    def percent(self):
        return self._percent


class Name:
    def __init__(self, last_name, first_name, father):
        names_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'- "
        if len(last_name) == 26 and all((ch in names_chars for ch in last_name)):
            self._last_name = last_name
        else:
            raise Exception
        if len(first_name) == 28 and all((ch in names_chars for ch in first_name)):
            self._first_name = first_name
        else:
            raise Exception
        if len(father) == 27 and all((ch in names_chars for ch in father)):
            self._father = father
        else:
            raise Exception

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def father(self):
        return self._father


class Date:
    def __init__(self, year, month, day):
        if 2000 <= int(year) <= 2021 and len(year) == 4:
            self._year = int(year)
        else:
            raise Exception
        if 1 <= int(month) <= 12 and len(month) <= 2:
            self._month = int(month)
        else:
            raise Exception
        if 1 <= int(day) <= 31 and len(day) <= 2:
            self._day = int(day)
        else:
            raise Exception

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day
