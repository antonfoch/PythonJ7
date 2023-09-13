import json

def extract_data_from_json(json_data):
    categories = set()
    laureate_names = set()
    countries = set()

    for laureate in json_data["laureates"]:

        name = laureate["firstname"]
        if "surname" in laureate:
            name += " " + laureate["surname"]
        laureate_names.add(name)


        for prize in laureate["prizes"]:
            categories.add(prize["category"])

        if "bornCountry" in laureate and "bornCountryCode" in laureate:
            countries.add((laureate["bornCountry"], laureate["bornCountryCode"]))
        if "diedCountry" in laureate and "diedCountryCode" in laureate:
            countries.add((laureate["diedCountry"], laureate["diedCountryCode"]))

    return sorted(categories), sorted(laureate_names), sorted(countries, key=lambda x: x[0])

if __name__ == "__main__":
    with open("D-POO-300_07_nobelLaureates.json", "r") as file:
        data = json.load(file)
    
    categories, names, countries = extract_data_from_json(data)
    
    print(categories)
    print("------------------")
    print(names)
    print("------------------")
    print(countries)