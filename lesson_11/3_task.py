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
        while '()' in self.line or '[]' in self.line or '{}' in self.line or '<>' in self.line:
            self.line = self.line.replace('()', '')
            self.line = self.line.replace('[]', '')
            self.line = self.line.replace('{}', '')
            self.line = self.line.replace('<>', '')
        return not self.line


TEXT = Brackets()
print(TEXT.read_lines())
print(TEXT.check_elements())
