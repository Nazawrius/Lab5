class Try:
    def __init__(self, student, date, description, percent):
        self._student = student
        self._date = date
        self._description = description
        if 0 <= int(percent) <= 100:
            self._percent = int(percent)
        else:
            raise Exception

    @property
    def student(self):
        return self._student

    @property
    def date(self):
        return self._date

    @property
    def description(self):
        return self._description

    @property
    def percent(self):
        return self._percent

    def to_str(self):
        return (str(self.date.year) + '\t' + str(self.date.month) + '\t' +
                str(self.percent) + '\t' + self.student.to_str())


class Student:
    def __init__(self, last_name, first_name, father):
        names_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'- "
        if len(last_name) <= 26 and all((ch in names_chars for ch in last_name)) and \
           last_name.strip() == last_name:
            self._last_name = last_name
        else:
            raise Exception
        if len(first_name) <= 28 and all((ch in names_chars for ch in first_name)) and \
           first_name.strip() == first_name:
            self._first_name = first_name
        else:
            raise Exception
        if len(father) <= 27 and all((ch in names_chars for ch in father)) and \
           father.strip() == father:
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

    def to_str(self):
        return self.last_name + '\t' + self.first_name + '\t' + self.father


class Date:
    def __init__(self, year, month, day):
        if 2000 <= int(year) <= 9999 and len(year) == 4:
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
