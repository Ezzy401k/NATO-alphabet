import pandas as pd  # Import the pandas library for data manipulation

# Ask the user to input a word and convert it to uppercase
fix= True
while fix:
    name = input("Please enter a word: ").upper()

    # Create a list comprehension to store each letter of the input word
    name_list = [letter for letter in name]

    # Read the NATO phonetic alphabet data from the CSV file into a DataFrame
    data = pd.read_csv("nato_phonetic_alphabet.csv")

    # Create a dictionary comprehension to map each letter to its corresponding phonetic code
    data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    try:

        # Use list comprehension to generate a list of phonetic codes for each letter in the input word
        phonetic_code = [data_dict[key] for key in name_list]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")

    else:
        # Print the list of phonetic codes
        print(phonetic_code)


