# Task 1
print("\nCustomer Service Ticket Tracker")

customer_service_tickets = {}
 
def open_service_ticket():
    
    ticket_number = input("\nTicket #")
        
    name = input("\nWhat is your name? ")
    
    issue = input("\nWhat issue are you having? ")
    
    status = input("\nCurrent status? (Open or Closed) ")
    
    new_ticket = customer_service_tickets[ticket_number] = {
        "Customer": name,
        "Issue": issue,
        "Status": status
        }
    print(f"Ticket has been added {new_ticket}")


def display_tickets():
 if not customer_service_tickets:
        print("\nThere are currently no tickets.")
        return
 else:
        for service_ticket, information in customer_service_tickets.items():
            print(f"\nTicket #{service_ticket}")
            for key in information:
                print(key + ": " + information[key])


def update_status():
   if not customer_service_tickets:
        print("\nThere are currently no tickets.")
        return
   else:
       display_tickets()
       print("\nWhat ticket would you like to update")
       ticket_number = input("Ticket #")

       customer_service_tickets[ticket_number]["Status"] = "Closed"


while True:
    print("\nMenu")
    print('1. Add a new ticket')
    print('2. Update Existing Status')
    print('3. Display all tickets')
    print('4. Quit')
    try:
        decision = input("\nWhat would you like to do? ")
    except ValueError:
        print('\nPlease enter a number.')
    

    if decision == '1': # Add a ticket
        open_service_ticket()
    elif decision == '2': # Update a ticket
        update_status()
    elif decision == '3': # Show all tickets
        display_tickets()
    elif decision == '4': # Exit the system
        break
    else:
        print("\nInvalid input. Please enter another number and try again.")

