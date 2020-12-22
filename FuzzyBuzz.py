# 3 different variants to complete challenge.

# for i in range(1,31):
#     if i%15 == 0:
#         print(i,'.', '\tFuzzy Buzz', sep='')
#     elif i%3 == 0:
#         print(i,'.', '\tFuzzy', sep='')
#     elif i%5 == 0:
#          print(i,'.', '\tBuzz', sep='')

for i in range(1,31):
    if i % 3 == 0 and i%15 != 0:
        print(i, '.', '\tFuzzy', sep='')
    elif i % 5 == 0 and i%15 != 0:
        print(i, '.', '\tBuzz', sep='')
    elif i%3 == 0 and i%5 == 0:
        print(i, '.', '\tFuzzy Buzz', sep='')

for i in range(1,31):
    if i % 3 == 0 and i%15 != 0:
        print(i, '.', '\tFuzzy', sep='')
    elif i % 5 == 0 and i%15 != 0:
        print(i, '.', '\tBuzz', sep='')
    elif i%3 == 0 and i%5 == 0:
        print(i, '.', '\tFuzzy Buzz', sep='')

# list = list(range(1, 31))
#
# for i in list:
#     if i%15 == 0:
#         print(i,'.', '\tFozzie Bear', sep='')
#     elif i%5 == 0:
#         print(i, '.', '\tBear', sep='')
#     elif i%3 == 0:
#         print(i,'.', '\tFozzie', sep='')
