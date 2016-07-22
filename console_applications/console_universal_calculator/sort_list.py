import random
import string
import math


def sort_list(ls):
    ls.sort()
    return ls


#Function for custom list of integers
def generate_custom_ls_int(size):
    #List Input
    cur_index = 0
    ls = []
    #Decremented size to use lists that start at 1 instead of 0
    size -= 1
    while cur_index <= size:
        #Incremented cur_index to show a list that starts at 1 instead of 0
        item = int(eval(input("Enter item " + str(cur_index + 1) + " of the list: ")))
        ls.append(item)
        cur_index += 1

    return ls


#Function for custom list of floats
def generate_custom_ls_float(size):
    #List Input
    cur_index = 0
    ls = []
    #Decremented size to use lists that start at 1 instead of 0
    size -= 1
    while cur_index <= size:
        #Incremented cur_index to show a list that starts at 1 instead of 0
        item = float(eval(input("Enter item " + str(cur_index + 1) + " of the list: ")))
        ls.append(item)
        cur_index += 1

    return ls


#Function for custom list of strings
def generate_custom_ls_string(size):
    #List Input
    cur_index = 0
    ls = []
    #Decremented size to use lists that start at 1 instead of 0
    size -= 1
    while cur_index <= size:
        #Incremented cur_index to show a list that starts at 1 instead of 0
        item = str((input("Enter item " + str(cur_index + 1) + " of the list: ")))
        ls.append(item)
        cur_index += 1

    return ls


#Function for generating a random list of integers
def generate_random_ls_integer(size, min_val, max_val):
    ls = []

    #Increment max_val by 1 because range is exclusive for the second parameter
    max_val += 1

    for i in range(0, size):
        ls.append(random.randrange(min_val, max_val))

    return ls


#Function for generating a random list of floats
def generate_random_ls_float(size, min_val, max_val):
    ls = []

    for i in range(0, size):
        random_float = random.uniform(min_val, max_val)
        ls.append(random_float)

    return ls


#Function for generating a random list of strings
def generate_random_ls_string(size, min_length, max_length, non_letters_included, white_space_included):

    if not non_letters_included and not white_space_included:
        ls = []

        # Increment max_length by 1 because range is exclusive for the second parameter
        max_length += 1

        acceptable_chars = string.ascii_letters

        for i in range(0, size):
            random_string = ""
            # Add one to the length to ensure that there is at least 1 character
            string_len = random.randrange(min_length, max_length) + 1
            for char in range(min_length, string_len):
                random_character = random.choice(acceptable_chars)
                random_string += random_character

            ls.append(random_string)

        return ls

    elif non_letters_included and white_space_included:
        ls = []

        # Increment max_length by 1 because range is exclusive for the second parameter
        max_length += 1

        acceptable_chars = string.printable

        for i in range(0, size):
            random_string = ""
            # Add one to the length to ensure that there is at least 1 character
            string_len = random.randrange(min_length, max_length) + 1
            for char in range(min_length, string_len):
                random_character = random.choice(acceptable_chars)
                random_string += random_character

            ls.append(random_string)

        return ls

    elif non_letters_included and not white_space_included:
        ls = []

        # Increment max_length by 1 because range is exclusive for the second parameter
        max_length += 1

        acceptable_chars = string.ascii_letters + string.digits + string.punctuation

        for i in range(0, size):
            random_string = ""
            # Add one to the length to ensure that there is at least 1 character
            string_len = random.randrange(min_length, max_length) + 1
            for char in range(min_length, string_len):
                random_character = random.choice(acceptable_chars)
                random_string += random_character

            ls.append(random_string)

        return ls

    elif not non_letters_included and white_space_included:
        ls = []

        # Increment max_length by 1 because range is exclusive for the second parameter
        max_length += 1

        acceptable_chars = string.ascii_letters + string.whitespace

        for i in range(0, size):
            random_string = ""
            # Add one to the length to ensure that there is at least 1 character
            string_len = random.randrange(min_length, max_length) + 1
            for char in range(min_length, string_len):
                random_character = random.choice(acceptable_chars)
                random_string += random_character

            ls.append(random_string)

        return ls


