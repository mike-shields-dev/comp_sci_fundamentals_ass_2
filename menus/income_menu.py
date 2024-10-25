from finances import finances

def income_menu():
    while finances.get_income() == 0.0:
        try:
            PROMPT = "Please enter your income: "
            finances.set_income(float(input(PROMPT)))
        
        except ValueError as e:
            print(str(e))        
        
    if finances.get_income() == 0.0:
        return income_menu