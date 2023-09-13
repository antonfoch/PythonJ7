import sqlite3
import json
from ex_00bis import extract_data_from_json

# Function to insert prize data into the prize table
def insert_prize_data(cursor, laureate_id, category_id, year, affiliation_id):
    cursor.execute(
        "INSERT INTO prize (laureate_id, category_id, year, affiliation_id) VALUES (?, ?, ?, ?)",
        (laureate_id, category_id, year, affiliation_id)
    )

if __name__ == "__main__":
    with open("D-POO-300_07_nobelLaureates.json", "r") as file:
        data = json.load(file)

    conn = sqlite3.connect('laureate.db')
    cursor = conn.cursor()

    # Extract data from JSON
    categories, names, countries = extract_data_from_json(data)

    # Insert categories into the category table
    for category_name in categories:
        cursor.execute("INSERT OR IGNORE INTO category (name) VALUES (?)", (category_name,))

    # Insert countries into the country table
    for country_info in countries:
        if len(country_info) >= 2:
            country_name, country_code = country_info[:2]
            cursor.execute("INSERT OR IGNORE INTO country (name, code) VALUES (?, ?)", (country_name, country_code))

    # Insert prize data into the prize table
    for laureate in data["laureates"]:
        laureate_id_result = cursor.execute("SELECT id FROM laureate WHERE name = ?", (laureate["firstname"],)).fetchone()

        # Check if the laureate has any prizes
        if "prizes" in laureate:
            for prize in laureate["prizes"]:
                category_id_result = cursor.execute("SELECT id FROM category WHERE name = ?", (prize["category"],)).fetchone()
                affiliation_country = prize["affiliations"][0]["country"]
                affiliation_id_result = cursor.execute("SELECT id FROM country WHERE name = ?", (affiliation_country,)).fetchone()

                # Check if the query results are not None
                if laureate_id_result is not None and category_id_result is not None and affiliation_id_result is not None:
                    laureate_id = laureate_id_result[0]
                    category_id = category_id_result[0]
                    affiliation_id = affiliation_id_result[0]

                    insert_prize_data(cursor, laureate_id, category_id, prize["year"], affiliation_id)

    conn.commit()
    conn.close()

    print("Data inserted into category, country, and prize tables successfully.")
