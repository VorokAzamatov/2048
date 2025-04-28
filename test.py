list = [[5, 8], [6, 9]]

for i in range(0, 2):
    list[i][0] -= 1
    list[i][1] -= 1

for x, y in list:
    x -= 1
    y -= 1

print(list)



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