import tkinter as tk
    
def hasil_prediksi():
    popup = tk.Toplevel(jendela)
    popup.title("Hasil Prediksi")
    popup.geometry("350x150")
    popup.configure(bg="#202050") 

    hasil_lbl = tk.Label(popup, text="Prediksi Prodi: Teknologi Informasi", 
        font=("Arial", 12, "bold"), fg="#00ffff", bg="#202050")
    hasil_lbl.pack(expand=True)

jendela = tk.Tk()
jendela.title("Aplikasi Prediksi Prodi Pilihan")
jendela.geometry("450x650")
jendela.configure(bg="#202050")

judul = tk.Label(jendela, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"), fg="white", bg="#202050")
judul.pack(pady=15)

frame_nilai = tk.Frame(jendela, bg="#202050")
frame_nilai.pack()