import csv
import json


def load_ini(path_ini):
    open_ini = open(path_ini)
    ini_file =import csv
import json


def load_ini(path_ini):
    open_ini = open(path_ini)
    ini_file = json.load(open_ini)
    if 'input' not in ini_file or 'output' not in ini_file:
        raise Exception('UPS')
    Input = ini_file['input']
    Output = ini_file['output']
    if 'json' not in Input or 'csv' not in Input or 'encoding' not in Input or 'fname' not in Output or \
            'encoding' not in Output:
        raise Exception('UPS')
    return Input, Output


"""def load_stat(Input):
    with open(Input['json'], encoding=Input['encoding']) as f:
        load_json = json.load(f)
        return load_json

"""


def load_stat(filename, encoding):
    with open(filename, encoding=encoding) as json_file:
        return json.load(json_file)
