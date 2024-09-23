from db.migrations import create_tables
from db.seed import seed_data
from models.band import Band
from models.venue import Venue
from models.concert import Concert

def main():
    # Create tables and seed data
    create_tables()
    seed_data()
    

    # Fetch a band instance
    beatles = Band(1)
    print("Beatles Concerts:", beatles.concerts())
    print("Beatles Venues:", beatles.venues())
    
    # Add a new concert
    beatles.play_in_venue("Madison Square Garden", "2023-09-23")
    
    # Fetch a venue instance
    msg = Venue(1)
    print("MSG Concerts:", msg.concerts())
    print("Bands at MSG:", msg.bands())
    
    # Fetch a concert instance
    concert = Concert(1)
    print("Concert Band:", concert.band())
    print("Concert Venue:", concert.venue())
    print("Is Hometown Show:", concert.hometown_show())
    print("Introduction:", concert.introduction())

if __name__ == '__main__':
    main()
