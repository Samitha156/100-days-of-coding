# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + "pie")
#
#
# make_pie(4)

facebook_post = [
    {'likes': 21, "Comments": 2},
    {'likes': 13, 'Comments': 2, 'Shares': 1},
    {'likes': 33, 'Comments':8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 4, 'Shares':1},
    {'likes':19, 'Comments': 3}
]

total_likes = 0

for post in facebook_post:
    try:
        total_likes = total_likes + post['likes']
    except KeyError:
        print("error")
else:
    print(total_likes)