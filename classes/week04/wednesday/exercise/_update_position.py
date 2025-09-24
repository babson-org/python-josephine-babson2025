'''
## Rethinking input_client() and Position Updates

Take a look at input_client() in client.py in the portfolio folder.  
Right now, this is the function that creates a new client.  

### Current Behavior
- Every new client starts with:
  - An empty portfolio (positions = []).
  - An initial **cash contribution**.
- We record that contribution by:
  1. Creating a transaction using create_transaction().
  2. Updating the cash position inside input_client().

This works, but it's not a great design. The logic for updating positions is **scattered**, 
and input_client() is doing too much.

---

### Why This Is a Problem
- Every time a transaction happens, we **must** also update the corresponding position.  
- Right now, there is no single place that enforces this rule.  
- If we forget to update positions after creating a transaction, the system will drift out of sync.

---

### Better Design
We should create a helper function (e.g., _update_position(client, transaction)) that:
- Takes the active client and the new transaction as input.
- Updates the client's positions accordingly.
- Ensures consistency between **transactions** and **positions**.

This helper would be called inside create_transaction(), so that every transaction automatically 
updates the portfolio.

---

### Issues We Need to Handle


1. **Buying a Security**
   - Validate ticker: does it exist in ticker.data?
   - Check available cash: do we have enough to cover the purchase?
   - Update (or create) the position for that symbol.
   - Recalculate the average cost.

2. **Selling a Security**
   - Validate position: do we own that ticker?
   - Check share count: do we have at least that many shares?
   - Reduce (or remove) the position if shares go to zero.
   - Add cash back to the portfolio.

3. **Contributions**
   - no positions exist (first contribution)
   - add to existing cash balance

4. **Withdrawals**
   - Check available cash balance.
   - Reduce the cash position accordingly.

---

### Next Step
Refactor:
- Move position-update logic out of input_client().
- Implement _update_position(client, transaction).
- Call it automatically inside create_transaction() for every transaction type.

For Wednesday, write the function so it handles CONTRIBUTIONS and
WITHDRAWALS.  For now, return None for transaction types BUY or SELL

This way:
- transactions become the **source of truth**.
- positions` always stay consistent with recorded transactions.



'''

import datetime

# --- Utilities -------------------------------------------------------------

def _get_position(client, ticker):
    """Return the position dict for ticker, or None if not present."""
    for p in client.get('positions', []):
        if p.get('ticker') == ticker:
            return p
    return None

# --- Position updater -----------------------------------------------------

def _update_position(client, transaction):
    """
    Update client's positions based on a transaction.
    For now: handle 'CONTRIBUTION' and 'WITHDRAWAL'.
    For 'BUY' and 'SELL' return None (not implemented yet).
    Raises ValueError when a withdrawal is not possible.
    """

    ttype = transaction['type']
    # We treat cash position under ticker name 'CASH'
    cash_ticker = 'CASH'

    # Ensure the client has a positions list
    if 'positions' not in client:
        client['positions'] = []

    # Handle contribution: add cash (create cash position if needed)
    if ttype == 'CONTRIBUTION':
        amount = float(transaction['amount'])
        pos = _get_position(client, cash_ticker)
        if pos is None:
            pos = {'ticker': cash_ticker, 'quantity': 0.0}
            client['positions'].append(pos)
        pos['quantity'] += amount
        return pos

    # Handle withdrawal: subtract cash (validate sufficient balance)
    elif ttype == 'WITHDRAWAL':
        amount = float(transaction['amount'])
        pos = _get_position(client, cash_ticker)
        current = pos['quantity'] if pos is not None else 0.0
        if current < amount:
            # Not enough cash — do not change positions; caller should handle the exception
            raise ValueError("Insufficient cash for withdrawal")
        # safe to subtract
        pos['quantity'] = current - amount
        return pos

    # For BUY/SELL we return None for now (placeholder per requirements)
    elif ttype in ('BUY', 'SELL'):
        return None

    else:
        raise ValueError(f"Unknown transaction type: {ttype}")

# --- Transaction creation -------------------------------------------------

def create_transaction(client, ttype, amount=None, ticker=None, shares=None, price=None):
    """
    Create a transaction record and update positions.
    Design decision: update positions BEFORE appending the transaction so that
    if position update fails, no transaction is recorded (keeps data consistent).
    """

    # Basic validation for the two supported types
    if ttype in ('CONTRIBUTION', 'WITHDRAWAL') and amount is None:
        raise ValueError("amount is required for contribution/withdrawal")

    tx = {
        'type': ttype,
        'amount': float(amount) if amount is not None else None,
        'ticker': ticker,
        'shares': shares,
        'price': price,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }

    # Try to update positions first. If this raises, nothing will be appended to transactions.
    _update_position(client, tx)

    # If update succeeded, record the transaction (transactions list is the source of truth)
    client.setdefault('transactions', []).append(tx)
    return tx

# --- Client creation helper (refactored) ---------------------------------

def input_client(client_id, initial_contribution=0.0):
    """
    Create a new client dict. Do NOT manipulate positions directly here.
    If initial contribution > 0, create a CONTRIBUTION transaction (which will update positions).
    """
    client = {
        'id': client_id,
        'positions': [],       # start empty; create_transaction will populate CASH if needed
        'transactions': []
    }

    if initial_contribution and initial_contribution > 0:
        create_transaction(client, 'CONTRIBUTION', amount=initial_contribution)

    return client

# --- Tiny demo ------------------------------------------------------------

if __name__ == "__main__":
    c = input_client("client-123", initial_contribution=1000.0)
    print("After contribution positions:", c['positions'])
    print("After contribution transactions:", c['transactions'])

    # Make a withdrawal that succeeds
    create_transaction(c, 'WITHDRAWAL', amount=200.0)
    print("After withdrawal positions:", c['positions'])
    print("After withdrawal transactions:", c['transactions'])

    # Attempt a withdrawal that fails (insufficient funds) -> raises ValueError
    try:
        create_transaction(c, 'WITHDRAWAL', amount=2000.0)
    except ValueError as e:
        print("Expected error:", e)

    # BUY/SELL are not implemented yet, they just return None from _update_position
    tx = create_transaction(c, 'BUY', amount=None, ticker='AAPL', shares=1, price=150.0)
    print("BUY transaction recorded (positions not changed):", tx)
    print("Final positions:", c['positions'])
