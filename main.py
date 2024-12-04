import os
import time
from threading import Thread, Lock
from datetime import datetime

# lock = Lock()

def file_create(file_base_name = "File", extension = ".txt", folder_name = "Files"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_number = 1
    while True:
        file_name = os.path.join(folder_name, f"{file_base_name}_{file_number}{extension}")

        try:
            # with lock:
                with open(file_name, mode="x") as f:
                    f.write("Текст")
                    print(f"Created: {file_name}\n"
                        f"At {datetime.now()}\n")
                    time.sleep(1)
                    break
        except FileExistsError:
            file_number += 1

def file_100():
    start_time = time.perf_counter()
    for i in range(1,101):
        file_create(file_base_name=f"File_{i}")
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Функция '100' заняла:\n"
        f"{elapsed_time:.2f} секунды")

def file_multiple_threads(threads_count = 100):
    threads = []
    start_time = time.perf_counter()

    for i in range(threads_count):
        thread = Thread(target=file_create, kwargs={"file_base_name": f"File_{i}"})
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Функция 'многопоточности' заняла:\n"
        f"{elapsed_time:.2f} секунды")

if __name__ == "__main__":
    # file_100()
    file_multiple_threads(100)