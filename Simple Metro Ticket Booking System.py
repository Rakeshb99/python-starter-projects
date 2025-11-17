# Simple Metro Ticket Booking System

print("===== Welcome to Metro Ticket Booking System =====")

# Available stations and their ticket prices
stations = {
    1: ("Madavara", 20),
    2: ("Vijaya nagara", 25),
    3: ("Jayanagara", 15),
    4: ("Banashankari", 30)
}

# Display available stations
print("\nAvailable Destinations:")
for key, (name, price) in stations.items():
    print(f"{key}. {name} - ₹{price}")

# User selects station
choice = int(input("\nEnter the station number you want to travel to: "))

if choice in stations:
    station_name, ticket_price = stations[choice]
    print(f"Selected Destination: {station_name}")
    
    # Number of tickets
    qty = int(input("Enter number of tickets: "))
    
    total_cost = ticket_price * qty
    
    # Print receipt
    print("\n===== TICKET RECEIPT =====")
    print(f"Destination : {station_name}")
    print(f"Ticket Price: ₹{ticket_price}")
    print(f"Tickets     : {qty}")
    print(f"Total Cost  : ₹{total_cost}")
    print("==========================")
else:
    print("Invalid station number. Please restart the program.")
