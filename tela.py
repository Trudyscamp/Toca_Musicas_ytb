#Importando o Módulo e a biblioteca
import sys
from PyQt6.QtWidgets import QApplication , QPushButton , QComboBox , QLabel , QWidget , QVBoxLayout , QHBoxLayout , QMessageBox 
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon , QPixmap
from tocador import *


class tela(QWidget):
    ###############################################
    #Construindo a janela e definindo os atributos
    ###############################################
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(300,280)
        self.setWindowTitle('Tocador de musicas')
        self.setWindowIcon(QIcon('clava.png'))
        self.interface()
        self.show()
        
    
        
    def interface(self):
        
        ###############################################
                #Instanciando o Layout principal
        ###############################################
        layout_principal = QVBoxLayout()
        layout_principal.setAlignment(Qt.AlignmentFlag.AlignBaseline)
        ###############################################
             #Adicionando a Imagem a Interface
        ###############################################
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap('clava.png').scaled(180,180)) 
        layout_principal.addWidget(self.logo)      
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        ###############################################
                #Criando o Combobox com as opções
        ###############################################
        
        self.tela_principal = QComboBox(self)
        self.tela_principal.addItem('Selecione a musica.')
        self.tela_principal.addItem('Undertale')
        self.tela_principal.addItem('interstellar')
        self.tela_principal.addItem('Zelda')
        
        layout_principal.addWidget(self.tela_principal)
        
        #Layout dos botões
        layout_botoes = QHBoxLayout()
        
        ###############################################
                    #Definindo os botões
        ###############################################
        
        self.botao_tocar = QPushButton('Play' , self)
        self.botao_tocar.clicked.connect(self.lercaixa)
        self.botao_sair = QPushButton('Sair' , self)
        self.botao_sair.clicked.connect(self.sair)
        #adicionando os botoes no layout botoes        
        layout_botoes.addWidget(self.botao_tocar)
        layout_botoes.addWidget(self.botao_sair)
        #adicionando o layout botoes ao layout principal
        layout_principal.addLayout(layout_botoes)
        
        #setando o layout principal
        self.setLayout(layout_principal)
        ###############################################
                            #O aviso 
        ###############################################
        self.aviso = QLabel('Ao apertar o play, não mexer no mouse ou teclado!')
        self.aviso.setAlignment(Qt.AlignmentFlag.AlignBottom)
        layout_principal.addWidget(self.aviso)
    
    
    ###############################################
            #Lendo o que o usuario escolheu
    ###############################################
           
    def lercaixa(self):
        try:
            content = self.tela_principal.currentText()

            if content == 'Selecione a musica.':
                raise ValueError
            elif content == 'Undertale':
              return undertale()  
            elif content == 'Zelda':
                return zelda()
            elif content == 'interstellar':
                return interstellar()    
        except ValueError:
            info = QMessageBox.critical(self, 'Erro' , 'Você deve escolher uma opção!' , QMessageBox.StandardButton.Ok)
            if info == QMessageBox.StandardButton.Ok:
                pass            
    ###############################################
                #confirmar a saída
    ###############################################
    
    def sair(self):
        sair = QMessageBox.question(self, 'Sair','Deseja fechar o programa?' , QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if sair == QMessageBox.StandardButton.Yes:
            sys.exit()
        else:
            pass    

qt = QApplication(sys.argv)
app = tela()  
sys.exit(qt.exec())                  
