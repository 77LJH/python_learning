class Record:
    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f'date:{self.date}, order_id: {self.order_id}, money:{self.money}, province:{self.province}'
