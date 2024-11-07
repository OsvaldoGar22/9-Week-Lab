
# Exercise 1 - Course Information

# course_room = {
#     "CS101": "3004",
#     "CS102": "4501",
#     "CS103": "6755",
#     "NT110": "1244",
#     "CM241": "1411",
# }
#
# course_instructors = {
#     "CS101": "Haynes",
#     "CS102": "Alvarado",
#     "CS103": "Rich",
#     "NT110": "Burke",
#     "CM241": "Lee",
# }
#
# course_meeting = {
#     "CS101": "8:00 a.m.",
#     "CS102": "9:00 a.m.",
#     "CS103": "10:00 a.m.",
#     "NT110": "11:00 a.m.",
#     "CM241": "1:00 p.m.",
# }
#
# course_number = input("Enter a course number: ")
#
# if course_number in course_room:
#     print(f"Room Number: {course_room[course_number]}")
#     print(f"Instructor: {course_instructors[course_number]}")
#     print(f"Meeting Time: {course_meeting[course_number]}")
# else:
#     print("Wrong Course Number.")

# --------------------------------------------------------------------

# Exercise 2 - Capital Quiz

# NUM_STATES = 5
#
# def main():
#     state_caps = state_cap_dict()
#
#     correct = 0
#     incorrect = 0
#
#     for count in range(NUM_STATES):
#         state, capital = state_caps.popitem()
#
#         print(f"What is the capital of {state}?")
#         response = input()
#     
#         if response.lower() == capital.lower():
#             correct += 1
#             print("Correct!")
#         else:
#             incorrect += 1
#             print("Incorrect!")
#
#     print(f"Correct responses: {correct}")
#     print(f"Incorrect responses: {incorrect}")
#
# def state_cap_dict():
#     sc = {
#         "Alabama": "Montgomery",
#         "Alaska": "Juneau",
#         "Arizona": "Phoenix",
#         "Arkansas": "Little Rock",
#         "California": "Sacramento",
#         "Colorado": "Denver",
#         "Connecticut": "Hartford",
#         "Delaware": "Dover",
#         "Florida": "Tallahassee",
#         "Georgia": "Atlanta",
#         "Hawaii": "Honolulu",
#         "Idaho": "Boise",
#         "Illinois": "Springfield",
#         "Indiana": "Indianapolis",
#         "Iowa": "Des Moines",
#         "Kansas": "Topeka",
#         "Kentucky": "Frankfort",
#         "Louisiana": "Baton Rouge",
#         "Maine": "Augusta",
#         "Maryland": "Annapolis",
#         "Massachusetts": "Boston",
#         "Michigan": "Lansing",
#         "Minnesota": "Saint Paul",
#         "Mississippi": "Jackson",
#         "Missouri": "Jefferson City",
#         "Montana": "Helena",
#         "Nebraska": "Lincoln",
#         "Nevada": "Carson City",
#         "New Hampshire": "Concord",
#         "New Jersey": "Trenton",
#         "New Mexico": "Santa Fe",
#         "New York": "Albany",
#         "North Carolina": "Raleigh",
#         "North Dakota": "Bismarck",
#         "Ohio": "Columbus",
#         "Oklahoma": "Oklahoma City",
#         "Oregon": "Salem",
#         "Pennsylvania": "Harrisburg",
#         "Rhode Island": "Providence",
#         "South Carolina": "Columbia",
#         "South Dakota": "Pierre",
#         "Tennessee": "Nashville",
#         "Texas": "Austin",
#         "Utah": "Salt Lake City",
#         "Vermont": "Montpelier",
#         "Virginia": "Richmond",
#         "Washington": "Olympia",
#         "West Virginia": "Charleston",
#         "Wisconsin": "Madison",
#         "Wyoming": "Cheyenne"
#     }
#     
#     return sc
#
# main()

# --------------------------------------------------------------------

# Exercise 3 - File Encryption and Decryption

# codes = {
#     "A": "%", "a": "9", "B": "@", "b": "#", "C": "!", "c": "1", "D": "&", "d": "4",
#     "E": "*", "e": "5", "F": "(", "f": "6", "G": ")", "g": "3", "H": "^", "h": "7",
#     "I": "+", "i": "2", "J": "=", "j": "8", "K": "$", "k": "0", "L": "[", "l": "]",
#     "M": "{", "m": "}", "N": ";", "n": ":", "O": "<", "o": ">", "P": "/", "p": "?",
#     "Q": "|", "q": "~", "R": "`", "r": "-", "S": "_", "s": ".", "T": ",", "t": "'",
#     "U": "\\", "u": "}", "V": "(", "v": ")", "W": "!", "w": "&", "X": ":", "x": ";",
#     "Y": "[", "y": "]", "Z": "{", "z": "}"
# }
#
# def encrypt_file(input_file, output_file):
#     with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
#         text = infile.read()
#         
#         encrypted_text = ""
#         for letter in text:
#             encrypted_text += codes.get(letter, letter)
#         
#         outfile.write(encrypted_text)
#
# encrypt_file('input.txt', 'encrypted.txt')
#
#
# reverse_codes = {unencrypted: encrypted for encrypted, unencrypted in codes.items()}
#
# def decrypt_file(input_file):
#     with open(input_file, 'r') as infile:
#         encrypted_text = infile.read()
#         
#         decrypted_text = ""
#         for letter in encrypted_text:
#             decrypted_text += reverse_codes.get(letter , letter)
#         
#         print(decrypted_text)
#
# decrypt_file('encrypted.txt')

# --------------------------------------------------------------------

# Exercise 4 - Unique Words
#
# unique_words = set()
#
# with open("words.txt", "r") as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             clean_word = "".join(letter for letter in word if letter.isalnum()).lower()
#             
#             if clean_word:
#                 unique_words.add(clean_word)
#
# print("Unique words found in the file:")
# print(sorted(unique_words))

# --------------------------------------------------------------------

# Exercise 5 - Word Frequency

# word_frequencies = {}
# input_file = "input.txt"
# output_file = "output.txt"
#
# with open(input_file, "r") as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             clean_word = "".join(letter for letter in word if letter.isalnum()).lower()
#             
#             if clean_word:
#                 word_frequencies[clean_word] = word_frequencies.get(clean_word, 0) + 1
#
# if output_file:
#     with open(output_file, "w") as outfile:
#         for word, frequency in sorted(word_frequencies.items()):
#             outfile.write(f"{word}: {frequency}\n")
#     print(f"Word frequencies have been written to output.txt")
# else:
#     print("Word frequencies in the file:")
#     for word, frequency in sorted(word_frequencies.items()):
#         print(f"{word}: {frequency}")

# --------------------------------------------------------------------

# Exercise 6 - File Analysis

file1 = "file1.txt"
file2 = "file2.txt"


def get_unique_words(file):
    words_set = set()
    with open(file, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                clean_word = "".join(letter for letter in word if letter.isalnum()).lower()
                if clean_word:
                    words_set.add(clean_word)
    return words_set

file1 = get_unique_words(file1)
file2 = get_unique_words(file2)

unique_in_both = file1 | file2 
print("Unique words in both files:")
print(sorted(unique_in_both))

in_both_files = file1 & file2
print("\nWords that appear in both files:")
print(sorted(in_both_files))

only_in_file1 = file1 - file2
print("\nWords that appear in the first file but not the second:")
print(sorted(only_in_file1))

only_in_file2 = file2 - file1
print("\nWords that appear in the second file but not the first:")
print(sorted(only_in_file2))

either_not_both = file1 ^ file2
print("\nWords that appear in either the first or second file, but not both")
print(sorted(either_not_both))















