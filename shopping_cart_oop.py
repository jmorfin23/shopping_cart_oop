
class Cart():
    sList = []

    def __init__(self, *item):
        self.item = item

    # create a method to show cart

    def showCart(self, blist):
        self.blist = blist                                       #dont think i have to do this
        print(" ")
        print(  "\tYour Shopping Cart"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in self.blist:
                print(f'{i}')


    def addToCart(self, rlist):
        rlist = rlist
        while True:
            add = input('Enter what you would like to add: ')
            rlist.append(add)
            q = input('Would you like to add another item?(y or n) ')
            if q.lower() == 'y':
                True
            elif q.lower() =='n':
                bag.showCart(rlist)
                bag.startMenu(rlist)
                break

    def deleteFCart(self, elist):
        elist = elist
        bag.showCart(elist)
        delet = input('Enter what you would like to delete: ')
        for i in range(len(elist)):
            if delet.lower() == elist[i].lower():
                print(' ')
                print('..that item is now removed from your shopping cart')
                print(' ')
                elist.remove(elist[i])
                bag.startMenu(elist)
                return
            else:
                continue



    def transferCart(self,blist):
        if blist:
            return blist
        else:
            pass
    def checkOut(self,flist):
        flist = flist
        print(" ")
        print(  "\tYour Shopping Cart"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in flist:
                print(f'{i}')
        questi = input('How would you like to pay? (Enter: cash or card) ')
        if questi.lower() == 'cash':
            print(' ')
            print('*cha-ching*')
            print(' ')
            print('Here is your change.')
            print(' ')
            print('Thank you for shopping with us. Enjoy the rest of your day!')
        if questi.lower() == 'card':
            print(' ')
            print('Please slide your card..')
            print('*...*')
            print('oops, try the other way...')
            print('*.....*')
            print('alright, you are all set')
            questio = input('Would you like a receipt? (Enter: y or n) ')
            if questio == 'y':
                print('Okay, here is your receipt. Have a good day. ')
                pass
            if questio == 'n':
                print('Ok')
                print('* throws reipt in the trash *')
                print('Have a good day.')
                pass

    # I want a menu to control the whole program
    def startMenu(self, blist):
        blist = blist
        dlist = []
        print(  "\tShopping Cart Menu"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        print("1. Add items to your shopping cart")
        print("2. Delete items from your shopping cart")
        print("3. View your current shopping cart")
        print("4. Check-out")
        print("5. Menu")
        question = int(input('What would you like to do? '))
        if question == 1:
            if blist:
                bag.addToCart(blist)
            else:
                bag.addToCart(dlist)
        if question == 2:
            if blist:
                bag.deleteFCart(blist)
            else:
                print('Your shopping cart is empty.')
        if question == 3:
            if blist:
                bag.showCart(blist)
            else:
                print('Your shopping cart is empty.')
        if question == 4:
            if blist:
                bag.checkOut(blist)
            else:
                print('Your shopping cart is empty.')
        if question == 5:
            print('This is the start menu silly.')

#Initiates the program:

tlist = []
qu = input('Would you like to shop at Jonathan\'s Grocery Market?(Y or N)')
if qu.lower() == 'y':
    bag = Cart()         #instance of Cart
    bag.startMenu(tlist)
else:
    pass
