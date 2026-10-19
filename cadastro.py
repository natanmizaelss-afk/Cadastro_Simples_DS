#apenas a tela de visualização 
while True:
    print ("==================")
    print ("Sistema de Cadastro")
    print ("==================")

    print("1 - Cadastrar")
    print("2 - Fazer login")
    print("3 - sair")

    opcao = int(input("Escolha uma opção: "))
#Funcionalidades
    #Se o usuario digitar o valor 1, vai ser exebido
    # a ação abaixo:
    if (opcao == 1) :
         print("==========================")
         print("=====Tela de Cadastro=====")
         print("==========================")
    elif (opcao == 2) :
        print ("===========")
        print ("=====Tela de Login=======")
        print ("===========")
    else:
        print("Você está saindo do cadastro, até mais!")
        break