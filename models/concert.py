from db.connection import get_db_connection

class Concert:
    def __init__(self, concert_id):
        self.id = concert_id
    
    def band(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.id, bands.name, bands.hometown
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.id = ?
        ''', (self.id,))
        band = cursor.fetchone()
        conn.close()
        return band

    def venue(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT venues.id, venues.title, venues.city
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        ''', (self.id,))
        venue = cursor.fetchone()
        conn.close()
        return venue

    def hometown_show(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT concerts.id
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ? AND bands.hometown = venues.city
        ''', (self.id,))
        hometown_show = cursor.fetchone() is not None
        conn.close()
        return hometown_show

    def introduction(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.name, bands.hometown, venues.city
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        ''', (self.id,))
        band_name, band_hometown, venue_city = cursor.fetchone()
        conn.close()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"
