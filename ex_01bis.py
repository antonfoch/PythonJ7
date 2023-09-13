import sqlite3
import json


def extract_data_from_json(json_data):
    categories = set()
    countries = set()

    for laureate in json_data["laureates"]:
        for prize in laureate["prizes"]:
            categories.add(prize["category"])

        if "bornCountry" in laureate and "bornCountryCode" in laureate:
            countries.add((laureate["bornCountry"], laureate["bornCountryCode"]))
        if "diedCountry" in laureate and "diedCountryCode" in laureate:
            countries.add((laureate["diedCountry"], laureate["diedCountryCode"]))

    return sorted(categories), sorted(countries, key=lambda x: x[0])

with open("D-POO-300_07_nobelLaureates.json", "r") as file:
    data = json.load(file)

categories, countries = extract_data_from_json(data)

conn = sqlite3.connect('laureate.db')
cursor = conn.cursor()

for category_name in categories:
    cursor.execute("INSERT OR IGNORE INTO category (name) VALUES (?)", (category_name,))

conn.commit()
conn.close()

print("Data inserted into category and country tables successfully.")
