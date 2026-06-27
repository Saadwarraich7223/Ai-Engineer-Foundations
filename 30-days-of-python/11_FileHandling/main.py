# Day 11 � File I/O & Context Managers
# Date: July 04, 2026
#
# Learning Goals:
# TODO: Fill in what you learned today, code exercises, and notes.


while True:
    print("\n========== FILE MANAGER ==========")
    print("1. Create / Overwrite File")
    print("2. Read Entire File")
    print("3. Read Line by Line")
    print("4. Append to File")
    print("5. Show Pointer Position")
    print("6. Replace First Word")
    print("7. Exit")

    choice = input("Choose an option: ")

    try:

        if choice == "1":
            text = input("Enter text: ")

            with open("data.txt", "w") as f:
                f.write(text)

            print("File saved successfully.")

        elif choice == "2":

            with open("data.txt", "r") as f:
                print("\n----- FILE CONTENT -----")
                print(f.read())

        elif choice == "3":

            with open("data.txt", "r") as f:

                print("\nUsing readline():")
                f.seek(0)
                print(f.readline().strip())

                print("\nUsing readlines():")
                f.seek(0)

                for line in f.readlines():
                    print(line.strip())

        elif choice == "4":

            text = input("Enter text to append: ")

            with open("data.txt", "a") as f:
                f.write("\n" + text)

            print("Text appended.")

        elif choice == "5":

            with open("data.txt", "r") as f:

                print("Pointer:", f.tell())

                print(f.read(5))

                print("Pointer:", f.tell())

                f.seek(0)

                print("Pointer after seek:", f.tell())

        elif choice == "6":

            with open("data.txt", "r+") as f:

                content = f.read()

                f.seek(0)

                f.write("Python ")

                print("\nUpdated Content:\n")

                f.seek(0)

                print(f.read())

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print("Unexpected Error:", e)

    finally:
        print("\nOperation Completed.")
    