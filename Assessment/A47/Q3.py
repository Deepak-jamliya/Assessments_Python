class Bank:
    def getInterestRate(self):
        return 0


class SBI(Bank):
    def getInterestRate(self):
        return 5


class ICICI(Bank):
    def getInterestRate(self):
        return 6


class Axis(Bank):
    def getInterestRate(self):
        return 7



banks = [SBI(), ICICI(), Axis(), Bank()]

for bank in banks:
    print(bank.__class__.__name__, "Interest Rate:", bank.getInterestRate(), "%")