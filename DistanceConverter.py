#Convert Metres to Kilometres
def metres_to_kilometres(metres):
    return metres / 1000

#Convert Kilometres to Metres
def kilometres_to_metres(kilometres):
    return kilometres * 1000

#Convert Metres to Miles
def metres_to_miles(metres):
    return metres / 1609.344

#Convert Miles to Metres
def miles_to_metres(miles):
    return miles * 1609.344

#Convert Kilometres to Miles
def kilometres_to_miles(kilometres):
    return kilometres / 1.609

#Convert Miles to Kilometres
def miles_to_kilometres(miles):
    return miles * 1.609


def main():
    print("Distance Conversion Program")
    print("1. Metres to Kilometres")
    print("2. Kilometres to Metres")
    print("3. Metres to Miles")
    print("4. Miles to Metres")
    print("5. Kilometres to Miles")
    print("6. Miles to Kilometres")

    #take user input and select method depending on converstion
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
        #if the input is not an integer between 1-6 then return this message
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")


if __name__ == "__main__": # pragma: no mutate
    main()