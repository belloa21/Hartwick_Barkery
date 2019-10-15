#Alex Bello
#10/14/19


cookie_sales = []
candy_sales = []

def cookie_input():
    for i in range(6):
        current_cookie = input(f"Enter month {i + 1}'s cookie data. \n")
        if int(current_cookie):
            current_cookie = int(current_cookie)
        else:
            current_cookie = 0
        cookie_sales.append(current_cookie)


def candy_input():
    for i in range(6):
        current_candy = input(f"Enter month {i + 1}'s candy data. \n")
        if int(current_candy):
            current_candy = int(current_candy)
        else:
            current_candy = 1
        candy_sales.append(current_candy)


def cookie_avg():
    print(sum(cookie_sales) / len(cookie_sales))


def candy_avg():
    print(sum(candy_sales) / len(candy_sales))


def cookie_max():
    print(max(cookie_sales))


def candy_max():
    print(max(candy_sales))


def cookie_min():
    print(min(cookie_sales))


def candy_min():
    print(min(candy_sales))


def most_popular():
    if sum(candy_sales) > sum(cookie_sales):
        return('Candy')
    elif sum(candy_sales) < sum(cookie_sales):
        return('Cookies')
    else:
        return('Equal')

cookie_input()
print()
candy_input()
print()
print('Averages')
cookie_avg()
candy_avg()
print()
print('Maximums')
cookie_max()
candy_max()
print()
print('Minimums')
cookie_min()
candy_min()
print()
print(f'The most popular is {most_popular()}')



