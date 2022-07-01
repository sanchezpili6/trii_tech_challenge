import requests

possible_stocks = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'FB', 'TWTR', 'UBER', 'LYFT', 'SNAP', 'SHOP']


def get_stock_price(name):
    api_url = 'https://financialmodelingprep.com/api/v3/quote-short/{}?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22'.format(
        name)
    response = requests.get(api_url)
    data = response.json()
    return data[0].get('price')


def get_stock_price_list(names):
    prices = []
    for name in names:
        prices.append(get_stock_price(name))
    return prices


def get_total_stock_price(names):
    prices = get_stock_price_list(names)
    total = 0
    for price in prices:
        total += price
    return total


def get_cheapest_stock_price():
    return min(get_stock_price_list(possible_stocks))


def get_possible_buy_stocks_for_money(money):
    current_portfolio_values = {}
    while money > get_cheapest_stock_price():
        for stock in possible_stocks:
            if get_stock_price(stock) <= money:
                money -= get_stock_price(stock)
                current_portfolio_values[stock] = current_portfolio_values.get(stock, 0) + get_stock_price(stock)
    return current_portfolio_values, money


def menu():
    print('1. Get stock price')
    print('2. Get total stocks price')
    print('3. Get cheapest stock price')
    print('4. Get possible buy stocks for your money')
    print('5. Exit')

    option = input('Enter your choice: ')

    if option == '1':
        name = input('Enter stock name: ')
        print(get_stock_price(name))
        menu()
    elif option == '2':
        names = input('Enter stock names: ')
        print(get_total_stock_price(names.split(' ')))
        menu()
    elif option == '3':
        print(get_cheapest_stock_price())
        menu()
    elif option == '4':
        money = int(input('Enter money: '))
        if money < get_cheapest_stock_price():
            print('You can not buy all stocks for this money')
            print('Would you like to see the ones you can buy anyway?')
            if input('(y/n): ') == 'y':
                print(get_possible_buy_stocks_for_money(money))
                menu()
            menu()
    elif option == '5':
        exit()
    else:
        print('Invalid option')
        menu()


menu()

