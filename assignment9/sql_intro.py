import sqlite3

# functions for adding data
def add_publisher(cursor, name, website, email, phone, address):
    try:
        cursor.execute("INSERT INTO Publishers (name, website, email, phone, address) VALUES (?,?,?,?,?)", (name, website, email, phone, address))
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def add_magazine(cursor, title, isbn, category, language, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (title, isbn, category, language, publisher_id) VALUES (?,?,?,?,?)", (title, isbn, category, language, publisher_id))
    except sqlite3.IntegrityError:
        print(f"{title} is already in the database.")

def add_subscriber(cursor, first_name, last_name, email, phone):
    # check if already exists
    cursor.execute("SELECT * FROM Subscribers WHERE first_name = ? AND last_name = ? AND email = ?", (first_name, last_name, email))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber {first_name} {last_name} is already in the database.")
        return    

    try:
        cursor.execute("INSERT INTO Subscribers (first_name, last_name, email, phone) VALUES (?,?,?,?)", (first_name, last_name, email, phone))
    except sqlite3.IntegrityError:
        print(f"{first_name} {last_name} is already in the database.")

def add_subscription(cursor, subscriber_id, magazine_id, date_start, date_end):
    # check if already exists
    cursor.execute("SELECT * FROM Subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    results = cursor.fetchall()
    if len(results) > 0:
        print(f"Subscriber {subscriber_id} is already subscribed to magazine {magazine_id}.")
        return
    
    try:
        cursor.execute("INSERT INTO Subscriptions (subscriber_id, magazine_id, date_start, date_end) VALUES (?,?,?,?)", (subscriber_id, magazine_id, date_start, date_end))
    except sqlite3.IntegrityError:
        print(f"Subscription for {subscriber_id} and {magazine_id} is already in the database.")


# Connect to a new SQLite database
with  sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()
    
    # creating tables
    try: cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        website TEXT,
        email TEXT,
        phone INTEGER,
        address TEXT
    )
    """)
    except: 
        print("Unsuccessful")

    try: cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        isbn TEXT,
        category TEXT,
        language TEXT,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    )
    """)
    except: 
        print("Unsuccessful")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        phone INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        date_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
        date_end TIMESTAMP, 
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
    """)


    # adding sample data
    add_publisher(cursor, 'River Publishing', 'https://blueriverpub.com', 'contact@blueriverpub.com', '4255551283', '123 Maple St, Seattle, WA')
    add_publisher(cursor, 'Northstar Media', 'https://northstarmedia.org', 'info@northstarmedia.org', 5032229844, '42 Pine Ave, Portland, OR')
    add_publisher(cursor, 'Evergreen Press', 'https://evergreenpress.net', 'support@evergreenpress.net', 2087774521, '88 Cedar Rd, Boise, ID')
    add_publisher(cursor, 'Cascade Publications', 'https://cascadebooks.com', 'hello@cascadebooks.com', 5096647722, '501 Lakeview Dr, Virginia Beach, VA')
    add_publisher(cursor, 'Harborlight Publishing', 'https://harborlightpub.io', 'admin@harborlightpub.io', 2534419088, '77 Harbor Ln, New York City, NY')
    add_publisher(cursor, 'River Publishing', 'https://blueriverpub.com', 'contact@blueriverpub.com', '4255551283', '123 Maple St, Seattle, WA')
    
    add_magazine(cursor, 'The Nature', '978-0-123456-78-9', 'Literature', 'English', 1)
    add_magazine(cursor, 'Science Monthly', '978-1-234567-89-0', 'Science', 'English', 2)
    add_magazine(cursor, 'Travel Guide', '978-2-345678-90-1', 'Travel', 'Spanish', 3)
    add_magazine(cursor, 'Tech Trends', '978-3-456789-01-2', 'Technology', 'French', 4)
    add_magazine(cursor, 'Art & Culture', '978-4-567890-12-3', 'Art & Culture', 'English', 5)
    add_magazine(cursor, 'The Nature', '978-0-123456-78-9', 'Literature', 'English', 1)
    
    add_subscriber(cursor, 'Alice', 'Prince', 'alice.smith@example.com', 5551234567) 
    add_subscriber(cursor, 'Alice', 'Johnson', 'bob.johnson@example.com', 5559876543) 
    add_subscriber(cursor, 'Charlie', 'Brown', 'charlie.brown@example.com', 5555555555) 
    add_subscriber(cursor, 'Diana', 'Prince', 'diana.prince@example.com', 5551112222)
    add_subscriber(cursor, 'Ethan', 'Smith', 'ethan.hunt@example.com', 5553334444)
    add_subscriber(cursor, 'Alice', 'Prince', 'alice.smith@example.com', 5551234567) 
    
    add_subscription(cursor, 1, 1, '2024-01-01', '2024-12-31')
    add_subscription(cursor, 1, 2, '2024-02-01', '2024-11-30')
    add_subscription(cursor, 2, 3, '2024-03-01', '2024-10-31')
    add_subscription(cursor, 3, 4, '2024-04-01', '2024-09-30')
    add_subscription(cursor, 4, 5, '2024-05-01', '2024-08-31')
    add_subscription(cursor, 1, 1, '2024-01-01', '2024-12-31')
    

    # SQL queries
    # List of subscribers
    try: 
        cursor.execute("SELECT * FROM Subscribers")
        results = cursor.fetchall()
        for row in results: 
            print("Subscribers:",row)
    except Exception as e:
        print(f"Error occurred: {e}")

    # List of magazines
    try: 
        cursor.execute("SELECT * FROM Magazines ORDER BY title")
        results = cursor.fetchall()
        for row in results: 
            print("Magazines:",row)
    except Exception as e:
        print(f"Error occurred: {e}")

    # List of magazines by a specific publisher
    try: 
        cursor.execute("SELECT m.magazine_id, m.title, m.isbn, m.category, m.language FROM Publishers p JOIN Magazines m ON p.publisher_id = m.publisher_id WHERE p.publisher_id = 2 ORDER BY m.title")
        results = cursor.fetchall()
        for row in results: 
            print("Northstar Media Magazines:",row)
    except Exception as e:
        print(f"Error occurred: {e}")


    # cursor.execute("DROP TABLE IF EXISTS subscriptions")
    # cursor.execute("DROP TABLE IF EXISTS subscribers")
    # cursor.execute("DROP TABLE IF EXISTS magazines")
    # cursor.execute("DROP TABLE IF EXISTS publishers")

    conn.commit() 
    print("Updated successfully.")
    

    

