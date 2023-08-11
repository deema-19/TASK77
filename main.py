# q1:
# def print_number_pattern(rows):
#     for i in range(1, 6):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
#
# def main():
#     rows = int(input("Enter the number of rows: "))
#     print_number_pattern(rows)
#
# main()


# q2:
# def calculate_sum(num):
#     sum = 0
#     for i in range(1, num + 1):
#         sum += i
#     return sum
#
# num = int(input("Enter your number: "))
# result = calculate_sum(num)
# print(result)

# q3:
# def print_name_pattern(name):
#     for i in range(0, len(name)):
#         print(name[:i + 1])
#
#     for i in range(len(name)):
#         print(name[:len(name) - i])
#
# def main():
#     name = input("Enter your name: ")
#     print_name_pattern(name)
# main()

# q4:
# def reverse_word(word):
#     reversed_word = word[::-1]
#     return reversed_word
#
# def main():
#     word = input("Enter a word: ")
#     reversed_word = reverse_word(word)
#     print("Reversed word:", reversed_word)
#
# main()


# q5:
# def print_numbers_in_reverse_range(x):
#     while x >= 1:
#         print(x, end=" ")
#         x -= 1
#
# def main():
#     range_value = int(input("Enter range: "))
#     print_numbers_in_reverse_range(range_value)
#
# main()


# q6:
# def print_multiples(num, count):
#     while count <= 10:
#         multiple = num * count
#         print(multiple, end=" ")
#         count += 1
#
# def main():
#     num = 5
#     count = 1
#     print_multiples(num, count)
#
# main()


# q7:
# def print_multiples_within_limit(Limit_number, Max_display_on_screen, Target_number):
#     count = 0
#     multiple = Target_number
#
#     while multiple <= Limit_number and count < Max_display_on_screen:
#         print(multiple, end=" ")
#         multiple += Target_number
#         count += 1
#
# def main():
#     Limit_number = int(input("Enter the Limit_number: "))
#     Max_display_on_screen = int(input("Enter the maximum outputs to display (Max_display_on_screen): "))
#     Target_number = int(input("Enter the Target_number: "))
#
#     print_multiples_within_limit(Limit_number, Max_display_on_screen, Target_number)
#
# main()