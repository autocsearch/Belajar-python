# 🧩 Exercise: “The Fruit Basket”
# 📝 Problem:

# Charlie owns a fruit basket 🧺. Every morning, he receives a list of fruits written line by line by his friend. But Charlie only likes apples and bananas.

# Write a Python program that:

#     Accepts an integer N — the number of fruits in the basket.
#     Accepts N fruit names (each on a new line).
#     Counts how many apples and bananas he got.
#     Ignores other fruits.
#     Prints the result in this format:

# Apples: X
# Bananas: Y

# input:
# 5
# apple
# banana
# orange
# banana
# apple

# Apples: 2
# Bananas: 2

# ✅ Requirements:

#     Input is case-insensitive (Apple, APPLE, or apple all count as "apple").

#     Ignore any fruits that aren’t apple or banana.


input = [
    5,
"apple",
"banana",
"orange",
"banana",
"apple",
"Orange",
"Patung",
"Labu",
"Apple"
"Pintar",
"Apple",
"Apple",
"APPLE",
"APPLE",
]

count_apple = 0
count_banana = 0

for x in input:
    fruit = str(x).lower()
    if fruit == "apple":
        count_apple += 1
    elif fruit == "banana":
        count_banana += 1  

print(f"apple: {count_apple} \n banana: {count_banana}")
          

    

 

