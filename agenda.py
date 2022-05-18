


from distutils.log import error


AGENDA = {}

AGENDA['Thor'] = {

'telefone': '55555555',
'Email': 'Thor@hotmail.com',
'Endereço': 'AV,8'}


def mostra_contatos():#método para mostrar os contatos 
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscar_contato(contato)#Uso o buscar contato que já está formato para pegar todos os contatos
            
    else:
        print ('>>> Nenhum Contato adicionado <<<')

       
        


def buscar_contato(contato):#método busca contato
    try:
        print (f'Nome: {contato}')#vai olhar agenda e o parametro contato vai ser oque irá filtra o nome
        print (f'Telefone: {AGENDA[contato]["telefone"]}')
        print (f'Email: {AGENDA[contato]["Email"]}')
        print (f'Endereço: {AGENDA[contato]["Endereço"]}')
        print (' ')
    except KeyError:
        print ('>>> Contato Inexistente <<<')

def incluir_edita_contato(contato,telefone,email,endereco):#função adiciona contato e edita
    AGENDA[contato] = {
    
   'telefone': telefone,
   'Email': email,
   'Endereço':endereco
   }
    print (f'>>> Contato {contato} adicionado/editado com sucesso <<< ')
    print (' ')

def exclui_contato(contato):
    try:
        AGENDA.pop(contato)#comando pop para deletar um contato
        print (f'Contato {contato} deletado com sucesso')
        print (' ')
    except:
        print ('>>> O Contato não existe <<<')



def exportar_contatos():
  try:
        with open('arquivo.csv','w') as file:

            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                Email = AGENDA[contato]["Email"]
                Endereço = AGENDA[contato]["Endereço"]
                file.write(f'Contato: {contato}, Telefone: {telefone}, Email: {Email}, Endereço: {Endereço}'+ '\n') 
            print('>>> Agenda Exportada com sucesso. <<<')

  except:
        print ('>>> Algo deu errado. <<<')



def importar_contatos(filename):
   try:
        with open(filename, 'r') as arquivo:

            linhas = print(arquivo.readline())

   except FileNotFoundError:

        print ('>>> Arquivo não encontrado <<<')
    
   except: 
        print ('Algo deu errado.')
        print (error)



def escreval(txt):

  
    print (f'-'*35)
    print (f'         {txt}')
    print (f'-'*35)


def menu():

    while True:
        escreval('Menu Principal')
        print ('| 1 - Mostra todos os contatos   |')
        print ('| 2 - Buscar contato             |')
        print ('| 3 - Incluir contato            |')
        print ('| 4 - Editar contato             |')
        print ('| 5 - Excluir contato            |')
        print ('| 6 - Exportar contatos para Csv |')
        print ('| 7 - Importar arquivos Csv      |')
        print ('| 0 - Sair do programa           |') 
        print('-'*35)

        

        opcao = int(input('Escolha a opção: '))

        if opcao == 1:

            mostra_contatos()

        elif opcao == 2:
            
                contato = str(input('Nome do contato: '))
                buscar_contato(contato)

            

        elif opcao == 3 or opcao == 4: #Junção de funções: Incluir/Editar

            contato = str(input('Informe o nome: '))
            telefone = int(input('Informe o Telefone: '))
            email = str(input('Informe o Email: '))
            endereco = str(input('Informe o Endereço: '))
            incluir_edita_contato(contato,telefone,email,endereco)

        elif opcao == 5:
            contato = str(input('Nome do contato: '))

            exclui_contato(contato)
        
        elif opcao == 6:
            exportar_contatos()
        
        elif opcao == 7:
            
            filename = input('Digite o nome do arquivo: ')
            importar_contatos(filename)



        elif opcao == 0: 
            print (f'Programa Finalizado.')
            break

        else:
            print ('Opção inválida')
   

