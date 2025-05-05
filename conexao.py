import pg8000 

conexao = pg8000.connect(user= 'postgres',
                         password = '6',
                         host = 'localhost',
                         database = 'aulas_rad_quarta'                       ls
                        )

# print('conexão realizada com sucesso!')
# conexao.close()

def inserir_novo_empregado(nome, data_nascimento, tel, endereço):
    cursor = conexao.cursor()
    cursor.execute('insert into novos_empregados (nome_emprega, data_nascimento, telefone, endereço)values (%s,%s,%s,%s)', (nome, data_nascimento,tel, endereço))

    conexao.commit()
    cursor.close()
    print('Novo empregado cadastrado com sucesso!')

def atualizar_empregado(novo_nome, matricula):
    cursor = conexao.cursor()
    cursor.execute('update novos_empregados set nome_emprega = %s where matricula = %s',(novo_nome, matricula))
    print('Empregado atualizado!')

def deletar_empregado(matricula):
    cursor = conexao.cursor()
    cursor.execute('delete from novos_empregados where matricula = %s',(matricula,))
    conexao.commit()
    cursor.close()
    print('Empregado deletado com sucesso!')
  
def listar_novos_empregados():
    cursor =  conexao.cursor()
    cursor.execute('select * from novos_empregados')
    empregados = cursor.fetchall()
    for emp in empregados:
       print(f'matricula = {emp[0]} nome = {emp[1]}, data_nasc= ={emp[2]}, tel = {emp[3]}, endereço = {emp[4]}')

    conexao.commit()
    cursor.close()


#inserir_novo_empregado('Patrcia Fogosa', '2001-12-03', '11965854255', 'rua Berenice Barrosa')

#atualizar_empregado('Rodolfo Abrantes',1)

#deletar_empregado('')

atualizar_empregado('Carlos Pereira', '357683ac-2ccf-4b47-94e5-44866e54ecb8')

listar_novos_empregados()
conexao.close()


