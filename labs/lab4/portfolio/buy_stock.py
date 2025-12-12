

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    
    
<<<<<<< HEAD
=======
    closing_price = _prices.get_last_close_map([sym])
    buy_price = closing_price[sym]



    # rss updated directions said to use the price that was passed into the method
    buy_price = price



    total_cost = buy_price * shares

    if total_cost > self.cash:
        print('Insufficient funds')
>>>>>>> 207ce133d500f3b9bcc6f3b4b480191033443a71
    
    return



