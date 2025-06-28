# 🧩 Exercise 6: Input Checkpoint — Planet Validation

# Level: Medium
# Theme: Input validation across multiple test cases
# 🚀 Story:

# Back on Planet Numara, you’re now trusted to validate multiple alien messages. Each message comes in two lines — but sometimes, the aliens make mistakes! Your job is to validate each message.
# 📝 Problem:

# You’ll be given several test cases.
# Each test case consists of:
#     An integer X on its own line (1 ≤ X ≤ 10)
#     A line of space-separated integers, supposedly X items long.

# ✅ Your Task:
#     For each test case:
#         If the number of integers on the second line matches X, print the list.
#         If not, print -1.
# 📥 Input Example:

# 3
# 5 7 9
# 2
# 10 11
# 4
# 1 2

# 📤 Output:

# [5, 7, 9]
# [10, 11]
# -1

# 🧠 Notes:
#You can simulate the input as a list of strings (or handle real input() if you want to go advanced).
#Focus on checking the count for each test case.
#It’s okay to use loops here — we’ll restrict them later 😉
# Sleep well, warrior. Planet Numara awaits your return 🌙🪐
# Let me know when you’re ready to tackle this one.

input_line_1 = "2"
input_line_2 = "5 7 9"

splitWord = input_line_2.split(" ")
changeWord = int(input_line_1)

wordLen = len(splitWord)

if wordLen == changeWord:
    print(list(splitWord))
elif wordLen != changeWord:
    print(-1)
