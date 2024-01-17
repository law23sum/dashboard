import logging
import os
import sqlite3

# Set up logging
logging.basicConfig(level=logging.DEBUG)


def create_connection(db_name):
    """Create a database connection and return the connection object"""
    conn = sqlite3.connect(db_name)
    return conn


def close_connection(conn):
    """Close the database connection"""
    conn.close()


def initialize(conn):
    """Create the posts table in the database if it doesn't exist."""
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


def add_post(conn, title, content):
    """Add a new post to the posts table."""
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
    """Retrieve all posts from the posts table."""
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM posts;
        """
    )
    posts = cursor.fetchall()
    logging.debug(f"Retrieved posts: {posts}")
    return posts


def delete_post(conn, id):
    """Delete a post by its ID."""
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM posts WHERE id = ?;
        """,
        (id,)
    )
    conn.commit()
    logging.debug(f"Deleted post with ID: {id}")


def main():
    """Main function that drives the program."""
    print("Welcome to the Blog Management System! This application is an example of Python's Procedural Programming.")
    print(
        "You will interact with a SQLite database to manage blog posts. Please choose your action from the menu below.")

    # Create a database connection
    db_name = 'blog.db'
    conn = create_connection(db_name)

    try:
        # Initialize the database
        initialize(conn)

        while True:
            print("\n1. Add post\n2. View all posts\n3. Delete post\n4. Quit")
            choice = input("Choose an option: ")

            if choice == '1':
                title = input("Enter the post title: ")
                content = input("Enter the post content: ")
                add_post(conn, title, content)
            elif choice == '2':
                posts = get_all_posts(conn)
                for id, title, content in posts:
                    print(f"\nID: {id}\nTitle: {title}\nContent: {content}")
            elif choice == '3':
                id = int(input("Enter the ID of the post you want to delete: "))
                delete_post(conn, id)
            elif choice == '4':
                break
            else:
                print("Invalid option. Please choose again.")
    finally:
        # Close the connection
        close_connection(conn)

        # Remove the database file
        if os.path.exists(db_name):
            os.remove(db_name)
            logging.debug(f"Removed database file: {db_name}")


if __name__ == "__main__":
    main()
