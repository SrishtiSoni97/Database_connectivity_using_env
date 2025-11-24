from dbconnection import get_connection

def insert(table, data):
    columns = ",".join(data.keys())
    placeholder = ",".join(["%s"] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table} ({columns}) values ({placeholder})"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()

    print("Record inserted Successfully")

    cursor.close()
    conn.close()


def get_data(table):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()


def delete_data(table, col, value):
    conn = get_connection()
    cursor = conn.cursor()

    query = f"DELETE FROM {table} WHERE {col} = %s"

    cursor.execute(query, (value,))
    conn.commit()

    print("Record deleted successfully!")

    cursor.close()
    conn.close()


# ------------------ MENU PROGRAM --------------------

def run_menu():
    while True:
        print("\nChoose an action:")
        print("1. Insert")
        print("2. Get (Select All)")
        print("3. Delete")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ").strip()

        if choice == "1":
            table = input("Enter table name: ").strip()
            data = {}

            print("Enter column/value pairs. Type 'done' when finished.")

            while True:
                col = input("Column name: ").strip()
                if col.lower() == "done":
                    break

                val = input("Value: ").strip()

                
                if val.isdigit():
                    val = int(val)

                data[col] = val

            insert(table, data)

        elif choice == "2":
            table = input("Enter table name: ").strip()
            get_data(table)

        elif choice == "3":
            table = input("Enter table name: ").strip()
            col = input("Enter column name to delete by: ").strip()
            val = input("Enter value to match: ").strip()

           
            if val.isdigit():
                val = int(val)

            delete_data(table, col, val)

        elif choice == "4":
            print("Exiting program…")
            break

        else:
            print("Invalid choice. Try again.")


# Start Menu
run_menu()
