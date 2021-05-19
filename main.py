from sys import argv
import loading

def process():
    print("Робота Пашенюка Нікіти, Варіант 22, описує задачу про зчитування та обробку файлів")
    print("*****")
    if len(argv) != 2:
        print('***** program aborted *****')
        return None

    print(f'ini {argv[1]}: ', end='')
    try:
        Input, Output = loading.load_ini(argv[1])
    except Exception:
        print('***** program aborted *****')
        return None
    print('OK')

    print(f'input-csv {Input["csv"]}: ', end='')
    info = loading.load_info(Input)
    try:
        info = loading.load_info(Input)
    except Exception:
        print('***** program aborted *****')
        return None
    print('OK')

    print(f'input-json {Input["json"]}: ', end='')
    try:
        json_loading = loading.load_json(Input)
    except Exception:
        print('***** program aborted *****')
        return None
    print('OK')

    print('json?=csv: ', end='')
    if loading.fit(json_loading, info):
        print('OK')
    else:
        print('UPS')

    print(f'output {Output["fname"]}: ', end='')
    loading.search(info, Output)
    try:
        loading.search(info, Output)
    except Exception:
        print('***** program aborted *****')
        return None
    print('OK')


if __name__ == '__main__':
    process()
