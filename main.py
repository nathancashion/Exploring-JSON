import json


def read_from_file():
    json_file = open("countries.json", "r")
    countries = json.load(json_file)

    # print(countries)
    for Country in countries:
        print(f"name: {countries[Country]['name']}")
        print(f"population: {countries[Country]['population']}")
        print(f"capital: {countries[Country]['capital']}")
        print(f"languages: ")
        for lang in countries[Country]['languages']:
            print(f"\t{lang}")
        print("\n")

    json_file.close()


def write_to_file():
    canada = {
        "name": "Canada",
        "population": "plenty",
        "capitol": "Ottawa",
        "languages":
            [
                "English",
                "French"
            ]
    }

    json_file = open("canada.json", "w")
    json.dump(canada, json_file)
    json_file.close()


if __name__ == '__main__':
    read_from_file()
    write_to_file()
