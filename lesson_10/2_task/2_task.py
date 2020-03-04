# Текстовый файл содержит записи о телефонах и их владельцах.
# Переписать в другой файл телефоны тех владельцев, фамилии которых начинаются с букв К и С.


def work_in_file(file):
    lst = []
    result = []
    result2 = []
    with open(file, 'r') as f:
        for line in f.readlines():
            lst.append(line.strip('\t\n'))
        for element in lst:
            if 'K' in element[10:11]:
                result.append(element)
            elif 'C' in element[10:11]:
                result2.append(element)
    output = result + result2
    file2 = open('output.txt', 'w')
    for elem in output:
        file2.write(elem + '\n')
    file2.close()


work_in_file('base.txt')
