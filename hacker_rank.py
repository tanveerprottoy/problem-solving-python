import sys
from typing import List

import core


def diagonals(arr):
    length = len(arr[0])
    primary_diagonal = list()
    secondary_diagonal = list()
    for i in range(length):
        primary_diagonal.append(arr[i][i])
        secondary_diagonal.append(arr[i][length - i - 1])
    print(primary_diagonal)
    print(secondary_diagonal)


def absolute_diagonal_difference(arr):
    length = len(arr[0])
    primary_sum = 0
    secondary_sum = 0
    for i in range(length):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][length - i - 1]
    print(primary_sum)
    print(secondary_sum)
    print(abs(primary_sum - secondary_sum))


# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
# Print the decimal value of each fraction on a new line.
def decimal_of_fractions(arr, n):
    counter_list = list([0, 0, 0])
    for i in range(n):
        if arr[i] > 0:
            counter_list[0] += 1
        elif arr[i] < 0:
            counter_list[1] += 1
        elif arr[i] == 0:
            counter_list[2] += 1
    print('{0:.6f}'.format(round(counter_list[0] / n, 6)))
    print('{0:.6f}'.format(round(counter_list[1] / n, 6)))
    print('{0:.6f}'.format(round(counter_list[2] / n, 6)))


# Consider a staircase of size n = 4
#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces.
# The last line is not preceded by any spaces
# Write a program that prints a staircase of size n
def staircase_builder(n):
    value = '#'
    ws = ' '
    lb = '\n'
    start_index = n - 1
    result = ''
    ran = range(n)
    for i in ran:
        for j in ran:
            if j >= start_index:
                result += value
            else:
                result += ws
        result += lb
        start_index -= 1
    print(result)


# Given five positive integers, find the minimum and maximum values
# that can be calculated by summing exactly four of the five integers.Then print the respective minimum
# and maximum values as a single line of two space-separated long integers.
# For example 1 2 3 4 5 . Our minimum sum is  and our maximum sum is . We would print
# 10 14
def min_max_sum(nums: List[int]):
    nums.sort()
    min_sum = 0
    max_sum = 0
    length = len(nums)
    min_values = list()
    max_values = list()
    for i in range(length):
        if i < 4:
            min_sum += nums[i]
            min_values.append(nums[i])
        if i >= length - 4:
            max_sum += nums[i]
            max_values.append(nums[i])
    print(nums)
    print(min_sum)
    print(max_sum)
    print(min_values)
    print(max_values)
    print(min_sum.__str__() + ' ' + max_sum.__str__())


# You are in charge of the cake for your niece's birthday and have decided the cake will have
# one candle for each year of her total age. When she blows out the candles, she’ll only be able
# to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
# For example, if your niece is turning 4 years old, and the cake will have candles of height 4, 4, 1, 3
# she will be able to blow out  candles successfully, since the tallest candles are of height
# and there are 2 such candles.
# this problem is essentially finding the count of max value in an array
def birthday_cake_candles(arr):
    max_value = 0
    max_value_count = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            # reset the counter as it could hold previous count
            if max_value_count > 0:
                max_value_count = 0
            max_value_count += 1
        elif arr[i] == max_value:
            max_value_count += 1
    print(max_value)
    print(max_value_count)


# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
def time_conversion(time):
    splits = time.split(':')
    time_postfix = splits[2][2:4]
    splits[2] = splits[2][:2]
    if time_postfix == 'PM':
        hour_int = int(splits[0])
        if hour_int < 12:
            splits[0] = str(12 + hour_int)
    elif time_postfix == 'AM':
        if splits[0] == '12':
            splits[0] = '00'
    converted_time = splits[0] + ':' + splits[1] + ':' + splits[2]
    print(converted_time)


# If the difference between the grade and the next multiple of 5 is less than 3,
# round grade up to the next multiple of 5.
# If the value of grade is less than 40, no rounding occurs as the result will still be a failing grade.
# For example,  will be rounded to  but  will not be rounded because the rounding would result
def grading_students(grades):
    rounded_grades = list()
    grade_values = ''
    for grade in grades:
        if grade > 37:
            diff_next_multiple = 5 - (grade % 5)
            if diff_next_multiple < 3:
                grade += diff_next_multiple
        rounded_grades.append(grade)
        grade_values += str(grade) + '\n'
    print(grade_values)
    return rounded_grades


# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise
def number_line_jump(x1, v1, x2, v2):
    # x1, x2 <= 10000
    # check the x and v and compare the rate
    # 0 3 4 2 => YES
    print(
        "inputs: ",
        x1, v1, x2, v2
    )
    max_val = 1000000
    former = 0
    later = 0
    former_rate = 0
    later_rate = 0
    if x1 > x2:
        # v2 has to be larger
        if v1 >= v2:
            return "NO"
        former = x2
        later = x1
        former_rate = v2
        later_rate = v1
    if x2 > x1:
        # v1 has to be larger
        if v2 >= v1:
            return "NO"
        former = x1
        later = x2
        former_rate = v1
        later_rate = v2
    # for i in range(0, max_val):
    #     later_steps = abs((multiple - later) // later_rate)
    #     former_steps = abs((multiple - former) // former_rate)
    #     if former_steps == later_steps:
    #         print(
    #             "later, former, multiple, later_steps, former_steps",
    #             later, former, multiple, later_steps, former_steps
    #         )
    #         return "YES"
    return "NO"


def number_line_jump1(x1, v1, x2, v2):
    # x1, x2 <= 10000
    # check the x and v and compare the rate
    # 0 3 4 2 => YES
    print(
        "inputs: ",
        x1, v1, x2, v2
    )
    max_val = 1000000
    former = 0
    later = 0
    former_rate = 0
    later_rate = 0
    if x1 > x2:
        # v2 has to be larger
        if v1 >= v2:
            return "NO"
        former = x2
        later = x1
        former_rate = v2
        later_rate = v1
    if x2 > x1:
        # v1 has to be larger
        if v2 >= v1:
            return "NO"
        former = x1
        later = x2
        former_rate = v1
        later_rate = v2
    multiples = core.multiples(former - former_rate, 1, max_val)
    for i in range(0, len(multiples)):
        multiple = multiples[i]
        if multiple % later_rate == 0:
            later_steps = abs((multiple - later) // later_rate)
            former_steps = abs((multiple - former) // former_rate)
            if former_steps == later_steps:
                print(
                    "later, former, multiple, later_steps, former_steps",
                    later, former, multiple, later_steps, former_steps
                )
                return "YES"
    return "NO"


array = [[11, 2, 4], [4, 5, 6], [10, 8, - 12]]
# diagonals(array)
# absolute_diagonal_difference(array)
# decimal_of_fractions([-4, 3, -9, 0, 4, 1], 6)
# staircase_builder(10)
# min_max_sum([7, 3, 9, 1, 5])
# birthday_cake_candles([4, 4, 1, 3])
# time_conversion('12:45:54PM')
# print(grading_students([73, 67, 38, 33]))
# print(number_line_jump(0, 3, 4, 2))
# print(number_line_jump(0, 2, 5, 3))
# print(number_line_jump(2, 1, 1, 2))
# print(number_line_jump(4523, 8092, 9419, 8076))
# print(number_line_jump(43, 2, 70, 2))  # NO
print(number_line_jump(21, 6, 47, 3))  # NO
# print(number_line_jump(1571, 4240, 9023, 4234))  # YES