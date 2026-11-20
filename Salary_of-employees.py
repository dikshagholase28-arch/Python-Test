n = int(input("Enter number of employees: "))

total = 0

for i in range(1, n+1):
    bs = float(input("Enter basic salary: "))

    if bs < 20000:
        da = bs * 10 / 100
        ta = bs * 12 / 100
        hra = bs * 15 / 100
    else:
        da = bs * 15 / 100
        ta = bs * 18 / 100
        hra = bs * 20 / 100

    salary = bs + da + ta + hra

    print("Employee salary =", salary)

    total = total + salary

print("Total salary of all employees =", total)