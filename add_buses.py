
from database import get_connection

conn = get_connection()
cursor = conn.cursor()

buses = [
    ("SETC Express", "Chennai", "Bangalore", "2026-11-10", 40, 40, 650),
    ("SETC Deluxe", "Chennai", "Coimbatore", "2026-11-11", 40, 40, 550),
    ("Express Bus", "Bangalore", "Chennai", "2026-11-12", 40, 40, 700)
]

cursor.executemany("""
    INSERT INTO buses
    (bus_name, source, destination, journey_date,
     total_seats, available_seats, price)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", buses)

conn.commit()

print(cursor.rowcount, "buses added successfully!")

cursor.close()
conn.close()
