Projeto: Jogo da Forca com Interface Gráfica em Python (Tkinter)

Este projeto consiste em uma aplicação simples do clássico Jogo da Forca, desenvolvida utilizando a biblioteca gráfica Tkinter, padrão da linguagem Python para criação de interfaces gráficas (GUI).

O objetivo principal do projeto é proporcionar uma experiência interativa, onde o usuário deve adivinhar uma palavra secreta — neste caso, pré-definida como "python". O jogador possui um número limitado de tentativas (4 chances), e a cada letra errada, perde uma chance. O jogo termina quando o usuário acerta todas as letras da palavra ou esgota as tentativas disponíveis.

Funcionalidades implementadas:
Interface gráfica intuitiva com labels, campo de entrada e botão de ação.

Exibição dinâmica da palavra oculta, revelando letras corretamente adivinhadas.

Controle de tentativas restantes, exibido de forma clara ao jogador.

Mensagens de vitória ou derrota com uso da biblioteca messagebox.

Validação de letras já tentadas, impedindo repetições.

Estrutura do código:
A aplicação é encapsulada em uma classe JogoForca, que herda de tk.Tk.

O método mostrar_palavra() exibe a palavra oculta com os caracteres descobertos.

O método verificar_letra() trata toda a lógica do jogo a cada tentativa.

O método mostrar_mensagem() é responsável por exibir os alertas de fim de jogo.

O loop principal da aplicação é iniciado com jogo.mainloop().

Tecnologias utilizadas:
Python 3

Tkinter (interface gráfica nativa do Python)

Este projeto é ideal para iniciantes que desejam praticar lógica de programação, manipulação de strings e introdução ao desenvolvimento de interfaces gráficas em Python. Além disso, pode ser expandido facilmente com recursos como: seleção aleatória de palavras, níveis de dificuldade, desenho da forca com Canvas, ou até integração com banco de dados para salvar placares.
