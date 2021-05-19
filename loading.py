import csv
import json
from Info import Info

def load_ini(path_ini):
    with open(path_ini) as open_ini:
        ini_file = json.load(open_ini)
        if 'input' not in ini_file or 'output' not in ini_file:
            raise Exception('UPS')
        Input = ini_file['input']
        Output = ini_file['output']
        if 'json' not in Input or 'csv' not in Input or \
           'encoding' not in Input or 'fname' not in Output or \
           'encoding' not in Output:
            raise Exception('UPS')
        return Input, Output

def load_json(Input):
    with open(Input['json'], encoding=Input['encoding']) as f:
        Json = json.load(f)
        return Json

def load_info(Input):
    with open(Input['csv'], encoding=Input['encoding']) as f:
        Csv = csv.reader(f, delimiter=';')
        info = Info(Csv)
        return info

def fit(json_loading, info):
    problem_number = json_loading["кількість різних задач"] == len(info.problems)
    entries_number = json_loading["кількість записів"] == info.entries
    return problem_number and entries_number

def key(try_):
    return (-try_.percent, try_.date.year, try_._date.month,
            try_.student.last_name, try_.student.first_name, try_.student.father)

def search(info, Output):
    with open(Output['fname'], 'w', encoding=Output['encoding']) as f:
        max_perfect_tries = 0
        perfect_list = []
        for problem in info.problems.values():
            perfect_tries = 0
            for try_ in problem.tries:
                if try_.percent == 100:
                    perfect_tries += 1
            if perfect_tries == max_perfect_tries:
                perfect_list.append(problem)
            if perfect_tries > max_perfect_tries:
                perfect_list = [problem]
                max_perfect_tries = perfect_tries
        for problem in perfect_list:
            f.write(f'{problem.description}\t{max_perfect_tries}\t{len(problem.tries)}\n')
            tries = list()
            for try_ in problem.tries:
                if try_.percent >= 75:
                    tries.append(try_)
            tries.sort(key=key)
            for try_ in tries:
                f.write(f'\t{try_.to_str()}\n')
