
import uuid
from database import get_connection


def book_ticket(passenger_name, bus_id, seats):
    if not passenger_name.strip() or seats <= 0:
        return False, "Invalid booking details."

    conn = get_connection()
    cursor = conn.cursor()

    try:
        conn.start_transaction()

        # Lock the selected bus row to prevent overbooking
        cursor.execute(
            "SELECT available_seats, price FROM buses WHERE id = %s FOR UPDATE",
            (bus_id,)
        )

        bus = cursor.fetchone()

        if bus is None:
            conn.rollback()
            return False, "Bus not found."

        available_seats, price = bus

        if seats > available_seats:
            conn.rollback()
            return False, "Not enough seats available."

        total_price = price * seats
        ticket_id = "BUS-" + uuid.uuid4().hex[:10].upper()

        cursor.execute(
            "UPDATE buses SET available_seats = available_seats - %s WHERE id = %s",
            (seats, bus_id)
        )

        cursor.execute("""
            INSERT INTO bookings
            (ticket_id, passenger_name, bus_id, seats, total_price)
            VALUES (%s, %s, %s, %s, %s)
        """, (ticket_id, passenger_name, bus_id, seats, total_price))

        conn.commit()
        return True, ticket_id

    except Exception:
        conn.rollback()
        return False, "Booking failed. Please try again."

    finally:
        cursor.close()
        conn.close()
