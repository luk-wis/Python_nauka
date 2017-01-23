# -*- coding: UTF-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox
from PIL import ImageTk, ImageFilter

max_h = 500
max_w = 900


class Okno(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.inicjalizuj()

    def wczytaj_ponownie(self):
        szer, wys = self.im.size
        factor_w = 1
        factor_h = 1
        if szer > max_w:
            factor_w = max_w / szer
        if wys > max_h:
            factor_h = max_h / wys
        if factor_h >= factor_w:
            factor = factor_w
        else:
            factor = factor_h
        size = int(szer * factor), int(wys * factor)
        self.im = ImageTk.PhotoImage(self.im.resize(size))
        self.podst.create_image(0, 0, image=self.im, anchor=NW)

    def wczytaj_obraz(self):
        sciezka = self.o.get()
        self.im = open(sciezka)

        try:
            self.filtrbox.config(state='normal')
            self.zbtn.config(state='normal')
            self.skalbox.config(state='normal')
            self.przywrocbtn.config(state='normal')
            self.obraz_oryg = self.im
        except FileNotFoundError:
            messagebox.showerror('Błąd!', 'Plik nie istnieje!')
        except OSError:
            messagebox.showerror('Błąd!', 'Wybierz plik z formatem graficznym')
        self.wczytaj_ponownie()

    def skalowanie_obrazu(self):
        w, h = self.im.size
        mnoznik = float(self.skalbox.get())
        size = int(w * mnoznik), int(h * mnoznik)
        self.im = self.im.resize(size)
        self.wczytaj_ponownie()

    def zastosuj_filtr(self):
        filtry = self.filtrbox.get()
        if filtry == 'BLUR':
            self.im = self.im.filter(ImageFilter.BLUR)
        elif filtry == 'CONTOUR':
            self.im = self.im.filter(ImageFilter.CONTOUR)
        else:
            self.im = self.im.filter(ImageFilter.EMBOSS)
        self.wczytaj_ponownie()

    def przywroc_obraz(self):
        self.im = self.obraz_oryg
        self.wczytaj_ponownie()

    def zapisz_obraz(self):
        sciezka = self.z.get()
        if sciezka == '':
            sciezka = self.o.get()
        self.im.save(sciezka)

    def inicjalizuj(self):
        self.parent.title("Edytor Grafiki")
        self.styl = Style()
        self.styl.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        self.columnconfigure(1, weight=1)
        etykieta = Label(self, text="Ścieżka do pliku:")
        etykieta.grid(sticky=W, pady=4, padx=5)

        self.o = Entry(self)
        self.o.grid(row=1, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E + W + S + N)

        self.z = Entry(self)
        self.z.grid(row=2, column=0, columnspan=2, rowspan=1, padx=5, pady=4, sticky=E + W + S + N)

        self.obtn = Button(self, text="Otwórz", command= lambda: self.wczytaj_ponownie())
        self.obtn.grid(row=1, column=3)

        self.zbtn = Button(self, text="Zapisz", command= lambda: self.zapisz_obraz())
        self.zbtn.grid(row=2, column=3)
        self.zbtn.config(state='disable')

        self.skalbox = Combobox(self, values='0.1 0.2 0.3 0.4')
        self.skalbox.grid(row=3, column=0, padx=5, pady=4, sticky=W + N)

        self.filtrbox = Combobox(self, value='BLUR CONTOUR EMBROS')
        self.filtrbox.grid(row=4, column=0, padx=5, pady=4, sticky=W + N)

        self.skalbox = Button(self, text="Skaluj", command= lambda: self.skalowanie_obrazu())
        self.skalbox.grid(row=3, column=1, padx=5, pady=4, sticky=W + N)
        self.skalbox.config(state='disable')

        self.filtrbox = Button(self, text="Filtruj", command= lambda: self.skalowanie_obrazu())
        self.filtrbox.grid(row=4, column=1, padx=5, pady=4, sticky=W + N)
        self.filtrbox.config(state='disable')

        self.podst = Canvas(self, width=max_w, height=max_h)
        self.podst.grid(row=5, column=0, padx=5, pady=4, sticky=E + W + N + S, columnspan=3)

        self.przywrocbtn = Button(self, text="Przywróć", command= lambda: self.przywroc_obraz())
        self.przywrocbtn.grid(row=5, column=3, padx=5, pady=4, sticky=W + N)
        self.przywrocbtn.config(state='disable')





if __name__ == '__main__':
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()
