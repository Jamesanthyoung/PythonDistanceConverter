def metres_to_kilometres(metres):
    """Convert Metres to Kilometres."""
    return metres / 1000


def kilometres_to_metres(kilometres):
    """Convert Kilometres to Metres."""
    return kilometres * 1000


def metres_to_miles(metres):
    """Convert Metres to Miles."""
    return metres / 1609.344


def miles_to_metres(miles):
    """Convert Miles to Metres."""
    return miles * 1609.344


def kilometres_to_miles(kilometres):
    """Convert Kilometres to Miles."""
    return kilometres / 1.609


def miles_to_kilometres(miles):
    """Convert Miles to Kilometres."""
    return miles * 1.609


def main():
    print("Distance Conversion Program")
    print("1. Metres to Kilometres")
    print("2. Kilometres to Metres")
    print("3. Metres to Miles")
    print("4. Miles to Metres")
    print("5. Kilometres to Miles")
    print("6. Miles to Kilometres")

    choice = int(input("Enter your choice (1/2/3/4/5/6): "))

    if choice == 1:
        distance_metres = float(
            input("Enter the distance in metres: "))
        distance_kilometres = metres_to_kilometres(distance_metres)
        print(f"{distance_metres:.2f} metres is equal to {distance_kilometres:.2f} kilometres.")
    elif choice == 2:
        distance_kilometres = float(
            input("Enter the distance in Kilometres: "))
        distance_metres = kilometres_to_metres(distance_kilometres)
        print(f"{distance_kilometres:.2f} kilometres is equal to {distance_metres:.2f} metres.")
    elif choice == 3:
        distance_metres = float(
            input("Enter the distance in metres: "))
        distance_miles = metres_to_miles(distance_metres)
        print(
            f"{distance_metres:.2f} metres is equal to {distance_miles:.2f} miles.")
    elif choice == 4:
        distance_miles = float(input("Enter the distance in miles: "))
        distance_metres = miles_to_metres(distance_miles)
        print(
            f"{distance_miles:.2f} miles is equal to {distance_metres:.2f} metres.")
    elif choice == 5:
        distance_kilometres = float(
            input("Enter the distance in kilometres: "))
        distance_miles = kilometres_to_miles(distance_kilometres)
        print(f"{distance_kilometres:.2f} kilometres is equal to {distance_miles:.2f} miles.")
    elif choice == 6:
        distance_miles = float(
            input("Enter the distance in miles: "))
        distance_kilometres = miles_to_kilometres(distance_miles)
        print(
            f"{distance_miles:.2f} miles is equal to {distance_kilometres:.2f} kilometres.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")


if __name__ == "__main__":
    main()