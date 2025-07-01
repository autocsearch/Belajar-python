# 🧩 Exercise 8: Danger Level Filter

# Level: Harder
# Concepts: Input length validation, negation, filtering by sign, exponentiation, and totals
# 🧨 Scenario:
# You’re analyzing a security log. Each number represents the threat level of an event — some are harmless, but some are deeply dangerous.
# 📝 Input:

# Two lines:
#     An integer X representing how many events should be in the list
#     A space-separated list of integers (positive, zero, or negative)

# ✅ Your job:
#     If the list does not match X, print -1
#     Otherwise:
#         Only negative odd numbers are considered critical
#         For every critical value, raise it to the power of 4 (n ** 4) and add it to a total
#     Print the total of those raised values

# 📥 Example input:
# 5  
# -3 -2 1 -5 4

# 📤 Output:
# 706

# Because:

#     Critical numbers: -3 and -5
#     (-3)**4 = 81, (-5)**4 = 625
#     Total = 81 + 625 = 706

line1 = "8"
line2 = "1 2 3 -4 -5 -7 -9 -13"

splitInput = line2.split(" ")
changeInput = int(line1)

total = 0

if len(splitInput) == changeInput:
    for n in splitInput:
        if int(n) < 0 and int(n) % 2 != 0:
            T = int(n) ** 4
            total += T
elif len(splitInput) != changeInput:
    print(-1)

print(total)