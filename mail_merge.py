# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)



PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_line = letter_file.read()
    print(letter_line)
# for name in each_name:
#     x = str(name).strip("'\n")
#     print(x)



