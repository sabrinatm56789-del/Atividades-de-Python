Vm= int(input('Valor da venda: R$ '))
if Vm>= 100000:
    C= 700 + (0.16 * Vm)
    print (f'Comissão: R${C:.2f}')
elif Vm<= 100000 and Vm>= 80000:
    C= 650 + (0.14 * Vm)
    print (f'Comissão: R${C:.2f}')
elif Vm<= 80000 and Vm>= 60000:
    C= 600 + (0.14 * Vm)
    print (f'Comissão: R${C:.2f}')
elif Vm<= 80000 and Vm>= 40000:
    C= 550 + (0.14 * Vm)
    print (f'Comissão: R${C:.2f}')
elif Vm<= 400000 and Vm>= 20000:
    C= 500 + (0.14 * Vm)
    print (f'Comissão: R${C:.2f}')
elif Vm< 20000:
    C= 400 + (0.14 * Vm)
    print (f'Comissão: R${C:.2f}')
# C= Comissão e Vm= Valor mensal de vendas