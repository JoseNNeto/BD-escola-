import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

print('1=Funcionário. 2=Aluno.')
tabela = str(input('Qual tabela você deseja acessar?'))

if tabela == '1':
    print('1=inserir. 2=alterar. 3=excluir. 4=listar.')
    acao = str(input('O que você deseja fazer?'))
    if acao == '1':

        nome_func = (input('Digite o nome completo: '))
        cpf_func = (input('Digite o cpf: '))
        nasc_func = (input('Digite a data de nascimento (DD/MM/AA): '))
        fone_func = (input('Digite o telefone: '))
        print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
        funcao_func = (input('Digite a função: '))

        cursor.execute(""" INSERT INTO funcionario (nome,cpf,data_nasci,telefone,funcao)
        VALUES (?,?,?,?,?)""",(nome_func, cpf_func, nasc_func, fone_func, funcao_func))
        print('Funcionário inserido com sucesso!!')

    elif acao == '2':
        print('1= Nome; 2= Cpf; 3=Data de nascimento;\n 4=Telefone; 5= Função; 6=Tudo.')
        alter = str(input('O que Deseja alterar?'))
        id_func = input('Qual o ID do funcionário? ')
        if alter == '1':
            nome_func = str(input('Digite o nome completo'))
            cursor.execute(""" UPDATE funcionario SET nome = ?
                               WHERE id = ?""",(nome_func,id_func))
        elif alter == '2':
            cpf_func = int(input('Digite o CPF: '))
            cursor.execute(""" UPDATE funcionario SET cpf = ?
                                WHERE id = ? """,(cpf_func,id_func))

        elif alter == '3':
            nasc_func = int(input('Digite a Data de nascimento:'))
            cursor.execute(""" UPDATE funcionario SET data_nasci = ?
                                WHERE id = ?""",(nasc_func, id_func))
        elif alter == '4':
            fone_func = int(input('Digite o Telefone: '))
            cursor.execute(""" UPDATE funcionario SET telefone = ?
                                WHERE id = ? """, (fone_func, id_func))
        elif alter == '5':
            print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
            funcao_func = str(input(' Digite a função: '))
            cursor.execute(""" UPDATE funcionario SET funcao = ?
                                WHERE id = ? """, (funcao_func, id_func))
        elif alter == '6':
            nome_func = (input('Digite o nome completo: '))
            cpf_func = (input('Digite o cpf: '))
            nasc_func = (input('Digite a data de nascimento (DD/MM/AA): '))
            fone_func = (input('Digite o telefone: '))
            print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
            funcao_func = (input('Digite a função: '))

            cursor.execute(""" UPDATE funcionario SET nome = ? ,
                                cpf = ? , data_nasci = ?,
                                telefone = ? , funcao = ?)
                                WHERE id = ?""", (nome_func, cpf_func, nasc_func, fone_func, funcao_func, id_func))
        else:
            print('Valor incorreto!')
        print('Funcionário alterado com sucesso!!')


    elif acao == '3':
        id_func = int(input('Qual o id que você deseja deletar? '))
        cursor.execute(""" DELETE FROM funcionario 
                            WHERE id = ? """,(id_func))
        print('Funcionário deletado com sucesso!!')

    elif acao == 4:
        print('1= todos os funcionários; 2= pesquisar por id; 3= pesquisar por outro atributo.')
        list_func = str(input('Por onde você deseja pesquisar? '))
            if list_func == '1':
                cursor.execute(""" SELECT * FROM funcionario;""")
                for linha in cursor.fetchall():
                    print(linha)

            elif list_func== '2':
                id_func = int(input('Digite o id: '))
                cursor.execute(""" SELECT FROM funcionario WHERE id = ?""",(id_func))

            elif list_func== '3':
                print('1=Pesquisar pelo CPF; 2= Pesquisar pela função.')
                atrib_func =str(input('Por onde você deseja pesquisar?'))

                if atrib_func == '1':
                    cpf_func = int(input('Digite o CPF do funcionário: '))
                    cursor.execute("""SELECT FROM funcionario WHERE cpf = ?""", (cpf_func))

                elif atrib_func == '2':
                    print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
                    funcao_func = str(input('Digite a função:'))

                else:
                    print('Local inválido!!')
            else:
                print('Ação Inválida!!')
    else:
        print('Valor incorreto!!!!!')
conn.commit()
#elif tabela == 2:
    #acao = int(input('O que você deseja fazer?'))
    #print('1=inserir. 2=alterar. 3=excluir. 4=listar.')
    #if acao == 1:

  #  elif acao == 2:

   # elif acao == 3:

  #  elif acao == 4:

   # else:
        #print('Valor incorreto!!!!!')

#else:
   # print('Tabela inexistente.')
conn.commit()
conn.close()