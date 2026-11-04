# CodeAlpha_Cloud_Task3_BusPass
# Bus Pass Booking System

## Project Overview
The Bus Pass Booking System is a web-based application developed using Python Flask and MySQL. It allows users to search for available buses and book bus tickets online.

## Features
- Search buses by source, destination and journey date.
- View available seats and ticket prices.
- Book bus tickets.
- Generate a unique ticket ID.
- Store bus and booking details in MySQL database.
- Cloud deployment using Render and Aiven MySQL.

## Technologies Used
- Python
- Flask
- MySQL
- HTML
- CSS
- Render
- Aiven Cloud Database
- GitHub

## Project Structure
- `app.py` – Main Flask application
- `database.py` – Database connection and table creation
- `booking.py` – Booking functionality
- `add_buses.py` – Add sample bus details
- `templates/` – HTML templates
- `requirements.txt` – Python dependencies
- `Procfile` – Deployment configuration

## Installation and Setup

1. Clone the repository:
   `git clone https://github.com/Jaya719/CodeAlpha_Cloud_Task3_BusPass.git`

2. Install dependencies:
   `pip install -r requirements.txt`

3. Configure database environment variables:
   - DB_HOST
   - DB_PORT
   - DB_USER
   - DB_PASSWORD
   - DB_NAME

4. Run the application:
   `python app.py`

## Live Deployment
https://codealpha-cloud-task3-buspass.onrender.com/

## Author
Jayashree Srinivasan

Artificial Intelligence and Data Science Student
