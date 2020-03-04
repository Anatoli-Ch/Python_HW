# 1. Скачать архив
# https://drive.google.com/open?id=1ClMk5tVl5tDzXqc84CbDcBYHxRceztvx
# 2. Подобрать пароль (3 строчных латинских буквы).
# Для работы с архивами можно использовать модуль zipfile. Для подбора паролей - itertools.
# 3. Распаковать (в итоге получится группа папок с файлами логов в таком формате)
#  “device\tage\tsex\tcity\tuser_id\tsearch_keyword\tdomain\turl\ttype”
# 4. Создать папку и в ней для каждого города который встретится в логах,
# создать файл (вида “new_jersey.tsv”) в котором вывести все поисковые запросы
# и количество уникальных user_id с которыми они встречались (через \t)

# alabama.tsv
#    facebook\t23
#    youtube\t13
#    facebook login\t6
#    ebay\t6
import os
import zipfile
import itertools
import string


def generator():
    base = []
    letters = string.ascii_lowercase
    for item in itertools.permutations(letters, 3):
        base.append(''.join(item).encode('utf-8'))
    return base


ARCHIVE = zipfile.ZipFile('lesson6.zip', 'r')
for element in generator():
    try:
        ARCHIVE.extractall(pwd=element)
        print("\n---- УСПЕХ! {} ----".format(element.decode('utf-8')))
    except Exception:
        print("{} - не подходит.".format(element.decode('utf-8')))

TXT_FOLDER = []
for top, dirs, files in os.walk("lesson6"):
    for nm in files:
        TXT_FOLDER.append(os.path.join(top, nm))

SORTING_TXT_FOLDER = sorted(TXT_FOLDER)
count = 0
all_list = []

for i in range(0, len(SORTING_TXT_FOLDER)):
    path = SORTING_TXT_FOLDER[count]
    count += 1
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            l = line.split('\t')
            a, *b = l[3], l[4], l[6]
            all_list.append([a, b])


def write_file(city):
    body = []
    for i in all_list:
        if i[0] == city:
            value = i[1]
            try:
                url = value[1].split('.')[0]
                body.append([url, value[0]])
            except Exception:
                pass

    list_name = []
    for l in body:
        list_name.append(l[0])
    for site_name in set(list_name):
        list_id = set([l[1] for l in body if l[0] == site_name])
        number = len(list_id)
        line = '{}{}{}'.format(site_name, '\t', str(number))
        try:
            myfile.write(line + '\n')
        except Exception:
            chunk = line.encode('utf-16')
            myfile.write(chunk.decode('cp1251', 'replace') + '\n')


all_city = []
for i in all_list:
    all_city.append(i[0])
all_city = set(all_city)
all_city.remove('\\N')

os.mkdir('Cities')
os.chdir('Cities')

for city in all_city:
    if ' ' in city:
        file_name = city.replace(' ', '_') + '.tsv'
    else:
        file_name = city + '.tsv'
    print('Создан {}'.format(file_name))
    myfile = open(file_name, 'w')
    write_file(city)
    myfile.close()
