print('Good Day! Welcome to Airlines Corner. Book your flight today!')
print('Choose your routes here: \n')

print('=================================')
print('| AVAILABLE ROUTES:      | CODE |')
print('|                               |')
print('| METRO MANILA           |  A   |')
print('| BAGUIO                 |  B   |')
print('| CEBU                   |  C   |')
print('| BOHOL                  |  D   |')
print('| CAGAYAN DE ORO         |  E   |')
print('| DAVAO                  |  F   |')
print('=================================')

# 0 = location, 1 = code letter, 2 = airport location
a = 'METRO MANILA', 'A', 'NINOY AQUINO INTERNATIONAL AIRPORT'
b = 'BAGUIO', 'B', 'LOAKAN AIRPORT'
c = 'CEBU', 'C', 'MACTAN CEBU INTERNATIONAL AIRPORT'
d = 'BOHOL', 'D', 'BOHOL-PANGLAO INTERNATIONAL AIRPORT'
e = 'CAGAYAN DE ORO', 'E', 'LAGUINDINGAN AIRPORT'
f = 'DAVAO', 'F', 'FRANCISCO BANGOY INTERNATIONAL AIRPORT'

# 0 = timestamp, 1 = code number, 2 = ticket amount

#ECONOMY CLASS
g = '7:30AM ---> 9:00AM', 'G', 1400
h = '10:00AM ---> 11:30AM', 'H', 1600
i = '1:30PM ---> 3:00PM', 'I', 1700
j = '4:30PM ---> 6:00PM', 'J',1900
k = '7:30PM ---> 9:00PM', 'K', 2100

#PREMIUM ECONOMY CLASS
o = '7:30AM ---> 9:00AM', 'O', 2400
p = '10:00AM ---> 11:30AM', 'P', 2600
q = '1:30PM ---> 3:00PM', 'Q', 2700
r = '4:30PM ---> 6:00PM', 'R',2900
s = '7:30PM ---> 9:00PM', 'S', 3100

#BUSINESS CLASS
t = '7:30AM ---> 9:00AM', 'T', 3400
w = '10:00AM ---> 11:30AM', 'W', 3600
x = '1:30PM ---> 3:00PM', 'X', 3700
y = '4:30PM ---> 6:00PM', 'Y',3900
z = '7:30PM ---> 9:00PM', 'Z', 4100

#FIRST CLASS
aa = '7:30AM ---> 9:00AM', 'AA', 4400
bb = '10:00AM ---> 11:30AM', 'BB', 4600
cc = '1:30PM ---> 3:00PM', 'CC', 4700
dd = '4:30PM ---> 6:00PM', 'DD',4900
ee = '7:30PM ---> 9:00PM', 'EE', 5100                 

def section_class_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['0','1','2','3']")
    print('================================')
    print('|SECTION CLASS          | CODE |')
    print('--------------------------------')
    print('|ECONOMY CLASS          |  0   |')
    print('|PREMIUM-ECONOMY SECTION|  1   |')
    print('|BUSINESS CLASS SECTION |  2   |')
    print('|FIRST CLASS SECTION    |  3   |')
    print('================================')

def available_route_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','B','C','D','E','F']")
    print('=================================')
    print('| AVAILABLE ROUTES:      | CODE |')
    print('|                               |')
    print('| METRO MANILA           |  A   |')
    print('| BAGUIO                 |  B   |')
    print('| CEBU                   |  C   |')
    print('| BOHOL                  |  D   |')
    print('| CAGAYAN DE ORO         |  E   |')
    print('| DAVAO                  |  F   |')
    print('=================================')

def manila_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['B','C','D','E','F']")
    manila_origin()

def baguio_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','C','D','E','F']")    
    baguio_origin()

def cebu_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','B','D','E','F']")
    cebu_origin()

def bohol_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','B','C','E','F']")
    bohol_origin()

def cdo_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','B','C','D','F']")
    cdo_origin()

def davao_destination_invalid_keyword():
    print("INVALID KEYWORD,PICK ONLY ONE SPECIFIC CODE BETWEEN['A','B','C','D','E']")
    davao_origin()

def manila_origin():
    print('\n============================================')
    print('|-----METRO MANILA ROUTES-----        | CODE |')
    print('|                                            |')
    print('| METRO MANILA ------> BAGUIO         |  B   |')
    print('| METRO MANILA ------> CEBU           |  C   |')
    print('| METRO MANILA ------> BOHOL          |  D   |')
    print('| METRO MANILA ------> CDO            |  E   |')
    print('| METRO MANILA ------> DAVAO          |  F   |')
    print('==============================================')

def baguio_origin():
    print('\n============================================')
    print('|--------BAGUIO ROUTES---------       | CODE |')
    print('|                                            |')
    print('| BAGUIO ------> METRO MANILA         |  A   |')
    print('| BAGUIO ------> CEBU                 |  C   |')
    print('| BAGUIO ------> BOHOL                |  D   |')
    print('| BAGUIO ------> CDO                  |  E   |')
    print('| BAGUIO ------> DAVAO                |  F   |')
    print('==============================================')

def cebu_origin():
    print('\n============================================')
    print('|--------CEBU ROUTES---------         | CODE |')
    print('|                                            |')
    print('| CEBU ------> METRO MANILA           |  A   |')
    print('| CEBU ------> BAGUIO                 |  B   |')
    print('| CEBU ------> BOHOL                  |  D   |')
    print('| CEBU ------> CDO                    |  E   |')
    print('| CEBU ------> DAVAO                  |  F   |')
    print('==============================================')

def bohol_origin():
    print('\n============================================')
    print('|--------BOHOL ROUTES---------        | CODE |')
    print('|                                            |')
    print('| BOHOL ------> METRO MANILA          |  A   |')
    print('| BOHOL ------> BAGUIO                |  B   |')
    print('| BOHOL ------> CEBU                  |  C   |')
    print('| BOHOL ------> CDO                   |  E   |')
    print('| BOHOL ------> DAVAO                 |  F   |')
    print('==============================================')

def cdo_origin():
    print('\n============================================')
    print('|--------CDO ROUTES----------         | CODE |')
    print('|                                            |')
    print('| CDO ------> METRO MANILA            |  A   |')
    print('| CDO ------> BAGUIO                  |  B   |')
    print('| CDO ------> CEBU                    |  C   |')
    print('| CDO ------> BOHOL                   |  D   |')
    print('| CDO ------> DAVAO                   |  F   |')
    print('==============================================')

def davao_origin():
    print('\n============================================')
    print('|--------DAVAO ROUTES----------       | CODE |')
    print('|                                            |')
    print('| DAVAO ------> METRO MANILA          |  A   |')
    print('| DAVAO ------> BAGUIO                |  B   |')
    print('| DAVAO ------> CEBU                  |  C   |')
    print('| DAVAO ------> BOHOL                 |  D   |')
    print('| DAVAO ------> CDO                   |  E   |')
    print('==============================================')
"""
def timestamp():
    from datetime import date
    today = date.today()
    print(f'\nAVAILABLE FLIGHTS AS OF {today}.')
    print('\n===============================================')
    print('| |    TIME STAMPS           |   PRICE   | CODE |')
    print('|-----------------------------------------------|')
    print('| 7:30 AM -----> 9:00 AM     |  ₱1,400   |  G   |')
    print('| 10:00 AM -----> 11:30 AM   |  ₱1,600   |  H   |')
    print('| 1:30 PM -----> 3:00 PM     |  ₱1,700   |  I   |')
    print('| 4:30 PM -----> 6:00 PM     |  ₱1,900   |  J   |')
    print('| 7:30 PM -----> 9:00 PM     |  ₱2,100   |  K   |')
    print('=================================================')
"""



def receipt():
    print(f'CHANGE: {change}')
    print('\n=========================================')
    print('-------------AIRLINES CORNER-------------')
    print('             BOOKING DETAILS             ')
    print(f'{origin} -----> {destination}')
    print(f'{origin_airport} \n-----> {destination_airport}')
    print(f'TIME: {time}')
    print(f'NUMBER OF PASSENGERS: {quantity}')
    print(f'AMOUNT: ₱{float(amount)}')
    print(f'TOTAL AMOUNT: ₱{total}')    
    print('=========================================')

def final_receipt():
    print('\n=========================================')
    print('-------------AIRLINES CORNER-------------')
    print('             BOOKING DETAILS             ')
    print(f'{origin} -----> {destination}')
    print(f'{origin_airport} \n-----> {destination_airport}')
    print(f'TIME: {time}')
    print(f'NUMBER OF PASSENGERS: {quantity}')
    print(f'AMOUNT: ₱{float(amount)}')
    print(f'TOTAL AMOUNT: ₱{total}')    
    print(f'CASH: ₱{money}')
    print(f'CHANGE: ₱{change}')
    print('=========================================')
    print('\nTHANK YOU FOR BOOKING IN AIRLINES CORNER! HAVE A SAFE TRIP!')
    quit()

def economy_time():
    while(5):
        global time
        time = input('\nINPUT FLIGHT TIME (G-K): \n').upper()
        if time == (g[1]):
            time = (g[0])
            global amount
            amount = (g[2])
            economy_class_payment()
            receipt()
            confirm()
            
        if time == (h[1]):
            time = (h[0])
            amount = (h[2])
            economy_class_payment()
            receipt()
            confirm()

        if time == (i[1]):
            time = (i[0])
            amount = (i[2])
            economy_class_payment()
            receipt()
            confirm()

        if time == (j[1]):
            time = (j[0])
            amount = (j[2])
            economy_class_payment()
            receipt()
            confirm()

        if time == (k[1]):
            time = (k[0])
            amount = (k[2])
            economy_class_payment()
            receipt()
            confirm()

        else:
            print('INVALID KEYWORD')

def confirm():
    while(4):
        confirm = input('\nCONFIRM BOOKING? (y/n): ').upper()
        if confirm == 'Y':
            final_receipt()
        elif confirm == 'N':
            print('THANK YOU FOR VISITNG AIRLINES CORNER! STAY SAFE PIPS!')
            quit()
        else:
            print('INVALID KEYWORD!')

def economy_class_payment():
    while(1):
        pass
        while(2):
            try:
                global quantity
                quantity = int(input('BOOK TICKETS: \n'))
                if quantity > 112:
                    print('ECONOMY CLASS CURRENTLY 112 SEAT AVALIABLE')
                    break
                else:
                    global total
                    total = float(quantity) * amount
                    print(f'\nTOTAL AMOUNT: ₱{total}')
                    while(3):
                        global money
                        money = float(input('\nMONEY RECEIVED: \n'))
                        if money < total:
                            print('INSUFFICIENT MONEY')
                        
                        else:
                            global change
                            change = money - total
                            return


            except ValueError:
                print('INVALID NUMBER!!')

def class_passenger():
    print('================================')
    print('|SECTION CLASS          | CODE |')
    print('--------------------------------')
    print('|ECONOMY CLASS          |  0   |')
    print('|PREMIUM-ECONOMY SECTION|  1   |')
    print('|BUSINESS CLASS SECTION |  2   |')
    print('|FIRST CLASS SECTION    |  3   |')
    print('================================')
    while(1):
        try:
            class_passenger_choose = int(input('ENTER THE CODE CLASS: \n'))
            if class_passenger_choose == 0:
                economy_class()
            elif class_passenger_choose == 1:
                premium_economy_class()
            elif class_passenger_choose == 2:
                business_class()
            elif class_passenger_choose == 3:
                first_class()
            else:
                section_class_invalid_keyword()
        except ValueError:
            section_class_invalid_keyword()      
               






    

def economy_class():    
    while(6):
            print('ECONOMY CLASS')
            from datetime import date
            today = date.today()
            print(f'\nAVAILABLE FLIGHTS AS OF {today}.')
            print('=================================================')
            print('|      TIME STAMPS           |   PRICE   | CODE |')
            print('|-----------------------------------------------|')
            print('| 7:30 AM -----> 9:00 AM     |  ₱1,400   |  G   |')
            print('| 10:00 AM -----> 11:30 AM   |  ₱1,600   |  H   |')
            print('| 1:30 PM -----> 3:00 PM     |  ₱1,700   |  I   |')
            print('| 4:30 PM -----> 6:00 PM     |  ₱1,900   |  J   |')
            print('| 7:30 PM -----> 9:00 PM     |  ₱2,100   |  K   |')
            print('=================================================')
            economy_time()
           
def premium_economy_class():
    while(6):
        print('PREMIUM ECONOMY CLASS')
        from datetime import date
        today = date.today()
        print(f'\nAVAILABLE FLIGHTS AS OF {today}.')
        print('=================================================')
        print('|      TIME STAMPS           |   PRICE   | CODE |')
        print('|-----------------------------------------------|')
        print('| 7:30 AM -----> 9:00 AM     |  ₱2,400   |  O   |')
        print('| 10:00 AM -----> 11:30 AM   |  ₱2,600   |  P   |')
        print('| 1:30 PM -----> 3:00 PM     |  ₱2,700   |  Q   |')
        print('| 4:30 PM -----> 6:00 PM     |  ₱2,900   |  R   |')
        print('| 7:30 PM -----> 9:00 PM     |  ₱3,100   |  S   |')
        print('=================================================')
        premium_time()

        
def business_class():
    while(6):
        print('BUSINESS CLASS')
        from datetime import date
        today = date.today()
        print(f'\nAVAILABLE FLIGHTS AS OF {today}.')
        print('=================================================')
        print('|      TIME STAMPS           |   PRICE   | CODE |')
        print('|-----------------------------------------------|')
        print('| 7:30 AM -----> 9:00 AM     |  ₱3,400   |  T   |')
        print('| 10:00 AM -----> 11:30 AM   |  ₱3,600   |  W   |')
        print('| 1:30 PM -----> 3:00 PM     |  ₱3,700   |  X   |')
        print('| 4:30 PM -----> 6:00 PM     |  ₱3,900   |  Y   |')
        print('| 7:30 PM -----> 9:00 PM     |  ₱4,100   |  Z   |')
        print('=================================================')
        business_time()

def first_class():
    while(6):
        print('FIRST CLASS')
        from datetime import date
        today = date.today()
        print(f'\nAVAILABLE FLIGHTS AS OF {today}.')
        print('==================================================')
        print('|      TIME STAMPS           |   PRICE   | CODE  |')
        print('|------------------------------------------------|')
        print('| 7:30 AM -----> 9:00 AM     |  ₱4,400   |  AA   |')
        print('| 10:00 AM -----> 11:30 AM   |  ₱4,600   |  BB   |')
        print('| 1:30 PM -----> 3:00 PM     |  ₱4,700   |  CC   |')
        print('| 4:30 PM -----> 6:00 PM     |  ₱4,900   |  DD   |')
        print('| 7:30 PM -----> 9:00 PM     |  ₱5,100   |  EE   |')
        print('==================================================')
        first_time()

def premium_time():
    while(5):
        global time
        time = input('\nINPUT FLIGHT TIME (O-S): \n').upper()
        if time == (o[1]):
            time = (o[0])
            global amount
            amount = (o[2])
            premium_class_payment()
            receipt()
            confirm()
            
        if time == (p[1]):
            time = (p[0])
            amount = (p[2])
            premium_class_payment()
            receipt()
            confirm()

        if time == (q[1]):
            time = (q[0])
            amount = (q[2])
            premium_class_payment()
            receipt()
            confirm()

        if time == (r[1]):
            time = (r[0])
            amount = (r[2])
            premium_class_payment()
            receipt()
            confirm()

        if time == (s[1]):
            time = (s[0])
            amount = (s[2])
            premium_class_payment()
            receipt()
            confirm()

        else:
            print('INVALID KEYWORD')

def business_time():
    while(5):
        global time
        time = input('\nINPUT FLIGHT TIME (T-Z): \n').upper()
        if time == (t[1]):
            time = (t[0])
            global amount
            amount = (t[2])
            business_class_payment()
            receipt()
            confirm()
            
        if time == (w[1]):
            time = (w[0])
            amount = (w[2])
            business_class_payment()
            receipt()
            confirm()

        if time == (x[1]):
            time = (x[0])
            amount = (x[2])
            business_class_payment()
            receipt()
            confirm()

        if time == (y[1]):
            time = (y[0])
            amount = (y[2])
            business_class_payment()
            receipt()
            confirm()

        if time == (z[1]):
            time = (z[0])
            amount = (s[2])
            business_class_payment()
            receipt()
            confirm()

        else:
            print('INVALID KEYWORD')
    

def first_time():
    while(5):
        global time
        time = input('\nINPUT FLIGHT TIME (AA-EE): \n').upper()
        if time == (aa[1]):
            time = (aa[0])
            global amount
            amount = (aa[2])
            first_class_payment()
            receipt()
            confirm()
            
        if time == (bb[1]):
            time = (bb[0])
            amount = (bb[2])
            first_class_payment()
            receipt()
            confirm()

        if time == (cc[1]):
            time = (cc[0])
            amount = (cc[2])
            first_class_payment()
            receipt()
            confirm()

        if time == (dd[1]):
            time = (dd[0])
            amount = (dd[2])
            first_class_payment()
            receipt()
            confirm()

        if time == (ee[1]):
            time = (ee[0])
            amount = (ee[2])
            first_class_payment()
            receipt()
            confirm()

        else:
            print('INVALID KEYWORD')

def premium_class_payment():
    while(1):
        pass
        while(2):
            try:
                global quantity
                quantity = int(input('BOOK TICKETS: \n'))
                if quantity > 40:
                    print('PREMIUM CLASS CURRENTLY 40 SEAT AVALIABLE')
                    break
                else:
                    global total
                    total = float(quantity) * amount
                    print(f'\nTOTAL AMOUNT: ₱{total}')
                    while(3):
                        global money
                        money = float(input('\nMONEY RECEIVED: \n'))
                        if money < total:
                            print('INSUFFICIENT MONEY')
                        
                        else:
                            global change
                            change = money - total
                            return
            except ValueError:
                print('INVALID NUMBER!!')

def business_class_payment():
     while(1):
        pass
        while(2):
            try:
                global quantity
                quantity = int(input('BOOK TICKETS: \n'))
                if quantity > 48:
                    print('BUSINESS CLASS CURRENTLY 48 SEAT AVALIABLE')
                    break
                else:
                    global total
                    total = float(quantity) * amount
                    print(f'\nTOTAL AMOUNT: ₱{total}')
                    while(3):
                        global money
                        money = float(input('\nMONEY RECEIVED: \n'))
                        if money < total:
                            print('INSUFFICIENT MONEY')
                        
                        else:
                            global change
                            change = money - total
                            return
            except ValueError:
                print('INVALID NUMBER!!')

def first_class_payment():
    while(1):
        pass
        while(2):
            try:
                global quantity
                quantity = int(input('BOOK TICKETS: \n'))
                if quantity > 14:
                    print('FIRST CLASS CURRENTLY 14 SEAT AVALIABLE')
                    break
                else:
                    global total
                    total = float(quantity) * amount
                    print(f'\nTOTAL AMOUNT: ₱{total}')
                    while(3):
                        global money
                        money = float(input('\nMONEY RECEIVED: \n'))
                        if money < total:
                            print('INSUFFICIENT MONEY')
                        
                        else:
                            global change
                            change = money - total
                            return
            except ValueError:
                print('INVALID NUMBER!!')



while(1):
    origin = input('ROUTE ORIGIN CODE (A-F): \n').upper()
    if origin == 'A' or origin == 'B' or origin == 'C' or origin == 'D' or origin == 'E' or origin == 'F':
        while(1):
        #manila_origin
            if origin == (a[1]):
                origin = (a[0])
                origin_airport = (a[2])
                manila_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (B-F): \n').upper()
                    if destination == 'B' or destination == 'C' or destination == 'D'or destination == 'E' or destination == 'F':

                        #baguio_destination
                        if destination == (b[1]):
                            destination = (b[0])
                            destination_airport = (b[2])
                            class_passenger()

                        #cebu_destination
                        if destination == (c[1]):
                            destination = (c[0])
                            destination_airport = (c[2])
                            class_passenger()

                        #bohol_destination
                        if destination == (d[1]):
                            destination = (d[0])
                            destination_airport = (d[2])
                            class_passenger()

                        #cdo_destination
                        if destination == (e[1]):
                            destination = (e[0])
                            destination_airport = (e[2])
                            class_passenger()

                        #davao_destination
                        if destination == (f[1]):
                            destination = (f[0])
                            destination_airport = (f[2])
                            class_passenger()              

                    else:
                        manila_destination_invalid_keyword()
            #baguio origin            
            if origin == (b[1]):
                origin = (b[0])
                origin_airport = (b[2])
                baguio_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (A-F): \n').upper()
                    if destination == 'A' or destination == 'C' or destination == 'D' or destination == 'E' or destination == 'F':

                        #manila_destination
                        if destination == (a[1]):
                            destination = (a[0])
                            destination_airport = (a[2])
                            class_passenger()

                        #cebu_destination
                        if destination == (c[1]):
                            destination = (c[0])
                            destination_airport = (c[2])
                            class_passenger()

                        #bohol_destination
                        if destination == (d[1]):
                            destination = (d[0])
                            destination_airport = (d[2])
                            class_passenger()

                        #cdo_destination
                        if destination == (e[1]):
                            destination = (e[0])
                            destination_airport = (e[2])
                            class_passenger()

                        #davao_destination
                        if destination == (f[1]):
                            destination = (f[0])
                            destination_airport = (f[2])
                            class_passenger()
                    else:
                        baguio_destination_invalid_keyword()

            #cebu_origin()                       
            if origin == (c[1]):
                origin = (c[0])
                origin_airport = (c[2])
                cebu_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (A-F): \n').upper()
                    if destination == 'A' or destination == 'B' or destination == 'D' or destination == 'E' or destination == 'F':

                        #manila_destination
                        if destination == (a[1]):
                            destination = (a[0])
                            destination_airport = (a[2])
                            class_passenger()

                        #baguio_destination
                        if destination == (b[1]):
                            destination = (b[0])
                            destination_airport = (b[2])
                            class_passenger()

                        #bohol_destination
                        if destination == (d[1]):
                            destination = (d[0])
                            destination_airport = (d[2])
                            class_passenger()

                        #cdo_destination
                        if destination == (e[1]):
                            destination = (e[0])
                            destination_airport = (e[2])
                            class_passenger()
                            
                        #davao_destination
                        if destination == (f[1]):
                            destination = (f[0])
                            destination_airport = (f[2])
                            class_passenger()
                    else:
                        cebu_destination_invalid_keyword()

            #bohol_origin         
            if origin == (d[1]):
                origin = (d[0])
                origin_airport = (d[2])
                bohol_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (A-F): \n').upper()
                    if destination == 'A' or destination == 'B' or destination == 'C' or destination == 'E' or destination == 'F':

                        #manila_destination
                        if destination == (a[1]):
                            destination = (a[0])
                            destination_airport = (a[2])
                            class_passenger()

                        #baguio_destination
                        if destination == (b[1]):
                            destination = (b[0])
                            destination_airport = (b[2])
                            class_passenger()

                        #cebu_destination
                        if destination == (c[1]):
                            destination = (c[0])
                            destination_airport = (c[2])
                            class_passenger()

                        #cdo_destination
                        if destination == (e[1]):
                            destination = (e[0])
                            destination_airport = (e[2])
                            class_passenger()

                        #davao_destination
                        if destination == (f[1]):
                            destination = (f[0])
                            destination_airport = (f[2])
                            class_passenger()
                    else:
                        bohol_destination_invalid_keyword()        


            #cdo_origin
            if origin == (e[1]):
                origin = (e[0])
                origin_airport = (e[2])
                cdo_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (A-F): \n').upper()
                    if destination == 'A' or destination == 'B' or destination == 'C' or destination == 'D' or destination == 'F':

                        #manila_destination
                        if destination == (a[1]):
                            destination = (a[0])
                            destination_airport = (a[2])
                            class_passenger()

                        #baguio_destination
                        if destination == (b[1]):
                            destination = (b[0])
                            destination_airport = (b[2])
                            class_passenger()

                        #cebu_destination
                        if destination == (c[1]):
                            destination = (c[0])
                            destination_airport = (c[2])
                            class_passenger()
                            
                        #bohol_destination
                        if destination == (d[1]):
                            destination = (d[0])
                            destination_airport = (d[2])
                            class_passenger()

                        #davao_destination
                        if destination == (f[1]):
                            destination = (f[0])
                            destination_airport = (f[2])
                            class_passenger()
                    else:
                        cdo_destination_invalid_keyword()        

            #davao_origin
            if origin == (f[1]):
                origin = (f[0])
                origin_airport = (f[2])
                davao_origin()
                while(2):
                    destination = input('ROUTE DESTINATION (A-F): \n').upper()
                    if destination == 'A' or destination == 'B' or destination == 'C' or destination == 'E' or destination == 'F':

                        #manila_destination
                        if destination == (a[1]):
                            destination = (a[0])
                            destination_airport = (a[2])
                            class_passenger()

                        #baguio_destination
                        if destination == (b[1]):
                            destination = (b[0])
                            destination_airport = (b[2])
                            class_passenger()

                        #cebu_destination
                        if destination == (c[1]):
                            destination = (c[0])
                            destination_airport = (c[2])
                            class_passenger()

                        #bohol_destination
                        if destination == (d[1]):
                            destination = (d[0])
                            destination_airport = (d[2])
                            class_passenger()

                        #cdo_destination
                        if destination == (e[1]):
                            destination = (e[0])
                            destination_airport = (e[2])
                            class_passenger()
                    else:
                        davao_destination_invalid_keyword()

    else:
        available_route_invalid_keyword()