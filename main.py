# # task 1
# import random
# numbers = []
# nums_length = 10
# negatives = 0
# evens = 0
# odds = 0
# divides3 = 1
# num1 = 0
# num2 = 0
# product_min_max = 1
# first_positive = 0
# last_positive = 0
# sum_of_elements = 0
#
# # Сумa негативних чисел, сума парних чисел та сума непарних
#
# for num in range(nums_length):
#     numbers.append(random.randint(-10, 10))
# print(numbers)
# print()
#
# for num in numbers:
#     if num < 0:
#         negatives += num
#     if num % 2 == 0:
#         evens += num
#     if num % 2 != 0:
#         odds += num
#
# # Добуток елементів з кратними індексами 3
#
# for index in range(len(numbers)):
#     if index % 3 == 0:
#         divides3 *= numbers[index]
# print(f"The sum of negative numbers is {negatives}")
# print()
# print(f"The sum of even numbers is {evens}")
# print()
# print(f"The sum of odd numbers is {odds}")
# print()
# print(f"The product of elements indices of which are divisible by three is {divides3}")
# print()
#
# # Добуток елементів між мінімальним та максимальним елементом
#
# try:
#     min_num = min(numbers)
#     max_num = max(numbers)
#     for i in numbers:
#         if min_num < i < max_num:
#             product_min_max *= i
#     print(f"The product of elements between the min and max numbers is {product_min_max}")
# except Exception as e:
#     print(f"An error occurred: {e}")
# print()
#
# # Сума елементів, що знаходяться між першим та останнім позитивними елементами
# try:
#     for num in numbers:
#         if num > 0:
#             first_positive = num
#             print(f"First positive: {first_positive}")
#             break
#     for num in reversed(numbers):
#         if num > 0:
#             last_positive = num
#             print(f"Last positive: {last_positive}")
#             break
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# try:
#     index_1 = numbers.index(first_positive)
#     index_2 = numbers.index(last_positive)
#
#     for numb in numbers:
#         if index_1 < numbers.index(numb) < index_2:
#             sum_of_elements += numb
#     print(f"This is the sum of numbers between the first and last positive: {sum_of_elements}")
# except Exception as e:
#     print(f"Error occurred: {e}")

# # task 2
# import random
# numbers = []
# even_numbers = []
# odd_numbers = []
# negative_numbers = []
# positive_numbers = []
# nums_length = 10
#
# for num in range(nums_length):
#     numbers.append(random.randint(-10, 10))
# print(f"This is the initial lit: {numbers}")
# print()
#
# try:
#     for num in numbers:
#         if num < 0:
#             negative_numbers.append(num)
#         if num % 2 == 0:
#             even_numbers.append(num)
#         if num % 2 != 0:
#             odd_numbers.append(num)
#         if num >= 0:
#             positive_numbers.append(num)
# except Exception as e:
#     print(f"An error occurred: {e}")
# print(f"This list contains only negative numbers: {negative_numbers}")
# print(f"This list contains only even numbers: {even_numbers}")
# print(f"This list contains only odd numbers: {odd_numbers}")
# print(f"This list contains only positive numbers: {positive_numbers}")

# all done