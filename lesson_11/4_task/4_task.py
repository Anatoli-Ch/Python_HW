#  У вас несколько JSON файлов.
#  В каждом из этих файлов есть произвольная структура данных.
#  Вам необходимо написать класс который будет описывать работу с этими файлами, а именно:
#       4.a запись в файл
#       4.b чтение из файла
#       4.c объединение данных из файлов в новый файл
#       4.d получить относительный путь к файлу
#       4.e получить абсолютный путь к файлу
import os
import json


class Filer:
    def __init__(self, file, enter_string, str1, str2, str3):
        self.file = file
        self.enter_string = enter_string
        self.str1 = str1
        self.str2 = str2
        self.str3 = str3

    def file_write(self):
        to_json = {"text": self.enter_string}
        with open(self.file, 'w') as f:
            f.write(json.dumps(to_json))

    def file_read(self):
        with open(self.file, 'r') as f:
            print(f.read())

    def file_merge(self):
        with open(self.str1, 'r') as finput:
            json1 = json.load(finput)
        with open(self.str2, 'r') as finput:
            json2 = json.load(finput)
        with open(self.str3, 'r') as finput:
            json3 = json.load(finput)

        merged = json1.copy()
        merged.update(json2)
        merged.update(json3)

        with open('output.json', 'w') as foutput:
            json.dump(merged, foutput)

    def relative_path(self):
        with open(self.file, 'r'):
            this_dir = os.path.abspath('output.json')
        print(this_dir)

    def absolute_path(self):
        with open(self.file, 'r'):
            dir_path = os.path.dirname(os.path.realpath('output.json'))
        print(dir_path)


if __name__ == '__main__':
    ENTER = 'this is my first json string'
    FIRST_STEP = Filer('file3.json', ENTER, str1=None, str2=None, str3=None)
    SECOND_STEP = Filer('file3.json', ENTER, str1=None, str2=None, str3=None)
    THIRD_STEP = Filer(file=None, enter_string=None, str1='file1.json', str2='file2.json', str3='file3.json')
    FOURTH_STEP = Filer('output.json', enter_string=None, str1=None, str2=None, str3=None)
    FIFTH_STEP = Filer('output.json', enter_string=None, str1=None, str2=None, str3=None)
    FIRST_STEP.file_write()
    SECOND_STEP.file_read()
    THIRD_STEP.file_merge()
    FOURTH_STEP.relative_path()
    FIFTH_STEP.absolute_path()
