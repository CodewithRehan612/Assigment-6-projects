class Bank:
    bank_name = "Default Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Example usage:
if __name__ == "__main__":
    b1 = Bank()
    b2 = Bank()
    print(b1.bank_name)  # Output: Default Bank
    print(b2.bank_name)  # Output: Default Bank
    Bank.change_bank_name("New Bank Name")
    print(b1.bank_name)  # Output: New Bank Name
    print(b2.bank_name)  # Output: New Bank Name 