# 🧩 Exercise 5: Spacewalker’s Numbers

# Level: Easy-to-Medium
# Theme: Structured input parsing
# 🚀 Story:

# You’ve just landed on Planet Numara, where aliens communicate using two-line number patterns. You must learn to understand their format to continue your mission.
# 📝 Problem:

# The aliens will give you two lines of input:
#     The first line contains a single integer X (1 ≤ X ≤ 10), which tells you how many numbers to expect on the next line.
#     The second line contains a list of integers, space-separated.

# ✅ Your Task:
#     Read the first line → that’s how many numbers you're expecting.
#     Read the second line → split it into individual numbers.
#     Print the list of numbers only if the number of values matches X.
#     If they don’t match, print -1.

# 📥 Input Examples:
# Example 1:
# 3
# 5 7 9

# ✅ Output:
# [5, 7, 9]

# Example 2:
# 4
# 8 3 1

# ❌ Output:
# -1

line_1 = "3"
line_2 = "5 7 9"

split_line_2 = line_2.split(" ")
change = int(line_1)

print(split_line_2)

length = len(split_line_2)
print(change)
print(length)

if length == change:
    print(split_line_2)
elif length != change:
    print(-1)

