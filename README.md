# Concerts Code Challenge

## Overview
This code challenge focuses on building a Concerts domain using raw SQL queries in Python. You will work with three main entities: `Band`, `Venue`, and `Concert`, and establish relationships between them without using an ORM like SQLAlchemy.

## Domain Description
- A `Band` has many concerts.
- A `Venue` has many concerts.
- A `Concert` belongs to a band and to a venue.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd concert_challenge
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install 
   ```

4. **Set Up Database**:
   - Create the SQLite database and tables using the provided schema.

5. **Run Migrations**:
   - Use raw SQL commands to create the `bands`, `venues`, and `concerts` tables.

## Usage

- Implement the required methods to interact with the database.
- Use `sqlite3` to execute raw SQL queries in your Python code.

## Deliverables

- Write methods to handle object relationships and aggregate data.
- Implement methods like `band()`, `venue()`, `concerts()`, and more as specified in the challenge.

## Testing

1. **Run Tests**:
   ```bash
   python -m unittest discover -s tests
   ```

## License
 - This project is licensed under the MIT License.