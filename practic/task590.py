# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определнном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.
def information_about_all(market):
    for i in market:
        print(*i.values(), sep='\t', end='\n')

def information_id(market):
    id = int(input())
    for i in market:
        if i["id"] == id:
            print(*i.values(), sep='\t', end='\t')
            break

def count_of_items(market, department):
    count = 0
    for i in market:
        if i["department"] == department:
            count += 1
    print(department, count, sep="\t", end="\n")

def update_information(market,  dict1):
    id = int(input())
    for i in market:
        if i["id"] == id:
            i.update(dict1)
            break

def removal_information(market):
    id = int(input())
    for i in market:
        if i["id"] == id:
            market.remove(i)
            break


market = [
    {"id": 1, "product": "coca-cola 0.5", "department": "drinks", "price": "55 rub", "expiration date": "02.2021"},
    {"id": 2, "product": "coca-cola 1.0", "department": "drinks", "price": "97 rub", "expiration date": "02.2021"},
    {"id": 3, "product": "coca-cola 1.5", "department": "drinks", "price": "110 rub", "expiration date": "02.2021"},
    {"id": 4, "product": "coca-cola 2.0", "department": "drinks", "price": "125 rub", "expiration date": "02.2021"},
    {"id": 5, "product": "coca-cola 0.33", "department": "drinks", "price": "50 rub", "expiration date": "02.2021"},
    {"id": 6, "product": "coca-cola zero 0.5", "department": "drinks", "price": "55 rub", "expiration date": "02.2021"},
    {"id": 7, "product": "coca-cola zero 1.0", "department": "drinks", "price": "97 rub", "expiration date": "02.2021"},
    {"id": 8, "product": "coca-cola zero 1.5", "department": "drinks", "price": "110 rub",
     "expiration date": "02.2021"},
    {"id": 9, "product": "coca-cola zero 2.0", "department": "drinks", "price": "125 rub",
     "expiration date": "02.2021"},
    {"id": 10, "product": "coca-cola zero 0.33", "department": "drinks", "price": "50 rub",
     "expiration date": "02.2021"}]

information_about_all(market)
