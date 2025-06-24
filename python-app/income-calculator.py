from typing import Dict


class Budget:
    """Handles income, expenses, and financial calculations."""

    def __init__(self):
        """
        Initialize a new Budget instance with empty income and expenses dictionaries.
        """
        self.income: Dict[str, float] = {}
        self.expenses: Dict[str, float] = {}

    def add_income(self, category: str, amount: float):
        """
        Add an income source to the budget.

        Args:
            category (str): The type of income (e.g. "salary", "tips", etc.).
            amount (float): The amount of income in the given category.
        """
        self.income[category] = amount

    def add_expense(self, category: str, amount: float):
        """
        Add an expense to the budget.

        Args:
            category (str): The type of expense (e.g. "rent", "groceries", etc.).
            amount (float): The amount of the expense in the given category.
        """
        self.expenses[category] = amount

    def total_income(self) -> float:
        """
        Calculate the total income from all sources.

        Returns:
            float: The total income.
        """
        return sum(self.income.values())

    def total_expenses(self) -> float:
        """
        Calculate the total expenses from all categories.

        Returns:
            float: The total expenses.
        """
        return sum(self.expenses.values())

    def net_income(self) -> float:
        """
        Calculate the net income after subtracting total expenses from total income.

        Returns:
            float: The net income.
        """
        return self.total_income() - self.total_expenses()

    def report(self):
        """
        Print a detailed budget report including income, expenses, and net income.
        
        The report displays a breakdown of income and expenses by category, as well 
        as the total income, total expenses, and net income.
        """
        print("\n=== 📋 Budget Report ===")
        print("\n--- Income ---")
        for category, amount in self.income.items():
            print(f"{category}: ${amount:.2f}")
        print(f"Total Income: ${self.total_income():.2f}")

        print("\n--- Expenses ---")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")
        print(f"Total Expenses: ${self.total_expenses():.2f}")

        print("\n--- Summary ---")
        print(f"Net Income: ${self.net_income():.2f}")


class BudgetApp:
    """Manages user interaction for the budget calculator."""

    def __init__(self):
        """
        Initializes a BudgetApp instance with a Budget object.
        """
        self.budget = Budget()

    @staticmethod
    def get_float_input(prompt: str) -> float:
        """
        Prompt the user to input a floating-point number.

        Continuously prompts the user until a valid floating-point number is entered.
        
        Args:
            prompt (str): The message displayed to the user to request input.

        Returns:
            float: The valid floating-point number entered by the user.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

    def collect_income(self):
        """
        Prompts the user to input their monthly income in different categories
        such as salary, bonus, and other.

        The user is prompted to enter the amount for each category, and the
        entered amounts are stored in the budget object as income.

        Args:
            None

        Returns:
            None
        """
        print("\n=== 💼 Enter Monthly Income ===")
        categories = ["Salary", "Bonus", "Other"]
        for category in categories:
            amount = self.get_float_input(f"  {category}: $")
            self.budget.add_income(category, amount)

    def collect_expenses(self):
        """
        Prompts the user to input their monthly expenses in different categories
        such as rent/mortgage, utilities, groceries, transportation, and other.

        The user is prompted to enter the amount for each category, and the
        entered amounts are stored in the budget object as expenses.

        Args:
            None

        Returns:
            None
        """
        print("\n=== 🧾 Enter Monthly Expenses ===")
        categories = ["Rent/Mortgage", "Utilities", "Groceries", "Transportation", "Other"]
        for category in categories:
            amount = self.get_float_input(f"  {category}: $")
            self.budget.add_expense(category, amount)

    def run(self):
        """
        Runs the income calculator program.

        The program welcomes the user and asks the user to input their monthly
        income. The user is also asked if they want to input their expenses, and if
        they choose to do so, they are prompted to enter the amounts for each
        category of expenses. After the income and expenses are input, the program
        displays a detailed report including the income, expenses, and net income.

        Args:
            None

        Returns:
            None
        """
        print("=== 🧮 Welcome to the Income Calculator ===")
        self.collect_income()

        choice = input("\nDo you want to enter expenses? (yes/no): ").strip().lower()
        if choice in ("yes", "y"):
            self.collect_expenses()

        self.budget.report()

# Run the program
if __name__ == "__main__":
    app = BudgetApp()
    app.run()
