from movies import MovieDB, UserDB

def main_menu():
    while True:
        print("\n1. Movie Operations")
        print("2. User Operations")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            movie_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again")

def movie_operations():
    db = MovieDB()
    while True:
        print("\n1. Add Movie")
        print("2. Delete Movie")
        print("3. Add Review to Movie")
        print("4. List Movies")
        print("5. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_movie(db)
        elif choice == '2':
            delete_movie(db)
        elif choice == '3':
            add_review(db)
        elif choice == '4':
            list_movies(db)
        elif choice == '5':
            db.close()
            break
        else:
            print("Invalid choice. Please try again")

def add_movie(db):
    title = input("Enter movie title: ")
    director = input("Enter director name: ")
    year = int(input("Enter release year: "))
    db.add_movie(title, director, year)

def delete_movie(db):
    movie_id = input("Enter Movie ID to delete: ")
    if movie_id.isdigit():
        db.delete_movie(int(movie_id))
    else:
        print("Invalid movie ID. Please enter a number.")

def add_review(db):
    movie_id = input("Enter movie ID to review: ")
    if movie_id.isdigit():
        review_text = input("Enter your review: ")
        db.add_review(int(movie_id), review_text)
    else:
        print("Invalid movie ID. Please enter a number.")

def list_movies(db):
    movies = db.list_movies()
    for movie in movies:
        print(f"Movie ID: {movie[0]}, Title: {movie[1]}, Director: {movie[2]}, Year: {movie[3]}")
        if movie[4]:  
            print("Reviews:")
            for review in movie[4].splitlines():
                print(f"  - {review}")

def user_operations():
    db = UserDB()
    while True:
        print("\n1. Add User")
        print("2. Delete User")
        print("3. List Users")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            add_user(db)
        elif choice == '2':
            delete_user(db)
        elif choice == '3':
            list_users(db)
        elif choice == '4':
            db.close()
            break
        else:
            print("Invalid choice. Please try again")

def add_user(db):
    username = input("Enter username: ")
    ticket = input("Enter ticket: ")
    ticket_amount = input("Enter ticket amount: ")
    gender = input("Enter gender: ")
    db.add_user(username, ticket, ticket_amount, gender)
    print(f"User '{username}' added.")

def delete_user(db,):
    username = input("Enter username to delete: ")
    db.delete_user(username)


def list_users(db):
    users = db.list_users()
    if users:
        for user in users:
            print(f"Username: {user[0]}")
    else:
        print("No users found.")

def delete_ticket(user_id):
    db = UserDB()
    db.delete_ticket(user_id)
    db.close()

if __name__ == '__main__':
    main_menu()
