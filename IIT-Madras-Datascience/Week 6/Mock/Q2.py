""" Accept a sequence of words as input.
    Create a dictionary named real_dict whose keys are the letters
    of theEnglish alphabet.
    For each key (letter), the corresponding value should be a list of
    words that begin with this key (letter).
    For any given key, the words should be appended to the corresponding
    list in the order in which they appear in the sequence.
    You can assume that all words of the sequence will be in lower case. """





sequence = input().split(",")

real_dict = {}

for word in sequence:
    key = word[0]  # Extract the first letter of the word as the key
    if key not in real_dict:
        real_dict[key] = []  # Create an empty list as the value for the key
    real_dict[key].append(word)  # Append the word to the list

for key in sorted(real_dict.keys()):
    words = ",".join(real_dict[key])
