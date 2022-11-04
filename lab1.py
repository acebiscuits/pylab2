
import os      
import random  
import requests
from bs4 import BeautifulSoup
import time
#import cv2

def download_pictures(url1: str, url2: str, folder: str, full_path: str):
    """скачивание фото"""
    count = 752
    for page in range(30, 37):
        url = url1 + str(page) + url2 + folder
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        blocks = soup.findAll('div', class_='serp-item__preview')
        for block in blocks:
            if (block):
                v1 = str(count)
                zero = 4 - len(v1)
                number = '0' * zero
                name = str(number) + str(count)
                preview_block = block.find('a', class_='serp-item__link').get('href')
                link = (preview_block.split('=')[3])
                link2 = link.replace('%3A', ':')
                link3 = link2.replace('%2F', '/')
                link4 = (link3.split('&')[0])
                print(link4)
                try:
                    link5 = requests.get(link4, timeout = 10)
                except:
                    continue
                if link5.status_code == 200:
                    image_byt = link5.content 
                    time.sleep(random.random())
                    with open(full_path + '\\' + folder + '\\' + name + '.jpg', 'wb') as file:
                        file.write(image_byt)
                    count += 1 


def create_folder(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
        """создание папок"""


path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\'
project_name = 'dataset'
folders = ['tiger', 'leopard']

full_path = os.path.join(path, project_name)
create_folder(full_path)

for f in folders:
    folder = os.path.join(full_path, f)
    create_folder(folder)
    """создание попок"""

url1_1 = "https://yandex.ru/images/search?p="
url1_2 = "&text="
folder1 = "tiger"
folder2 = "leopard" 
"""пути и ссылка"""  

download_pictures(url1_1, url1_2, folder1, full_path)
download_pictures(url1_1, url1_2, folder2, full_path)
"""скачивание фото"""
