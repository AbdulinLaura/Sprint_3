class OnlineSalesRegisterCollector:

    def __init__(self):
        self.name = None
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        self.name = name
        if len(self.name) == 0 or len(self.name) > 40:
            raise ValueError("Нельзя добавить товар, если в его названии нет символов или их больше 40")
        if self.name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        else:
            self.__name_items.append(self.name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        self.name = name
        if self.name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            price = self.__item_price.get(item, 0)
            total.append(price)
        if self.__number_items > 10:
            total_price = sum(total) * (1 - 10 / 100)
            print(total_price)
        else:
            total_price = sum(total)
            return total_price

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
        for item in twenty_percent_tax:
            total.append(self.__item_price.get(item, 0) * 0.2)
        if self.__number_items > 10:
            return sum(total) * (1 - 10 / 100)
        else:
            return sum(total)

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
        for item in ten_percent_tax:
            total.append(self.__item_price.get(item, 0) * 0.1)
        if self.__number_items > 10:
            return sum(total) * (1 - 10 / 100)
        else:
            return sum(total)

    def total_tax(self):
        total_tax = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_tax

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{telephone_number}'


check = OnlineSalesRegisterCollector()

check.add_item_to_cheque('чипсы')
check.add_item_to_cheque('кола')
check.add_item_to_cheque('молоко')

print("Товары в чеке:", check.name_items)
print("Общая сумма:", check.check_amount())
print("НДС 20%:", check.twenty_percent_tax_calculation())
print("НДС 10%:", check.ten_percent_tax_calculation())
print("Итого НДС:", check.total_tax())

check.delete_item_from_check('молоко')
print("После удаления:", check.name_items)

print(check.get_telephone_number(9876543210))
