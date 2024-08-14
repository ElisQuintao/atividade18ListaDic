# Crie, em Python, um CRUD de usuários completo (Cadastrar, Pesquisar/Listar, Alterar e Excluir).
# O programa deverá:

# - Cadastrar usuário
# - Listar todos os usuários
# - Pesquisar por um usuário
# - Alterar os dados do usuário
# - Excluir usuário
# - Sair do programa

# O usuário deverá cadastrar:

# - Nome completo
# - Data de Nascimento
# - CPF
# - Profissão
# - E-mail
# - Endereço
# - Telefone

chaves = ('Nome completo', 'Data de Nascimento', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

usuarios = [
     {
     chaves[0]: 'Elisangela',
     chaves[1]: '06-02-80',
     chaves[2]:8693532,
     chaves[3]:'Programadora',
     chaves[4]: 'fsgsgsgsg@fdfggagag',
     chaves[5]: 'rua brasil 19',
     chaves[6]:5165658478454
     },
     {
     chaves[0]: 'Bruno',
     chaves[1]: '06-02-79',
     chaves[2]:8693532,
     chaves[3]:'Programador',
     chaves[4]: 'fsgsgsgsg@fdfggagag',
     chaves[5]: 'rua brasil 80',
     chaves[6]:516565847   
     }
]
print(f'\n{'='*10} LISTA DE USUARIOS {'='*10} \n')
for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')
    print(f'\n{'-'*10}\n')

#adicionar novo dicionario a lista de dicionarios
# colocar aqui o match case - verificar a atividade da calculadora
usuario ={}
for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'informe {chaves[i]}:')
usuarios.append(usuario)

print(f'\n{'='*10}LISTA DE USUARIOS{'='*10}\n')
for usuario in usuarios:
            for chave in chaves:
                print(f'{chave}: {usuario[chave]}')
            print(f'\n{'-'*10}\n')


    


            