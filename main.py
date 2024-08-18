
"""
Ce programme est un jeu de devinette de mots informatiques réalisé avec customtkinter.

Auteur: [Muina Lukusa Jonathan]

Ce jeu affiche un mot informatique dont les lettres sont mélangées. L'utilisateur doit deviner le mot correct.
S'il devine correctement, le jeu affiche un message de confirmation. Sinon, il affiche la réponse correcte.
Le jeu permet également de voir les indices sur le mot à deviner.

Classes:
    WordDevine: Classe principale qui gère l'interface graphique et la logique du jeu.

Méthodes principales:
    __init__: Initialise l'application et crée l'interface graphique.
    melanger_mot: Méthode pour mélanger les lettres d'un mot.
    play: Méthode pour lancer le jeu et gérer les interactions avec l'utilisateur.
"""

from tkinter import *
import customtkinter
import random
from PIL import ImageTk,Image  
from tkinter import messagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class WordDevine:
    def __init__(self,app) :
        # THE COMMENT ...
        self.app = app
        self.app.geometry("600x600+550+100")
        self.app.title("Word Game")
        self.app.resizable(False,False)
        self.app.iconbitmap("image/logo.ico")
        self.score = 0
        
        # 
        frame_principal = customtkinter.CTkFrame(master=app,width=450,height=300)
        frame_principal.place(x=70,y=50)
        
        img_welcome = PhotoImage(file="image/174849.png")
        self.lbl = customtkinter.CTkLabel(master=frame_principal,image=img_welcome
                                          ,text='').place(x=170,y=10)
        img_next = customtkinter.CTkImage(Image.open("image/892657.png").resize((20,20), Image.ANTIALIAS))
        img_exit = customtkinter.CTkImage(Image.open("image/3917759.png").resize((20,20), Image.ANTIALIAS))
        img_run = customtkinter.CTkImage(Image.open("image/retablir.png").resize((20,20), Image.ANTIALIAS))
        
        self.label_principal = customtkinter.CTkLabel(master=frame_principal,text="Bienvenue dans le jeu: \nTrouvez le mot\ninformatique",font=("Arial",25,"bold"))
        self.label_principal.place(x=100,y=130)
        
        self.entry_word_user  = customtkinter.CTkEntry(master=app,corner_radius=0,border_color="white",
                                                       width=450,height=50,font=("Helvetica",16,"bold"))
        self.entry_word_user.place(x=70,y=360)
        
        self.entry_word_ia  = customtkinter.CTkEntry(master=app,corner_radius=0,border_color="yellow",
                                                       width=450,height=50,font=("Helvetica",16,"bold"))
        self.entry_word_ia.place(x=70,y=420)
        
        self.btn_valid = customtkinter.CTkButton(master=app,width=100,height=50,corner_radius=5,
                                                text=""
                                                ,image=img_next,cursor="hand2",command=self.check_valid_word)
        self.btn_valid.place(x=250,y=500)
        
        self.btn_exit = customtkinter.CTkButton(master=app,width=100,height=50,corner_radius=5,
                                                text=""
                                                ,image=img_exit,cursor="hand2",fg_color="red",
                                                hover_color="grey",command=self.stop_game)
        self.btn_exit.place(x=420,y=500)
        
        self.btn_run =  customtkinter.CTkButton(master=app,width=100,height=50,corner_radius=5,
                                                text=""
                                                ,image=img_run,cursor="hand2",fg_color="red",hover_color="grey",
                                                command=self.play)
        self.btn_run.place(x=70,y=500)
        
        self.copyright = customtkinter.CTkLabel(master=app,text="copyright : jordanmuina@gmail.com",font=("Arial",15))
        self.copyright.place(x=170,y=560)
        
    
    #
    global word_list
    #
    word_list = ["programmation", "algorithme", "variable", "boucle", 
                        "condition", "fonction", "classe", "objet", "méthode",
                    "tableau", "chaîne", "entier", "flottant", "booléen",
                    "déclaration", "initialisation", "assignation", 
                    "opérateur", "expression", "itération", "récursivité",
                    "compilation", "interprétation", "débogage", 
                    "erreur", "exception", "portée", "référence", "pointeur", "mémoire", "allocation", "libération", 
                    "fichier", "lecture", "écriture", "flux", "système", "exploitation", "réseau", "protocole", 
                    "socket", "client", "serveur", "HTTP", "HTTPS", 
                    "API", "JSON", "XML", "HTML", "CSS", "JavaScript", "Java",
                    "Python", "C+","C", "Ruby", "Swift", "Go", "Rust", "SQL", "NoSQL", "base de données", 
                    "index", "clé", "requête", "transaction", "sécurité", "cryptographie", "authentification", 
                    "autorisation", "pare-feu", "attaque", "virus", "malware"]
    
      
    def melanger_mot(self,word):
            """
                 Cette fonction vous permet de melanger les lettres de chaque mot
            """
            word = list(word)
            melanger_word =random.shuffle(word)
            return ''.join(word)
        
    def play(self):
            """Cette vous fonction vous donne la possibilité de deviner le mot afficher par le programme
            """
            global word
    
            word_play_again = []    
           
            word =random.choice(word_list)
            
            word_play_again.append(word)
            melange_word = self.melanger_mot(word)    
            #print(f"Le mot a devinnez est : {melange_word} ")
            indice_debut = word[0]
            indice_fin = word[-1]
            self.label_principal.configure(text=f"LES INDICES\n\nLe mot debute par : {indice_debut}\nEt se termine par : {indice_fin}")
    
            self.entry_word_ia.delete(0, END)
            self.entry_word_user.delete(0, END)
            self.entry_word_ia.insert(0, melange_word)
                   
    def check_valid_word(self):
        """
            Cette fonction vous permet de verifier la réponse de l'utilisateur
        """
        global word
        
        if self.entry_word_user.get() == "":
            messagebox.showwarning("Alerte","Veuillez renseigner votre réponse !",parent=self.app)
        elif self.entry_word_user.get() == word:
            self.score += 2
            messagebox.showinfo("Bravo",f"C'est la bonne reponse !\nVotre score  est de {self.score}",parent=self.app)
        else:
            messagebox.showwarning("Dommage",f"Vous avez echoué, la bonne réponse est {word}",parent=self.app)
        self.play()
        
    def stop_game(self):
        #
        self.label_principal.configure(text=f"Merci d'avoir paticiper \nVous quittez le jeu avec \n{self.score} points ")
        self.entry_word_ia.delete(0, END)
        
if __name__ == "__main__":
    app = customtkinter.CTk()#
    objet  = WordDevine(app)
    app.mainloop()