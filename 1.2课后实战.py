import sys
try:
    assert len(sys.argv) == 2
except:
    print('Parameter Error')
    exit()

salary = sys.argv[1]  # 直接用 ctrl + B 的时候这里会报错，但是不用管，在cmd里面运行的时候加上参数就好了。
tax_num = int(salary) - 3500
if ((tax_num < 0) or (tax_num == 0)):
    tax_rate = 0
    deduction = 0
elif 0 < tax_num < 1500:
    tax_rate = 0.03
    deduction = 0
elif 1500 < tax_num < 4500:
    tax_rate = 0.1
    deduction = 105
elif 4500 < tax_num < 9000:
    tax_rate = 0.2
    deduction = 555
elif 9000 < tax_num < 35000:
    tax_rate = 0.25
    deduction = 1005
elif 35000 < tax_num < 55000:
    tax_rate = 0.3
    deduction = 2755
elif 55000 < tax_num < 80000:
    tax_rate = 0.35
    deduction = 5505
else:
    tax_rate = 0.45
    deduction = 13505
tax = tax_num * tax_rate - deduction
print('the tax you should pay is: ', tax)
