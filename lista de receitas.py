#lista pré definida
list = ['pão','panqueca']

size = len(list)

print(list)

choice = input('\n  qual receita voce deseja saber? ')

def choose():
    print ('\n' , list)

    choice = input('\n  qual receita voce deseja saber? ')


if choice == 'pão' or 1:
    print(24*'*','\n'," farinha, leite, lorem, ipsum.\n\n   1- bate o lorem por 3 minutos")

    choose()

if choice == 'panqueca' or 2:
    print(24*'*','\n',' fulano, beutrano')

    choose()