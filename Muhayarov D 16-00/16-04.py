items = []
cost = []
count = 1


def add_item(item_name, item_cost):
    items.append(item_name)
    cost.append(int(item_cost))


def print_receipt():
    if len(items) > 0:
        global count
        print("Чек ", count, ". Всего предметов: ", len(items), sep="")
        a = 0
        for i in range(len(items)):
            print(items[i], "-", cost[a])
            a += 1
        print("Итого:", sum(cost))
        print("-----")
        items.clear()
        cost.clear()
        count += 1


def main():
    add_item('Блокнот', 100)
    print_receipt()
    add_item('Ручка', 70)
    print_receipt()
    print_receipt()
    add_item('Булочка', 15)
    add_item('Булочка', 15)
    add_item('Чай', 5)
    print_receipt()
    add_item('Булочка', 15)
    add_item('Булочка', 15)
    # (Отменить чек) - этот чек не печатаем

main()