import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def band(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT bands.* FROM concerts JOIN bands ON concerts.band_id = bands.id WHERE concerts.id = ?", (concert_id,))
        return cursor.fetchone()

    @staticmethod
    def venue(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT venues.* FROM concerts JOIN venues ON concerts.venue_id = venues.id WHERE concerts.id = ?", (concert_id,))
        return cursor.fetchone()

    @staticmethod
    def hometown_show(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (concert_id,))
        result = cursor.fetchone()
        return result[0] == result[1]

    @staticmethod
    def introduction(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (concert_id,))
        band_name, band_hometown, venue_city = cursor.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
