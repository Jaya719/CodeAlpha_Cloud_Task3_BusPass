
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
print("DATABASE NAME:", os.getenv("DB_NAME"))


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "bus_pass_db")
    )


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS buses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            bus_name VARCHAR(100) NOT NULL,
            source VARCHAR(100) NOT NULL,
            destination VARCHAR(100) NOT NULL,
            journey_date DATE NOT NULL,
            total_seats INT NOT NULL,
            available_seats INT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            CHECK (total_seats > 0),
            CHECK (available_seats >= 0),
            CHECK (available_seats <= total_seats),
            CHECK (price >= 0)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INT AUTO_INCREMENT PRIMARY KEY,
            ticket_id VARCHAR(50) UNIQUE NOT NULL,
            passenger_name VARCHAR(100) NOT NULL,
            bus_id INT NOT NULL,
            seats INT NOT NULL,
            total_price DECIMAL(10,2) NOT NULL,
            booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (bus_id) REFERENCES buses(id)
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()
