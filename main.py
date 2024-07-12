from PyQt5 import QtWidgets
from main_form import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog

import os, sqlite3, configparser

DB_CONF = 'db_conf.ini'

class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = None
        self.db_config = None

        self.selDB = self.findChild(QtWidgets.QPushButton, 'selDB')
        self.selDB.clicked.connect(self.sel_data_base)

        self.load_app()

    #Метод выбора БД
    def sel_data_base(self): # Определение метода для выбора файла базы данных
        # Открытие диалогового окна для выбора файла базы данных
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать файл","", "Файлы баз данных (*.db)")  
        if file_name:  # Проверка, был ли выбран файл
            try:
                self.db = sqlite3.connect(file_name)    # Подключение к выбранной базе данных
                self.db_config = list()                 # Создание списка для хранения конфигурационных данных о базе данных
                self.db_config.append(file_name)        # Добавление пути к выбранной базе данных в список
                self.save_config()                      # Сохранение конфигурационных данных о базе данных в файл
                print('connect ok...')                  # Вывод сообщения об успешном подключении
            except:
                print('connect filed...')               # Вывод сообщения об ошибке при подключении


    #Метод сохранения конфигураций программы в файл
    def save_config(self):                    # Определение метода для сохранения конфигурационных данных
        config = configparser.ConfigParser()  # Создание объекта ConfigParser
        config['data_base'] = {               # Создание секции 'data_base' и добавление параметра 'path' в неё
        'path': self.db_config[0]             # Задание пути к базе данных (путь хранится в переменной db_config)
            }

        with open(DB_CONF, 'w') as conffile:  # Открытие файла для записи (DB_CONF - это путь к конфигурационному файлу)
            config.write(conffile)            # Запись конфигурационных данных в файл


    #Функции выполняемые при загрузке программы    
    def load_app(self):
        if self.load_db_conf():                               # Проверка успешной загрузки конфигурационных данных о базе данных
            try:
                self.db = sqlite3.connect(self.db_config[0])  # Подключение к базе данных, используя путь из конфигурационных данных
                print('connect ok...')                        # Вывод сообщения об успешном подключении
            except:
                print('connfect filed...')                    # Вывод сообщения об ошибке при подключении



    #Чтение файла конфигураций для БД
    def load_db_conf(self): 
        if os.path.exists(DB_CONF):                             # Проверка существования файла конфигурации базы данных
            config = configparser.ConfigParser()                # Создание объекта ConfigParser
            config.read(DB_CONF)                                # Чтение конфигурационных данных из файла
            self.db_config = list()                             # Создание списка для хранения конфигурационных данных о базе данных
            self.db_config.append(config['data_base']['path'])  # Добавление пути к базе данных из конфигурационного файла в список
            return True                             # Возвращение True, если конфигурационные данные успешно загружены
        else:
            return False                            # Возвращение False, если файл конфигурации не найден

            
        


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec_()