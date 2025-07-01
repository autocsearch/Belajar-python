# 🧩 Exercise 9: Secure Device Logs

# Level: Hard
# Concepts: Input validation, filtering by multiple conditions, negatives, exponentiation, summation
# 🛡️ Scenario:
# You’re analyzing logs from a set of IoT devices. Some logs are corrupted. The only logs we care about are negative even numbers that are multiples of 3.
# 📝 Input:

# Two lines:
#     An integer X — the expected number of log entries
#     A space-separated list of integers (some positive, some negative, some even, some odd)

# ✅ Your task:

#     If the number of entries doesn’t match X, print -1
#     Otherwise:
#         Only include numbers that are:
#             Negative
#             Even
#             Divisible by 3
#         For each of those numbers, raise it to the 3rd power (n ** 3)
#         Add them all together
#     Print the total

# 📥 Example input:
# 6  
# -6 -3 2 9 -12 -8

# 📤 Output:
# -216 + (-1728) = -1944

# Only -6 and -12 qualify
#     -6 ** 3 = -216
#     -12 ** 3 = -1728

line1 = "6"
line2 = "-6 -3 2 9 -12 -8"

raw_values = line2.split(" ")
count_as_int = int(line1)

total = 0

if len(raw_values) == count_as_int:
    for n in raw_values:
        if int(n) < 0 and int(n) % 2 == 0 and int(n) % 3 == 0:
            x = int(n) ** 3
            total += x
elif len(raw_values) != count_as_int:
    print(-1)

print(total)
