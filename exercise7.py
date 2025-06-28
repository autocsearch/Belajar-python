# 🧩 Exercise 7: Power Plant

# Level: Medium
# Theme: Conditional logic + math
# ⚡ Story:

# You're now managing the alien power plant. Each reactor gives off energy readings. But the readings have a catch — only the negative numbers are useful, and you must calculate the power of 4 for those.
# 📝 Problem:

# You are given two lines of input:

#     An integer X → the number of values expected

#     A space-separated list of X integers, some may be negative or positive

# ✅ Your Task:

#     Convert all values into integers

#     Ignore all positive numbers

#     For each negative number, raise it to the power of 4: n ** 4

#     Then sum all those powered values

#     If the number of inputs doesn’t match X, print -1

# 📥 Input Example:

# 5
# -2 3 -1 0 -3

# 📤 Output:

# 98

#     Because:
#     (-2)^4 = 16
#     (-1)^4 = 1
#     (-3)^4 = 81
#     Sum = 16 + 1 + 81 = 98