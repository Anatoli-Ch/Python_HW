# Из текстового файла удалить все слова, содержащие от трех до пяти символов,
# но при этом из каждой строки должно быть удалено только четное количество таких слов.

base = []
examples = [5, 4, 3]
file = open('text.txt', 'r', encoding='windows-1251')
text = file.readlines()
for elements in text:
    for word in elements.split():
        base.append(word)

for example in examples:
    for elem in base:
        if len(elem) == example:
            base.remove(elem)
file.close()

file_write = open('text.txt', 'w', encoding='windows-1251')
for i in base:
    if i[-1] == '.':
        file_write.write(i + ' ' + '\n')
    else:
        file_write.write(i + ' ')
file_write.close()
