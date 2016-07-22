import time
import random


def bubble_sort(ls):
    #Time Algorithm
    start = time.time()

    #Bubble Sort
    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                temp = ls[i]
                ls[i] = ls[j]
                ls[j] = temp

    end = time.time()

    runtime = end - start
    big_o = """
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
    return [str(ls), runtime, big_o]


def insertion_sort(ls):
    #Time Algorithm
    start = time.time()
    #Insertion Sort
    for i in range(0, len(ls)):
        temp = ls[i]
        j = i
        while j > 0 and ls[j - 1] > temp:
            ls[j] = ls[j - 1]
            j -= 1
        ls[j] = temp

    end = time.time()
    runtime = end - start
    big_o = """
    Best Case: O(n)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
    return [str(ls), runtime, big_o]


def selection_sort(ls):
    #Time Algorithm
    start = time.time()
    #Selection Sort
    for i in range(0, len(ls)):
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        if min_index != i:
            temp = ls[i]
            ls[i] = ls[min_index]
            ls[min_index] = temp

    end = time.time()
    runtime = end - start
    big_o = """
    Best Case: O(n^2)
    Average Case: O(n^2)
    Worst Case: O(n^2)
    """
    return [str(ls), runtime, big_o]


#Quick sort manager
def quick_sort(ls):
    #Time Algorithm
    start = time.time()

    #Quick Sort
    ls = quick_sort_exec(ls)

    end = time.time()
    runtime = end - start

    big_o = """
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n^2)
    """

    return [str(ls), runtime, big_o]


#Quicksort execution
def quick_sort_exec(ls):
    less = []
    equal = []
    greater = []

    if len(ls) > 1:
        pivot = ls[0]
        for x in ls:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort_exec(less) + equal + quick_sort_exec(greater)

    else:
        return ls


#Function for custom list
def generate_custom_ls(size):
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

    #Convert list of strings to a list of ints
    ls = list(map(int, ls))
    return ls


#Function for random list
def generate_random_ls(size, min_val, max_val):
    ls = []

    #Randrange is exclusive
    max_val += 1

    for i in range(0, size):
        ls.append(random.randrange(min_val, max_val))

    #Convert list of strings to a list of ints
    ls = list(map(int, ls))
    return ls
