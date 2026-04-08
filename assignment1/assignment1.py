# Write your code here.
# pytest -v -x assignment1-test.py


# Task 1
def hello():
    return "Hello!"


# Task 2
def greet(name):
    return f"Hello, {name}!"


# Task 3
# Operands: add, subtract, multiply, divide, modulo, int_divide (for integer division) and power
def calc(v1, v2, op="multiply"):

    if op == "add":
        return v1 + v2
    elif op == "subtract":
        return v1 - v2
    elif op == "multiply":
        try:
            v1 * v2
        except TypeError:
            return "You can't multiply those values!"
        else:
            return v1 * v2
    elif op == "divide":
        try:
            v1 / v2
        except ZeroDivisionError:
            return "You can't divide by 0!"
        else:
            return v1 / v2
    elif op == "modulo":
        return v1 % v2
    elif op == "int_divide":
        try:
            v1 / v2
        except ZeroDivisionError:
            return "You can't divide by 0!"
        else:
            return v1 // v2
    elif op == "power":
        return v1**v2


# Task 4
# Types requested: float, str, or int.
def data_type_conversion(value, type_requested):

    try:
        match type_requested:
            case "float":
                converted_value = float(value)
            case "str":
                converted_value = str(value)
            case "int":
                converted_value = int(value)
            case _:
                return f"Please select float, string or integer for the type_requested argument."
    except ValueError:
        return f"You can't convert {value} into a {type_requested}."
    return converted_value


# Task 5
# Arbitrary number of parameters, computes the average, and returns the grade by scale:
# A: 90 and above
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60
def grade(*args):

    try:
        grade_num = sum(args) / len(args)
        if grade_num >= 90:
            grade = "A"
        elif grade_num >= 80:
            grade = "B"
        elif grade_num >= 70:
            grade = "C"
        elif grade_num >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade
    except TypeError:
        return "Invalid data was provided."


# Task 6
# Two parameters, a string and a count, returns a new string that is the old one repeated count times
def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result


# Task 7
# One positional parameter ("best" or "mean"), arbitrary number of keyword parameters.
# "best": the name of the student with the higest score is returned.
# "mean": the average score is returned.
def student_scores(position, **kwargs):

    match position:
        case "best":
            highest_score = 0
            student = ""
            # Checking the dictionary of students and grades to find the highest score
            for key, value in kwargs.items():
                if value > highest_score:
                    highest_score = value
                    student = key
            return student

        case "mean":
            return sum(kwargs.values()) / len(kwargs.values())


# Task 8
# The rules for title capitalization are:
# (1) The first word is always capitalized.
# (2) The last word is always capitalized.
# (3) All the other words are capitalized, except little words. For the purposes of this task,
# the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
def titleize(name):

    title = ""
    words = name.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            title += word.capitalize() + " "
        elif word in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            title += word + " "
        else:
            title += word.capitalize() + " "

    return title.strip()


# Task 9
# Two parameters, both strings, the secret and the guess.
# A string with each letter not in a guess masked with "_" is returned
def hangman(secret, guess):

    word = ""
    letters = list(guess)

    for i in list(secret):
        if i in letters:
            word += i
        else:
            word += "_"

    return word


# Task 10
# Each word is modified according to the following rules.
# (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end.
# (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them.
# (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
# Currently does not account for double qq, test case fails


def pig_latin(sentence):

    result = ""

    for word in sentence.split():
        print("word", word)

        # Find the index of the first vowel
        vowels = [word.find(v) for v in "aeiou"]
        vowels = [p for p in vowels if p != -1]
        first_vowel = min(vowels)

        # Find the index of "qu" case
        qu = [word.find(v) for v in "qu"]
        qu = [p for p in qu if p != -1]
        qu = min(qu) if qu else -1

        # Slice the word into parts before and after the first vowel
        before_vowel = word[:first_vowel]
        after_vowel = word[first_vowel:]
        qu = word[qu : qu + 2]

        if qu:
            result += after_vowel + before_vowel + qu + "ay"
        else:
            result += after_vowel + before_vowel + "ay "

    return result.strip()


pig_latin("banana")
pig_latin("apple")
