def total_calc(BILL_AMOUNT, TIP_PERC):
    
    total = BILL_AMOUNT *(1+ 0.01 * TIP_PERC)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc(150, 20)