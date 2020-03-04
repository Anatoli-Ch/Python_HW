#  Реализовать класс который будет:
#       3.a читать из ввода строку
#       3.b проверять, что строка состоит только из скобочек “{}[]()<>”
#       3.c проверять, что строка является правильной скобочной последовательностью - выводить вердикт


class Brackets:
    def __init__(self):
        self.line = input('Enter a string: ')

    def read_lines(self):
        return self.line

    def check_elements(self):
        sample = '{', '}', '[', ']', '(', ')', '<', '>'
        sample1 = '{', '[', '(', '<'
        sample2 = '}', ']', ')', '>'
        meetings = 0
        for element in self.line:
            for _ in sample:
                if element in sample:
                    for elem in self.line:
                        if elem in sample1:
                            meetings += 1
                        elif elem in sample2:
                            meetings -= 1
                            if meetings < 0:
                                return False
                    return meetings == 0
                else:
                    return False


TEXT = Brackets()
print(TEXT.read_lines())
print(TEXT.check_elements())
