def _update_position(active_client, transaction):
    # helper function to only be used inside create_transaction    

    if transaction['type'] == 'CONTRIBUTION':
        if active_client['positions']:
            for position in active_client['positions']:                
                if position['symbol'] == transaction['symbol']:
                    position['shares'] += transaction['shares']
        else:
            position = {'id': transaction['id'],            
            'shares': round(transaction['shares'], 2),
            'symbol': transaction['symbol'],
            'name': transaction['name'],
            'avg_cost': transaction['trn_price']}

            active_client['positions'].append(position)    # or client['positions].append(position)
    elif transaction['type'] == 'BUY':
        stock = input('Please enter the ticker symbol of what shares you would like to buy: ') #user input from ticker

        while True:
            try:
                share = input('Please enter the amount of shares you would like to buy: ') #user input  # of shares
                if share > 0:
                    break
            except ValueError:
                print('Please enter an integer: ')
        
        #get price and share from ticker also need to update average cost 
        price= 5.00

        #check if we have enough cash
        cost = price * share
        if cash > cost:
            #change cash position by - cost
        else:
            print('You cannot afford this transaction.')
        #if we have enough then buy


        #deduct from cash purchase
        #if not enough return 'you do not have enough cash'
        pass
    elif transaction['type'] == 'SELL':
        pass
    elif transaction['type'] == 'WITHDRAWAL':
        pass
    else:
        print('FATAL ERROR: we should never get here _update_postion')
        exit()
    return