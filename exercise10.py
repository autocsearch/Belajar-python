# 🧩 Exercise 10: Loopless Final Form
# 🎯 Goal:

# Replicate the logic from Exercise 9, but this time, you are NOT allowed to use any of these:

#     ❌ for loops
#     ❌ while loops
#     ❌ List/set/dict comprehensions

# ✅ What you can use:

#     map()
#     filter()
#     sum()
#     lambda
#     Basic if statements
#     int(), split(), len()

# 📜 Scenario:

# You’re auditing IoT logs for secure devices.

# Input:
#     Line 1: An integer X → the expected number of log entries
#     Line 2: A space-separated list of integers (some positive, some negative, some even, some odd)

# Requirements:
#     If the number of entries in line 2 does not match X, print -1
#     If the count is correct:
#         Only include numbers that are:
#             Negative
#             Even
#             Divisible by 3
#         Raise each of those numbers to the 3rd power (n ** 3)
#         Sum them all and print the total

# 🧪 Example:

# Input:
# 6  
# -6 -3 2 9 -12 -8

# Output:
# -1944

# Only -6 and -12 match all 3 conditions:
#     -6 ** 3 = -216
#     -12 ** 3 = -1728

input_line1 = "6"
input_line2 = "-6 -3 2 9 -12 -8 -10"

raw_values = input_line2.split(" ")
input_as_int = int(input_line1)



# if len(raw_values) == input_as_int:
#     if raw_values
# elif len(raw_values) != input_as_int:
#     print(-1)