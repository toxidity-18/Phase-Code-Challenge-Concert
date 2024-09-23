from .connection import get_db_connection

def seed_data():
    bands_data = [
        ('The Beatles', 'Liverpool'),
        ('Pink Floyd', 'London'),
        ('The Rolling Stones', 'London')
    ]
    
    venues_data = [
        ('Madison Square Garden', 'New York'),
        ('The O2 Arena', 'London'),
        ('Hollywood Bowl', 'Los Angeles')
    ]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert sample data into bands
    cursor.executemany("INSERT INTO bands (name, hometown) VALUES (?, ?)", bands_data)
    
    # Insert sample data into venues
    cursor.executemany("INSERT INTO venues (title, city) VALUES (?, ?)", venues_data)
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_data()
