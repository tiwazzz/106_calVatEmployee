def vatCal(sal):
    if sal >= 30000.00:
        vatTotal = sal-(sal*0.05)
    else:
        vatTotal = sal-(sal*0.00)
    return vatTotal

def total(sal, com):
    finalSal = sal+com
    return finalSal

empSal = float(input("Enter your salary: "))
empCom = float(input("Enter your commission: "))

vated = vatCal(empSal)
plusCom = total(vated, empCom)

print(f"Salary per month (VAT already): {plusCom} Thai Baht")