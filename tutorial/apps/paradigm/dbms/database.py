import logging
import sqlite3

# Set up logging
logging.basicConfig(level=logging.INFO)


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
