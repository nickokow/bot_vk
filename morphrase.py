import pymorphy2

word = 'Час'
morph = pymorphy2.MorphAnalyzer()
word = morph.parse(word)[0]
cases = (('nomn', 'именительный'),
         ('gent', 'родительный'),
         ('datv', 'дательный'),
         ('accs', 'винительный'),
         ('ablt', 'творительный'),
         ('loct', 'предложный'))
numbers = (('sing', 'Единственное'), ('plur', 'Множественное'))
if 'NOUN' in word.tag:
    for i in numbers:
        print(f"{i[1]} число:")
        for j in cases:
            print(f"{j[1].capitalize()} падеж: {word.inflect({i[0], j[0]}).word}")
else:
    print('Не существительное')
