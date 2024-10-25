from utilities.is_positive_number import is_positive_number


def prompt_expense_amount() -> float | None:
    """
    Prompts the user for an expense amount.

    Raises: 
        ValueError: 
            If the provided expense amount
            fails validation according to 
            the `is_positive_number` utility function.
    """
    expense_amount = None
    
    while expense_amount == None:
        try:
            expense_amount = float(input("Please enter an expense amount: "))
            if not is_positive_number(expense_amount):
                raise ValueError(
                    "Error: Expense amount must be a positive number."
                )
        except ValueError as e: 
            expense_amount = None
            print(str(e))

    return expense_amount