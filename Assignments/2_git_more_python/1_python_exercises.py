# Exercise nr. 1
list_of_number = [5, 2, 15, 7, 36, 41, 4]


def sum_of_even(list_of_numbers):
    sum_of_even_numbers = sum([number for number in list_of_numbers if number % 2 == 0])
    return sum_of_even_numbers


print(sum_of_even(list_of_number))

# Exercise nr. 2
list_of_strings = ['cat', 'pineapple', 'grandmother', 'wisdom', 'constitution', 'dog']


def string_length_check(list_of_strings):
    list_of_length_strings = [word for word in list_of_strings if len(word) > 5]
    return list_of_length_strings


print(string_length_check(list_of_strings))

# Exercise nr. 3
list_of_people = [
    {
        'name': 'Ernestas',
        'age': 16,
    },
    {
        'name': "Agne",
        'age': 24,
    },
    {
        'name': 'Tommy',
        'age': 35
    }
]


def names_of_adults(list_of_people):
    list_of_adults = [person['name'] for person in list_of_people if person['age'] > 18]
    return list_of_adults


print(names_of_adults(list_of_people))

# Exercise nr. 4
word_string = "This is an example string that will be checked for the longest word"


def find_longest_word(string):
    word_list = string.split(' ')
    longest_word_length = len(max(word_list, key=len))
    longest_words = [word for word in word_list if len(word) == longest_word_length]
    return longest_words


print(find_longest_word(word_string))

# Exercise nr. 5
list_of_numbers_1 = [4, 5, 8, 12, 25, 45]
list_of_numbers_2 = [3, 5, 9, 11, 25, 45, 16]


def find_matching_numbers(list_1, list_2):
    matching_numbers = [number for number in list_1 if number in list_2]
    return matching_numbers


print(find_matching_numbers(list_of_numbers_1, list_of_numbers_2))

# Exercise nr. 6
list_of_tuples = [
    ('Ernestas', 25),
    ('Tomas', 45),
    ('Jonas', 29),
    ('Ana', 32),
    ('Jean', 27),
]


def find_over_30_year_old(list_of_tuples):
    over_thirty_year_old = [person for person, age in list_of_tuples if age > 30]
    return over_thirty_year_old


print(find_over_30_year_old(list_of_tuples))

# Exercise nr. 7
dict_of_grades = {
    'math': 7,
    'history': 9,
    'biology': 10,
    'chemistry': 4,
    'english': 10
}


def get_average_grade(dict_of_grades):
    all_grades = [dict_of_grades[grade] for grade in dict_of_grades]
    return sum(all_grades) / len(all_grades)


print(get_average_grade(dict_of_grades))


# Exercise nr. 8
def reverse_words(string):
    all_words = ' '.join([word[::-1] for word in string.split(' ')])
    return all_words


print(reverse_words(word_string))


# Exercise nr. 9
def sort_numbers_descending(list_of_numbers):
    list_of_numbers.sort(reverse=True)
    return list_of_numbers


print(sort_numbers_descending(list_of_number))


# Exercise nr. 10
def sort_word_list_descending(word_list):
    word_list.sort(key=len)
    return word_list


print(sort_word_list_descending(list_of_strings))
