# Дан текст - найти все заглавные буквы и объединить их в слово.

string1 = "Help ELephant learn LOops. While's and fOrs. RLD!"
base_list = []
for i in string1:
    if i == i.upper():
        base_list.append(i)
    for j in base_list:
        if j in ".!' ":
            base_list.remove(j)
result = ''.join(base_list)
print(result)
