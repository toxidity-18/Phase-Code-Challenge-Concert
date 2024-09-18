import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def concerts(venue_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE venue_id = ?", (venue_id,))
        return cursor.fetchall()

    @staticmethod
    def most_frequent_band(venue_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.name, COUNT(concerts.band_id) AS performance_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
            GROUP BY bands.name
            ORDER BY performance_count DESC
            LIMIT 1
        """, (venue_id,))
        return cursor.fetchone()
