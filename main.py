from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

hunians = []
fotos = []
hunians.append(Apartemen("Nelly Joy", 3, 3, 50, 900))
hunians.append(Rumah("Sekar MK", 5, 2, 100, 1300))
hunians.append(Indekos("Bp. Romi", "Cahya", 10, 250))
hunians.append(Rumah("Satria", 1, 4, 70, 900))

root = Tk()
root.title("Praktikum DPBO Python")

# label = Label(root, text = "HELOOOOO")
img = ImageTk.PhotoImage(Image.open("rumah.png").resize((200,200)))
label = Label(root, image = img)
label.pack()
# label.pack()
to_main = Button(root, text="Home", command=lambda : home(),  padx=10, pady=10, width=40)
# to_main.grid(row=0, column=1)
to_main.pack()

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    img = Image.open("./" + hunians[index].get_foto()) 
    img = img.resize((200, 200)) 
    foto = ImageTk.PhotoImage(img)
    fotos.append(foto)
    img_label = Label(d_frame, image=foto)
    img_label.grid(row=0, column=0)


    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w")
    d_summary.grid(row=1, column=0, sticky="w")



    d_summary = Label(d_frame, text="Pemilik Hunian : " +
        hunians[index].get_nama_pemilik(), anchor="w").grid(row=2, column=0, sticky="w")

    if hunians[index].get_jenis() == "Indekos":
        d_summary = Label(d_frame, text="Penghuni : " + hunians[index].get_nama_penghuni(), anchor="w").grid(row=2, column=0, sticky="w")
    else:
        d_summary = Label(d_frame, text="Jumlah Kamar : " + str(
            hunians[index].get_jml_kamar()), anchor="w").grid(row=3, column=0, sticky="w")

    d_summary = Label(d_frame, text="Luas Tanah : " + str(
        hunians[index].get_luas_tanah()) + "m^2", anchor="w").grid(row=4, column=0, sticky="w")

    d_summary = Label(d_frame, text="Kapasitas Listrik : " + str(
        hunians[index].get_kapasitas_listrik()) + "VA", anchor="w").grid(row=5, column=0, sticky="w")
    
    d_summary = Label(d_frame, text= hunians[index].get_dokumen(), anchor="w")
    d_summary.grid(row=6, column=0, sticky="w")

    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    def kembali():
        top.destroy()

    d_kembali = Button (opts, text = "Back", command = kembali)
    d_kembali.grid(row=0, column=0)

    d_exit = Button(opts, text="Exit", command=root.quit)
    d_exit.grid(row=0, column=1)

def home():
    to_main.destroy()

    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos":
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)


root.mainloop()
