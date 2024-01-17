import logging
import os
import sqlite3

logging.basicConfig(level=logging.DEBUG)


def create_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def close_connection(conn):
    conn.close()


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


def add_post(conn):
    title = input("Enter the post title: ")
    content = input("Enter the post content: ")
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


def get_all_posts(conn):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM posts;
        """
    )
    posts = cursor.fetchall()
    logging.debug(f"Retrieved posts: {posts}")
    for id, title, content in posts:
        print(f"\nID: {id}\nTitle: {title}\nContent: {content}")


def delete_post(conn):
    id = int(input("Enter the ID of the post you want to delete: "))
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM posts WHERE id = ?;
        """,
        (id,)
    )
    conn.commit()
    logging.debug(f"Deleted post with ID: {id}")


def remove_db(conn, db_name):
    close_connection(conn)
    if os.path.exists(db_name):
        os.remove(db_name)
        logging.debug(f"Removed database file: {db_name}")


def main():
    print("Welcome to the Blog Management System!")
    print(
        "\nThis application uses the reflective programming paradigmnn. Reflective programming allows a program to inspect and modify its own structure and behavior.")
    print(
        "Now you will interact with a SQLite database to manage blog posts. Please choose your action from the menu below.")

    db_name = 'blog.db'
    conn = create_connection(db_name)
    initialize(conn)

    # Reflective Concept: Mapping user inputs to function calls
    # The program inspects this mapping to determine which function to call based on the user's input
    actions = {'1': add_post, '2': get_all_posts, '3': delete_post}

    while True:
        print("\n1. Add post\n2. View all posts\n3. Delete post\n4. Quit")
        choice = input("Choose an option: ")

        # Reflective Concept: Dynamically calling a function based on user's choice
        # The program modifies its behavior at runtime based on this dynamic function call
        if choice in actions:
            actions[choice](conn)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

    remove_db(conn, db_name)


if __name__ == "__main__":
    main()
