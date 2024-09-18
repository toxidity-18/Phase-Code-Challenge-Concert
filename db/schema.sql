-- Create bands table
CREATE TABLE IF NOT EXISTS bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
);

-- Create venues table
CREATE TABLE IF NOT EXISTS venues (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    city TEXT NOT NULL
);

-- Create concerts table
CREATE TABLE IF NOT EXISTS concerts (
    id INTEGER PRIMARY KEY,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
);
