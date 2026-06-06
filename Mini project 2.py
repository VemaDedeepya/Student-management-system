students = {}

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. View One Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully.")

    elif choice == '2':
        if not students:
            print("No students found.")
        else:
            for roll, details in students.items():
                print("Roll:", roll)
                print("Name:", details["name"])
                print("Marks:", details["marks"])
                print("------")

    elif choice == '3':
        roll = input("Enter roll number to search: ")

        if roll in students:
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
        else:
            print("Student not found.")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
