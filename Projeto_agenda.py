def menu():
    opcao = input('\n'
                  '    ====================================================\n'
                  '                        AGENDA\n'
                  '    \n'
                  '    MENU:\n'
                  '    \n'
                  '    [1] CADASTRAR CONTATO\n'
                  '    [2] LISTAR CONTATO\n'
                  '    [3] DELETAR CONTATO\n'
                  '    [4] BUSCAR CONTATO PELO ID\n'
                  '    \n'
                  '    =======================================================\n'
                  '    ESCOLHA A OPÇÃO ACIMA')

    return print(opcao)


def main():
    menu()
