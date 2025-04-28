dict = {(10, 10): 2, "2": 2}

del dict["2"]

for i in dict:
    print(i)


# segment_size = 150
# segment_margin = 10
#
# list = []
#
# for i in range(1, 5):
#     for k in range(1, 5):
#         current = (segment_margin * k + segment_size * (k - 1),segment_margin * i + segment_size * (i - 1))
#         list.append(current)
#
#
# print(list)