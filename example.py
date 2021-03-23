import argparse, os, csv
from typing import List, Dict

columns = {'open': 0.0, 'high': 0.0, 'low': 0.0, 'close': 0.0}
DEFAULT_PATH = os.path.normpath(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description='-p путь с csv файлами; -n имя колонки которое должно совпадать')
parser.add_argument("-p", "--paths", type=str,
                    default=DEFAULT_PATH,
                    help="путь с csv файлами")
parser.add_argument("-n", "--name", type=str, default='AAPL',
                    help="имя колонки Name, для которых будет подсчёт среднего значения")

args = parser.parse_args()
path = args.paths
names = args.name


def get_file_list(path: str) -> List[str]:
    """
    список файлов
    :param path:
    :return list:
    """
    paths = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith('.csv'):
                paths.append(os.path.normpath(os.path.join(root, filename)))

    if len(paths) == 0:
        raise Exception('Отсутствуют csv файлы, проверьте наличие файлов в каталоге')

    return paths


def csv_average_reader() -> Dict[str, float]:
    """
    Среднее значение csv файлов
    :return average type - Dict:
    """
    length = 0
    for file_name in get_file_list(path):
        with open(file_name) as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['Name'] == names:
                    length += 1
                    columns['open'] += float(row['open'])
                    columns['high'] += float(row['high'])
                    columns['low'] += float(row['low'])
                    columns['close'] += float(row['close'])
    for key in columns.keys():
        columns[key] = float('{:.3f}'.format(columns[key] / length))
    return columns


if __name__ == '__main__':
    try:
        print(csv_average_reader())
    except KeyError as er:
        print('не правильная структура csv файлов, отсутствует колонка:', er)
