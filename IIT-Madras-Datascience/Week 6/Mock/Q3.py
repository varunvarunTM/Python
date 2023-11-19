"""   The scores dataset is a list of dictionaries one of whose entries is given below for your reference:

            {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 85, 'Physics': 100, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 60, 'Civics': 88, 'Philosophy': 95}

      Write the following functions:

            (1) group_by_city:
                        accepts the scores_dataset as argument.
                        It should return a dictionary named cities whose
                        keys are names of the cities that the students are from.
                        The value corresponding to a key (city) is the list of
                        names of all students who hail from this city.
                        The order in which names are appended to the list
                        doesn't matter.

            (2) busy_cities:
                        accepts the scores_dataset as argument.
                        It should return a list of cities.
                        Each city in this list has the property that the
                        number of students from this city is greater than
                        or equal to the number of students from every other
                        city in the dataset. Your function should make use
                        of group_by_city. The order in which the cities
                        appended to the list doesn't matter.

            
            
      (1) You do not have to accept input from the user or print the output
      to the console.
      You just have to write the definition of both the functions.

      (2) Do not try to process the output produced.
      We randomly sample a few elements from the dictionary or list
      returned by your function and print that in the desired form. """



def group_by_city(scores_dataset):
    """
    Group students by cities
	
    Argument:
        scores_dataset: list of dicts
    Return:
        cities: dict: (key: string, value: list of strings)
    """
    cities = {}
    for data in scores_dataset:
        city = data['City']
        name = data['Name']
        if city in cities:
            cities[city].append(name)
        else:
            cities[city] = [name]
    return cities

    
def busy_cities(scores_dataset):
    """
    Get the busy cities
	
    Argument:
        scores_dataset: list of dicts
    Return:
        result: list of strings
    """
    cities = group_by_city(scores_dataset)
    busy_cities = []
    max_students = 0
    for city, students in cities.items():
        num_students = len(students)
        if num_students >= max_students:
            if num_students > max_students:
                busy_cities = []
            busy_cities.append(city)
            max_students = num_students
    return busy_cities