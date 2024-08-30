from Conexao import Conexao

import os

conexaoBD = Conexao("localhost", "root", "mysql", "spotninho")

while True: 
    
    print('''MENU SPOT-NINHO:
          
[1] - CADASTRAR USUÁRIO.
[2] - REMOVER USUÁRIO.
[3] - ENTRAR.
[0] - SAIR.
''')
    
    escolha = input("Insira uma opção: ")
    
    if (escolha  == "1"):
        
        print("\n----- CADASTRAR USUÁRIO -----")
        
        nome = input("\nInsira um nome de usuário: ")
        
        email = input("Insira um email válido: ")
        
        senha = input("Insira uma senha válida: ")
        
        usuarios = conexaoBD.consultar("SELECT * FROM usuario")
        
        consultar_email = conexaoBD.consultarComParametros("SELECT * FROM usuario WHERE email = %s", (email,))
        
        consultar_nome = conexaoBD.consultarComParametros("SELECT * FROM usuario WHERE nome = %s", (nome,))
        
        if consultar_email == [] and consultar_nome == []:
            
            if "@gmail.com" in email:
            
                print("\nNOME E EMAIL DE USUÁRIO VÁLIDOS.")
            
                conexaoBD.manipularComParametros('''INSERT INTO usuario VALUES (DEFAULT, %s, %s, %s)''', (nome, senha, email))
            
                print("USUÁRIO CADASTRADO!")
                
            else:
                
                print("\nEMAIL INVÁLIDO.")
            
        else:
            
            print("NOME OU EMAIL DE USUÁRIO INVÁLIDO.")
            
        print("")     
       
        os.system("PAUSE")
        
    if (escolha == 2):
        
        pass
    
    if (escolha == 3):
        
        pass
    
    if (escolha == 0):
        
        break
    
    
        
        
                
                