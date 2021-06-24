import pymorphy2
import random
from random import randint
morph = pymorphy2.MorphAnalyzer()
def dirt_morph_1():
    dirty_words = ['Сраный','Долбаный','Ничтожный','Бесполезный','Лучший','Прекрасный', 'Замечательный']
    dirty = random.choice(dirty_words)
    dirand_1 = morph.parse(dirty)[0]
    return dirand_1
def dirt_morph_2():
    dirty_words_2 = ['Сраный','Долбаный','Ничтожный','Бесполезный','Лучший','Прекрасный', 'Замечательный']
    dirty_2 = random.choice(dirty_words_2)
    dirand_2 = morph.parse(dirty_2)[0]
    return dirand_2
def hour_morph():
    hourses = morph.parse('Час')[0]
    return hourses
def minu_morph():
    minutes = morph.parse('Минута')[0]
    return minutes


def number_to_words(n):
    f = {0o1: 'один', 0o2: 'два', 0o3: 'три', 0o4: 'четыре', 0o5: 'пять',
         0o6: 'шесть', 0o7: 'семь', 0x8: 'восемь', 0x9: 'девять'}
    o = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
         50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
         80: 'восемьдесят', 90: 'девяносто'}
    s = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
         14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
         17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
    n1 = n % 10
    n2 = n - n1
    if n < 10:
        return f.get(n)
    elif 10 < n < 20:
        return s.get(n)
    elif n >= 10 and n in o:
        return o.get(n)
    else:
        return o.get(n2) + ' ' + f.get(n1)
