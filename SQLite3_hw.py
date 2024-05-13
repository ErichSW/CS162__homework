import sqlite3

# initial data
artist_table = [['Miley', 'Rock', 14], ['Dolly', 'Country', 123], ['Eminem', 'HipHop', 98], ['Brittany', 'Rock', 37]]
genre_table = [['Rock', 'Los Angeles'], ['Hippie', 'Eugene'], ['Opera', 'Florence']]
city_table = [['Los Angeles', 'CA', 66666, 10000000], ['Eugene', 'OR', 55555, 80000],
              ['Nashville', 'TN', 11111, 1500000]]

# create a connection to the database
connection = sqlite3.connect('music.db')
c = connection.cursor()

# create a table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS artists
             (artist TEXT, genre TEXT, recordings INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS genre
             (genre TEXT, city TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS city
             (city TEXT, state TEXT, zip INTEGER, population INTEGER)''')

# check if the table is empty
c.execute("SELECT COUNT(*) FROM artists")
if c.fetchone()[0] == 0:
    # insert data into the table
    for artist in artist_table:
        c.execute("INSERT INTO artists VALUES (?, ?, ?)", (artist[0], artist[1], artist[2]))

# check if the table is empty
c.execute("SELECT COUNT(*) FROM genre")
if c.fetchone()[0] == 0:
    # insert data into the table
    for genre in genre_table:
        c.execute("INSERT INTO genre VALUES (?, ?)", (genre[0], genre[1]))

# check if the table is empty
c.execute("SELECT COUNT(*) FROM city")
if c.fetchone()[0] == 0:
    # insert data into the table
    for city in city_table:
        c.execute("INSERT INTO city VALUES (?, ?, ?, ?)", (city[0], city[1], city[2], city[3]))

# commit and close the connection
connection.commit()
connection.close()


# function to print artist table
def print_artist_table():
    print("Artists:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT * FROM artists")
    for row in con:
        print(row)
    conn.close()


# function to print genre table
def print_genre_table():
    print("Genre:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT * FROM genre")
    for row in con:
        print(row)
    conn.close()


# function to print city table
def print_city_table():
    print("City:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT * FROM city")
    for row in con:
        print(row)
    conn.close()


# function to print artist names from the artist table whose genre exists in the genre table using JOIN
def print_artist_genre_table():
    print("Artists with existing genre:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT artists.artist FROM artists JOIN genre ON artists.genre = genre.genre")
    for row in con:
        print(row)
    conn.close()


print_artist_table()
print_genre_table()
print_city_table()
print_artist_genre_table()
