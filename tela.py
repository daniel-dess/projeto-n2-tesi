import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

import sqlite3

def criar_tabela_questoes(materia):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS questoes_{materia.lower().replace(" ", "_")} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            opcao_a TEXT NOT NULL,
            opcao_b TEXT NOT NULL,
            opcao_c TEXT NOT NULL,
            opcao_d TEXT NOT NULL,
            resposta_correta INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Cria a tabela de questões para diferentes matérias
materias = ["Redes de Computadores", "Sistemas Operacionais", "Introdução à Informática", "Linguagem de Programação", "Arquitetura de Computadores"]

for materia in materias:
    criar_tabela_questoes(materia)


def criar_tabela_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def cadastrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()

    if len(senha) < 8:
        messagebox.showerror("Erro no Cadastro", "A senha deve ter pelo menos 8 caracteres.")
        return
    elif not any(char.isupper() for char in senha):
        messagebox.showerror("Erro no Cadastro", "A senha deve conter pelo menos uma letra maiúscula.")
        return
    elif not any(char.isdigit() for char in senha):
        messagebox.showerror("Erro no Cadastro", "A senha deve conter pelo menos um número.")
        return
    elif not any(char in '!@#$%^&*()_+' for char in senha):
        messagebox.showerror("Erro no Cadastro", "A senha deve conter pelo menos um caractere especial.")
        return

    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE email=?', (email,))
    if cursor.fetchone() is not None:
        conn.close()
        messagebox.showerror("Erro no Cadastro", "Este e-mail já está cadastrado.")
        return

    cursor.execute('''
        INSERT INTO usuarios (nome, email, senha)
        VALUES (?, ?, ?)
    ''', (nome, email, senha))

    conn.commit()
    conn.close()

    messagebox.showinfo("Cadastro Concluído", "Usuário cadastrado com sucesso!")

def abrir_pagina_cadastro():
    global nome_entry, email_entry, senha_entry
    cadastro_window = tk.Toplevel(janela)
    cadastro_window.title("Cadastro de Usuário")

    tk.Label(cadastro_window, text="Crie sua conta", font=("Helvetica", 16)).pack(pady=(10, 0))

    frame_erros = tk.Frame(cadastro_window)
    frame_erros.pack(pady=(10, 0))

    nome_label = tk.Label(frame_erros, text="Nome Completo:")
    nome_label.pack()

    nome_entry = tk.Entry(frame_erros)
    nome_entry.pack()

    email_label = tk.Label(frame_erros, text="Email:")
    email_label.pack()

    email_entry = tk.Entry(frame_erros)
    email_entry.pack()

    senha_label = tk.Label(frame_erros, text="Senha (Mínimo 8 caracteres, 1 maiúscula, 1 especial, 1 número):")
    senha_label.pack()

    senha_entry = tk.Entry(frame_erros, show="*")
    senha_entry.pack()

    cadastrar_button = tk.Button(cadastro_window, text="Cadastrar", font=("Helvetica", 12), fg="white", bg="#0078D7", command=cadastrar_usuario)
    cadastrar_button.pack(pady=(10, 0))

def fazer_login():
    login_window = tk.Toplevel(janela)
    login_window.title("Faça Login")

    email_label = tk.Label(login_window, text="Email:")
    email_label.pack()

    email_entry = tk.Entry(login_window)
    email_entry.pack()

    senha_label = tk.Label(login_window, text="Senha:", width=20)
    senha_label.pack(pady=25)

    senha_entry = tk.Entry(login_window, show="*")
    senha_entry.pack()

    def autenticar_usuario():
        email = email_entry.get()
        senha = senha_entry.get()

        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
        usuario = cursor.fetchone()

        conn.close()

        if usuario is not None:
            messagebox.showinfo("Login Concluído", "Login bem sucedido!")
            login_window.destroy()
        else:
            cursor.execute('SELECT * FROM usuarios WHERE email=?', (email,))
            usuario_por_email = cursor.fetchone()

            if usuario_por_email is not None:
                messagebox.showerror("Erro no Login", "Senha incorreta.")
            else:
                messagebox.showerror("Erro no Login", "Este e-mail não possui um registro.")

    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 12), fg="white", bg="#0078D7", command=autenticar_usuario)
    login_button.pack(pady=10)

def criar_pagina_perfil():
    perfil_janela = tk.Toplevel(janela)
    perfil_janela.title("Perfil do Usuário")
    perfil_janela.geometry("800x600")

    perfil_frame = tk.Frame(perfil_janela, bg="white")
    perfil_frame.pack(fill="both", expand=True)

    # Adicionando o menu
    menu = tk.Menu(perfil_janela)
    perfil_janela.config(menu=menu)

    file_menu = tk.Menu(menu)
    menu.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Página Inicial", command=perfil_janela.destroy)  # Alteração aqui
    file_menu.add_separator()
    file_menu.add_command(label="Sair", command=janela.quit)

    # Adicionando o banner
    banner_frame = tk.Frame(perfil_frame, bg="#0078D7")
    banner_frame.pack(fill="x")

    logo_image = ImageTk.PhotoImage(Image.open("logo.jpg"))
    logo_label = tk.Label(banner_frame, image=logo_image, bg="#0078D7")
    logo_label.pack(side="left", padx=10)

    title_label = tk.Label(banner_frame, text="Perfil do Usuário", font=("Helvetica", 16), fg="white", bg="#0078D7")
    title_label.pack(side="left", padx=15)

    # Adicionando informações do usuário
    nome_label = tk.Label(perfil_frame, text=f"Nome: {nome}", font=("Helvetica", 12), bg="white")
    nome_label.pack(pady=(20, 0))

    email_label = tk.Label(perfil_frame, text=f"Email: {email}", font=("Helvetica", 12), bg="white")
    email_label.pack()

    # Adicionando os botões de funcionalidades
    funcionalidades_frame = tk.Frame(perfil_frame, bg="white")
    funcionalidades_frame.pack(pady=(20, 0))

    filtro_button = tk.Button(funcionalidades_frame, text="Filtre suas questões", font=("Helvetica", 12), fg="white", bg="#0078D7", width=20, height=2, command=filter_questions)
    filtro_button.pack(side="left", padx=10)

    compartilhar_button = tk.Button(funcionalidades_frame, text="Compartilhe seu conhecimento", font=("Helvetica", 12), fg="white", bg="#0078D7", width=20, height=2)
    compartilhar_button.pack(side="left", padx=10)

    interagir_button = tk.Button(funcionalidades_frame, text="Interaja a partir de comentários", font=("Helvetica", 12), fg="white", bg="#0078D7", width=20, height=2)
    interagir_button.pack(side="left", padx=10)

    # Adicionando o rodapé
    footer_frame = tk.Frame(perfil_frame, bg="#0078D7")
    footer_frame.pack(fill="x")

    footer_label = tk.Label(footer_frame, text="© 2023 Daneil Santos & Erika Da Hora", font=("Helvetica", 10), fg="white", bg="#0078D7")
    footer_label.pack(pady=5)

def exibir_opcoes_cadastro():
    opcoes_cadastro_window = tk.Toplevel(janela)
    opcoes_cadastro_window.title("Cadastro de Usuário")

    mensagem_label = tk.Label(opcoes_cadastro_window, text="Já está cadastrado?")
    mensagem_label.pack()

    nao_button = tk.Button(opcoes_cadastro_window, text="Não", command=abrir_pagina_cadastro)
    nao_button.pack(side="left", padx=10)

    sim_button = tk.Button(opcoes_cadastro_window, text="Sim", command=fazer_login)
    sim_button.pack(side="left", padx=10)

def filter_questions():
    groups = ["Redes de Computadores", "Sistemas Operacionais", "Introdução à Informática", "Linguagem de Programação", "Arquitetura de Computadores"]

    filter_window = tk.Toplevel(janela)
    filter_window.title("Filtre suas Questões")

    label = tk.Label(filter_window, text="Selecione uma matéria:")
    label.pack()

    for group in groups:
        group_button = tk.Button(filter_window, text=group, command=lambda g=group: exibir_questoes(g))
        group_button.pack()

def exibir_questoes(materia):
    questoes_frame = tk.Toplevel(janela)
    questoes_frame.title(f"Questões de {materia}")

    # Adicione as questões conforme a matéria
    if materia == "Redes de Computadores":
        questoes = [
            {
                "pergunta": "Qual é a diferença entre um switch e um roteador em uma rede de computadores? Como eles funcionam e qual é o seu propósito?",
                "opcoes": ["Switches encaminham pacotes apenas dentro da rede local, enquanto roteadores encaminham pacotes entre diferentes redes. Switches operam na camada de enlace do modelo OSI e roteadores operam na camada de rede.",
                            "Switches encaminham pacotes apenas entre diferentes redes, enquanto roteadores encaminham pacotes apenas dentro da rede local. Switches operam na camada de rede do modelo OSI e roteadores operam na camada de enlace.",
                            "Switches e roteadores são termos intercambiáveis e ambos encaminham pacotes entre diferentes redes. Ambos operam na camada de rede do modelo OSI.",
                            "Switches e roteadores são dispositivos diferentes, mas funcionam da mesma maneira. Ambos operam na camada física do modelo OSI."],
                "resposta_correta": 0
            },
            {
                "pergunta": "Explique o que é NAT (Network Address Translation) e por que é usado em redes.",
                "opcoes": ["NAT é uma técnica que traduz endereços IP públicos em endereços IP privados e vice-versa. É usado para permitir que vários dispositivos compartilhem um único endereço IP público.",
                            "NAT é uma técnica usada para criptografar a comunicação entre dispositivos em uma rede, garantindo segurança e privacidade.",
                            "NAT é uma técnica que resolve problemas de latência em redes de alta velocidade, garantindo uma comunicação mais eficiente.",
                            "NAT é um protocolo de roteamento usado para determinar a melhor rota para os pacotes de dados na rede."],
                "resposta_correta": 0
            },
            # Adicione mais questões sobre Redes de Computadores aqui
        ]
    # ... (adicionar questões para as outras matérias)
    else:
        messagebox.showerror("Matéria não encontrada", "A matéria selecionada não possui questões.")
        questoes_frame.destroy()
        return

    def verificar_respostas():
        for idx, var in enumerate(respostas_vars):
            if var.get() != questoes[idx]["resposta_correta"]:
                messagebox.showinfo("Resposta Incorreta", f"Infelizmente, você errou a questão {idx+1}.")
                return
        messagebox.showinfo("Respostas Corretas", "Parabéns, você acertou todas as questões!")

    respostas_vars = []  # Lista de variáveis para armazenar as escolhas do usuário

    for pergunta_info in questoes:
        pergunta = pergunta_info["pergunta"]
        opcoes = pergunta_info["opcoes"]

        tk.Label(questoes_frame, text=pergunta).pack(anchor="w")

        var = tk.IntVar()
        respostas_vars.append(var)  # Adiciona a variável à lista

        for i, opcao in enumerate(opcoes):
            tk.Radiobutton(questoes_frame, text=f"Opção {chr(65 + i)}: {opcao}", value=i, variable=var).pack(anchor="w")

    confirm_button = tk.Button(questoes_frame, text="Confirmar Respostas", command=verificar_respostas)
    confirm_button.pack()
# Código inicial

janela = tk.Tk()
janela.title("Plataforma de Atividades Interativas")
janela.geometry("800x600")

banner_frame = tk.Frame(janela, bg="#0078D7")
banner_frame.pack(fill="x")

logo_image = ImageTk.PhotoImage(Image.open("logo.jpg"))
logo_label = tk.Label(banner_frame, image=logo_image, bg="#0078D7")
logo_label.pack(side="left", padx=10)

title_label = tk.Label(banner_frame, text="Bem-vindo à Plataforma de Atividades Interativas", font=("Helvetica", 16), fg="white", bg="#0078D7")
title_label.pack(side="left", padx=15)

home_frame = tk.Frame(janela, bg="white")
home_frame.pack(fill="both", expand=True)

red_button = tk.Button(home_frame, text="Começar", font=("Helvetica", 24), fg="white", bg="#E81123", width=10, height=2, command=exibir_opcoes_cadastro)
red_button.pack(pady=20)

blue_buttons_frame = tk.Frame(home_frame, bg="white")
blue_buttons_frame.pack()

blue_button1 = tk.Button(blue_buttons_frame, text="Filtre suas questões", font=("Helvetica", 12), fg="white", bg="#0078D7", width=25, height=2, command=filter_questions)
blue_button1.pack(side="left", padx=10)

blue_button2 = tk.Button(blue_buttons_frame, text="Interaja a partir de comentários", font=("Helvetica", 12), fg="white", bg="#0078D7", width=25, height=2)
blue_button2.pack(side="left", padx=10)

blue_button3 = tk.Button(blue_buttons_frame, text="Compartilhe seu conhecimento", font=("Helvetica", 12), fg="white", bg="#0078D7", width=25, height=2)
blue_button3.pack(side="left", padx=10)

footer_frame = tk.Frame(janela, bg="#0078D7")
footer_frame.pack(fill="x")

footer_label = tk.Label(footer_frame, text="© 2023 Daneil Santos & Erika Da Hora", font=("Helvetica", 10), fg="white", bg="#0078D7")
footer_label.pack(pady=5)

menu = tk.Menu(janela)
janela.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="menu", menu=file_menu)
file_menu.add_command(label="Perfil", command=criar_pagina_perfil)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=janela.quit)
menu.add_command(label="Perfil", command=criar_pagina_perfil)




# Inicializa o programa
janela.mainloop()
