import os
import re
import glob
import multiprocessing
import logging

from config import settings
from common.decorators import execution_time


logger = logging.getLogger("process_files")


@execution_time(logger=logger)
def handle_file(filepath: str):
    """
    Все числа из строки в исходном файле сортируются в порядке возрастания, 
    учитывая что в последовательности могут быть указаны диапазоны чисел. 

    Результат сохраняется в новый файл по маске `TEST_AUCHAN_success_*`, 
    где каждое число находится на новой строке.
    """

    if not os.path.exists(filepath):
        logger.error(f'File {filepath} does not exist')
        return

    filename = os.path.basename(filepath)
    out_filename = "TEST_AUCHAN_success_" + filename[-5:]
    out_filepath = os.path.join(settings.OUTPUT_FOLDER, out_filename)

    with open(filepath, 'r') as f:
        data = f.read()

    numbers = []
    for match in re.findall(r'\d+', data):
        if '-' in match:
            start, end = map(int, match.split('-'))
            numbers.extend(range(start, end + 1))
        else:
            numbers.append(int(match))

    numbers.sort()
    os.makedirs(settings.OUTPUT_FOLDER, exist_ok=True)
    with open(out_filepath, 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')


@execution_time(logger=logger)
def main():
    """
    Функция итерируется по директориям `TEST_Folder_*` и обрабатывает файлы по маске `TEST_*` функцией `handle_file`.
    """
    files_paths = []
    for folder in glob.glob('TEST_Folder_*'):
        for filepath in glob.glob(folder + '/TEST_*'):
            files_paths.append(filepath)

    with multiprocessing.Pool(settings.NUMBER_OF_PROCESSES) as pool:
        pool.map(handle_file, files_paths)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()

