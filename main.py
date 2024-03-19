import pandas as pd

name = input("Please enter a word: ").upper()
name_list = [letter for letter in name]

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

phonetic_code = [data_dict[key] for key in name_list]
print(phonetic_code)