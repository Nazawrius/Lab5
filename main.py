from sys import argv
from loading import load_ini, load_stat
import re
import csv
import json


def process():
    print("Робота Пашенюка Нікіти, Варіант 22, описує задачу про зчитування та обробку файлів")
    print("*****")
    if len(argv) != 2:
        print('***** program aborted *****')
        return None
    else:
        print('Ты хоть с чем-то не обосрался')

    print(f'ini {argv[1]}: ', end='')
    input, output = load_ini(argv[1])
    try:
        input, output
    except Exception as e:
        print(e)
        print('***** program aborted *****')
        return None
    else:
        print('OK')

    print(f'input-csv {input["csv"]} :', efrom sys import argv
from loading import load_ini, load_stat
import re
import csv
import json


def process():
    print("Робота Пашенюка Нікіти, Варіант 22, описує задачу про зчитування та обробку файлів")
    print("*****")
    if len(argv) != 2:
        print('***** program aborted *****')
        return None
    else:
        print('Ты хоть с чем-то не обосрался')

    print(f'ini {argv[1]}: ', end='')
    input, output = load_ini(argv[1])
    try:
        input, output
    except Exception as e:
        print(e)
        print('***** program aborted *****')
        return None
    else:
        print('OK')

    print(f'input-csv {input["csv"]} :', end='')
    csv_loading = load_csv('Input')
    try:
       csv_loading
    except Exception as e:
        print(e)
        print('***** program aborted *****')
        return None
    else:
        print('OK')


    print(f'input-json {input["json"]} :', end='')
    json_loading = load_stat(r'C:\Users\Admin\PycharmProjects\Lab5\Input\input.json', f'{input["encoding"]}')
    try:
        json_loading
    except Exception as e:
        print(e)
        print('***** program aborted *****')
        return None
    else:
        print('OK')
"""
    print(f'json?=csv ')                                    Как-нибудь и это

    print(f'output {Output(output.txt)} ')                   Вместе с этим

"""
process()








