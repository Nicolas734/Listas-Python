usuário = input('digite um nome de usuário: ')
senha = str(input('digite uma senha: '))
while ( senha == usuário ):
    print ( 'ERRO' )
    print ( 'SENHA NÃO PODE SER IGUAL AO NOME DE USUÁRIO, POR FAVOR INFORME UM VALOR VÁLIDO' )
    usuário = input('digite seu nome de usuário: ')
    senha = str(input('digite sua senha: '))
if (usuário != senha):
    print ( 'conta criada')
