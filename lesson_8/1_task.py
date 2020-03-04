# mobile numbers
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# Let's dive into decorators! You are given mobile numbers.
# Sort them in ascending order then print them in the standard format shown below:
# +91 xxxxx xxxxx
# The given mobile numbers may have +91, 91 or 0 written before the actual digit number.
# Alternatively, there may not be any prefix at all.
# Input Format
# The first line of input contains an integer, the number of mobile phone numbers.
# lines follow each containing a mobile number.
# Output Format
# Print mobile numbers on separate lines in the required format.
#
# Sample Input
# 3
# 07895462130
# 919875641230
# 9195969878
#
# Sample Output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230


def phones_fixer(func):
    def wrapper(nlist):
        result_list = []
        for numbr in nlist:
            result = list(numbr)
            if '+91' in numbr:
                if 10 < len(numbr) < 12:
                    result.insert(3, ' ')
                    result.insert(-5, ' ')
                else:
                    return 'The number is not correct'
            elif len(numbr) == 11:
                result.insert(0, '+')
                result.insert(1, '9')
                result.insert(2, '1')
                result.insert(3, ' ')
                result.remove(result[4])
                result.insert(-5, ' ')
            elif len(numbr) == 12:
                result.insert(0, '+')
                result.insert(3, ' ')
                result.insert(-5, ' ')
            elif len(numbr) == 10:
                result.insert(0, '+')
                result.insert(1, '9')
                result.insert(2, '1')
                result.insert(3, ' ')
                result.insert(-5, ' ')
            else:
                return 'The number is not correct'
            result_list.append(''.join(result))
        return func(result_list)
    return wrapper


@phones_fixer
def sort_numbers(numbers_list):
    return '\n'.join(sorted(numbers_list))


def read_numbers():
    n = int(input('Количество номеров: '))
    numbers = []
    for i in range(n):
        number = input('Введите номер: ')
        numbers.append(number)
    return numbers


if __name__ == '__main__':
    numbers = read_numbers()
    print(sort_numbers(numbers))
