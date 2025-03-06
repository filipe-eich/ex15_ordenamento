"""
Programa: ordenamento
Descrição: Este programa ordena três valores em ordem crescente, à escolha do usuário
Autor: Filipe Eich
Data: 28/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

a=""
b=""
c=""

aux=7


#Entrada de dados

a = float(input("\nOlá, posso colocar três números em ordem crescente para você. Comece me dizendo o primeiro: "))
b = float(input("\nAgora, o segundo: "))
c = float(input("\nPor fim, o terceiro: "))


# Processamento de dados

"""
a>b>c; aux=1
a>c>b; aux=2
b>a>c; aux=3
b>c>a; aux=4
c>a>b; aux=5
c>b>a; aux=6
"""

# para a>b>c; aux=1 e a>c>b; aux=2

if a>=b and a>=c:
    if b>=c:
        aux=1
    else:
        aux=2

# para b>a>c; aux=3 e b>c>a; aux=4
elif b>=c and b>=a:
    if a>=c:
        aux=3
    else:
        aux=4

# para c>a>b; aux=5 e c>b>a; aux=6
elif c>=b and c>=a:
    if a>=b:
        aux=5
    else:
        aux=6


#Saida de dados

if aux==1:
    print(f"\nAqui estão os valores em ordem crescente: {c}; {b}; {a}")
elif aux==2:
    print(f"\nAqui estão os valores em ordem crescente: {b}; {c}; {a}")
elif aux==3:
    print(f"\nAqui estão os valores em ordem crescente: {c}; {a}; {b}")
elif aux==4:
    print(f"\nAqui estão os valores em ordem crescente: {a}; {c}; {b}")
elif aux==5:
    print(f"\nAqui estão os valores em ordem crescente: {b}; {a}; {c}")
elif aux==6:
    print(f"\nAqui estão os valores em ordem crescente: {a}; {b}; {c}")

