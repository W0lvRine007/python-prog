print("Welcome to the tip calculater")
bill = int(input("What was the total bill\n"))
tip = float(input("What percentage tip you would like to give\n"))
people = int(input("How many people to split the bill in\n"))
total_bill = tip / 100 + bill
bill_per_head = total_bill / people
final_amt = round(bill_per_head, 2) 


ans = f"The bill you have to pay per head is {final_amt}"
print(ans)