empty_string = ''
string_sample = "Hello world world"
string_sample2 = "first letteR is loweRcase"
string_sample3 = "extra whitespace sting" \
#german_sample = "der Fluß"

# print(string_sample[0])
# print(string_sample[0:5])
# print(string_sample[:])
# print(string_sample[0::2])
#
# test_string = "Hello world. It's a beautiful day."
# print(test_string[0:5], test_string[19:29])
# print(len(test_string))
# print(test_string.find("beautiful"))
# print(len("beautiful"))
# print(test_string[19:29])
# print(test_string.upper())
# print(test_string[0:5].upper())
# print(test_string[0:5].upper(), test_string)
# print(test_string.lower())
# print(string_sample2.capitalize())
#
# user_name = "pEtra"
# print(user_name)
# user_name = user_name.lower().capitalize()


# print(user_name.lower().capitalize())
# print(user_name.capitalize().lower())
# print(user_name)

# search_string = "12457"
# print(string_sample.find("world"))
# print(string_sample.count(search_string))
#
# print("world" in string_sample)
# print("word" in string_sample)
# print(string_sample + " " + string_sample2)
# print(string_sample, ".", string_sample2)
# worker = "John"
# worker2 = "Mary"
# salary = 1000
# salary2 = 2000
# worker_string = "John's salary is", salary
# print(worker + worker_string, salary)
# print(worker2 + worker_string, salary2)
#
# price_string = "This {product:} costs {price:.2f} euros"  # .2f stands fpr 2 numbers after decimal point f - float
# print(price_string.format(price=350, product="computer"))
# id_code = input("Please enter your national ID: ")
#
# if len(id_code) == 11:
#     print("Your ID code is", id_code)
# elif len(id_code) > 11:
#     print("The code you entered is longer than 11 digits")

some_string = "Hello world. It's a beautiful day."
some_number = 300
# # print(len(some_string))
# #
# # if "beautiful" in some_string:
# #     print("beautiful is in some_string variable")
# # else:
# #     print("beautiful is NOT in some_string variable")
# if len(some_string[0:5]) < 10:
#     print("Some string is shorter than 10 characters")
# elif len(some_string[0:5]) > 20:
#     print("Some string is also greater than 20 characters")
# #
# # if "beautiful" in some_string:
# #     print("beautiful is in some_string variable")
# # else:
# #     print("beautiful is NOT in some_string variable")
# if len(some_string) > 10:
#     print("Some string is greater than 10 characters")
# elif len(some_string) > 20:
#     print("Some string is also greater than 20 characters")
if some_number < 10 or some_number < 200:
    print("all good")
else:
    print("ERROR")