import tkinter as tk
from tkinter import messagebox

class JogoForca(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Jogo da Forca")
        self.geometry("400x300")
        
        self.palavra = "python"
        self.letras_usuario = []
        self.chances = 4
        
        self.label_palavra = tk.Label(self, text=self.mostrar_palavra(), font=("Arial", 20))
        self.label_palavra.pack(pady=20)
        
        self.label_chances = tk.Label(self, text=f"Chances restantes: {self.chances}", font=("Arial", 14))
        self.label_chances.pack()
        
        self.entry_letra = tk.Entry(self, font=("Arial", 14))
        self.entry_letra.pack(pady=10)
        
        self.botao_adivinhar = tk.Button(self, text="Adivinhar", command=self.verificar_letra)
        self.botao_adivinhar.pack()
    
    def mostrar_palavra(self):
        return " ".join(letra if letra in self.letras_usuario else "_" for letra in self.palavra)
    
    def verificar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)
        
        if letra in self.letras_usuario:
            messagebox.showinfo("Aviso", f"Você já tentou a letra '{letra}' antes.")
            return
        
        self.letras_usuario.append(letra)
        
        if letra not in self.palavra:
            self.chances -= 1
            self.label_chances.config(text=f"Chances restantes: {self.chances}")
            if self.chances == 0:
                self.mostrar_mensagem("Você perdeu!", f"A palavra era '{self.palavra}'.")
                self.destroy()
                return
        
        if all(letra in self.letras_usuario for letra in self.palavra):
            self.mostrar_mensagem("Você ganhou!", f"A palavra era '{self.palavra}'.")
            self.destroy()
            return
        
        self.label_palavra.config(text=self.mostrar_palavra())
    
    def mostrar_mensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

if __name__ == "__main__":
    jogo = JogoForca()
    jogo.mainloop()
