
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    if sym not in _prices.DOW30:  #checks that the ticker exists
        print('Invalid ticker symbol.')
    
    try:
        if shares <= 0:            #makes sure we have shares of it
            raise ValueError('Shares must be positive')
    except ValueError:
        print(f"Invalid Amount: Shares must be greater than zero")
    
    if shares > pos["shares"]:   #makes sure we have enough shares to be sold
            print(f'Cannot sell {shares} shares of {sym}: only {pos['shares']} owned.') 

    closing_price = _prices.get_last_close_map([sym]) #gets the dictionary
    sell_price = closing_price[sym]    #gets the actual price
    proceeds = sell_price * shares
    self.cash += proceeds


    prev_shares = pos['shares']
    cost_red = (shares / prev_shares) * pos["cost"]

    pos["cost"] -= cost_red
    pos['shares'] -= shares

    if pos['shares'] == 0:
        self.positions.remove(pos)
        
    return
       
