from containers import Name, Date, Try

class Info:
    def __init__(self, Csv):
        self._students = dict()
        self._problems = dict()
        self._entries = 0
        for row in Csv:
            self._entries += 1
            name = Name(row[5], row[4], row[0])
            if name in self._students:
                self._students[name] = Student(name)
            self._students[name].add_try(row)

            description = row[7]
            if description not in self._problems:
                self._problems[description] = Problem(description)
            self._problems[description].add_try(row)

    @property
    def entries(self):
        return self._entries

    @property
    def problems(self):
        return self._problems

    @property
    def students(self):
        return self._students


class Student:
    def __init__(self, name):
        self._name = name
        self._tries = dict()

    def add_try(self, row):
        date = Date(row[1], row[3], row[6])
        description = row[7]
        percent = row[1]
        try_ = Try(self._name, date, description, percent)
        if description in self._tries:
            self._tries[description].append(try_)
        else:
            self._tries[description] = [try_]

    @property
    def name(self):
        return self.name

    @property
    def tries(self):
        return self._tries


class Problem:
    def __init__(self, description):
        description_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" -.,_{}$+*\\()%[]'
        if 4 <= len(description) <= 68 and all((ch in description_chars for ch in description)):
            self._description = description
        else:
            raise Exception
        self._tries = dict()

    def add_try(self, row):
        date = Date(row[1], row[3], row[6])
        name = Name(row[5], row[4], row[0])
        percent = row[1]
        try_ = Try(name, date, self._description, percent)
        if name in self._tries:
            self._tries[name].append(try_)
        else:
            self._tries[name] = [try_]

    @property
    def description(self):
        return self.description

    @property
    def tries(self):
        return self._tries
