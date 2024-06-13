# to start the application - python3 cli.py
import sqlite3

class MovieDB:
    def __init__(self):
        self.connection = sqlite3.connect('movies.db')
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               title TEXT NOT NULL,
                               director TEXT,
                               year INTEGER,
                               reviews TEXT
                               )''')
        self.connection.commit()
        

    def add_movie(self, title, director, year):
        self.cursor.execute('''INSERT INTO movies (title, director, year)
                               VALUES (?, ?, ?)''', (title, director, year))
        self.connection.commit()
        print(f"Movie '{title}' added.")

    def add_review(self, movie_id, review_text):
        self.cursor.execute('''SELECT reviews FROM movies WHERE id = ?''', (movie_id,))
        current_reviews = self.cursor.fetchone()[0]

        if current_reviews:
            new_reviews = current_reviews + review_text + "\n"
        else:
            new_reviews = review_text + "\n"

        self.cursor.execute('''UPDATE movies SET reviews = ? WHERE id = ?''', (new_reviews, movie_id))
        self.connection.commit()
        print(f"Review added for movie ID {movie_id}.")

    def list_movies(self):
        self.cursor.execute("SELECT * FROM movies")
        return self.cursor.fetchall()

    def delete_movie(self, movie_id):
        self.cursor.execute('''DELETE FROM movies WHERE id = ?''', (movie_id,))
        self.connection.commit()
        print(f"Movie ID {movie_id} deleted.")

    def close(self):
        self.connection.close()


class UserDB :
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               username TEXT NOT NULL,
                               ticket TEXT NOT NULL,
                                ticket_amount INTEGER NOT NULL,
                                gender TEXT NOT NULL
                               )''')
        self.connection.commit()
    
    def add_user(self, username, ticket, ticket_amount, gender):
        self.cursor.execute('''INSERT INTO users (username, ticket, ticket_amount, gender)
                               VALUES (?, ?, ?, ?)''', (username, ticket, ticket_amount, gender))
        self.connection.commit()
        print(f"User '{username}' added.")

    def list_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()

    def get_user(self, username):
        self.cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
        return self.cursor.fetchone()
    
    def get_ticket(self, ticket):
        self.cursor.execute('''SELECT * FROM users WHERE ticket = ?''', (ticket,))
        return self.cursor.fetchone()
    
    def get_ticket_amount(self, ticket):
        self.cursor.execute('''SELECT ticket_amount FROM users WHERE ticket = ?''', (ticket,))
        return self.cursor.fetchone()

    def update_ticket_amount(self, ticket, ticket_amount):
        self.cursor.execute('''UPDATE users SET ticket_amount = ? WHERE ticket = ?''', (ticket_amount, ticket))
        self.connection.commit()
        print(f"Ticket amount updated for ticket {ticket}.")

    def update_gender(self, ticket, gender):
        self.cursor.execute('''UPDATE users SET gender = ? WHERE ticket = ?''', (gender, ticket))
        self.connection.commit()
        print(f"Gender updated for ticket {ticket}.")

    def delete_user(self, user_id):
        self.cursor.execute('''DELETE FROM users WHERE ticket = ?''', (user_id,))
        self.connection.commit()
        print(f"User deleted for ticket {user_id,}.")

    def delete_all_users(self):
        self.cursor.execute('''DELETE FROM users''')
        self.connection.commit()
        print(f"All users deleted.")

    def delete_all_tickets(self):
        self.cursor.execute('''DELETE FROM tickets''')
        self.connection.commit()
        print(f"All tickets deleted.")

    def delete_all_movies(self):
        self.cursor.execute('''DELETE FROM movies''')
        self.connection.commit()
        print(f"All movies deleted.")

    def delete_all_reviews(self):
        self.cursor.execute('''DELETE FROM reviews''')
        self.connection.commit()
        print(f"All reviews deleted.")

    def delete_all(self):
        self.delete_all_users()
        self.delete_all_tickets()
        self.delete_all_movies()
        self.delete_all_reviews()

    def close(self):
        self.connection.close()
        
        