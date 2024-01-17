from categories import functional, procedural, imperative, reflective, scripting
from dbms import Blog
import os


def show_example(choice):
    if choice == "1":
        print("\nProcedural Programming")
        procedural.main()
    elif choice == "2":
        print("\nObject-Oriented Programming")
        Blog.main()
    elif choice == "3":
        print("\nFunctional Programming")
        functional.main()
    elif choice == "4":
        print("\nImperative Programming")
        imperative.main()
    elif choice == "5":
        print("\nReflective Programming")
        reflective.main()
    elif choice == "6":
        print("\nScripting Language Paradigm")
        scripting.main()
    elif choice == "7":
        print("\nModular Programming")
    # TODO: fix package reference - cannot access main python
    #        modulee.main.main()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")


def main():
    while True:
        print("\n\nChoose a programming paradigmnn example to display:")
        print("1: Procedural Programming")
        print("2: Object-Oriented Programming")
        print("3: Functional Programming")
        print("4: Imperative Programming")
        print("5: Reflective Programming")
        print("6: Scripting Language Paradigm")
        print("7: Modular Programming")
        print("Enter 'q' to quit.")

        user_input = input("Your choice: ")
        if user_input.lower() == 'q':
            break
        else:
            show_example(user_input)


if __name__ == "__main__":
    main()
