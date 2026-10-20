import tkinter as tk
    
def hasil_prediksi():
    popup = tk.Toplevel(jendela)
    popup.title("Hasil Prediksi")
    popup.geometry("350x150")
    popup.configure(bg="#202050") 

    hasil_lbl = tk.Label(popup, text="Prediksi Prodi: Teknologi Informasi", 
        font=("Arial", 12, "bold"), fg="#00ffff", bg="#202050")
    hasil_lbl.pack(expand=True)