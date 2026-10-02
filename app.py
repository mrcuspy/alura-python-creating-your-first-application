# Importando bilbiotecas py
import os

# definindo variáveis globais
restaurantes = [{'nome':'Coco Bambu', 'categoria':'Mediterrânea','ativo':False}, 
                {'nome':'Outback', 'categoria':'Carnes', 'ativo':True},
                {'nome':'Kanpai', 'categoria':'Japonesa', 'ativo':True}
]

# definindo funções globais
def voltar_ao_menu_principal():
    '''Essa função é responsável por retornar ao menu principal

    Inputs:
    - Tecla Enter pressionada pelo usuário

    Outputs:
    - Retorna ao menu principal do aplicativo
    '''
    input('\nPressione Enter para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsável por limpar a tela e exibir um subtítulo

    Inputs:
    - texto: str - O texto do subtítulo

    Outputs:
    - Exibe o subtítulo na tela limpa
    '''
    os.system('cls')
    print(texto)
    print()

# Definindo o nome do aplicativo
def exibir_nome_do_app():
    '''Essa função é responsável por exibir o nome estilizado do aplicativo

    Outputs:
    - Exibe o nome do aplicativo em arte ASCII
    '''
    print('''

█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█

        ''')

# Definindo e exibindo o menu de opções do aplicativo
def exibir_menu_de_opcoes():
    '''Essa função é responsável por exibir as opções do menu principal

    Outputs:
    - Exibe a lista de opções disponíveis
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status restaurante')
    print('4. Sair\n')

# Definindo funções para cada opção
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante_cadastrado = {'nome':nome_do_restaurante,
         'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurante_cadastrado)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
    

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes cadastrados

    Outputs:
    - Exibe o nome, a categoria e o status de cada restaurante
    '''
    exibir_subtitulo('Lista de restaurantes cadastrados\n')
    print (f'{'Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        restaurante_ativo = 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {restaurante_ativo}')
    voltar_ao_menu_principal()

def situacao_cadastro():
    '''Essa função é responsável por alternar o status de cadastro dos restaurantes

    Inputs:
    - Nome do restaurante

    Outputs:
    - Alterna o restaurante entre ativo e inativo e exibe uma mensagem
    - Exibe um aviso caso o restaurante não seja encontrado
    '''
    exibir_subtitulo('Alterando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado de cadastro: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'{nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'{nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não foi encontrado')
    voltar_ao_menu_principal()

def finalizar_app():
    '''Essa função é responsável por finalizar o aplicativo

    Outputs:
    - Exibe a mensagem de saída do aplicativo
    '''
    exibir_subtitulo('Saindo do aplicativo\n')

def opcao_invalida():
    '''Essa função é responsável por tratar uma opção inválida

    Outputs:
    - Exibe uma mensagem de opção inválida e retorna ao menu principal
    '''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

# Solicitando escolha do usuário
def escolher_opcao():
    '''Essa função é responsável por ler e executar a opção escolhida pelo usuário

    Inputs:
    - Número da opção escolhida

    Outputs:
    - Executa a função correspondente à opção escolhida
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                situacao_cadastro()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
    

# Definindo arquivo como main
def main():
    '''Essa função é responsável por iniciar o aplicativo

    Outputs:
    - Limpa a tela, exibe o nome do aplicativo e o menu e solicita uma opção
    '''
    os.system('cls')
    exibir_nome_do_app()
    exibir_menu_de_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()