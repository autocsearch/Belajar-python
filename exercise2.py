# 📝 Story:

# You’ve been hired as the mayor of Numberland, where villagers only accept even or odd numbers as citizens 🏡. Your job is to sort them properly

# Write a program that:
#     Accepts an integer N — the number of villagers.
#     Accepts N numbers (one per line).
#     Counts how many are even and how many are odd.
#     Prints the result like:

# Even: X
# Odd: Y

# 🧪 Sample Input:

# 7
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# 📤 Sample Output:

# Even: 3
# Odd: 4

input = [7, 1, 2, 3, 4, 5, 6, 7]

even_number = 0
odd_number = 0

for n in input:
    if n % 2 == 0:
        even_number += 1
    elif n % 2 != 0: 
        odd_number += 1
        

print(f"odd : {odd_number} \n even : {even_number}")
       



# print(f"even: {even_number} \n odds: {odd_number}")
