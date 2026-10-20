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

input_nilai = []
for i in range(1, 11):
    lbl = tk.Label(frame_nilai, text="Nilai Mata Pelajaran " + str(i) + ":", fg="white", bg="#202050", font=("Arial", 10, "bold"))
    lbl.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    
    kotak_input = tk.Entry(frame_nilai, width=20)
    kotak_input.grid(row=i, column=1, padx=10, pady=5)
    input_nilai.append(kotak_input)

frame_bawah = tk.Frame(jendela, bg="#202050")
frame_bawah.pack(pady=15)

lbl_jurusan = tk.Label(frame_bawah, text="Pilihan Jurusan Anda:", fg="white", bg="#202050", font=("Arial", 10))
lbl_jurusan.pack()


pilihan = ["Teknologi Informasi", "Teknik Komputer", "Sistem Informasi"]
jurusan_dipilih = tk.StringVar(jendela)
jurusan_dipilih.set(pilihan[0])

dropdown = tk.OptionMenu(frame_bawah, jurusan_dipilih, *pilihan)
dropdown.pack(pady=5)

tombol = tk.Button(jendela, text="Hasil Prediksi", font=("Arial", 10, "bold"), command=hasil_prediksi)
tombol.pack(pady=10)