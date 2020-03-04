# Вам дано целое число N.
# Ваша задача напечатать алфавит ранголи размером N.
# (Ранголи - это форма индийского народного искусства, основанная на создании узоров.)
# В центре ранголи есть первая буква алфавита a , а на границе - буква алфавита (в алфавитном порядке).


def rangoly(size):
    alpha = ['a']
    for i in range(size - 1):
        alpha.append(chr(ord(alpha[i]) + 1))
    poped = []
    beta = list(alpha)
    beta.reverse()
    beta.pop()
    full_list = list(beta)
    full_list.extend(alpha)
    max_len = len('-'.join(full_list))
    for j in range(1, size + 1):
        m_str = ''
        if (j - 1) > 0:
            m_str = '-'.join(beta[:j - 1]) + '-'
        m_str += '-'.join(alpha[j * -1:])
        string = '{s:{c}^{n}}'.format(s=m_str, n=max_len, c='-')
        poped.append(string)
    print('\n'.join(poped))
    poped.pop()
    poped.reverse()
    print('\n'.join(poped))


rangoly(int(input('Введите размер: ')))
