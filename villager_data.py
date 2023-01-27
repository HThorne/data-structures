"""Functions to parse a file containing villager data."""
villagers = 'villagers.csv'

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()

    villager_info = open(filename)

    for line in villager_info:
        line = line.rstrip().split("|")
        species = line[1]

        unique_species.add(species)
    
    villager_info.close()

    return unique_species




def get_villagers_by_species(filename, search_species ="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    villager_list = []

    villager_info = open(filename)

    for line in villager_info:
        line = line.rstrip().split("|")
        villager_name = line[0]
        species = line[1]

        if search_species == species or search_species == "All":
            villager_list.append(villager_name)  

    villager_info.close()

    return sorted(villager_list)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    villager_info = open(filename)

    for line in villager_info:
        line = line.rstrip().split("|")
        villager_name = line[0]
        hobby = line[3]

        if hobby == "Fitness":
            fitness.append(villager_name)
        elif hobby == "Nature":
            nature.append(villager_name)
        elif hobby == "Education":
            education.append(villager_name)
        elif hobby == "Music":
            music.append(villager_name)
        elif hobby == "Fashion":
            fashion.append(villager_name)
        elif hobby == "Play":
            play.append(villager_name)

    villager_info.close()

    return [sorted(fitness),
            sorted(nature),
            sorted(education),
            sorted(music),
            sorted(fashion),
            sorted(play)
    ]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    villager_info = open(filename)

    for line in villager_info:
        line = tuple(line.rstrip().split("|"))
        all_data.append(line)
    
    villager_info.close()
    
    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    villager_info = open(filename)

    for line in villager_info:
        line = line.rstrip().split("|")
        villager_motto = line[4]
        name = line[0]

        if villager_name == name:
            return villager_motto  



def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    villager_info = open(filename)

    likeminded = set()
   
    expected_personality = None
    
    for line in villager_info:
        line = line.rstrip().split("|")
        villager_personality = line[2]
        name = line[0]

        if villager_name == name:
            expected_personality = villager_personality
            break
    
    if expected_personality:
        for line in villager_info:
            line = line.rstrip().split("|")
            villager_personality = line[2]
            name = line[0]

            if villager_personality == expected_personality:
                likeminded.add(name)

            
    return likeminded


# print(all_species(villagers))
# print(get_villagers_by_species(villagers, "Bear"))
# print(all_names_by_hobby(villagers))
# print(all_data(villagers))
# print(find_motto(villagers, "Maple"))
print(find_likeminded_villagers(villagers, "Maple"))