""" Accept the date in DD-MM-YYYY format as input and print the year as output. """


date = input()

#  METHODS
year = date.split("-")
print(year[-1])
    # OR
year = date.split("-")
print(year[2])
    # OR
print(date[6]+date[7]+date[8]+date[9])
    # OR
print(date[6:])