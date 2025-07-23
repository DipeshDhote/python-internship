import requests
from api.db_config import connect_to_db

# Fetch data from Public API Cat Facts
response = requests.get("https://catfact.ninja/fact")
data = response.json()

print(data['fact'])

conn = connect_to_db()
cur = conn.cursor()
insert_script = "INSERT INTO cat_fact(fact) VALUES(%s)"
insert_data = (data['fact'],)

cur.execute(insert_script,insert_data)

conn.commit()
conn.close()
print("Cat fact inserted into database.")