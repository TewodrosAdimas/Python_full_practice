amount = float(input("how much money did you spend? "))

if amount >= 1000:
    discount = 0.1

elif amount >=500:
    discount = 0.05

else:
    discount = 0

final_amount = amount * (1-discount)
print (f"Final amount is : {final_amount}")
