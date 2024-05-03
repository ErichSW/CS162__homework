import sqlite3

# initial data by artist, genre, and number of recordings
artist_table = [['Miley', 'Rock', 14], ['Dolly', 'Country', 123], ['Eminem', 'HipHop', 98], ['Brittany', 'Rock', 37]]

# create a connection to the database
connection = sqlite3.connect('music.db')

# create a cursor object
c = connection.cursor()

# create a table if it does not exist
c.execute('''CREATE TABLE IF NOT EXISTS artists
             (artist text, genre text, recordings integer)''')

# check if the table is empty
c.execute("SELECT COUNT(*) FROM artists")
if c.fetchone()[0] == 0:
    # insert data into the table
    for artist in artist_table:
        c.execute("INSERT INTO artists VALUES (?, ?, ?)", (artist[0], artist[1], artist[2]))

# commit the changes
connection.commit()

# close the connection
connection.close()


# function to print all the data in the table
def print_table():
    print("All Data:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT * FROM artists")
    for row in c:
        print(row)
    conn.close()


# function to print only rows with genre 'rock'
def print_rock():
    print("Rock Genre:")
    conn = sqlite3.connect('music.db')
    con = conn.cursor()
    con.execute("SELECT * FROM artists WHERE genre='Rock'")
    for row in c:
        print(row)
    conn.close()


print_table()
print()
print_rock()
