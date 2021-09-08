import pandas

# student_dict = {
#     "student": ["Angela", "James", "Sam"],
#     "score": [50, 62, 65]
# }
#
# #Looping through dictionary
# for (key, value) in student_dict.items():
#     print(key)
#

#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Sam":
#         print(row.score)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# df = pandas.DataFrame(data)
# print(data)
# data_dict = {}

# for (index, row) in data.iterrows():
#     # print(type(row.letter))
#     data_dict[row.letter].append(str(row.code))
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

user_input = input("Enter your name: ").upper()
nato_list = [data_dict[item] for item in user_input]
# nato_list = []
# for letter in user_input:
#     nato_list.append(data_dict[letter.upper()])


print(nato_list)


