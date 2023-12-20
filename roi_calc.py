class Roi_calc:
    def __init__(self, income={},expenses={},invested={}):
        self.income = income
        self.expenses = expenses
        self.invested = invested

    def __calculate_total(self, category):
        #Calculate the total value for a given category (income, expenses, or invested).
        total = 0
        for item in category.values():
            total += int(item)
        return total

    def __cash_flow(self, inmoney, outmoney):
        #after income-outcome
        return self.__calculate_total(inmoney) - self.__calculate_total(outmoney)

    def __cash_on_cash_ROI(self, income, expenses, invested):
        #cash on cash!
        anual_cash_flow  = self.__cash_flow(income, expenses) * 12
        total_invested = self.__calculate_total(invested)
        percent  = str(anual_cash_flow/total_invested*100) + '%'
        return percent

    def user_input(self):
        self.income = {}
        self.expenses = {}
        #takes input for income
        user = input("first we are going to grab a list of your income\n if you know and just want to put in your total income please type total\n otherwise type your income source or q to finish\n")
        while user.lower() != 'q' and user != 'total':
            self.income[user] = input("how much income is genorated a month?\n")
            user = input("income source or q to finish\n")
        if user == 'total':
            self.income = {}
            self.income['total'] = input("how much total income is genorated a month?\n")
            #takes input for expenses
        user = input("next we are going to grab a list of your expenses\n if you know and just want to put in your total expenses please type total\n otherwise type the name of your expences or q to finish\n")
        while user.lower() != 'q' and user != 'total':
            self.expenses[user] = input("how much are you spending a month?\n")
            user = input("expence source or q to finish\n")
        if user == 'total':
            self.expenses = {}
            self.expenses['total'] = input("how much total expenses are you spending a month?\n")
        #takes input for investments
        user = input("next we are going to grab a list of your invested money\n if you know and just want to put in your total invested please type total\n otherwise type the what you invested into or q to finish\n")
        while user.lower() != 'q' and user != 'total':
            self.invested[user] = input("how much did you invest?\n")
            user = input("investment source or q to finish\n")
        if user == 'total':
            self.invested = {}
            self.invested['total'] = input("how much total did you invest?\n")
        #does math in background and returns cash on cash value 
        return self.__cash_on_cash_ROI(self.income, self.expenses, self.invested)
        
#def a lot bad w this code, much more to optimize, but it works 
joe = Roi_calc()
print(joe.user_input())