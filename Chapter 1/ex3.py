print("I will now count my chickents:")

print("Hens", 25 + 30 / 6)
# 25 + (30 / 6) evaluates to 25+5 or 30
print("Roosters", 100.00 - 25 * 3 % 4)
#100 - 25 * 3 mod 4
#100 - 75 mod 4
# 75 mod 4 or 75/4 is simply the numerator of a MIXED fraction (18 + 3/4) simplified to the max, so 3
#100 - 3 = 97

print("Now I will count the eggs:")

print(3.00 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
#3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#evaluate higher priority calculations
#3 + 2 + 1 - 5 + (0) - .25 + 6
#6 - 5 - .25 + 6
#6.75

print("Is it true that 3 + 2 < 5 - 7?")

print(3.00 + 2 < 5 - 7)
# (3 + 2) < (5 - 7)
# 5 < -2

#The following lines either print text, or print text and concatonate an evaluation.
print("What is 3 + 2?", 3.00 + 2)
print("What is 5 - 7?", 5.00 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.00 > -2)
print("Is it greater or equal?", 5.00 >= -2)
print("Is it less or equal?", 5.00 <= -2)