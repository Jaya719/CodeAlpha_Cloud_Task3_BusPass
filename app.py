
from flask import Flask, render_template, request
from database import get_connection
from booking import book_ticket
from datetime import date

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Search buses
@app.route("/search", methods=["POST"])
def search_buses():
    source = request.form.get("source", "").strip()
    destination = request.form.get("destination", "").strip()
    journey_date = request.form.get("journey_date", "")

    if not source or not destination or not journey_date:
        return render_template(
            "index.html",
            message="Please enter all search details."
        )

    if journey_date < date.today().isoformat():
        return render_template(
            "index.html",
            message="Please select a valid future date."
        )

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        print("SOURCE:", source)
        print("DESTINATION:", destination)
        print("DATE:", journey_date)

        cursor.execute("""
            SELECT * FROM buses
            WHERE LOWER(TRIM(source)) = LOWER(TRIM(%s))
            AND LOWER(TRIM(destination)) = LOWER(TRIM(%s))
            AND journey_date = %s
            AND available_seats > 0
        """, (source, destination, journey_date))

        buses = cursor.fetchall()

        print("BUS SEARCH RESULT:", buses)

        return render_template("buses.html", buses=buses)

    except Exception as e:
        print("Bus search error:", e)
        return "Unable to search buses. Please try again.", 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# Book ticket
@app.route("/book", methods=["POST"])
def book():
    passenger_name = request.form.get(
        "passenger_name", ""
    ).strip()

    bus_id = request.form.get("bus_id", type=int)
    seats = request.form.get("seats", type=int)

    if not passenger_name or not bus_id or not seats:
        return "Invalid booking details.", 400

    try:
        success, result = book_ticket(
            passenger_name, bus_id, seats
        )

        if success:
            return render_template(
                "ticket.html",
                ticket_id=result
            )

        return f"Booking failed: {result}", 400

    except Exception as e:
        print("Booking error:", e)
        return "Unable to complete booking. Please try again.", 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
