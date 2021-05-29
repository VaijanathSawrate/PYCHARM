## Rule 72 of Finance
## 1000 INR--> Stocks / Mutual funds / FDs
## 10% 8% 5%

class Investments:
    def __init__(self, amount, roi, type):
        self.amount = amount
        self.roi = roi
        self.type = type

    def YearsToDouble(self):
        try:
            return 72 / self.roi
        except ZeroDivisionError:
            return "Enter valid roi"
        except ValueError:
            return "Enter valid roi"



i1 = Investments(1000, 8, 'stock')
print("Years To Double   :", i1.YearsToDouble())

i2 = Investments(1000, 0, 'stocks')
print("Years To Double   :", i2.YearsToDouble())

