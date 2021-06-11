"""

Task 3

"""

tutors = ['Виталий', 'Семен', 'Татьяна', 'Нина',
          'Маша', 'Юрий', 'Никита', 'Владимир']
klasses = ['11Б', '8В', '5А', '9В', '4Г', '1Б', '10Б', '9А', '3Б']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


from itertools import zip_longest

gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

