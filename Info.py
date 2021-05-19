from containers import Student, Date, Try

class Info:
    def __init__(self, Csv):
        self._problems = dict()
        self._entries = 0
        for row in Csv:
            self._entries += 1
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


class Problem:
    def __init__(self, description):
        description_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" -.,_{}$+*\\()%[]'
        if 4 <= len(description) <= 68 and all((ch in description_chars for ch in description)) and \
           description.strip() == description:
            self._description = description
        else:
            raise Exception(1)
        self._tries = list()

    def add_try(self, row):
        date = Date(row[1], row[3], row[6])
        name = Student(row[5], row[4], row[0])
        percent = row[2]
        try_ = Try(name, date, self._description, percent)
        self._tries.append(try_)

    @property
    def description(self):
        return self._description

    @property
    def tries(self):
        return self._tries
