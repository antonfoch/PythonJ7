import sqlite3
import json


def extract_data_from_json(json_data):
    laureate_names = set()

    for laureate in json_data["laureates"]:
        name = laureate["firstname"]
        if "surname" in laureate:
            name += " " + laureate["surname"]
        laureate_names.add(name)

    return sorted(laureate_names)

with open("D-POO-300_07_nobelLaureates.json", "r") as file:
    data = json.load(file)

laureate_names = extract_data_from_json(data)

conn = sqlite3.connect('laureate.db')
cursor = conn.cursor()

for laureate_name in laureate_names:
    cursor.execute("INSERT OR IGNORE INTO laureate (name) VALUES (?)", (laureate_name,))


conn.commit()
conn.close()

print("Data inserted into category and country tables successfully.")
