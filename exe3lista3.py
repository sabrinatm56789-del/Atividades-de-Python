d= float(input('Distancia Percorida:'))
l= float(input('Quantidade de Gasolina:'))
c= d/l
if c<8:
    print ('Venda o carro')
elif c==8 or c<=12:
    print ('Econômico!')
elif c>12:
    print ('Super econômico!')
