""" You are given the names and dates of birth of a group of people.
    Find all pairs of members who share a common date of birth.
    Note that this date need not be common across all pairs.
    It is sufficient if both members in a pair have the same date of birth.

    The first line of input is a sequence of comma-separated names.
    The second line of input is a sequence of comma-separated positive integers.
    Each integer in the sequence will be in the range [1,365], endpoints
    inclusive, and stands for some day in the year.

    Find all pairs of names that share a common date of birth and store
    them in a list called common.
    Each element of this list is itself a list,
    and should be of the form [name1, name2], such that name1 comes
    before name2 in alphabetical order.

    Notes

        (1) The pairs can be appended to the list common in any order.
            Only the names within a pair should be in dictionary order.

        (2) You can assume that each test case will have at least one pair
            of members who share the same date of birth.

        (3) You do not have to print the output to the console.
            This is the responsibility of the autograder.
            You just have to populate the list common in the required format.

    Sample Input/Output

        For example, consider the input:

            sachin,ramesh,rohit,priya,saina,sandeep,stella
            100,50,100,20,30,20,20

    
        Your list common could look like this:

            [['rohit', 'sachin'], ['priya', 'sandeep'], ['priya', 'stella'], ['sandeep', 'stella']] """



names = input().split(',')
dates = [int(x) for x in input().split(',')]
common = []
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        if dates[i] == dates[j]:
            if names[i] < names[j]:
                common.append([names[i], names[j]])
            else:
                common.append([names[j], names[i]])
print(common) # do not include this line in your code