import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from tkinter import font

from PIL import Image, ImageTk

import conexao as bd

class Tela():
    
    def __init__(self, master):
        self.janela = master
        self.janela.title('Plataforma de Atividades Interativas')
        self.janela.minsize(1000, 600)
        try: self.janela.attributes('-zoomed', True)
        except: self.janela.state('zoomed')
        
        self.style = Style()
        self.style.theme_use('sandstone')
        self.bg_light = '#A6A6A6'
        self.bg_dark = '#D9D9D9'
        self.bg_atual = self.bg_light

        self.header = ttk.Frame(self.janela, height=50)
        self.header.pack(side='top', fill='x')

        self.header.grid_rowconfigure(0, weight=1)
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid_columnconfigure(2, weight=1)
        self.header.grid_columnconfigure(3, weight=1)
        self.header.grid_columnconfigure(4, weight=1)
        
        self.imagem1 = Image.open('logo.png')
        self.logo_image = ImageTk.PhotoImage(self.imagem1)
        self.logo_label = ttk.Label(self.header, image=self.logo_image)
        self.logo_label.grid(row=0, column=0)
        
        self.inicio = ttk.Label(self.header, text='INÍCIO', font=('Times New Roman', 18), padding=(50, 50), cursor='hand2')
        self.inicio.grid(row=0, column=1)
        self.inicio.bind('<Button-1>', lambda event, label_name=self.inicio: self.atualiza_header(label_name))
        
        self.questoes = ttk.Label(self.header, text='QUESTÕES', font=('Times New Roman', 18), padding=(50, 50), cursor='hand2')
        self.questoes.grid(row=0, column=2)
        self.questoes.bind('<Button-1>', lambda event, label_name=self.questoes: self.atualiza_header(label_name))
        
        self.perfil = ttk.Label(self.header, text='PERFIL', font=('Times New Roman', 18), padding=(50, 50), cursor='hand2')
        self.perfil.grid(row=0, column=3)
        self.perfil.bind('<Button-1>', lambda event, label_name=self.perfil: self.atualiza_header(label_name))
        
        self.tema = ttk.Label(self.header, text='☀', font=('Times New Roman', 18), padding=(50, 50), cursor='hand2')
        self.tema.grid(row=0, column=4)
        self.tema.bind('<Button-1>', self.troca_tema)

        self.actual_header_option = self.inicio
        self.actual_header_option.config(background='')
        self.actual_header_option = self.inicio
        self.inicio.config(background=self.bg_atual)
        
        self.style.configure('Footer.TFrame', background=self.bg_atual)
        self.style.configure('Button.TButton', font=('Times New Roman', 24))
        self.style.configure('Label.TLabel', foreground='white', background='#004AAD')

        self.footer = ttk.Frame(self.janela, style='Footer.TFrame')
        self.footer.pack(side='bottom', fill='x')

        self.footer_label = ttk.Label(self.footer, text='© 2023 Daniel Elias & Erika da Hora', background=self.bg_atual, font=('Times New Roman', 12))
        self.footer_label.pack()
        
        self.main = ttk.Frame(self.janela)
        self.main.pack(expand=True, fill='both')
        
        self.nav = tk.Frame(self.main)
        self.nav.pack(side='top', fill='x')
        self.nav.configure(background='#004AAD')
        
        self.nav_inicio()
        
        self.usuario_logado = ''

    # header
    def atualiza_header(self, seleceted_header_option):

        def muda_estilo():
            self.actual_header_option.config(background='')
            self.actual_header_option = seleceted_header_option
            seleceted_header_option.config(background=self.bg_atual)
            self.limpa_tela(self.nav)
            self.limpa_tela(self.main)

        if seleceted_header_option == self.inicio:
            muda_estilo()
            self.nav_inicio()
        elif seleceted_header_option == self.questoes:
            muda_estilo()
            self.nav_questoes()
        elif seleceted_header_option == self.perfil:
            if self.usuario_logado:
                muda_estilo()
                self.nav_perfil()
                self.main_perfil()
            else:
                self.login()

    # nav
    def nav_inicio(self):
        lbl1 = ttk.Label(self.nav, text='Reduza suas chaces de reprovação.', font=('Times New Roman', 24), style='Label.TLabel')
        lbl1.pack(pady=10)
        lbl2 = ttk.Label(self.nav, text='ESTUDE COM NOSSO BANCO DE QUESTÕES DAS DISCIPLINAS DO CURSO DE SISTEMAS DE INFORMAÇÃO.', font=('Times New Roman', 14), style='Label.TLabel')
        lbl2.pack(pady=10)
        self.nav_inicio_btn = ttk.Button(self.nav, text='Começar', style='Button.TButton', command=self.cadastro)
        self.nav_inicio_btn.pack(pady=10)
    
    def nav_questoes(self):
        lbl = ttk.Label(self.nav, text='Questões', style='Label.TLabel', font=('Times New Roman', 18))
        lbl.grid(padx=100, pady=20)

    def nav_perfil(self):
        lbl = ttk.Label(self.nav, text='Perfil', style='Label.TLabel', font=('Times New Roman', 18))
        lbl.grid(padx=100, pady=20)

    # main
    def main_perfil(self):
        
        def atualizar_senha():
            atual = ent_senha_atual.get()
            nova = ent_nova_senha.get()
            novo = ent_nome.get()
            r = bd.listar(f'SELECT * FROM usuario U WHERE U.id = {self.usuario_logado[0]} AND U.senha = "{atual}";')
            s = bd.listar(f'SELECT * FROM usuario U WHERE U.id != {self.usuario_logado[0]} AND U.nome = "{novo}";')
            if r and not s:
                valida_senha(ent_nova_senha)
                if self.vv1.cget('text') == self.vv2.cget('text') == self.vv3.cget('text') == self.vv4.cget('text') == '✅':
                    bd.atualizar(f'UPDATE usuario SET nome = "{novo}", senha = "{nova}";')
                    messagebox.showinfo('Aviso', 'Dados atualizados com sucesso!', parent=self.janela)
                    t = bd.listar(f'SELECT * FROM usuario U WHERE id = {self.usuario_logado[0]}')
                else:
                    messagebox.showerror('Aviso', 'Senha incorreta!')

        def valida_senha(entry):
            senha = entry.get()
            self.vv1.config(text='✅' if len(senha) >= 8 else '❌')
            self.vv2.config(text='✅' if len([i for i in range(65, 91) if chr(i) in senha]) > 0 else '❌')
            self.vv3.config(text='✅' if len([i for i in senha if not i.isalnum()]) > 0 else '❌')
            self.vv4.config(text='✅' if len([i for i in senha if i.isdigit()]) > 0 else '❌')
        
        self.frm_perfil = ttk.Frame(self.main)
        self.frm_perfil.pack(expand=True, fill='both')
        
        self.frm_perfil.grid_columnconfigure(0, weight=1)
        self.frm_perfil.grid_rowconfigure(0, weight=1)
        
        lbf = tk.LabelFrame(self.frm_perfil, text='Informações Cadastrais', font=('Times New Roman', 18))
        lbf.grid(column=0, row=0, ipadx=20)
        
        lbf.grid_columnconfigure(0, weight=1)
        lbf.grid_rowconfigure(0, weight=1)
        lbf.grid_rowconfigure(1, weight=1)
        lbf.grid_rowconfigure(2, weight=1)
        lbf.grid_rowconfigure(3, weight=1)
        lbf.grid_rowconfigure(4, weight=1)
        
        frm_nome = tk.Frame(lbf)
        frm_nome.grid(row=0, column=0)
        lbl_nome = ttk.Label(frm_nome, text='Nome:', font=('Times New Roman', 14), justify='center')
        lbl_nome.pack()
        ent_nome = ttk.Entry(frm_nome, width=25, font=('Times New Roman', 16), justify='center')
        ent_nome.pack()
        ent_nome.insert('end', self.usuario_logado[1])
        
        frm_senha_atual = tk.Frame(lbf)
        frm_senha_atual.grid(row=1, column=0)
        lbl_senha_atual = ttk.Label(frm_senha_atual, text='Senha atual:', font=('Times New Roman', 14))
        lbl_senha_atual.pack()
        ent_senha_atual = ttk.Entry(frm_senha_atual, width=25, font=('Times New Roman', 16), justify='center', show='*')
        ent_senha_atual.pack()
        
        frm_nova_senha = tk.Frame(lbf)
        frm_nova_senha.grid(row=2, column=0)
        lbl_nova_senha = ttk.Label(frm_nova_senha, text='Nova senha:', font=('Times New Roman', 14))
        lbl_nova_senha.pack()
        ent_nova_senha = ttk.Entry(frm_nova_senha, width=25, font=('Times New Roman', 16), justify='center', show='*')
        ent_nova_senha.pack()
        ent_nova_senha.bind('<KeyRelease>', lambda event, entry=ent_nova_senha: valida_senha(entry))
        
        frm2 = ttk.Frame(lbf)
        frm2.grid(row=3, column=0)
        frmv1 = ttk.Label(frm2)
        frmv1.pack(fill='x', anchor='w')
        self.vv1 = ttk.Label(frmv1, text='❌')
        self.vv1.pack(side='left')
        v1 = ttk.Label(frmv1, text='No mínimo 8 caracteres', font=('Times New Roman', 12))
        v1.pack(side='left')
        
        frmv2 = ttk.Label(frm2)
        frmv2.pack(fill='x', anchor='w')
        self.vv2 = ttk.Label(frmv2, text='❌')
        self.vv2.pack(side='left')
        v2 = ttk.Label(frmv2, text='Uma letra maiúscula', font=('Times New Roman', 12))
        v2.pack(side='left')
        
        frmv3 = ttk.Label(frm2)
        frmv3.pack(fill='x', anchor='w')
        self.vv3 = ttk.Label(frmv3, text='❌')
        self.vv3.pack(side='left')
        v3 = ttk.Label(frmv3, text='Um caracter especial', font=('Times New Roman', 12))
        v3.pack(side='left')
                
        frmv4 = ttk.Label(frm2)
        frmv4.pack(fill='x', anchor='w')
        self.vv4 = ttk.Label(frmv4, text='❌')
        self.vv4.pack(side='left')
        v4 = ttk.Label(frmv4, text='Um número', font=('Times New Roman', 12))
        v4.pack(side='left')
        
        btn = ttk.Button(lbf, text='Atualizar', style='Button.TButton', command=atualizar_senha)
        btn.grid(row=4, column=0)

    # visual
    def troca_tema(self, e):
        estilo_atual = self.style.theme_use()
        if estilo_atual == 'sandstone':
            self.tema.config(text='🌙')
            self.bg_atual = self.bg_light
            self.style.theme_use('darkly')
        else:
            self.tema.config(text='☀')
            self.bg_atual = self.bg_dark
            self.style.theme_use('sandstone')
        self.style.configure('Footer.TFrame', background=self.bg_atual)
        self.style.configure('Button.TButton', font=('Times New Roman', 24))
        self.style.configure('Label.TLabel', foreground='white', background='#004AAD')
        self.footer.config(style='Footer.TFrame')
        self.footer_label.config(background=self.bg_atual)
        self.nav.config(bg='#004AAD')
        self.nav_inicio_btn.config(style='Button.TButton')
        
    def limpa_tela(self, tela):
        for item in tela.winfo_children():
            if item == self.nav: pass
            else: item.destroy()

    # cadastro/login
    def cadastro(self):
        
        self.val_nome = False
        
        def cadastro_login(e):
            self.tvl_cadastro.destroy()
            self.login()
        
        def focus_in(entry):
            if entry == self.ent_nome:
                if self.ent_nome.get() == 'nome de usuario':
                    self.ent_nome.delete(0, 'end')
            elif entry == self.ent_senha:
                if self.ent_senha.get() == 'senha':
                    self.ent_senha.delete(0, 'end')
                    self.ent_senha.configure(show='*')

        def focus_out(entry):
            if entry == self.ent_nome:
                if self.ent_nome.get() == '':
                    self.ent_nome.insert('end', 'nome de usuario')
                else:
                    r = bd.listar(f'SELECT * FROM usuario U WHERE U.nome = "{self.ent_nome.get()}";')
                    if len(r) == 1:
                        if len(frm3.winfo_children()) == 1:
                            self.lbl4 = ttk.Label(frm3, text='Nome de usuário indisponível', font=('Times New Roman', 12))
                            self.lbl4.pack()
                    else:
                        self.val_nome = True
                        try: self.lbl4.destroy()
                        except: pass
            elif entry == self.ent_senha:
                if self.ent_senha.get() == '':
                    self.ent_senha.insert('end', 'senha')
                    self.ent_senha.configure(show='')
        
        def valida_senha(entry):
            senha = entry.get()
            self.vv1.config(text='✅' if len(senha) >= 8 else '❌')
            self.vv2.config(text='✅' if len([i for i in range(65, 91) if chr(i) in senha]) > 0 else '❌')
            self.vv3.config(text='✅' if len([i for i in senha if not i.isalnum()]) > 0 else '❌')
            self.vv4.config(text='✅' if len([i for i in senha if i.isdigit()]) > 0 else '❌')

        def habilitar_botao(e):
            valida_senha(self.ent_senha)
            val_senha = False
            if self.vv1.cget('text') == self.vv2.cget('text') == self.vv3.cget('text') == self.vv4.cget('text') == '✅':
                val_senha = True
            if self.val_nome and val_senha:
                btn_confirmar.config(state='normal')
            else:
                btn_confirmar.config(state='disabled')

        self.tvl_cadastro = tk.Toplevel(self.janela)
        self.tvl_cadastro.title('Crie sua conta')
        self.tvl_cadastro.geometry('500x400')
        self.tvl_cadastro.grab_set()
                
        self.tvl_cadastro.grid_columnconfigure(0, weight=1)
        self.tvl_cadastro.grid_rowconfigure(0, weight=1)
        self.tvl_cadastro.grid_rowconfigure(1, weight=1)
        self.tvl_cadastro.grid_rowconfigure(2, weight=1)
        self.tvl_cadastro.grid_rowconfigure(3, weight=1)
        self.tvl_cadastro.grid_rowconfigure(4, weight=1)
        self.tvl_cadastro.grid_rowconfigure(5, weight=1)
        
        self.imagem2 = Image.open('logo.png')
        self.logo = ImageTk.PhotoImage(self.imagem2)
        self.logo_label = ttk.Label(self.tvl_cadastro, image=self.logo)
        self.logo_label.grid(row=0, column=0)
        
        frm1 = ttk.Frame(self.tvl_cadastro)
        frm1.grid(row=1, column=0)
        
        lbl1 = ttk.Label(frm1, text='Já está cadastrado?', font=('Times New Roman', 16))
        lbl1.pack(side='left')
        lbl2 = ttk.Label(frm1, text='Faça login', foreground='#233dff', cursor='hand2', font=('Times New Roman', 16))
        lbl2.config(underline=6)
        fonte = font.Font(lbl2, lbl2.cget('font'))
        fonte.configure(underline=True)
        lbl2.configure(font=fonte)
        lbl2.bind('<Button-1>', cadastro_login)
        lbl2.pack(side='left')
        
        frm3 = ttk.Frame(self.tvl_cadastro)
        frm3.grid(row=2, column=0)
        self.ent_nome = ttk.Entry(frm3, width=25, font=('Times New Roman', 16), justify='center')
        self.ent_nome.insert('end', 'nome de usuario')
        self.ent_nome.pack()
        self.ent_nome.bind('<FocusIn>', lambda event, entry=self.ent_nome: focus_in(self.ent_nome))
        self.ent_nome.bind('<FocusOut>', lambda event, entry=self.ent_nome: focus_out(self.ent_nome))
        
        self.ent_senha = ttk.Entry(self.tvl_cadastro, width=25, font=('Times New Roman', 16), justify='center')
        self.ent_senha.insert('end', 'senha')
        self.ent_senha.grid(row=3, column=0)
        self.ent_senha.bind('<FocusIn>', lambda event, entry=self.ent_senha: focus_in(entry))
        self.ent_senha.bind('<FocusOut>', lambda event, entry=self.ent_senha: focus_out(entry))
        self.ent_senha.bind('<KeyRelease>', lambda event, entry=self.ent_senha: valida_senha(entry))
    
        frm2 = ttk.Frame(self.tvl_cadastro, style='Frame.TFrame')
        frm2.grid(row=4, column=0)

        frmv1 = ttk.Label(frm2)
        frmv1.pack(fill='x', anchor='w')
        self.vv1 = ttk.Label(frmv1, text='❌')
        self.vv1.pack(side='left')
        v1 = ttk.Label(frmv1, text='No mínimo 8 caracteres', font=('Times New Roman', 12))
        v1.pack(side='left')
        
        frmv2 = ttk.Label(frm2)
        frmv2.pack(fill='x', anchor='w')
        self.vv2 = ttk.Label(frmv2, text='❌')
        self.vv2.pack(side='left')
        v2 = ttk.Label(frmv2, text='Uma letra maiúscula', font=('Times New Roman', 12))
        v2.pack(side='left')
        
        frmv3 = ttk.Label(frm2)
        frmv3.pack(fill='x', anchor='w')
        self.vv3 = ttk.Label(frmv3, text='❌')
        self.vv3.pack(side='left')
        v3 = ttk.Label(frmv3, text='Um caracter especial', font=('Times New Roman', 12))
        v3.pack(side='left')
                
        frmv4 = ttk.Label(frm2)
        frmv4.pack(fill='x', anchor='w')
        self.vv4 = ttk.Label(frmv4, text='❌')
        self.vv4.pack(side='left')
        v4 = ttk.Label(frmv4, text='Um número', font=('Times New Roman', 12))
        v4.pack(side='left')
        
        btn_confirmar = ttk.Button(self.tvl_cadastro, text='Confirmar', style='Button.TButton', command=self.confirmar_cadastro, state='disabled')
        btn_confirmar.grid(row=5, column=0)
        btn_confirmar.bind('<Enter>', habilitar_botao)

    def confirmar_cadastro(self):
        nome = self.ent_nome.get()
        senha = self.ent_senha.get()
        sql_inserir = f"INSERT INTO usuario VALUES (NULL, '{nome}', '{senha}');"
        bd.inserir(sql_inserir)
        messagebox.showinfo('Aviso', 'Usuário cadastrado com sucesso!', parent=self.tvl_cadastro)
        self.tvl_cadastro.destroy()
    
    def login(self):
        
        def login_cadastro(e):
            self.tvl_login.destroy()
            self.cadastro()
        
        def focus_in(entry):
            if entry == self.ent_nome:
                if self.ent_nome.get() == 'nome de usuario':
                    self.ent_nome.delete(0, 'end')
            elif entry == self.ent_senha:
                if self.ent_senha.get() == 'senha':
                    self.ent_senha.delete(0, 'end')
                    self.ent_senha.configure(show='*')
        
        def focus_out(entry):
            if entry == self.ent_nome:
                if self.ent_nome.get() == '':
                    self.ent_nome.insert('end', 'nome de usuario')
            elif entry == self.ent_senha:
                if self.ent_senha.get() == '':
                    self.ent_senha.insert('end', 'senha')
                    self.ent_senha.configure(show='')
        
        self.tvl_login = tk.Toplevel(self.janela)
        self.tvl_login.title('Entre na sua conta')
        self.tvl_login.geometry('500x400')
        self.tvl_login.grab_set()
        
        self.tvl_login.grid_columnconfigure(0, weight=1)
        self.tvl_login.grid_rowconfigure(0, weight=1)
        self.tvl_login.grid_rowconfigure(1, weight=1)
        self.tvl_login.grid_rowconfigure(2, weight=1)
        self.tvl_login.grid_rowconfigure(3, weight=1)
        self.tvl_login.grid_rowconfigure(4, weight=1)
        
        self.imagem3 = Image.open('logo.png')
        self.logo = ImageTk.PhotoImage(self.imagem3)
        self.logo_label = ttk.Label(self.tvl_login, image=self.logo)
        self.logo_label.grid(row=0, column=0)
        
        frm1 = ttk.Frame(self.tvl_login)
        frm1.grid(row=1, column=0)
        lbl1 = ttk.Label(frm1, text='Não possui uma conta?', font=('Times New Roman', 16))
        lbl1.pack(side='left')
        lbl2 = ttk.Label(frm1, text='Cadastre-se', foreground='#233dff', cursor='hand2', font=('Times New Roman', 16))
        lbl2.config(underline=6)
        fonte = font.Font(lbl2, lbl2.cget('font'))
        fonte.configure(underline=True)
        lbl2.configure(font=fonte)
        lbl2.bind('<Button-1>', login_cadastro)
        lbl2.pack(side='left')
        
        self.ent_nome = ttk.Entry(self.tvl_login, width=25, font=('Times New Roman', 16), justify='center')
        self.ent_nome.insert('end', 'nome de usuario')
        self.ent_nome.bind('<FocusIn>', lambda event, entry=self.ent_nome: focus_in(self.ent_nome))
        self.ent_nome.bind('<FocusOut>', lambda event, entry=self.ent_nome: focus_out(self.ent_nome))
        self.ent_nome.grid(row=2, column=0)
        
        self.ent_senha = ttk.Entry(self.tvl_login, width=25, font=('Times New Roman', 16), justify='center')
        self.ent_senha.insert('end', 'senha')
        self.ent_senha.grid(row=3, column=0)
        self.ent_senha.bind('<FocusIn>', lambda event, entry=self.ent_senha: focus_in(entry))
        self.ent_senha.bind('<FocusOut>', lambda event, entry=self.ent_senha: focus_out(entry))
        
        btn_confirmar = ttk.Button(self.tvl_login, text='Confirmar', style='Button.TButton', command=self.confirmar_login)
        btn_confirmar.grid(row=4, column=0)   

    def confirmar_login(self):
        nome = self.ent_nome.get()
        senha = self.ent_senha.get()
        r = bd.listar(f'SELECT * FROM usuario U WHERE U.nome = "{nome}" AND U.senha = "{senha}";')
        if r:
            self.usuario_logado = r[0]
            messagebox.showinfo('Aviso', 'Usuário logado com sucesso!', parent=self.tvl_login)
            self.tvl_login.destroy()
        else:
            r1 = bd.listar(f'SELECT * FROM usuario U WHERE U.nome = "{nome}";')
            if r1:
                messagebox.showerror('Aviso', 'Senha incorreta!', parent=self.tvl_login)
            else:
                messagebox.showerror('Aviso', 'Usuário ou senha incorretos!', parent=self.tvl_login)

app = tk.Tk()
janelaPrincipal = Tela(app)
app.mainloop()