# A class which represents a single entry of the moneymanager xls export file
# it contains the following fields:
# - Date
# - Account
# - Category
# - Subcategory
# - Note
# - EUR
# - transfer type (income or expense or transfer)
# - Description
# - Amount
# - Currency
# - Konto

class MoneyManagerEntry:
    def __init__(self, date, account, category, subcategory, note, eur, transfer_type, description, amount, currency, konto):
        self.date = date
        self.account = account
        self.category = category
        self.subcategory = subcategory
        self.note = note
        self.eur = eur
        self.transfer_type = transfer_type
        self.description = description
        self.amount = amount
        self.currency = currency
        self.konto = konto

    def __str__(self):
        return "Date: " + str(self.date) + ", Account: " + str(self.account) + ", Category: " + str(
            self.category) + ", Subcategory: " + str(self.subcategory) + ", Note: " + str(self.note) + ", EUR: " + str(
            self.eur) + ", Type: " + str(self.transfer_type) + ", Description: " + str(self.description) + ", Amount: " + str(
            self.amount) + ", Currency: " + str(self.currency) + ", Konto: " + str(self.konto)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.date == other.date and
                self.account == other.account and
                self.category == other.category and
                self.subcategory == other.subcategory and
                self.note == other.note and
                self.eur == other.eur and
                self.transfer_type == other.transfer_type and
                self.description == other.description and
                self.amount == other.amount and
                self.currency == other.currency and
                self.konto == other.konto)

    def __hash__(self):
        return hash(self.date + self.account + self.category + self.subcategory + self.note + self.eur + self.transfer_type + self.description + self.amount + self.currency + self.konto)


