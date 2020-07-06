SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100  

# create the calculate_price functions, which takes number of tickets and returns
#   ticket_quantity * TICKET_PRICE

def calculate_price(ticket_quantity):
    #create new constant for $2 service charge
    #add service charge to amount due
    return (ticket_quantity * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    name = input("What is your name?  ")
    ticket_quantity = input("Hello, {}, how many tickets would you like to purchase?  ".format(name))
    try:        
        ticket_quantity = int(ticket_quantity)
        if ticket_quantity > tickets_remaining:
            raise ValueError("There are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {} Please try again.".format(err))
    else:    
        price = calculate_price(ticket_quantity)
        print("Thanks, {}!".format(name),  "Your order total is ${}.".format(price))
        proceed = input("Would you like to proceed? Y/N?  ")
        if proceed.lower() != "y":
            print("Thank you, {}.".format(name))
        else:
            print("SOLD!")
            tickets_remaining -= ticket_quantity

else: print("Sorry, but tickets for this event are sold out.")