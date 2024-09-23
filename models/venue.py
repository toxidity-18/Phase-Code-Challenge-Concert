from db.connection import get_db_connection

class Venue:
    def __init__(self, venue_id):
        self.id = venue_id
    
    def concerts(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ?
        ''', (self.id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    def bands(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT bands.*
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        ''', (self.id,))
        bands = cursor.fetchall()
        conn.close()
        return bands
    
    def concert_on(self, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM concerts WHERE venue_id = ? AND date = ?
        ''', (self.id, date))
        concert = cursor.fetchone()
        conn.close()
        return concert
    
    def most_frequent_band(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.id, bands.name, COUNT(concerts.id) as concert_count
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        WHERE concerts.venue_id = ?
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
        ''', (self.id,))
        band = cursor.fetchone()
        conn.close()
        return band
