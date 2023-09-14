# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение
# должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе. Например,
# URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg — Программа должна использовать
# многопоточный, многопроцессорный и асинхронный подходы. — Программа должна иметь возможность задавать список
# URL-адресов через аргументы командной строки. — Программа должна выводить в консоль информацию о времени скачивания
# каждого изображения и общем времени выполнения программы.
import argparse
import os.path
from multiprocessing import Process
from pathlib import Path
import asyncio
import requests
import threading
import time

# urls = ['https://dkrotov.com/delight.webpconverter/webp_converter_test_image.jpg',
#         'https://freelance.today/uploads/images/00/07/62/2017/06/13/14c404.jpg',
#         'https://www.krasavia.ru/storage/app/uploads/public/c56/247/9fb/thumb__800_0_0_0_crop.jpg',
#         'https://designonstop.com/wp-content/uploads/images/2010/04/useful/19pho_save/02.jpg',
#         ]
image_path1 = Path('./images1/')
image_path2 = Path('./images2/')
image_path3 = Path('./images3/')


def download_threaded(url):
    start_time = time.time()
    response = requests.get(url)
    filename = image_path1.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"download_threaded {url} in {time.time() - start_time:.2f} seconds")


def image_threaded(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_threaded, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time() - start_time
    print(f"image_threaded {end_time:.2f} seconds")


def download_processing(url):
    start_time = time.time()
    response = requests.get(url)
    filename = image_path2.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        f.write(response.content)
        print(f"download_processing {url} in {time.time() - start_time:.2f}seconds")


def image_processing(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        process = Process(target=download_processing, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time() - start_time
    print(f"image_processing {end_time:.2f} seconds")


async def download_async(url):
    start_time = time.time()
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {'stream': True})
    filename = image_path3.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


async def image_async(urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    end_time = time.time() - start_time
    print(f"image_async {end_time:.2f} seconds")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--urls', nargs='+')
    args = parser.parse_args()
    urls = args.urls

    image_processing(urls)
    image_threaded(urls)
    asyncio.run(image_async(urls))
