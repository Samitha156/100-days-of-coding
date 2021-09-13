import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

def generate_phonetic():

    user_input = input("Enter your name: ").upper()

    try:
        nato_list = [data_dict[item] for item in user_input]
    except KeyError:
        print("letters only")

        generate_phonetic()

    else:
        print(nato_list)


generate_phonetic()