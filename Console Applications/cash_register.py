#cash register object

class CashRegister(object):


    
    def __init__(self, total, lastTransactionAmount, name, cost):
        self.total = total
        self.lastTransactionAmount = lastTransactionAmount
        self.name = name
        self.cost = cost

    def add(self, itemCost):
        self.total += itemCost
        self.lastTransactionAmount = itemCost
    
    def scan(self, item, itemCost, quantity):
        self.add(itemCost * quantity)
            
    def voidLastTransaction(self):
        self.total -= self.lastTransactionAmount
        self.lastTransactionAmount = 0
    

#Main event loop (RUNTIME)

while True:
    #item number 
    itemNumber = int(raw_input("How many items do you want? "))

    try: 
        #1 unique item

        if itemNumber == 1:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                
            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #2 unique items

        elif itemNumber == 2:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                
            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #3 unique items
                
        elif itemNumber == 3:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #4 unique items            

        elif itemNumber == 4:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                 print "You entered the wrong data type for the item\'s description, please try again. "
                 continue


        #5 unique items

        elif itemNumber == 5:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
            except:
                 print "You entered the wrong data type for the item\'s description, please try again. "
                 continue

        #6 unique items

        elif itemNumber == 6:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)


            except:
                 print "You entered the wrong data type for the item\'s description, please try again. "
                 continue


        #7 unique items

        elif itemNumber == 7:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #8 unique items

        elif itemNumber == 8:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #9 unique items

        elif itemNumber == 9:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #10 unique items

        elif itemNumber == 10:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #11 unique items

        elif itemNumber == 11:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 11
                userItemName11 = raw_input("Enter item name ")
                userItemCost11 = input("Enter cost ")
                userItemQuantity11 = input("Enter quantity ")
                userItem11 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #12 unique items

        elif itemNumber == 12:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 11
                userItemName11 = raw_input("Enter item name ")
                userItemCost11 = input("Enter cost ")
                userItemQuantity11 = input("Enter quantity ")
                userItem11 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 12
                userItemName12 = raw_input("Enter item name ")
                userItemCost12 = input("Enter cost ")
                userItemQuantity12 = input("Enter quantity ")
                userItem12 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                 print "You entered the wrong data type for the item\'s description, please try again. "
                 continue

        #13 unique items

        elif itemNumber == 13:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 11
                userItemName11 = raw_input("Enter item name ")
                userItemCost11 = input("Enter cost ")
                userItemQuantity11 = input("Enter quantity ")
                userItem11 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 12
                userItemName12 = raw_input("Enter item name ")
                userItemCost12 = input("Enter cost ")
                userItemQuantity12 = input("Enter quantity ")
                userItem12 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 13
                userItemName13 = raw_input("Enter item name ")
                userItemCost13 = input("Enter cost ")
                userItemQuantity13 = input("Enter quantity ")
                userItem13 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #14 unique items

        elif itemNumber == 14:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 11
                userItemName11 = raw_input("Enter item name ")
                userItemCost11 = input("Enter cost ")
                userItemQuantity11 = input("Enter quantity ")
                userItem11 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 12
                userItemName12 = raw_input("Enter item name ")
                userItemCost12 = input("Enter cost ")
                userItemQuantity12 = input("Enter quantity ")
                userItem12 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 13
                userItemName13 = raw_input("Enter item name ")
                userItemCost13 = input("Enter cost ")
                userItemQuantity13 = input("Enter quantity ")
                userItem13 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 14
                userItemName14 = raw_input("Enter item name ")
                userItemCost14 = input("Enter cost ")
                userItemQuantity14 = input("Enter quantity ")
                userItem14 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue

        #15 unique items

        elif itemNumber == 15:
            try:
                #user item 1
                userItemName = raw_input("Enter item name ")
                userItemCost = input("Enter cost ")
                userItemQuantity = input("Enter quantity ")
                userItem = CashRegister(0, 0, userItemName, userItemCost)
                #user item 2
                userItemName2 = raw_input("Enter item name ")
                userItemCost2 = input("Enter cost ")
                userItemQuantity2 = input("Enter quantity ")
                userItem2 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 3
                userItemName3 = raw_input("Enter item name ")
                userItemCost3 = input("Enter cost ")
                userItemQuantity3 = input("Enter quantity ")
                userItem3 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 4
                userItemName4 = raw_input("Enter item name ")
                userItemCost4 = input("Enter cost ")
                userItemQuantity4 = input("Enter quantity ")
                userItem4 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 5
                userItemName5 = raw_input("Enter item name ")
                userItemCost5 = input("Enter cost ")
                userItemQuantity5 = input("Enter quantity ")
                userItem5 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 6
                userItemName6 = raw_input("Enter item name ")
                userItemCost6 = input("Enter cost ")
                userItemQuantity6 = input("Enter quantity ")
                userItem6 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 7
                userItemName7 = raw_input("Enter item name ")
                userItemCost7 = input("Enter cost ")
                userItemQuantity7 = input("Enter quantity ")
                userItem7 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 8
                userItemName8 = raw_input("Enter item name ")
                userItemCost8 = input("Enter cost ")
                userItemQuantity8 = input("Enter quantity ")
                userItem8 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 9 
                userItemName9 = raw_input("Enter item name ")
                userItemCost9 = input("Enter cost ")
                userItemQuantity9 = input("Enter quantity ")
                userItem9 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 10
                userItemName10 = raw_input("Enter item name ")
                userItemCost10 = input("Enter cost ")
                userItemQuantity10 = input("Enter quantity ")
                userItem10 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 11
                userItemName11 = raw_input("Enter item name ")
                userItemCost11 = input("Enter cost ")
                userItemQuantity11 = input("Enter quantity ")
                userItem11 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 12
                userItemName12 = raw_input("Enter item name ")
                userItemCost12 = input("Enter cost ")
                userItemQuantity12 = input("Enter quantity ")
                userItem12 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 13
                userItemName13 = raw_input("Enter item name ")
                userItemCost13 = input("Enter cost ")
                userItemQuantity13 = input("Enter quantity ")
                userItem13 = CashRegister(0, 0, userItemName, userItemCost)

                #user item 14
                userItemName14 = raw_input("Enter item name ")
                userItemCost14 = input("Enter cost ")
                userItemQuantity14 = input("Enter quantity ")
                userItem14 = CashRegister(0, 0, userItemName, userItemCost)
                #user item 15
                userItemName15 = raw_input("Enter item name ")
                userItemCost15 = input("Enter cost ")
                userItemQuantity15 = input("Enter quantity ")
                userItem15 = CashRegister(0, 0, userItemName, userItemCost)

            except:
                print "You entered the wrong data type for the item\'s description, please try again. "
                continue


            
        else:
            print "You can only have fifteen unique items. "

    except:
        print "You can only enter an integer. "





    #Scanning conditional
    #(make a total of all the available items 1 - itemNumber

    scan = raw_input("Do you want to scan? (yes/no)")
    if scan == "yes":
        #1 item
        if itemNumber == 1:
            userItem.scan(userItemName, userItemCost, userItemQuantity)
            print userItem.total
        #2 items
        elif itemNumber == 2:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            print userItem.total + userItem2.total
        #3 items 
        elif itemNumber == 3:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            print userItem.total + userItem2.total + userItem3.total
        #4 items
        elif itemNumber == 4:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total
        #5 items
        elif itemNumber == 5:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total
        #6 items
        elif itemNumber == 6:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total

        #7 items
        elif itemNumber == 7:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total
        #8 items
        elif itemNumber == 8:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total


        #9 items
        elif itemNumber == 9:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total

        #10 items
        elif itemNumber == 10:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total

        #11 items
        elif itemNumber == 11:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            userItem11.scan(userItemName11, userItemCost11, userItemQuantity11)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total + userItem11

        #12 items
        elif itemNumber == 12:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            userItem11.scan(userItemName11, userItemCost11, userItemQuantity11)

            userItem12.scan(userItemName12, userItemCost12, userItemQuantity12)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total + userItem11 + userItem12


        #13 items
        elif itemNumber == 13:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            userItem11.scan(userItemName11, userItemCost11, userItemQuantity11)

            userItem12.scan(userItemName12, userItemCost12, userItemQuantity12)

            userItem13.scan(userItemName13, userItemCost13, userItemQuantity13)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total + userItem11 + userItem12 + userItem13


        #14 items
        elif itemNumber == 14:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            userItem11.scan(userItemName11, userItemCost11, userItemQuantity11)

            userItem12.scan(userItemName12, userItemCost12, userItemQuantity12)

            userItem13.scan(userItemName13, userItemCost13, userItemQuantity13)

            userItem14.scan(userItemName14, userItemCost14, userItemQuantity14)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total + userItem11 + userItem12 + userItem13 + userItem14


        #15 items
        elif itemNumber == 15:
            userItem.scan(userItemName, userItemCost, userItemQuantity)

            userItem2.scan(userItemName2, userItemCost2, userItemQuantity2)

            userItem3.scan(userItemName3, userItemCost3, userItemQuantity3)

            userItem4.scan(userItemName4, userItemCost4, userItemQuantity4)

            userItem5.scan(userItemName5, userItemCost5, userItemQuantity5)

            userItem6.scan(userItemName6, userItemCost6, userItemQuantity6)

            userItem7.scan(userItemName7, userItemCost7, userItemQuantity7)

            userItem8.scan(userItemName8, userItemCost8, userItemQuantity8)

            userItem9.scan(userItemName9, userItemCost9, userItemQuantity9)

            userItem10.scan(userItemName10, userItemCost10, userItemQuantity10)

            userItem11.scan(userItemName11, userItemCost11, userItemQuantity11)

            userItem12.scan(userItemName12, userItemCost12, userItemQuantity12)

            userItem13.scan(userItemName13, userItemCost13, userItemQuantity13)

            userItem14.scan(userItemName14, userItemCost14, userItemQuantity14)

            userItem15.scan(userItemName15, userItemCost15, userItemQuantity15)

            print userItem.total + userItem2.total + userItem3.total + userItem4.total + userItem5.total + userItem6.total + userItem7.total + userItem8.total + userItem9.total + userItem10.total + userItem11 + userItem12 + userItem13 + userItem14 + userItem15



        #empty else conditional to avoid confusion
        else:
            pass


			
    #exits if user does not want to scan
    else:
        break