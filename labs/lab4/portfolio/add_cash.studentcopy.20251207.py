
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
    try:
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.cash += amount
        print(f'${amount:.2f} to portfolio. New cash balance: ${self.cash:.2f}')
    except ValueError:
        print(f"Error: Must be a positive value")
    