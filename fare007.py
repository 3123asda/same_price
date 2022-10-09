print("==============================================================")
print("|GOOD NEWS!                                                  |")
print("|TRAVELERS ✈ ,                                               |")
print("|                                                            |")
print("|Christmas is near,As special gift for our passengers.       |")
print("|GROUP 3 AIRLINES all ticket routes will ₱ 2,999.00          |")
print("|It's time to go your places want to spend your quality time |")
print("|with your family and love ones together.                    |")
print("|What are you wating for?                                    |")
print("|It's time limited and 500 slot only! Book your ticket now!  |")
print("==============================================================")

def flights():
    print("=============================================")
    print(f'|FLIGHTS FROM {origin} to {destination}                |')
    from datetime import date
    today = date.today()
    print(f'|AVAILABLE FLIGHTS AS OF {today}         |')
    print("---------------------------------------------")
    print(f'|7:30AM  |{origin}| ---> |9:00AM:  |{destination}| [0] |') 
    print(f'|10:00AM |{origin}| ---> |11:30AM: |{destination}| [1] |') 
    print(f'|1:30PM  |{origin}| ---> |3:00PM:  |{destination}| [2] |') 
    print(f'|4:30PM  |{origin}| ---> |6:00PM:  |{destination}| [3] |') 
    print(f'|7:30PM  |{origin}| ---> |9:00PM:  |{destination}| [4] |') 
    print("=============================================")

def payment():
    while(2):
        try:
            route = [f"7:30AM: {origin} ---> 9:00AM: {destination}",f"10:00AM: {origin} ---> 11:30AM: {destination}",f'1:30PM: {origin} ---> 3:00PM: {destination}',f'4:30PM: {origin} ---> 6:00PM: {destination}',f'7:30PM: {origin} ---> 9:00PM: {destination}']
            user = int(input("Enter the route number: \n"))
            a = route[user]
            print(a)
            while(1):
                    name_passengers = input("NAME: \n") 
                    try:
                        people_passengers = float(input('How much ticket you want to book: \n'))
                        price_ticket = 2999
                        subtotal_ticket_price_total = price_ticket * people_passengers
                        print(f'Total Amout: \n₱{subtotal_ticket_price_total}')
                        while(2):
                            try:
                                money_recieve = float(input('Money Receive: \n₱'))
                                if money_recieve < subtotal_ticket_price_total:
                                    #insu_total = money_recieve - subtotal_ticket_price_total
                                    #posu_total = insu_total * -1
                                    #print(f'Insufficient Money:\n₱{posu_total}')
                                    print('Insufficient Funds')
                                else:
                                    change_people_passengers = money_recieve - subtotal_ticket_price_total
                                    print(f'Change:₱{change_people_passengers}')
                                    quit()

                            except ValueError:
                                print('Please correctly INPUT your money')    
                    except ValueError:
                        print('Please correctly INPUT the ticket you want to book')
        except IndexError:
            route_help = input("Invalid Code! Try again! If you need help just type 'a' or 'A'").upper()
            if route_help == ('A'):
                 #put the complete information
                 pass
            else:
                print("Invalid Keyword! Try again!")    
                

while(1):
    answer = input("You want to book a ticket? (y/n/h):\n").upper()
    print('Choose your routes here: \n')

    if answer == ('Y'):
        print('=================================')
        print('| AVAILABLE ROUTES:       |CODE |')
        print('|-------------------------|-----|')
        print('| A. METRO MANILA         |  0  |')
        print('| B. BAGUIO               |  1  |')
        print('| C. CEBU                 |  2  |')
        print('| D. BOHOL                |  3  |')
        print('| E. CAGAYAN DE ORO       |  4  |')
        print('| F. DAVAO                |  5  |')
        print('=================================')
        while(2):
         while(3):
            places = ["METRO MANILA","BAGUIO","CEBU","BOHOL","CAGAYAN DE ORO","DAVAO"]
            try:
                origin_pick = int(input('Enter your location: \n'))
                display_origin_choose = places[origin_pick]
                print(display_origin_choose)

                destination_pick = int(input('Enter your destination: \n'))
                display_origin_choose = places[destination_pick]
                print(display_origin_choose)
                if origin_pick - destination_pick == 0:
                    help_ticket_book = input("Invalid Code! Try again! If you need help just type 'a' or 'A'").upper()
                    if help_ticket_book == ('A'):
                       #put the complete information
                       pass
                    else:
                        print("If you want to know all INSTRUCTION just press 'a' or 'A'")
                        #put the complete information

                    break
                else:
                     origin = places[origin_pick]
                     destination = places[destination_pick]
                     flights()
                     payment()
                     quit()
            except ValueError:
                print("Invalid Keyword! Try again!")    

        

        origin = places[origin_pick]
        destination = places[destination_pick]

        print(f'Your Flight is {origin} to {destination}')
        flights()

    elif answer == ('N'):
        quit()
    elif answer == ('H'):
        print("INSTRUCTION:")
        print(">If you want to buy a ticket just press 'y' or 'Y'")
        print(">if you don't want to buy a ticket just press 'n' or 'N'")
        help_register = input("If this helpful just press 'g' or 'G' and you want to know all INSTRUCTION just press 'a' or 'A':\n").upper()
        if help_register == ('G'):
            quit()
        elif help_register == ('A'):
            #put the complete information
            pass
        else:
            print("Invalid Keyword! Try again!")       
    else:
        print("Invalid Keyword! Try again! If you need help just type 'h' or 'H'")
