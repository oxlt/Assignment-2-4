salary = input("Enter salary: ")
numDependents = input("Enter number of dependents: ")
salary = int(salary)
numDependents = int(numDependents)

stateTax = 0.065
federalTax = 0.28
dependentDeduction = 0.025

stateTax = salary * stateTax
federalTax = salary * federalTax
dependentDeduction = salary * dependentDeduction * numDependents

totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

print("statetax: $", stateTax)
print("federaltax: $", federalTax)
print("dependentdeduction: $", dependentDeduction)
print("salary: $", salary)
print("takehomepay: $", takeHomePay)