countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

for country, filename in zip(countries, filenames):
    file = open(f"files/{filename}", "w")
    file.write(country)

