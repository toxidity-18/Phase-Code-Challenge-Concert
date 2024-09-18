from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Insert test data
Band.play_in_venue(1, 1, '2024-09-15')

# Test concert introduction
print(Concert.introduction(1))
