# 🧩 Python Challenge #3: “Sum of Even & Odd”
# 📝 Story:

# In the land of Sumatra Digitia, the villagers not only want to know how many odd and even numbers there are—but also the total sum of each kind!

# Write a program that:

#     - Accepts an integer N — the number of values.
#     - Accepts N integers.

#     Calculates:
#     - The total number of even and odd numbers.
#     - The sum of all even numbers.
#     - The sum of all odd numbers.

# Then prints it like this:

# Even count: X
# Even sum: Y
# Odd count: A
# Odd sum: B

# 🧪 Sample Input:

# 6
# 3
# 4
# 7
# 10
# 11
# 2

# 📤 Sample Output:

# Even count: 3
# Even sum: 16
# Odd count: 3
# Odd sum: 21

input = [6, 3, 4, 7, 10, 11, 2]

even_count = 0
even_sum = 0
odd_count = 0
odd_sum = 0

for n in input[1:]: 
    if n % 2 == 0:
        even_count += 1
        even_sum += n
    elif n % 2 != 0:
        odd_count += 1
        odd_sum += n
        
print(f"even sum : {even_sum} \n even count : {even_count}")
print(f"odd sum : {odd_sum} \n odd count : {odd_count}")

        
