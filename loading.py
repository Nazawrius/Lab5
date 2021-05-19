import csv
import json
from Info import Info

def load_ini(path_ini):
    open_ini = open(path_ini)
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

def fit(info, json_loading):
    problem_number = json_loading["кількість різних задач"] == len(info.problems)
    entries_number = json_loading["кількість записів"] == info.entries
    return problem_number and entries_number

def search(info):
    ...
