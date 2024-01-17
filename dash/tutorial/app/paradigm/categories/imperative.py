import logging
import os
import sqlite3

# Set up logging
logging.basicConfig(level=logging.DEBUG)


# Establish a connection to the database (Imperative: Command)
def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


# Close the database connection (Imperative: Command)
def close_connection(conn):
    conn.close()


# Initialize the database (Imperative: Sequence of commands)
def initialize(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
        """
    )
    conn.commit()
    logging.debug("Initialized the database.")


# Add a post to the database (Imperative: Sequence of commands)
def add_post(conn, title, content):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO posts (title, content)
        VALUES (?, ?);
        """,
        (title, content)
    )
    conn.commit()
    logging.debug(f"Added post: {title}")


# Retrieve all posts from the database (Imperative: Sequence of commands)
def get_all_posts(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM posts;
        """
    )
    posts = cursor.fetchall()
    logging.debug(f"Retrieved posts: {posts}")
    return posts


# Delete a post from the database (Imperative: Sequence of commands)
def delete_post(conn, id):
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM posts WHERE id = ?;
        """,
        (id,)
    )
    conn.commit()
    logging.debug(f"Deleted post with ID: {id}")


# Remove the database file (Imperative: Sequence of commands)
def remove_db(conn, db_name):
    close_connection(conn)
    if os.path.exists(db_name):
        os.remove(db_name)
        logging.debug(f"Removed database file: {db_name}")


# Main function that controls the program flow (Imperative: Sequence of commands)
def main():
    print("Welcome to the Blog Management System!")
    print("\nThis application uses the imperative programming paradigmnn.")
    print("Please choose your action from the menu below.")

    db_name = 'blog.db'
    conn = create_connection(db_name)  # Imperative: Command
    initialize(conn)  # Imperative: Command

    while True:  # Imperative: Loop (sequence of commands)
        print("\n1. Add post\n2. View all posts\n3. Delete post\n4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the post title: ")
            content = input("Enter the post content: ")
            add_post(conn, title, content)  # Imperative: Command
        elif choice == '2':
            posts = get_all_posts(conn)  # Imperative: Command
            for id, title, content in posts:  # Imperative: Loop (sequence of commands)
                print(f"\nID: {id}\nTitle: {title}\nContent: {content}")
        elif choice == '3':
            id = int(input("Enter the ID of the post you want to delete: "))
            delete_post(conn, id)  # Imperative: Command
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

    remove_db(conn, db_name)  # Imperative: Command


if __name__ == "__main__":
    main()
