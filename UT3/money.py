def run(to_give_back: float, available_currencies: list) -> dict:
    money_back = {}

 
    available_currencies.sort(reverse=True)

  
    for currency in available_currencies:
    
        num_notes = int(to_give_back // currency)
        if num_notes > 0:
            money_back[currency] = num_notes

        
            to_give_back -= num_notes * currency

    if to_give_back != 0:
        money_back = None

    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])
