from db.connection import get_db_connection
from models.concert import Concert

class Band:
    def __init__(self, band_id):
        self.id = band_id
    
    def concerts(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM concerts WHERE band_id = ?
        ''', (self.id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    def venues(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT DISTINCT venues.*
        FROM concerts
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.band_id = ?
        ''', (self.id,))
        venues = cursor.fetchall()
        conn.close()
        return venues
    
    def play_in_venue(self, venue_title, date):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT id FROM venues WHERE title = ?
        ''', (venue_title,))
        venue_id = cursor.fetchone()[0]
        
        cursor.execute('''
        INSERT INTO concerts (date, band_id, venue_id) VALUES (?, ?, ?)
        ''', (date, self.id, venue_id))
        
        conn.commit()
        conn.close()
    
    def all_introductions(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT concerts.id
        FROM concerts
        WHERE concerts.band_id = ?
        ''', (self.id,))
        concert_ids = cursor.fetchall()
        
        introductions = []
        for concert_id in concert_ids:
            concert = Concert(concert_id[0])
            introductions.append(concert.introduction())
            
        conn.close()
        return introductions
    
    @classmethod
    def most_performances(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.id, bands.name, COUNT(concerts.id) as concert_count
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        GROUP BY bands.id
        ORDER BY concert_count DESC
        LIMIT 1
        ''')
        band = cursor.fetchone()
        conn.close()
        return band
