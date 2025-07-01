# 🧩 Exercise 7.2: Filtered Voltage Anomaly

# Level: Medium-Hard
# Theme: Filtering + logic + math + range checking
# ⚡️ Situation:

# You're reading voltage data from a faulty sensor. The sensor reports N values, but some values are out of spec and must be ignored.
# 📝 Input:

# Two lines:
#     A number X indicating how many values to expect.
#     A space-separated list of integers (can include negative, zero, and large positive values).

# ✅ Your job:

#     If the length of the list does not match X, print -1
#     From the list, take only the numbers that are:
#         Greater than or equal to 10
#         Even
#     Square (n ** 2) those valid numbers and sum them all
#     Print the sum

# 🧪 Example Input:
# 6
# 12 5 9 14 11 8

# 📤 Output:
# 404

#     Because:
#     12 and 14 and 8 are valid (>= 10 and even)
#     12² = 144, 14² = 196, 8² = 64
#     Total = 144 + 196 + 64 = 404

line1 = "6"
line2 = "12 23 34 65 79 31"

splitWord = line2.split(" ")
intInput = int(line1)

total = 0

if len(splitWord) == intInput:
    for n in splitWord:
        if int(n) > 10 and int(n) % 2 == 0:
            y = int(n) ** 2
            total += y        
elif len(splitWord) != intInput:
    total = -1

print(total)