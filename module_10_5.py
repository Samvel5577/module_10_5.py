import time
import os
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file{number}.txt' for number in range(1, 5)]  # Имена файлов


def linear_read():
    start_time = time.time()

    for filename in filenames:
        read_info(filename)

    end_time = time.time()
    print(f"Линейный подход занял: {end_time - start_time:.6f} секунд")


def multiprocess_read():
    start_time = time.time()

    with Pool(processes=os.cpu_count()) as pool:
        pool.map(read_info, filenames)

    end_time = time.time()
    print(f"Многопроцессный подход занял: {end_time - start_time:.6f} секунд")


if __name__ == "__main__":
    linear_read()
