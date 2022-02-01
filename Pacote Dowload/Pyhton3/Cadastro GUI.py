from PySimpleGUI import PySimpleGUI as sg

sg,theme('Reddit')
layout - [
    [sg.text('Usuário'),sg.Input(key='usuario', size=(20,1))],
    [sg.text('Senha'),sg.Input(key='senha',password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'João' and valores['senha'] == '12345':
            print('Bem vindo ao mundo python!')