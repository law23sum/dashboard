import os

from database import create_connection, close_connection, initialize, add_post, get_all_posts, delete_post


def remove_db(conn, db_name):
    """Remove the database file"""
    close_connection(conn)
    if os.path.exists(db_name):
        os.remove(db_name)


def main():
    """Main function that drives the program."""
    print("Welcome to the Blog Management System!")
    print("\nThis application uses the imperative programming paradigmnn.")
    print("Please choose your action from the menu below.")

    db_name = 'blog.db'
    conn = create_connection(db_name)
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

    remove_db(conn, db_name)


if __name__ == "__main__":
    main()
