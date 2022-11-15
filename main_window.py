#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel , QLineEdit, QHBoxLayout, QMainWindow, QInputDialog, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import lab2
import os
import csv
import random

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')

        path_T = folder_path + '/tiger'
        path_L = folder_path + '/leopard'

        self.iter1 = lab2.iterator_2(path_T)
        pic_path1 = next(self.iter1)
        pic1 = QPixmap(pic_path1)
        pic1 = pic1.scaled(500, 400)
        self.lbl1 = QLabel(self)
        self.lbl1.setPixmap(pic1)
        self.lbl1.move(150, 150)
        self.btn_next_B = QPushButton('next tiger', self)
        self.btn_next_B.move(550, 600)
        self.btn_next_B.clicked.connect(self.next_T)
        self.btn_prev_B = QPushButton('previous tiger', self)
        self.btn_prev_B.move(150, 600)
        self.btn_prev_B.hide()
        self.btn_prev_B.clicked.connect(self.prev_T)

        self.iter2 = lab2.iterator_2(path_P)
        pic_path2 = next(self.iter2)
        pic2 = QPixmap(pic_path2)
        pic2 = pic2.scaled(500, 400)
        self.lbl2 = QLabel(self)
        self.lbl2.setPixmap(pic2)
        self.lbl2.move(800, 150)
        self.btn_next_P = QPushButton('next leopard', self)
        self.btn_next_P.move(1200, 600)
        self.btn_next_P.clicked.connect(self.next_L)
        self.btn_prev_P = QPushButton('previous leopard', self)
        self.btn_prev_P.move(800, 600)
        self.btn_prev_P.hide()
        self.btn_prev_P.clicked.connect(self.prev_L)
        


        self.btn_create_annotation = QPushButton('create annotation', self)
        self.btn_create_annotation.move(200, 680)
        self.btn_create_annotation.clicked.connect(self.write_annotation)

        self.btn_copy_dataset = QPushButton('copy dataset and write annotation', self)
        self.btn_copy_dataset.move(400, 680)
        self.btn_copy_dataset.clicked.connect(self.copy_dataset_1)

        self.btn_copy_dataset_R = QPushButton('copy dataset and write annotation with random numbers', self)
        self.btn_copy_dataset_R.move(800, 680)
        self.btn_copy_dataset_R.clicked.connect(self.copy_dataset_random)

        self.setGeometry(0, 0, 1600, 900)
        self.setWindowTitle('Application')
        self.show()

    def write_annotation(self):
        annotation_name = 'annotation_1_test.csv'
        print(annotation_name)
        with open(annotation_name, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        self.copy_iter_1 = lab2.iterator_1('tiger')
        self.copy_iter_2 = lab2.iterator_1('leopard')
        lab2.write_iteration_1(self.copy_iter_1, annotation_name)
        lab2.write_iteration_1(self.copy_iter_2, annotation_name)
    
    def copy_dataset_1(self):
        path = 'C:\\Users\\TUFman\\Desktop\\py lab 2\\'
        project_name = 'new_data_1'
        folder = 'dataset'
        fullpath = os.path.join(path, project_name)
        lab2.create_folder(fullpath)
        new_path = os.path.join(fullpath, folder)
        lab2.create_folder(new_path)
        annotation_name2 = 'annotation_2_test.csv'
        with open(annotation_name2, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        icopy_ter1_1 = lab2.iterator_1('tiger')
        lab2.copy_dataset(icopy_ter1_1, annotation_name2, new_path)
        icopy_ter1_2 = lab2.iterator_1('leopard')
        lab2.copy_dataset(icopy_ter1_2, annotation_name2, new_path)

    def copy_dataset_random(self):
        path = 'C:\\Users\\TUFman\\Desktop\\py lab 2\\'
        project_name = 'new_data_2'
        folder = 'dataset'
        fullpath = os.path.join(path, project_name)
        lab2.create_folder(fullpath)
        new_path = os.path.join(fullpath, folder)
        lab2.create_folder(new_path)
        print(new_path)
        annotation_name3 = 'annotation_3_test.csv'
        with open(annotation_name3, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        numbers = (list(range(1,10001)))
        random.shuffle(numbers)
        i_ter_ran_1 = lab2.iterator_1('tiger')
        lab2.copy_dataset_2(i_ter_ran_1, annotation_name3, new_path, numbers)
        i_ter_ran_2 = lab2.iterator_1('leopard')
        lab2.copy_dataset_2(i_ter_ran_2, annotation_name3, new_path, numbers)
            
    def next_T(self):
        pic_path1 = next(self.iter1)
        pic1 = QPixmap(pic_path1).scaled(500, 400)
        self.lbl1.setPixmap(pic1)
        if not (next(self.iter1)):
            self.btn_next_B.hide()
        if (self.iter1.__prev__()):
            self.btn_prev_B.show()

    def prev_T(self):
        pic_path1 = self.iter1.__prev__()
        pic1 = QPixmap(pic_path1).scaled(500, 400)
        self.lbl1.setPixmap(pic1)
        if not (self.iter1.__prev__()):
            self.btn_prev_B.hide()
        if (next(self.iter1)):
            self.btn_next_B.show()

    def next_L(self):
        pic_path2 = next(self.iter2)
        pic2 = QPixmap(pic_path2).scaled(500, 400)
        self.lbl2.setPixmap(pic2)
        if not (next(self.iter2)):
            self.btn_next_P.hide()
        if (self.iter2.__prev__()):
            self.btn_prev_P.show()

    def prev_L(self):
        pic_path2 = self.iter2.__prev__()
        pic2 = QPixmap(pic_path2).scaled(500, 400)
        self.lbl2.setPixmap(pic2)
        if not (self.iter2.__prev__()):
            self.btn_prev_P.hide()
        if (next(self.iter2)):
            self.btn_next_P.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
