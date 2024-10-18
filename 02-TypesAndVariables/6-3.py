# A program that prints a university abbreviation

university = "Krakow University Economics"


words = university.split()


abbreviation = ''.join([word[0] for word in words])


print(f'The abbreviation of the university is: {abbreviation}')