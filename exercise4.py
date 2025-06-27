# 🧩 Exercise 4: “The Oddball Market”

# Level: Easy → Medium
# 📝 Problem:

# You are managing a number stall at the Oddball Market, where customers only buy numbers that are not divisible by 3. The first line contains a number N indicating how many customer numbers you'll receive.

# Your task is to:
#     Read N integers from input (one per line).
#     Print how many of them are divisible by 3.
#     Print how many are not divisible by 3.
#     Print the sum of all numbers not divisible by 3.
# 📥 Input Example:

# 6
# 3
# 5
# 9
# 10
# 12
# 7

# 📤 Output Example:

# Divisible by 3: 3
# Not divisible by 3: 3
# Sum of not divisible by 3: 22

# ✅ Notes:

#     The first number is the count → N
#     You must process only the next N numbers
#     Use % to check divisibility


input = [6, 3, 5, 9, 10, 12, 7]

divisible_3 = 0
not_divisible_3 = 0 
sum_of_not_ddivisible_3 = 0

for n in input[1:]:
    if n % 3 == 0:
        divisible_3 += 1
    elif n % 3 != 0:
        not_divisible_3 += 1
        sum_of_not_ddivisible_3 += n


print(f"divisible by 3 : {divisible_3} \n not divisible : {not_divisible_3} \n sum of not divisible by 3 : {sum_of_not_ddivisible_3}")
    