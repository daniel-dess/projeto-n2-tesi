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
        
        seed = ["INSERT INTO usuario VALUES (NULL, 'user123', 'Abc123$%');",
        "INSERT INTO usuario VALUES (NULL, 'johnDoe89', '1234abcd');",
        "INSERT INTO usuario VALUES (NULL, 'emmaSmith45', 'Xyz456&*');",
        "INSERT INTO usuario VALUES (NULL, 'coolCat77', 'PqR789@!');",
        "INSERT INTO usuario VALUES (NULL, 'codingNinja22', 'Def456#*');",
        "INSERT INTO usuario VALUES (NULL, 'soccerFanatic', 'Mno123^%');",
        "INSERT INTO usuario VALUES (NULL, 'musicLover101', 'AbCdEfG1');",
        "INSERT INTO usuario VALUES (NULL, 'bookWorm2020', 'HijKlmN2');",
        "INSERT INTO usuario VALUES (NULL, 'techGeek55', 'OpQrStU3');",
        "INSERT INTO usuario VALUES (NULL, 'beachBum88', 'VwXyZ01@');",
        "INSERT INTO disciplina VALUES (NULL, 'Administração (CCJSA133)');",
        "INSERT INTO disciplina VALUES (NULL, 'Algoritmos e Linguagem de Programação (CCET005)');",
        "INSERT INTO disciplina VALUES (NULL, 'Arquitetura e Organizaçao de Computador (CCET178)');",
        "INSERT INTO disciplina VALUES (NULL, 'Banco de Dados I (CCET023)');",
        "INSERT INTO disciplina VALUES (NULL, 'Comportamento Organizacional (CCJSA134)');",
        "INSERT INTO disciplina VALUES (NULL, 'Comunicação e Redes de Computadores (CCET025');",
        "INSERT INTO disciplina VALUES (NULL, 'Economia e Finanças (CCJSA136)');",
        "INSERT INTO disciplina VALUES (NULL, 'Estrutura de Dados (CCET130)');",
        "INSERT INTO disciplina VALUES (NULL, 'Fundamentos de Sistemas de Informação (CCET143)');",
        "INSERT INTO disciplina VALUES (NULL, 'Informática e Sociedade (CCET197)');",
        "INSERT INTO disciplina VALUES (NULL, 'Inglês Técnico (CELA088)');",
        "INSERT INTO disciplina VALUES (NULL, 'Introdução à Informática (CCET186)');",
        "INSERT INTO disciplina VALUES (NULL, 'Introdução à Pequisa em Sistemas de Informação (CCET105');",
        "INSERT INTO disciplina VALUES (NULL, 'Linguagem de Programação I (CCET114)');",
        "INSERT INTO disciplina VALUES (NULL, 'Linguagem de Programação II (CCET115)');",
        "INSERT INTO disciplina VALUES (NULL, 'Marketing (CCJSA143)');",
        "INSERT INTO disciplina VALUES (NULL, 'Organização, Sistemas e Métodos (CCJSA138)');",
        "INSERT INTO disciplina VALUES (NULL, 'Pesquisa Operacional (CCET020)');",
        "INSERT INTO disciplina VALUES (NULL, 'Psicologia Aplicada (CFCH243');",
        "INSERT INTO disciplina VALUES (NULL, 'Sistemas de Apoio à Decisão (CCET202)');",
        "INSERT INTO disciplina VALUES (NULL, 'Sistemas Operacionais (CCET182)');",
        "INSERT INTO disciplina VALUES (NULL, 'Teoria Geral de Sistemas (CCET090)');",
        "INSERT INTO questao VALUES (NULL, 'O que significa a sigla "+'"'+"CEO"+'"'+"?', 0, 0, 2, 1, '2023-06-26 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que significa a sigla "+'"'+"FAQ"+'"'+"?', 0, 0, 4, 2, '2023-07-17 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que significa a sigla "+'"'+"IT"+'"'+"?', 0, 0, 1, 2, '2023-08-21 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que são Estruturas de Dados?', 0, 0, 1, 3, '2023-08-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que são fake news?', 0, 0, 3, 9, '2023-06-30 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que são fatores motivacionais, de acordo com a teoria de Herzberg?', 0, 0, 2, 8, '2023-08-24 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que são interfaces em programação orientada a objetos?', 0, 0, 4, 2, '2023-08-5 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que são Organização, Sistemas e Métodos (OSM)?', 0, 0, 1, 1, '2023-07-13 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a alfabetização digital?', 0, 0, 1, 1, '2023-08-5 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Análise de Sistemas?', 0, 0, 3, 5, '2023-08-4 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a análise SWOT?', 0, 0, 3, 4, '2023-08-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Arquitetura de Sistemas de Informação?', 0, 0, 4, 7, '2023-07-2 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a arquitetura RISC?', 0, 0, 5, 4, '2023-06-5 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a arquitetura Von Neumann?', 0, 0, 3, 10, '2023-08-26 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a cache de um processador?', 0, 0, 4, 2, '2023-06-21 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a definição clássica de administração?', 0, 0, 1, 3, '2023-08-26 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a forma normal conjuntiva (FNC) em lógica proposicional?', 0, 0, 4, 9, '2023-08-7 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a inflação?', 0, 0, 3, 6, '2023-06-19 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Lei da Oferta e da Procura na economia?', 0, 0, 1, 6, '2023-06-30 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a memória RAM em um computador?', 0, 0, 2, 8, '2023-08-18 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a memória virtual?', 0, 0, 3, 4, '2023-07-20 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a normalização em bancos de dados?', 0, 0, 4, 9, '2023-08-8 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a nuvem (cloud computing) na computação?', 0, 0, 4, 4, '2023-08-18 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a padronização de processos em OSM?', 0, 0, 4, 5, '2023-07-20 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a política monetária?', 0, 0, 5, 5, '2023-08-11 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a retroalimentação (feedback) em um sistema?', 0, 0, 4, 2, '2023-06-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Teoria das Contingências na administração?', 0, 0, 3, 4, '2023-08-8 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Teoria das Filas?', 0, 0, 4, 7, '2023-07-4 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Teoria dos Jogos?', 0, 0, 5, 3, '2023-08-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a Teoria Geral de Sistemas?', 0, 0, 1, 2, '2023-07-17 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é a unidade central de processamento (CPU)?', 0, 0, 1, 3, '2023-06-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é benchmarking em OSM?', 0, 0, 5, 6, '2023-06-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é Comportamento Organizacional?', 0, 0, 1, 8, '2023-06-22 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é encapsulamento em programação orientada a objetos?', 0, 0, 3, 2, '2023-08-19 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é herança em programação orientada a objetos?', 0, 0, 1, 4, '2023-08-11 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é inclusão digital?', 0, 0, 2, 9, '2023-08-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é Mineração de Dados (Data Mining) em um contexto de Sistemas de Apoio à Decisão?', 0, 0, 3, 4, '2023-06-19 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o ciclo de vida do produto?', 0, 0, 4, 4, '2023-06-18 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o ciclo PDCA?', 0, 0, 4, 8, '2023-06-23 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o composto de marketing (ou mix de marketing)?', 0, 0, 2, 4, '2023-06-27 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o conceito de "+'"'+"Benchmarking"+'"'+" na administração?', 0, 0, 5, 8, '2023-06-22 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o conceito de cultura organizacional?', 0, 0, 5, 6, '2023-07-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o conceito de liderança transformacional?', 0, 0, 3, 1, '2023-08-5 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o Marco Civil da Internet no Brasil?', 0, 0, 5, 1, '2023-07-12 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o marketing de relacionamento?', 0, 0, 5, 2, '2023-07-10 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o marketing?', 0, 0, 1, 2, '2023-06-7 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é o PIB (Produto Interno Bruto) em economia?', 0, 0, 2, 3, '2023-07-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é Pesquisa Operacional?', 0, 0, 1, 10, '2023-07-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é polimorfismo em programação orientada a objetos?', 0, 0, 2, 3, '2023-06-14 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é privacidade digital?', 0, 0, 4, 9, '2023-08-22 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é recursão em programação?', 0, 0, 5, 2, '2023-06-5 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é segmentação de mercado?', 0, 0, 3, 3, '2023-08-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um "+'"'+"prototype"+'"'+" em inglês técnico?', 0, 0, 5, 2, '2023-07-25 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um algoritmo de ordenação de complexidade O(n log n)?', 0, 0, 5, 1, '2023-08-20 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um algoritmo?', 0, 0, 1, 4, '2023-07-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um algoritmo?', 0, 0, 3, 7, '2023-06-20 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um array (ou vetor) em programação?', 0, 0, 4, 1, '2023-08-30 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um array em programação?', 0, 0, 4, 2, '2023-08-23 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um banco de dados?', 0, 0, 1, 6, '2023-08-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um conflito funcional em um ambiente organizacional?', 0, 0, 4, 3, '2023-06-8 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um deadlock em sistemas operacionais?', 0, 0, 5, 8, '2023-08-29 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um DNS (Sistema de Nomes de Domínio)?', 0, 0, 5, 2, '2023-06-25 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um dos objetivos principais de uma pesquisa em Sistemas de Informação?', 0, 0, 1, 1, '2023-08-17 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um endereço IP?', 0, 0, 3, 3, '2023-08-30 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um escalonador de processos em um sistema operacional?', 0, 0, 2, 2, '2023-07-22 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um firewall em uma rede de computadores?', 0, 0, 4, 9, '2023-06-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um fluxograma?', 0, 0, 2, 2, '2023-08-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Grafo em Estrutura de Dados?', 0, 0, 5, 4, '2023-08-13 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um instrumento de coleta de dados em uma pesquisa?', 0, 0, 4, 4, '2023-07-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um loop (ou laço) em programação?', 0, 0, 3, 8, '2023-06-7 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um loop em programação?', 0, 0, 3, 8, '2023-06-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um mercado de ações?', 0, 0, 4, 2, '2023-08-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um modelo de simulação?', 0, 0, 3, 9, '2023-06-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um método em programação orientada a objetos?', 0, 0, 5, 2, '2023-08-6 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um método qualitativo de pesquisa em Sistemas de Informação?', 0, 0, 5, 9, '2023-08-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um objetivo específico em uma pesquisa?', 0, 0, 3, 2, '2023-07-13 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um operador lógico?', 0, 0, 1, 3, '2023-06-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um padrão de design em programação?', 0, 0, 5, 9, '2023-08-21 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um problema de programação linear?', 0, 0, 2, 5, '2023-06-1 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um protocolo de comunicação em redes de computadores?', 0, 0, 2, 3, '2023-07-14 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um SGBD (Sistema de Gerenciamento de Banco de Dados)?', 0, 0, 2, 10, '2023-07-13 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um sistema aberto na Teoria Geral de Sistemas?', 0, 0, 3, 8, '2023-07-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema de Apoio à Decisão (SAD)?', 0, 0, 1, 6, '2023-08-10 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um sistema de arquivos em um sistema operacional?', 0, 0, 4, 5, '2023-06-4 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema de Informação Executiva (SIE)?', 0, 0, 5, 8, '2023-07-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema de Informação Geográfica (SIG) em Sistemas de Apoio à Decisão?', 0, 0, 4, 8, '2023-08-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema de Informação Gerencial (SIG)?', 0, 0, 2, 8, '2023-06-9 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema de Informação?', 0, 0, 1, 4, '2023-06-11 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um Sistema Especialista em Sistemas de Apoio à Decisão?', 0, 0, 5, 10, '2023-06-14 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um sistema operacional?', 0, 0, 1, 1, '2023-08-3 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é um sistema operacional?', 0, 0, 2, 2, '2023-06-2 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma "+'"'+"deadline"+'"'+"?', 0, 0, 3, 3, '2023-08-19 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma chave primária em um banco de dados?', 0, 0, 3, 3, '2023-07-2 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma linguagem de programação?', 0, 0, 1, 1, '2023-08-16 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma Lista Encadeada?', 0, 0, 2, 6, '2023-07-7 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma Pilha (Stack) em Estrutura de Dados?', 0, 0, 3, 3, '2023-07-24 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma rede de computadores?', 0, 0, 1, 2, '2023-06-28 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma revisão bibliográfica em uma pesquisa?', 0, 0, 2, 8, '2023-08-10 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma sinergia em um sistema?', 0, 0, 5, 8, '2023-07-6 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma tabela verdade?', 0, 0, 2, 10, '2023-08-4 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma transação em um banco de dados?', 0, 0, 5, 3, '2023-06-20 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma variável em programação?', 0, 0, 2, 4, '2023-06-19 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma variável em programação?', 0, 0, 2, 7, '2023-08-11 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'O que é uma Árvore Binária?', 0, 0, 4, 2, '2023-06-17 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Quais são os principais componentes de um Sistema de Apoio à Decisão?', 0, 0, 2, 3, '2023-06-10 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Qual é a definição básica de informática?', 0, 0, 1, 3, '2023-08-3 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Qual é a lei da absorção em álgebra booleana?', 0, 0, 5, 1, '2023-08-22 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Qual é a negação da afirmação "+'"'+"P AND Q"+'"'+"?', 0, 0, 3, 10, '2023-06-13 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Qual é uma das funções básicas da administração de acordo com Fayol?', 0, 0, 2, 9, '2023-08-10 00:00:00');",
        "INSERT INTO questao VALUES (NULL, 'Quem é considerado o fundador da Teoria Geral de Sistemas?', 0, 0, 2, 9, '2023-08-26 00:00:00');",
        "INSERT INTO alternativa VALUES (NULL, '(P∧Q)∨(¬P∧Q)=Q(P \land Q) \lor (\lnot P \land Q) = Q(P∧Q)∨(¬P∧Q)=Q', 0, 10);",
        "INSERT INTO alternativa VALUES (NULL, '(P∨Q)∧(¬P∨Q)=Q(P \lor Q) \land (\lnot P \lor Q) = Q(P∨Q)∧(¬P∨Q)=Q', 0, 10);",
        "INSERT INTO alternativa VALUES (NULL, 'A arte de atingir objetivos por meio de pessoas', 1, 11);",
        "INSERT INTO alternativa VALUES (NULL, 'A atividade de controlar recursos humanos', 0, 11);",
        "INSERT INTO alternativa VALUES (NULL, 'A automação completa de todos os processos', 0, 69);",
        "INSERT INTO alternativa VALUES (NULL, 'A capacidade de desmontar e montar computadores', 0, 91);",
        "INSERT INTO alternativa VALUES (NULL, 'A capacidade de uma classe ter múltiplos métodos com o mesmo nome, mas com diferentes implementações', 1, 72);",
        "INSERT INTO alternativa VALUES (NULL, 'A capacidade de usar tecnologia de forma eficaz e responsável para comunicar, acessar informações e realizar tarefas', 1, 91);",
        "INSERT INTO alternativa VALUES (NULL, 'A crença de que os recursos humanos são a única preocupação da administração', 0, 13);",
        "INSERT INTO alternativa VALUES (NULL, 'A criação de procedimentos e métodos uniformes para a execução de tarefas', 1, 69);",
        "INSERT INTO alternativa VALUES (NULL, 'A data limite para a conclusão de uma tarefa', 1, 18);",
        "INSERT INTO alternativa VALUES (NULL, 'A definição do preço de um produto baseado na concorrência', 0, 63);",
        "INSERT INTO alternativa VALUES (NULL, 'A definição do problema de pesquisa', 0, 33);",
        "INSERT INTO alternativa VALUES (NULL, 'A divisão do mercado em grupos distintos de consumidores com necessidades e características similares', 1, 63);",
        "INSERT INTO alternativa VALUES (NULL, 'A duração média de vida útil de um produto eletrônico', 0, 64);",
        "INSERT INTO alternativa VALUES (NULL, 'A eliminação de processos desnecessários em uma organização', 0, 69);",
        "INSERT INTO alternativa VALUES (NULL, 'A estratégia de aumentar os preços de produtos sazonais', 0, 65);",
        "INSERT INTO alternativa VALUES (NULL, 'A estratégia de marketing para atrair clientes', 0, 15);",
        "INSERT INTO alternativa VALUES (NULL, 'A estratégia de marketing para lançar um novo produto', 0, 63);",
        "INSERT INTO alternativa VALUES (NULL, 'A etapa final do processo de pesquisa', 0, 34);",
        "INSERT INTO alternativa VALUES (NULL, 'A habilidade de fazer cálculos complexos sem o uso de calculadoras', 0, 91);",
        "INSERT INTO alternativa VALUES (NULL, 'A habilidade de ler e escrever em um idioma estrangeiro', 0, 91);",
        "INSERT INTO alternativa VALUES (NULL, 'A ideia de que a administração é uma atividade puramente técnica', 0, 13);",
        "INSERT INTO alternativa VALUES (NULL, 'A ideia de que não existe uma única forma correta de administrar, e que a eficácia da administração depende do contexto', 1, 13);",
        "INSERT INTO alternativa VALUES (NULL, 'A memória temporária utilizada para armazenar dados e instruções durante a execução do programa', 1, 47);",
        "INSERT INTO alternativa VALUES (NULL, 'A prática de comparar os processos e desempenho da organização com os líderes do setor', 1, 15);",
        "INSERT INTO alternativa VALUES (NULL, 'A prática de comparar os processos e desempenho da organização com os líderes do setor', 1, 70);",
        "INSERT INTO alternativa VALUES (NULL, 'A prática de compartilhar senhas de acesso a sistemas', 0, 92);",
        "INSERT INTO alternativa VALUES (NULL, 'A prática de guardar grandes quantidades de dados sem analisá-los', 0, 88);",
        "INSERT INTO alternativa VALUES (NULL, 'A quantidade de dinheiro que um país deve a outros países', 0, 52);",
        "INSERT INTO alternativa VALUES (NULL, 'A redução da taxa de desemprego em uma economia', 0, 53);",
        "INSERT INTO alternativa VALUES (NULL, 'A relação entre a quantidade de um bem que os produtores estão dispostos a oferecer e a quantidade que os consumidores estão dispostos a comprar a um determinado preço', 1, 51);",
        "INSERT INTO alternativa VALUES (NULL, 'A relação entre a taxa de inflação e o crescimento econômico', 0, 51);",
        "INSERT INTO alternativa VALUES (NULL, 'A reorganização constante dos procedimentos operacionais', 0, 69);",
        "INSERT INTO alternativa VALUES (NULL, 'A revisão final antes da publicação', 0, 33);",
        "INSERT INTO alternativa VALUES (NULL, 'A soma de todos os bens e serviços produzidos em um país em um determinado período de tempo', 1, 52);",
        "INSERT INTO alternativa VALUES (NULL, 'A soma total de todas as atividades de marketing em uma organização', 0, 62);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de câmbio entre duas moedas', 0, 51);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de câmbio entre duas moedas', 0, 55);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de inflação anual', 0, 52);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de juros aplicada a empréstimos', 0, 53);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de juros de mercado', 0, 55);",
        "INSERT INTO alternativa VALUES (NULL, 'A taxa de juros definida pelo banco central', 0, 51);",
        "INSERT INTO alternativa VALUES (NULL, 'A teoria de que a administração deve se concentrar apenas em aspectos financeiros', 0, 13);",
        "INSERT INTO alternativa VALUES (NULL, 'A técnica de codificação de dados', 0, 88);",
        "INSERT INTO alternativa VALUES (NULL, 'A técnica de produção de bens e serviços', 0, 11);",
        "INSERT INTO alternativa VALUES (NULL, 'A unidade de saída de um computador', 0, 46);",
        "INSERT INTO alternativa VALUES (NULL, 'Adquirir habilidades de programação', 0, 31);",
        "INSERT INTO alternativa VALUES (NULL, 'Albert Einstein', 0, 27);",
        "INSERT INTO alternativa VALUES (NULL, 'As fases pelas quais um produto passa desde a introdução no mercado até a sua retirada', 1, 64);",
        "INSERT INTO alternativa VALUES (NULL, 'As ferramentas e estratégias utilizadas para promover um produto ou serviço', 0, 62);",
        "INSERT INTO alternativa VALUES (NULL, 'As ferramentas ou técnicas utilizadas para obter informações relevantes para a pesquisa', 1, 34);",
        "INSERT INTO alternativa VALUES (NULL, 'As quatro principais variáveis controláveis de marketing: produto, preço, praça (distribuição) e promoção', 1, 62);",
        "INSERT INTO alternativa VALUES (NULL, 'Base de dados, software de processamento de texto e hardware', 0, 87);",
        "INSERT INTO alternativa VALUES (NULL, 'Bubble Sort', 0, 5);",
        "INSERT INTO alternativa VALUES (NULL, 'Charles Darwin', 0, 27);",
        "INSERT INTO alternativa VALUES (NULL, 'Chief Engineering Officer', 0, 17);",
        "INSERT INTO alternativa VALUES (NULL, 'Chief Executive Officer', 1, 17);",
        "INSERT INTO alternativa VALUES (NULL, 'Conduzir análises de dados complexas', 0, 31);",
        "INSERT INTO alternativa VALUES (NULL, 'Corporate Education Officer', 0, 17);",
        "INSERT INTO alternativa VALUES (NULL, 'Creative and Efficient Organizer', 0, 17);",
        "INSERT INTO alternativa VALUES (NULL, 'Dados, modelos analíticos, interface do usuário e software de suporte à decisão', 1, 87);",
        "INSERT INTO alternativa VALUES (NULL, 'Desenvolver um novo software', 0, 31);",
        "INSERT INTO alternativa VALUES (NULL, 'Design', 0, 12);",
        "INSERT INTO alternativa VALUES (NULL, 'Fast Access Quota', 0, 19);",
        "INSERT INTO alternativa VALUES (NULL, 'Fatores que causam insatisfação se ausentes, mas não necessariamente satisfação se presentes', 1, 37);",
        "INSERT INTO alternativa VALUES (NULL, 'Fatores que sempre causam satisfação quando presentes', 0, 37);",
        "INSERT INTO alternativa VALUES (NULL, 'Fatores relacionados ao ambiente de trabalho', 0, 37);",
        "INSERT INTO alternativa VALUES (NULL, 'Fatores relacionados ao salário', 0, 37);",
        "INSERT INTO alternativa VALUES (NULL, 'Final Approval Qualification', 0, 19);",
        "INSERT INTO alternativa VALUES (NULL, 'Formal Assessment Query', 0, 19);",
        "INSERT INTO alternativa VALUES (NULL, 'Formas de representar, organizar e manipular dados para realizar operações específicas', 1, 76);",
        "INSERT INTO alternativa VALUES (NULL, 'Formas físicas de dados em um banco de dados', 0, 76);",
        "INSERT INTO alternativa VALUES (NULL, 'Frequently Asked Questions', 1, 19);",
        "INSERT INTO alternativa VALUES (NULL, 'Gerar conhecimento e compreensão sobre temas relacionados à área de Sistemas de Informação', 1, 31);",
        "INSERT INTO alternativa VALUES (NULL, 'Industrial Tool', 0, 16);",
        "INSERT INTO alternativa VALUES (NULL, 'Information Technology', 1, 16);",
        "INSERT INTO alternativa VALUES (NULL, 'Insertion Sort', 0, 5);",
        "INSERT INTO alternativa VALUES (NULL, 'International Travel', 0, 16);",
        "INSERT INTO alternativa VALUES (NULL, 'Interpersonal Training', 0, 16);",
        "INSERT INTO alternativa VALUES (NULL, 'Isaac Newton', 0, 27);",
        "INSERT INTO alternativa VALUES (NULL, 'Jornais impressos com baixa circulação', 0, 93);",
        "INSERT INTO alternativa VALUES (NULL, 'Ludwig von Bertalanffy', 1, 27);",
        "INSERT INTO alternativa VALUES (NULL, 'Marketing', 0, 12);",
        "INSERT INTO alternativa VALUES (NULL, 'NOT P AND NOT Q', 1, 8);",
        "INSERT INTO alternativa VALUES (NULL, 'NOT P AND Q', 0, 8);",
        "INSERT INTO alternativa VALUES (NULL, 'NOT P OR NOT Q', 0, 8);",
        "INSERT INTO alternativa VALUES (NULL, 'Notícias falsas ou desinformação que são apresentadas como informações reais', 1, 93);",
        "INSERT INTO alternativa VALUES (NULL, 'O aumento geral e sustentado no nível de preços de bens e serviços em uma economia', 1, 53);",
        "INSERT INTO alternativa VALUES (NULL, 'O componente que executa instruções e realiza operações lógicas e aritméticas', 1, 46);",
        "INSERT INTO alternativa VALUES (NULL, 'O componente responsável pela entrada e saída de dados', 0, 47);",
        "INSERT INTO alternativa VALUES (NULL, 'O conceito de esconder os detalhes de implementação de um objeto e expor apenas a interface', 1, 73);",
        "INSERT INTO alternativa VALUES (NULL, 'O conjunto de atividades para criar, comunicar, entregar e trocar ofertas que tenham valor para os clientes, parceiros e a sociedade em geral', 1, 61);",
        "INSERT INTO alternativa VALUES (NULL, 'O controle da oferta de dinheiro e das taxas de juros pelo banco central para influenciar a economia', 1, 55);",
        "INSERT INTO alternativa VALUES (NULL, 'O controle de preços de bens e serviços pelo governo', 0, 55);",
        "INSERT INTO alternativa VALUES (NULL, 'O cálculo do retorno sobre o investimento', 0, 15);",
        "INSERT INTO alternativa VALUES (NULL, 'O declínio do PIB em um período de recessão', 0, 53);",
        "INSERT INTO alternativa VALUES (NULL, 'O departamento responsável pelo gerenciamento de recursos humanos', 0, 61);",
        "INSERT INTO alternativa VALUES (NULL, 'O direito de manter a segurança de informações pessoais e atividades online', 1, 94);",
        "INSERT INTO alternativa VALUES (NULL, 'O dispositivo de armazenamento permanente de dados', 0, 46);",
        "INSERT INTO alternativa VALUES (NULL, 'O dispositivo de entrada primária de um computador', 0, 46);",
        "INSERT INTO alternativa VALUES (NULL, 'O esforço para garantir que todos tenham acesso e habilidades para usar tecnologia da informação', 1, 92);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo das estrelas', 0, 1);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo das estruturas físicas de uma organização', 0, 36);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo das interações humanas em uma organização', 1, 36);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo das plantas', 0, 1);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo do processamento de dados e informação', 1, 1);",
        "INSERT INTO alternativa VALUES (NULL, 'O estudo dos insetos', 0, 1);",
        "INSERT INTO alternativa VALUES (NULL, 'O gerenciamento financeiro de uma organização', 0, 36);",
        "INSERT INTO alternativa VALUES (NULL, 'O orçamento alocado para a equipe de marketing', 0, 62);",
        "INSERT INTO alternativa VALUES (NULL, 'O período de garantia oferecido pelo fabricante', 0, 64);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de adicionar novos recursos a um software', 0, 92);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de avaliar o desempenho das equipes de vendas', 0, 65);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de contabilidade de uma organização', 0, 11);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de criar cópias de segurança de dados', 0, 92);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de descobrir informações úteis a partir de grandes conjuntos de dados', 1, 88);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de elaboração do questionário', 0, 34);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de escolha do melhor local para abrir uma loja', 0, 63);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de marketing de uma organização', 0, 36);",
        "INSERT INTO alternativa VALUES (NULL, 'O processo de venda de produtos a preços baixos', 0, 61);",
        "INSERT INTO alternativa VALUES (NULL, 'O programa de computador utilizado na análise estatística', 0, 34);",
        "INSERT INTO alternativa VALUES (NULL, 'O resultado da interação de componentes que produz um efeito maior do que a soma das partes individuais', 1, 30);",
        "INSERT INTO alternativa VALUES (NULL, 'O tempo que um produto permanece no mercado', 0, 64);",
        "INSERT INTO alternativa VALUES (NULL, 'O termo técnico para a velocidade da conexão de internet', 0, 94);",
        "INSERT INTO alternativa VALUES (NULL, 'O total de dinheiro em circulação em uma economia', 0, 52);",
        "INSERT INTO alternativa VALUES (NULL, 'P OR Q', 0, 8);",
        "INSERT INTO alternativa VALUES (NULL, 'Pesquisa e Desenvolvimento', 0, 12);",
        "INSERT INTO alternativa VALUES (NULL, 'Planejamento', 1, 12);",
        "INSERT INTO alternativa VALUES (NULL, 'P∧(P∨Q)=PP \land (P \lor Q) = PP∧(P∨Q)=P', 0, 10);",
        "INSERT INTO alternativa VALUES (NULL, 'P∨(P∧Q)=PP \lor (P \land Q) = PP∨(P∧Q)=P', 1, 10);",
        "INSERT INTO alternativa VALUES (NULL, 'Quick Sort', 1, 5);",
        "INSERT INTO alternativa VALUES (NULL, 'Selection Sort', 0, 5);",
        "INSERT INTO alternativa VALUES (NULL, 'Tipos de linguagens de programação', 0, 76);",
        "INSERT INTO alternativa VALUES (NULL, 'Um atributo que identifica de forma única cada registro em uma tabela', 1, 98);",
        "INSERT INTO alternativa VALUES (NULL, 'Um bloco de código que realiza uma tarefa específica e pode ser chamado por um objeto', 1, 45);",
        "INSERT INTO alternativa VALUES (NULL, 'Um comando para encerrar um programa', 0, 23);",
        "INSERT INTO alternativa VALUES (NULL, 'Um comando para encerrar um programa', 0, 43);",
        "INSERT INTO alternativa VALUES (NULL, 'Um componente que gerencia a execução de diferentes programas e decide qual será executado em determinado momento', 1, 82);",
        "INSERT INTO alternativa VALUES (NULL, 'Um componente responsável pela leitura de CDs e DVDs', 0, 49);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conceito matemático avançado', 0, 30);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conceito que permite que uma classe herde os atributos e métodos de outra classe', 1, 71);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de aplicativos de escritório', 0, 81);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de dispositivos de armazenamento de dados', 0, 56);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de palavras e frases em inglês', 0, 41);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de passos para resolver um problema', 1, 21);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de procedimentos para instalar um novo software', 0, 106);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de programas que controla o hardware e permite a execução de outros softwares', 1, 2);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de regras que define como os dados são transmitidos entre dispositivos em uma rede', 1, 107);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de regras que determina como os arquivos são armazenados e organizados em um dispositivo de armazenamento', 1, 84);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto de símbolos que realizam operações em valores lógicos', 1, 6);",
        "INSERT INTO alternativa VALUES (NULL, 'Um conjunto organizado de pessoas, hardware, software, redes e recursos de dados que coletam, transformam e disseminam informações em uma organização', 1, 56);",
        "INSERT INTO alternativa VALUES (NULL, 'Um contrato que define um conjunto de métodos que uma classe deve implementar', 1, 74);",
        "INSERT INTO alternativa VALUES (NULL, 'Um departamento que lida exclusivamente com tecnologia da informação', 0, 66);",
        "INSERT INTO alternativa VALUES (NULL, 'Um dispositivo de armazenamento físico', 0, 96);",
        "INSERT INTO alternativa VALUES (NULL, 'Um dispositivo de entrada e saída', 0, 2);",
        "INSERT INTO alternativa VALUES (NULL, 'Um dispositivo de entrada e saída', 0, 4);",
        "INSERT INTO alternativa VALUES (NULL, 'Um dispositivo de entrada e saída', 0, 6);",
        "INSERT INTO alternativa VALUES (NULL, 'Um estilo de liderança autoritária', 0, 38);",
        "INSERT INTO alternativa VALUES (NULL, 'Um estilo de liderança que inspira e motiva os membros da equipe a atingirem seu melhor potencial', 1, 38);",
        "INSERT INTO alternativa VALUES (NULL, 'Um grupo de computadores conectados fisicamente uns aos outros', 1, 106);",
        "INSERT INTO alternativa VALUES (NULL, 'Um identificador único atribuído a cada dispositivo em uma rede IP', 1, 108);",
        "INSERT INTO alternativa VALUES (NULL, 'Um local na memória para armazenar dados que podem mudar durante a execução do programa', 1, 42);",
        "INSERT INTO alternativa VALUES (NULL, 'Um local na memória para armazenar dados', 1, 22);",
        "INSERT INTO alternativa VALUES (NULL, 'Um meio de comunicação entre humanos e computadores para escrever algoritmos', 1, 41);",
        "INSERT INTO alternativa VALUES (NULL, 'Um mercado onde a propriedade de empresas é comprada e vendida', 1, 54);",
        "INSERT INTO alternativa VALUES (NULL, 'Um mercado onde commodities são compradas e vendidas', 0, 54);",
        "INSERT INTO alternativa VALUES (NULL, 'Um mercado onde moedas estrangeiras são trocadas', 0, 54);",
        "INSERT INTO alternativa VALUES (NULL, 'Um mercado onde títulos de dívida são negociados', 0, 54);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de computador que armazena dados em cartões perfurados', 0, 48);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de computador que usa instruções de linguagem natural', 0, 48);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de computador que utiliza instruções complexas', 0, 50);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de computador que utiliza memória separada para dados e instruções', 1, 48);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de estrutura de capital', 0, 68);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de estrutura de mercado', 0, 40);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de estrutura organizacional', 0, 38);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de estrutura organizacional', 0, 66);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de fluxograma complexo', 0, 70);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de gestão que significa Planejar, Desenvolver, Controlar e Ajustar', 1, 14);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de negócio de uma organização', 0, 59);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo de produção em massa', 0, 14);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo inicial de um produto ou sistema', 1, 20);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo matemático para resolver equações complexas', 0, 26);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo que descreve como os componentes de um sistema de informação interagem', 1, 59);",
        "INSERT INTO alternativa VALUES (NULL, 'Um modelo que utiliza múltiplos processadores para executar tarefas simultaneamente', 0, 48);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de coleta de dados', 0, 101);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de criptografia de dados', 0, 75);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de criptografia de mensagens', 0, 41);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de marketing', 0, 14);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de otimização de código', 0, 71);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de otimização de código', 0, 73);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de otimização de processos', 0, 105);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de precificação de produtos', 0, 15);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método de programação de computadores', 0, 26);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método estatístico de análise de dados', 0, 20);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método estatístico de previsão', 0, 103);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método estatístico para analisar dados', 0, 104);",
        "INSERT INTO alternativa VALUES (NULL, 'Um método estatístico para avaliar a satisfação do cliente', 0, 68);",
        "INSERT INTO alternativa VALUES (NULL, 'Um número de telefone específico para computadores', 0, 108);",
        "INSERT INTO alternativa VALUES (NULL, 'Um padrão de codificação', 0, 20);",
        "INSERT INTO alternativa VALUES (NULL, 'Um problema de otimização onde se busca maximizar ou minimizar uma função linear sujeita a restrições lineares', 1, 102);",
        "INSERT INTO alternativa VALUES (NULL, 'Um processo de identificação, modelagem e solução de problemas de informação', 1, 58);",
        "INSERT INTO alternativa VALUES (NULL, 'Um processo de organização de dados em tabelas para reduzir a redundância e a inconsistência', 1, 99);",
        "INSERT INTO alternativa VALUES (NULL, 'Um processo de recuperação de dados perdidos', 0, 58);",
        "INSERT INTO alternativa VALUES (NULL, 'Um processo pelo qual o sistema recebe e responde a informações sobre seu próprio desempenho', 1, 29);",
        "INSERT INTO alternativa VALUES (NULL, 'Um programa de edição de texto', 0, 2);",
        "INSERT INTO alternativa VALUES (NULL, 'Um programa para editar imagens', 0, 82);",
        "INSERT INTO alternativa VALUES (NULL, 'Um programa que controla o hardware e atua como intermediário entre o usuário e o computador', 1, 81);",
        "INSERT INTO alternativa VALUES (NULL, 'Um protocolo de comunicação de rede', 0, 100);",
        "INSERT INTO alternativa VALUES (NULL, 'Um protocolo de comunicação entre servidores de banco de dados', 0, 99);",
        "INSERT INTO alternativa VALUES (NULL, 'Um protocolo de comunicação para redes sem fio', 0, 109);",
        "INSERT INTO alternativa VALUES (NULL, 'Um protocolo de comunicação utilizado para a transmissão de dados em redes locais', 0, 95);",
        "INSERT INTO alternativa VALUES (NULL, 'Um protocolo de segurança para acesso à internet', 0, 107);",
        "INSERT INTO alternativa VALUES (NULL, 'Um ramo da pesquisa operacional que estuda o comportamento de sistemas onde entidades aguardam por um serviço', 1, 104);",
        "INSERT INTO alternativa VALUES (NULL, 'Um ramo da pesquisa operacional que trata de situações de tomada de decisão estratégica', 1, 105);",
        "INSERT INTO alternativa VALUES (NULL, 'Um resumo do artigo científico', 0, 33);",
        "INSERT INTO alternativa VALUES (NULL, 'Um servidor web, navegador de internet e banco de dados', 0, 87);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema de armazenamento e processamento de dados online', 1, 4);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema de segurança avançado para proteger informações sensíveis', 0, 60);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema de segurança para proteger informações confidenciais', 0, 57);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que ajuda a gerência no processo de tomada de decisão', 1, 57);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que automatiza a produção de relatórios financeiros', 0, 57);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que automatiza processos de produção', 0, 60);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que controla o acesso à internet', 0, 57);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que fornece informações de resumo e tendências para tomadores de decisão de alto nível', 1, 60);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que fornece informações detalhadas para tomadores de decisão de nível operacional', 0, 60);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que fornece suporte para a tomada de decisões ao disponibilizar informações e ferramentas para análise', 1, 86);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que gerencia informações financeiras', 0, 89);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que integra dados espaciais para análise e tomada de decisões', 1, 89);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que interage com o ambiente externo e troca energia e informação com ele', 1, 28);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que não interage com o ambiente externo', 0, 28);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que não possui componentes', 0, 28);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que só funciona em condições específicas de temperatura', 0, 28);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que traduz nomes de domínio legíveis por humanos em endereços IP', 1, 110);",
        "INSERT INTO alternativa VALUES (NULL, 'Um sistema que utiliza inteligência artificial para fornecer recomendações ou soluções em um domínio específico', 1, 90);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software antivírus', 0, 82);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software de design gráfico', 0, 67);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software de edição de vídeo', 0, 84);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software de edição de vídeo', 0, 90);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software de gerenciamento de projetos', 0, 101);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software que automatiza a tomada de decisões para os gestores', 0, 86);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software que permite a criação, manipulação e gerenciamento de bancos de dados', 1, 97);",
        "INSERT INTO alternativa VALUES (NULL, 'Um software que permite aos usuários navegar na internet', 0, 81);",
        "INSERT INTO alternativa VALUES (NULL, 'Um termo usado em programação de computadores', 0, 18);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de compressão de dados', 0, 110);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação avançado', 0, 105);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação avançado', 0, 90);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 103);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 25);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 26);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 29);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 75);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 76);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de algoritmo de ordenação', 0, 79);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de análise estatística', 0, 30);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de armazenamento de dados de longo prazo', 0, 47);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de backup de dados', 0, 100);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de banco de dados', 0, 67);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de banco de dados', 0, 7);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de conflito que ocorre apenas entre membros da alta administração', 0, 39);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de conflito que é benéfico e estimula a inovação e a criatividade', 1, 39);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de conflito que é prejudicial e deve ser evitado', 0, 39);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de conflito relacionado à hierarquia organizacional', 0, 39);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de consulta complexa em SQL', 0, 100);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de consulta SQL', 0, 98);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de criptografia avançada', 0, 102);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de criptografia avançada', 0, 94);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de criptografia de dados', 0, 99);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de dado numérico', 0, 43);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de dado numérico', 0, 45);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de dado numérico', 0, 74);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de dado', 0, 23);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de equipamento de escritório', 0, 18);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de erro de compilação', 0, 72);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de erro no código', 0, 25);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de erro no código', 0, 71);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de impressora de alta resolução', 0, 4);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação avançada', 0, 59);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 104);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 106);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 110);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 3);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 56);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 6);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 73);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 81);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 89);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 9);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de linguagem de programação', 0, 94);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de loop especial', 0, 24);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de loop especial', 0, 45);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de loop especial', 0, 74);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de loop', 0, 42);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de loop', 0, 72);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de memória flash', 0, 83);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de monitor de computador', 0, 4);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de operador lógico', 0, 22);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de ordenação de dados', 0, 78);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de ordenação de dados', 0, 80);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de pesquisa de mercado', 0, 101);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de pesquisa de mercado', 0, 61);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de processador gráfico', 0, 49);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de programa antivírus', 0, 58);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de programa de computador', 0, 102);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de programação de computadores', 0, 35);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de servidor de internet', 0, 97);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de sistema de navegação na internet', 0, 84);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de sistema de segurança cibernética', 0, 93);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de sistema operacional', 0, 41);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software antivírus', 0, 107);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software antivírus', 0, 85);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de design gráfico', 0, 109);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de design gráfico', 0, 20);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de design gráfico', 0, 21);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de edição de texto', 0, 108);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de edição de texto', 0, 96);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de gerenciamento de projetos', 0, 66);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de gerenciamento de projetos', 0, 70);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de gerenciamento de projetos', 0, 86);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de gerenciamento de projetos', 0, 88);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de software de gestão', 0, 40);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de tecnologia de informação', 0, 38);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de vírus de computador', 0, 2);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de vírus de computador', 0, 3);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de vírus de computador', 0, 6);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tipo de índice de busca', 0, 98);",
        "INSERT INTO alternativa VALUES (NULL, 'Um tratado internacional sobre comércio eletrônico', 0, 95);",
        "INSERT INTO alternativa VALUES (NULL, 'Um valor constante que não pode ser alterado', 0, 22);",
        "INSERT INTO alternativa VALUES (NULL, 'Um valor constante que não pode ser alterado', 0, 42);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem de design de produtos', 0, 14);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem de design de software', 0, 50);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem interdisciplinar para estudar e entender sistemas', 1, 26);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem que se baseia em observações, entrevistas e análise de conteúdo', 1, 35);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem que se concentra em dados numéricos e análises estatísticas', 0, 35);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma abordagem que se concentra em manter e fortalecer os relacionamentos com os clientes existentes', 1, 65);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma análise detalhada de fontes de informação relevantes sobre o tema da pesquisa', 1, 32);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma análise estatística avançada', 0, 32);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma arquitetura de conjunto de instruções reduzido que enfatiza a simplicidade e a execução rápida de instruções', 1, 50);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma barreira de segurança que controla o tráfego entre uma rede privada e a internet', 1, 109);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma coleção de elementos não ordenados', 0, 77);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma coleção de elementos organizados em pares', 0, 78);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma coleção de elementos organizados em pares', 0, 80);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma coleção organizada de dados', 1, 96);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma declaração clara e mensurável do que o pesquisador pretende alcançar com a pesquisa', 1, 33);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma disciplina que estuda e otimiza os processos de uma organização', 1, 66);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma disciplina que utiliza técnicas matemáticas e estatísticas para apoiar a tomada de decisões em situações complexas', 1, 101);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma entrevista com especialistas na área', 0, 32);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estratégia de marketing voltada apenas para novos clientes', 0, 65);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de controle que permite a repetição de um bloco de código', 1, 23);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de controle que permite a repetição de um bloco de código', 1, 43);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados linear onde os elementos são armazenados de forma não contígua e cada um aponta para o próximo', 1, 77);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados onde cada nó pode ter no máximo dois filhos', 1, 79);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados onde os elementos são organizados em pares', 0, 77);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados que armazena elementos do mesmo tipo', 1, 24);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados que armazena elementos do mesmo tipo', 1, 44);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados que representa relações entre diferentes elementos', 1, 80);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma estrutura de dados que segue o princípio "+'"'+"primeiro a entrar, último a sair"+'"'+" (LIFO)', 1, 78);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma etapa onde são coletados dados primários', 0, 32);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma ferramenta de backup de dados', 0, 82);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma ferramenta para programação de computadores', 0, 68);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma avançada de tecnologia de realidade aumentada', 0, 93);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de armazenar dados em nuvem', 0, 106);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de backup de dados', 0, 98);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de compactar arquivos', 0, 84);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de compartilhar arquivos pela internet', 0, 83);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de comunicação de dados', 0, 89);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de criptografia de dados', 0, 71);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de criptografia de dados', 0, 90);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de escrever expressões lógicas usando apenas operadores AND e OR', 1, 9);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de medir a eficiência de um sistema', 0, 29);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de organizar algoritmos', 0, 24);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de organizar algoritmos', 0, 44);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de organizar dados em um banco de dados', 0, 108);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de organizar dados em uma planilha', 0, 77);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de organizar dados em uma tabela', 0, 79);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de otimizar o desempenho do sistema', 0, 85);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de representar dados em gráficos', 0, 78);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de representar dados em gráficos', 0, 80);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de retroalimentação negativa', 0, 30);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma forma de simplificar expressões lógicas complexas', 0, 9);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática avançada', 0, 24);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática avançada', 0, 44);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática complexa', 0, 23);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática complexa', 0, 43);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática', 0, 22);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma função matemática', 0, 42);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma lei que estabelece princípios, garantias, direitos e deveres para o uso da internet no país', 1, 95);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma linguagem de programação de alto nível', 0, 25);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma linguagem de programação popular', 0, 21);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma linguagem de programação', 0, 97);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma linha imaginária em um projeto', 0, 18);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma lista de operadores lógicos', 0, 7);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma lista de tabelas de multiplicação', 0, 7);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma memória de alta velocidade que armazena cópias frequentemente usadas de dados da memória principal', 1, 49);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma operação que altera o estado de um banco de dados, como inserção, atualização ou exclusão de registros', 1, 100);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma organização sem fins lucrativos dedicada ao desenvolvimento de software de código aberto', 0, 95);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma planilha de Excel', 0, 96);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma receita de cozinha', 0, 21);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma rede de computadores conectada à internet', 0, 56);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma rede de computadores e um sistema operacional', 0, 87);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma representação gráfica de um processo que mostra as etapas sequenciais e as interações entre elas', 1, 67);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma representação simplificada de um sistema real que é usado para estudar e analisar seu comportamento', 1, 103);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma situação em que dois ou mais processos estão incapazes de continuar a execução porque cada um está aguardando um recurso que o outro está utilizando', 1, 85);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma solução geral e reutilizável para um problema comum no desenvolvimento de software', 1, 75);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma série de instruções para realizar uma tarefa específica', 1, 3);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma tabela que mostra todas as combinações possíveis de valores lógicos para uma expressão', 1, 7);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de análise de dados', 0, 102);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de análise de dados', 0, 110);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de análise estatística', 0, 70);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de codificação de dados', 0, 72);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de compressão de arquivos', 0, 99);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia avançada', 0, 73);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia avançada', 0, 79);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia de dados', 0, 105);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia de dados', 0, 107);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia de dados', 0, 83);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de criptografia', 0, 44);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de design de sistemas', 0, 35);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de entrevista de emprego', 0, 67);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de gerenciamento de projetos', 0, 104);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de otimização de banco de dados', 0, 59);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de otimização de banco de dados', 0, 86);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de otimização de dados', 0, 109);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de otimização de dados', 0, 97);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de programação avançada', 0, 75);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de programação de alto nível', 0, 50);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de programação de computadores', 0, 29);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de programação em linguagem C++', 0, 103);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de resolução de conflitos', 0, 40);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de segurança de rede', 0, 74);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica de segurança de rede', 0, 85);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica onde uma função chama a si mesma', 1, 25);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica para avaliar os pontos fortes, fracos, oportunidades e ameaças de uma organização ou projeto', 1, 68);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica para criar gráficos e tabelas em planilhas', 0, 58);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica para otimizar algoritmos de busca', 0, 9);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma técnica que permite que um sistema operacional utilize parte do disco rígido como se fosse memória RAM', 1, 83);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma unidade de controle adicional para a CPU', 0, 49);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma unidade de medida de memória', 0, 3);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma unidade de processamento secundário', 0, 47);",
        "INSERT INTO alternativa VALUES (NULL, 'Uma variável de escopo global', 0, 45);",
        "INSERT INTO alternativa VALUES (NULL, 'Valores, crenças e normas compartilhadas por membros de uma organização', 1, 40);"]
        
        for i in seed:
            bd.inserir(i)
        
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
    def main_inicio(self):
        self.frm_inicio = ttk.Frame(self.main)
        self.frm_inicio.pack(expand=True, fill='both')
        
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
    
    def main_questoes(self):
        pass
    
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
        self.tvl_cadastro.geometry('500x600')
        self.tvl_cadastro.grab_set()
                
        self.tvl_cadastro.grid_columnconfigure(0, weight=1)
        self.tvl_cadastro.grid_rowconfigure(0, weight=1)
        self.tvl_cadastro.grid_rowconfigure(1, weight=1)
        self.tvl_cadastro.grid_rowconfigure(2, weight=1)
        self.tvl_cadastro.grid_rowconfigure(3, weight=1)
        self.tvl_cadastro.grid_rowconfigure(4, weight=1)
        self.tvl_cadastro.grid_rowconfigure(5, weight=1)
        self.tvl_cadastro.grid_rowconfigure(6, weight=1)
        
        self.imagem2 = Image.open('logo.png')
        self.logo = ImageTk.PhotoImage(self.imagem2)
        self.logo_label = ttk.Label(self.tvl_cadastro, image=self.logo)
        self.logo_label.grid(row=0, column=0)
        
        
        lbl_cadastro = ttk.Label(self.tvl_cadastro, text='CADASTRE-SE', font=('Times New Roman', 16))
        lbl_cadastro.grid(row=1, column=0)
         
        frm1 = ttk.Frame(self.tvl_cadastro)
        frm1.grid(row=4, column=0)
        
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
        frm2.grid(row=5, column=0)

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
        btn_confirmar.grid(row=6, column=0)
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
        self.tvl_login.geometry('500x600')
        self.tvl_login.grab_set()
        
        self.tvl_login.grid_columnconfigure(0, weight=1)
        self.tvl_login.grid_rowconfigure(0, weight=1)
        self.tvl_login.grid_rowconfigure(1, weight=1)
        self.tvl_login.grid_rowconfigure(2, weight=1)
        self.tvl_login.grid_rowconfigure(3, weight=1)
        self.tvl_login.grid_rowconfigure(4, weight=1)
        self.tvl_login.grid_rowconfigure(5, weight=1)
        
        self.imagem3 = Image.open('logo.png')
        self.logo = ImageTk.PhotoImage(self.imagem3)
        self.logo_label = ttk.Label(self.tvl_login, image=self.logo)
        self.logo_label.grid(row=0, column=0)

        
        frm1 = ttk.Frame(self.tvl_login)
        frm1.grid(row=4, column=0)
        lbl1 = ttk.Label(frm1, text='Não possui uma conta?', font=('Times New Roman', 16))
        lbl1.pack(side='left')
        lbl2 = ttk.Label(frm1, text='Cadastre-se', foreground='#233dff', cursor='hand2', font=('Times New Roman', 16))
        lbl2.config(underline=6)
        fonte = font.Font(lbl2, lbl2.cget('font'))
        fonte.configure(underline=True)
        lbl2.configure(font=fonte)
        lbl2.bind('<Button-1>', login_cadastro)
        lbl2.pack(side='left')

        lbl_login = ttk.Label(self.tvl_login, text='LOGIN', font=('Times New Roman', 16))
        lbl_login.grid(row=1, column=0)
        
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
        btn_confirmar.grid(row=5, column=0)   

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