from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from Users import Customer, Chef, Server, Manager
from order import Order


def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki', 600, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur Vorta', 500, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Dal Pizza', 450, 'large', ['dal', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beaf Burger', 1200, 'beaf', ['beaf', 'chili', 'onion'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffe = Drinks('Mocha', 300, False)
    menu.add_menu_item('drinks', coffe)

    # show menu
    menu.show_menu()

    resturant = Restaurant("Sai Baba Restaurant", 2000, menu)

    # add employees
    manager = Manager('Nowshad Manager', 123, 'nows165@gmail.com',
                      'khowaznagar', 1500, 'Jan 1 2020', 'core')
    resturant.add_employee('manager', manager)

    chef = Chef('Rustom Baburchi', 456, 'rustom@gmail.com',
                'jahangirnagar', 3500, 'Feb 1 2020', 'chef', 'everything')
    resturant.add_employee('chef', chef)

    server = Server('Chuto Server', 789, 'nai@gmail.com',
                    'resturant', 200, 'March 1 2020', 'server')
    resturant.add_employee('server', server)

    # show employees
    resturant.show_employees()

    # customer
    customer_1 = Customer('Sakib Khan', 6, 'king@khan', 'banani', 100000)

    # customer_1 placing an order
    order_1 = Order(customer_1, [pizza_3, coffe])
    customer_1.pay_for_order(order_1)
    resturant.add_order(order_1)

    # customer_1 paying for order_1
    resturant.receive_payment(order_1, 2000, customer_1)

    print('revenue and balance after first customer : ',
          resturant.revenue, resturant.balance)

    # customer
    customer_2 = Customer('Muntasir', 60, 'mun@khan', 'ctg', 100000)
    # customer_2 placing an order
    order_2 = Order(customer_1, [pizza_3, coffe, burger_2])
    customer_2.pay_for_order(order_2)
    resturant.add_order(order_2)

    # customer_1 paying for order_1
    resturant.receive_payment(order_2, 2000, customer_2)

    print('revenue and balance after second customer : ',
          resturant.revenue, resturant.balance)

    # pay rent
    resturant.pay_expense(resturant.rent, 'Rent')
    print('after rent', resturant.revenue,
          resturant.balance, resturant.expense)

    resturant.pay_salary(server)
    print('after paying salary', resturant.revenue,
          resturant.balance, resturant.expense)


# call the main
if __name__ == '__main__':
    main()
