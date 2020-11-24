import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

print('1=Funcionário. 2=Aluno.')
tabela_aluno = int(input('Qual tabela você deseja acessar?'))

if tabela_aluno == 1:
    print('1=inserir. 2=alterar. 3=excluir. 4=listar.')
    acao = int(input('O que você deseja fazer?'))
    if acao == 1:

        nome_func = (input('Digite o nome completo: '))
        cpf_func = (input('Digite o cpf: '))
        nasc_func = (input('Digite a data de nascimento (DD/MM/AA): '))
        fone_func = (input('Digite o telefone: '))
        print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
        funcao_func = (input('Digite a função: '))

        cursor.execute(""" INSERT INTO funcionario (nome,cpf,data_nasci,telefone,funcao)
        VALUES (?,?,?,?,?)""",(nome_func, cpf_func, nasc_func, fone_func, funcao_func))
        print('Funcionário inserido com sucesso!!')

    elif acao == 2:
        print('1= Nome; 2= Cpf; 3=Data de nascimento;\n 4=Telefone; 5= Função; 6=Tudo.')
        alter = int(input('O que Deseja alterar?'))
        id_func = input('Qual o ID do funcionário? ')
        if alter == 1:
            nome_func = str(input('Digite o nome completo'))
            cursor.execute(""" UPDATE funcionario SET nome = ?
                               WHERE id = ?""",(nome_func,id_func))
        elif alter == 2:
            cpf_func = int(input('Digite o CPF: '))
            cursor.execute(""" UPDATE funcionario SET cpf = ?
                                WHERE id = ? """,(cpf_func,id_func))

        elif alter == 3:
            nasc_func = int(input('Digite a Data de nascimento:'))
            cursor.execute(""" UPDATE funcionario SET data_nasci = ?
                                WHERE id = ?""",(nasc_func, id_func))
        elif alter == 4:
            fone_func = int(input('Digite o Telefone: '))
            cursor.execute(""" UPDATE funcionario SET telefone = ?
                                WHERE id = ? """, (fone_func, id_func))
        elif alter == 5:
            print('Funções: P=Professor; G=Gestão; L= Limpeza; \n C=Cantina; V=Vigilância; B=Biblioteca.')
            funcao_func = str(input(' Digite a função: '))
            cursor.execute(""" UPDATE funcionario SET funcao = ?
                                WHERE id = ? """, (funcao_func, id_func))
        elif alter == 6:
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
            print('Funcionário alterado sucesso!!')


    #elif acao == 3:

    #elif acao == 4:

    #else:
       # print('Valor incorreto!!!!!')
conn.commit()
#elif tabela == 2:
   # acao = int(input('O que você deseja fazer?'))
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