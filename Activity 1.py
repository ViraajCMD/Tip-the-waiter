def total_bill(bill_amount,tip):

    total = bill_amount*(1 + 0.01*tip)
    total = round(total,2)
    print(f"\nPlease pay {total} as the final amount!")

total_bill(12000, 2)