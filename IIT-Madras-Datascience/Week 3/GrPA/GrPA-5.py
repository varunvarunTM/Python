""" Accept a phone number as input.
    A valid phone number should satisfy the following constraints.

    (1) The number should start with one of these digits: 6, 7, 8, 9

    (2) The number should be exactly 10 digits long.

    (3) No digit should appear more than 7 times in the number.

    (4) No digit should appear more than 5 times in a row in the number.

    If the fourth condition is not very clear,
    then consider this example : the number 9888888765 is invalid
    because the digit 8 appears more than 5 times in a row.

    Print the string valid if the phone number is valid.
    If not , print the string invalid. """


n = input()
x = True
if len(n) == 10:
    if n[0] in ['6', '7', '8', '9']:
        for i in range(10):
            if n.count(n[i]) <= 7:
                for i in n:
                    if i * 6 not in n:
                        x = x and True
                        
                    else:
                        x = x and False
            else:
                x = x and False
    else:
        x = x and False
else:
    x = x and False

if x:
    print('valid')
else:
    print('invalid')
                    