class Budget(object):
    total_budget = 0
    amount_left = 0

    def __init__(self, item_name, cost):
        self.name = item_name
        self.cost = cost

    @classmethod
    def set_budget(cls, new_amount):
        cls.total_budget = new_amount
        cls.amount_left = new_amount

    @classmethod
    def reduce_budget(cls, item):
        if cls.amount_left == cls.total_budget:
            cls.amount_left = cls.total_budget - item
        else:
            cls.amount_left = cls.amount_left - item

    @classmethod
    def percentage(cls, item):
        percentage = (item.cost/cls.total_budget) * 100
        return percentage

    @classmethod
    def get_amount(cls):
        return cls.amount_left

    def getName(self):
        return self.name


def main():
    print('To exit from this program type exit()')

    notExit = True
    while notExit:
        budget_amount = input('What is your starting budget (or exit to close)? ')

        if budget_amount.isdigit():
            items = []
            Budget.set_budget(int(budget_amount))
            print('Enter the items you wanna buy and how much they cost (type end() to stop entering)')

            notStop = True
            while notStop:
                item = input('Item name: ')
                if item == 'end()':
                    notStop = False
                else:
                    cost = int(input('Item cost: '))
                    print('\n')
                    if Budget.get_amount()-cost < 0:
                        print('Sorry adding this item will cause you to exceed your budget')
                        more = input('Do you have more cheaper items to add')
                        if more == 'no':
                            notStop = False
                        else:
                            cost = 0
                    else:
                        Budget.reduce_budget(cost)
                        theitem = Budget(item, cost)
                        items.append(theitem)

            print('Each item in your budget and the amount of the budget it takes: ')
            for item in items:
                print(item.getName(), Budget.percentage(item), '%')
            print('Amount left in budget', Budget.get_amount())

        elif budget_amount == 'exit()':
            notExit = False

        else:
            print('Enter a proper input please.')


if __name__ == '__main__':
    main()