
import shutil
import random
import glob
import csv
import time
#import cv2
import os 
                    
def create_folder(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
"""создание папок"""

class iterator_1:
    """итератор: перебирает фото"""
    def __init__(self, c_name: str):
        self.c_name = c_name
        self.counter = 0
        print(c_name)

    def __next__(self):
        self_path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\dataset\\' + self.c_name + '\\' + str(self.counter).zfill(4) + '.jpg'
        if(os.path.exists(self_path)):
            #print(self_path)
            self.counter += 1
            return self_path
        else:
            raise StopIteration

class iterator_2:
    """итератор: перебирает фото"""
    def __init__(self, c_name: str):
        self.c_name = c_name
        self.counter = 0
        print(c_name)

    def __next__(self):
        self_path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\dataset\\' + self.c_name + '\\' + str(self.counter).zfill(4) + '.jpg'
        if(os.path.exists(self_path)):
            #print(self_path)
            self.counter += 1
            return self_path
        else:
            raise StopIteration
    
    def __prev__(self):
        self_path = 'C:\\Users\\TUFman\\Desktop\\python\\python\\dataset\\' + self.c_name + '\\' + str(self.counter).zfill(4) + '.jpg'
        if(os.path.exists(self_path)):
            self.counter -= 1
            return self_path
        else:
            raise StopIteration



def write_iteration_1(iter1: iterator1, annotation_name: str):
    """записьь первой аннотации"""
    while(True):
        try:
            self_path = next(iter1)
            print(self_path)
            rel_path = 'python' + self_path.split('python')[2]
            print(rel_path)
            c_name = rel_path.split('\\')[2]
            print(c_name)
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([self_path, rel_path, c_name])
        except:
            break
    

def copy_dataset(iiter: iterator1, annotation_name: str, new_path: str):
    """копирование фото в новую директорию и запись 2 аннотации"""
    while(True):
        try:
            print(new_path)
            self_path = next(iiter)
            #print(self_path)
            add_path = self_path.split('\\dataset\\')[1]
            photo_path = os.path.join(new_path, add_path.split('\\')[0]) + '_' + add_path.split('\\')[1]
            #print(photo_path)
            shutil.copyfile(self_path, photo_path)
            relative_path = photo_path.split('\\python\\')[1]
            name_class = add_path.split('\\')[0]
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([photo_path, relative_path, name_class])
        except:
            break

def copy_dataset_2(iiter: iterator1, annotation_name: str, new_path: str, random_number: int):
    """копирование фото в новую директорию и запись 3 аннотации"""
    while(True):
        try:
            print(new_path)
            self_path = next(iiter)
            #print(self_path)
            add_path = self_path.split('\\dataset\\')[1]
            #print(add_path)
            #print(random_number)
            photo_path = new_path + '\\' + add_path.split('\\')[0] + '_' + str(random_number.pop(0)).zfill(5) + '.jpg'
            #print(photo_path)
            shutil.copyfile(self_path, photo_path)
            relative_path = photo_path.split('\\python\\')[1]
            name_class = add_path.split('\\')[0]
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow([photo_path, relative_path, name_class])
        except:
            break

annotation_name_1 = 'annotation_1.csv'
with open(annotation_name_1, mode="w", encoding='utf-8') as write_file:
    file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])
"""создание 1 аннотации"""

iter_1 = iterator1('tiger')
write_iteration_1(iter_1, annotation_name_1)

iter_2 = iterator1('leopard')
write_iteration_1(iter_2, annotation_name_1)
"""запись 1 аннотации"""

path_new = 'C:\\Users\\TUFman\\Desktop\\python\\data_new'
project_name_new = 'dataset'

create_folder(path_new)
    
full_path_new = os.path.join(path_new, project_name_new)
create_folder(full_path_new)
"""создание новой директории"""

annotation_name_2 = 'annotation_2.csv'
with open(annotation_name_2, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])
"""создание 2 аннотации"""

iiter1 = iterator1('tiger')
copy_dataset(iiter1, annotation_name_2, full_path_new)

iiter2 = iterator1('leopard')
copy_dataset(iiter2, annotation_name_2, full_path_new)
"""копирование фото в новую директорию и запись 2 аннотации"""

random_number = list(range(0, 10001))
random.shuffle(random_number)
"""генерация случайных чисел"""

path_new_2 = 'C:\\Users\\TUFman\\Desktop\\python\\data_new_2'
project_name_new_2 = 'dataset'
    
create_folder(path_new_2)

full_path_new_2 = os.path.join(path_new_2, project_name_new_2)
create_folder(full_path_new_2)
"""создание новой директории"""

annotation_name3 = 'annotation_3.csv'
with open(annotation_name3, mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(['Абсолютный путь', 'Относительный путь', 'Класс'])
"""создании 3 аннотации"""

i2ter1 = iterator1('tiger')
copy_dataset_2(i2ter1, annotation_name3, full_path_new_2, random_number)


i2ter2 = iterator1('leopard')
copy_dataset_2(i2ter2, annotation_name3, full_path_new_2, random_number)
"""копирование фото в новую директорию и запись 3 аннотации"""
