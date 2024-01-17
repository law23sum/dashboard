import logging
import os
import sqlite3


def main():
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)

    db_name = 'blog.db'
    conn = sqlite3.connect(db_name)

    # Create posts table in the database if it doesn't exist
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

    while True:
        print("\n1. Add post\n2. View all posts\n3. Delete post\n4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            # Add a new post to the posts table
            title = input("Enter the post title: ")
            content = input("Enter the post content: ")
            cursor.execute(
                """
                INSERT INTO posts (title, content)
                VALUES (?, ?);
                """,
                (title, content)
            )
            conn.commit()
            logging.debug(f"Added post: {title}")

        elif choice == '2':
            # Retrieve all posts from the posts table
            cursor.execute(
                """
                SELECT * FROM posts;
                """
            )
            posts = cursor.fetchall()
            logging.debug(f"Retrieved posts: {posts}")
            for id, title, content in posts:
                print(f"\nID: {id}\nTitle: {title}\nContent: {content}")

        elif choice == '3':
            # Delete a post by its ID
            id = int(input("Enter the ID of the post you want to delete: "))
            cursor.execute(
                """
                DELETE FROM posts WHERE id = ?;
                """,
                (id,)
            )
            conn.commit()
            logging.debug(f"Deleted post with ID: {id}")

        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

    # Close the database connection
    conn.close()

    # Remove the database file
    if os.path.exists(db_name):
        os.remove(db_name)
        logging.debug(f"Removed database file: {db_name}")


if __name__ == "__main__":
    main()
