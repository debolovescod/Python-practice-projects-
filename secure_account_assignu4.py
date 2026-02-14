class Account:
    def __init__(self,pin):
        self.__pin = pin
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            return True
        else: 
            return False
        
account = Account("1234")
print(account.check_pin("1234"))
print(account.check_pin("9999"))
    