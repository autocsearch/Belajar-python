# 🧩 Exercise 7.1: Toxic Readings Filter

# Level: Medium
# Theme: Filtering + power math
# ☣️ Story:

# You’re monitoring a pipeline of toxic chemical readings. Each reading is a number, but only odd negative readings are dangerous and must be transformed.
# 📝 Problem:

# You are given two lines of input:
#     An integer X → how many readings are expected
#     A line of X space-separated integers (can be negative or positive)
# ✅ Your Task:
#     Check if the number of readings matches X
#         If not, print -1
#     Then, for each odd negative number, raise it to the power of 3 (n ** 3)
#     Sum all those powered values and print the total

# 📥 Example Input:
# 6
# -3 4 -2 -1 5 -5

# 📤 Output:
# -179

 
input_line_1 = "12"
input_line_2 = "-3 -4 -2 -1 -5 -5 1 2 3 4 5 6"

total = 0

splitInput = input_line_2.split(" ")
splitLength = len(splitInput)
intLine1 = int(input_line_1)

if intLine1 == splitLength:
    for n in splitInput:
        if int(n) > 0:
            power = int(n) ** 3
            total += power
elif intLine1 != splitLength:
    print("well its not same so -1")




    
print(total)
      
