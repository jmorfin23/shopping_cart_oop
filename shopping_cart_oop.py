# have a class called cart that retains items and has methods to add, remove, and show

# step #1: create the cart class
    # when instantiated, cart object should define empty list for items
class Cart():
    sList = []

    def __init__(self, *item):
        self.item = item

    # create a method to show cart

    def showCart(self, blist):
        self.blist = blist
        print(" ")
        print(  "\tYour Shopping Cart"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        for i in self.blist:
            print(f'{i}')

    # create a method to add to cart

    def addToCart(self):
        list = []
        while True:
            add = input('Enter what you would like to add: ')
            list.append(add)
            q = input('Would you like to add another item?(y or n) ')
            if q.lower() == 'y':
                True
            elif q.lower() =='n':
                bag.transferCart(list)
                bag.showCart(list)
                break

    # create a method to remove from cart

    def deleteFCart(self):
        delet = input('Enter what you would like to delete: ')

# create instance of cart object with empty list

    def transferCart(self,blist):
        if blist:
            return blist
        else:
            pass
# start the while loop until user quits

    # ask for input


    # base case

    # ask if they would like to add, remove, show, perform steps using cart methods
    # I want a menu to control the whole program
    def startMenu(self):
        print(  "\tShopping Cart Menu"  )
        print("–––––––––––––––––––––––––––––––––")
        print(" ")
        print("1. Add items to your shopping cart")
        print("2. Delete items from your shopping cart")
        print("3. View your current shopping cart")
        print("4. Exit")
        print("5. Menu")

        question = int(input('What would you like to do? '))
        if question == 1:
            bag.addToCart()
        if question == 2:
            bag.deleteFCart()
        if question == 3:
            bag.showCart()
        if question == 4:
            pass
        if question == 5:
            pass

#initiates the program
qu = input('Would you like to shop?(Y or N)')
if qu.lower() == 'y':
    bag = Cart()         #instance of Cart
    bag.startMenu()
else:
    pass
