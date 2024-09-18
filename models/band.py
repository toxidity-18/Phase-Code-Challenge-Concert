import sqlite3

class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def concerts(band_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (band_id,))
        return cursor.fetchall()

    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
        conn.commit()

    @staticmethod
    def all_introductions(band_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        """, (band_id,))
        results = cursor.fetchall()
        return [f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}" for venue_city, band_name, band_hometown in results]
