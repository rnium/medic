import sqlite3
import csv

with open('mbbs2021_22.csv', 'r') as f:
    csvFile = csv.reader(f)
    dataset = list(csvFile)

conn = sqlite3.connect('db.sqlite3')
for profile in dataset:
    sql = f"""
    INSERT INTO result_result ('roll', 'name', 'test_score', 'merit_score', 'position', 'college', 'selection')
    VALUES ({profile[0]}, "{profile[1]}", {profile[2]}, {profile[3]}, {profile[4]}, "{profile[5]}", "{profile[6]}")
    """
    conn.execute(sql)
    conn.commit()

conn.close()