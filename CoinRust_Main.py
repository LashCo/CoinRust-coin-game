import tkinter as tk
import random
from tkinter import messagebox
import webbrowser
import time
from tkinter import PhotoImage

# Bakiye değişkenim
bakiye = 0

# İngilizce listemiz
list_ing = [
    'Ability -- Yetenek',
    'Accomplish -- Başarmak',
    'Apologize -- Özür dilemek',
    'Serendipity -- Beklenmedik güzelliklerle karşılaşma, talih',
    'Mellifluous -- Tatlı ve akıcı bir şekilde söylenen (ses veya müzik için kullanılır)',
    'Effervescent -- Köpüklü, neşeli',
    'Ephemeral -- Geçici, fani',
    'Harbinger -- Haberci, müjdeci',
    'Quintessential -- Özdeş, tamamı temsil eden',
    'Resilient -- Dayanıklı, dirençli',
    'Ubiquitous -- Her yerde bulunan, yaygın',
    'Eloquent -- Etkileyici, güzel konuşan',
    'Quixotic -- Hayalperest, gerçekçi olmayan',
    'Ineffable -- Sözle tarif edilemeyen, anlatılmaz',
    'Cacophony -- Uğultu, gürültü',
    'Panacea -- Çare, şifa',
    'Nefarious -- Kötü niyetli, şeytani',
    'Tranquil -- Sakin, huzurlu',
    'Sagacious -- Bilge, akıllı',
    'Benevolent -- İyiliksever, hayırsever',
    'Euphoria -- Coşku, neşe',
    'Nostalgia -- Özlem, hasret',
    'Voracious -- Aşırı düşkün, obur',
    'Indomitable -- Yenilmez, mağlup edilemez',
    'Magnanimous -- Büyük yürekli, cömert',
    'Idyllic -- Cennet gibi, huzurlu',
    'Pernicious -- Zararlı, kötü',
    'Quagmire -- Bataklık, çıkmaz',
    'Rambunctious -- Kargaşa çıkaran, hiperaktif',
    'Serendipity -- Beklenmedik güzelliklerle karşılaşma, talih',
    'Mellifluous -- Tatlı ve akıcı bir şekilde söylenen (ses veya müzik için kullanılır)',
    'Nefarious -- Kötü niyetli, şeytani',
    'Sagacious -- Bilge, akıllı',
    'Benevolent -- İyiliksever, hayırsever',
    'Euphoria -- Coşku, neşe',
    'Nostalgia -- Özlem, hasret',
    'Voracious -- Aşırı düşkün, obur',
    'Indomitable -- Yenilmez, mağlup edilemez',
    'Magnanimous -- Büyük yürekli, cömert',
    'Idyllic -- Cennet gibi, huzurlu',
    'Pernicious -- Zararlı, kötü',
    'Quagmire -- Bataklık, çıkmaz',
    'Rambunctious -- Kargaşa çıkaran, hiperaktif',
    'Ephemeral -- Geçici, fani',
    'Harbinger -- Haberci, müjdeci',
    'Quintessential -- Özdeş, tamamı temsil eden',
    'Resilient -- Dayanıklı, dirençli',
    'Ubiquitous -- Her yerde bulunan, yaygın',
    'Eloquent -- Etkileyici, güzel konuşan',
    'Quixotic -- Hayalperest, gerçekçi olmayan',
    'Ineffable -- Sözle tarif edilemeyen, anlatılmaz',
    'Cacophony -- Uğultu, gürültü',
    'Panacea -- Çare, şifa'
]

#hediye listemiz:
hedylist = [
    'hediyeniz bir windows 10 pro anahtarı:6P99N-YF42M-TPGBG-9VMJP-YKHCF',
    'hediyeniz bir Windows 10 Enterprise anahtarı:CKFK9-QNGF2-D34FM-99QX2-8XC4K',
    'hediyeniz anlamlı bir söz: unutma her yanan hayallerin suya düşer bir güm denize girersen bulursun her şey cesaret ister.',
    'hediyeniz bir mail hesabı eposta = lashyco75@gmail.com, şifre = Acco123!',
    'Hediyeniz bir Udemy kursu: kurs adı = Python for Beginners',
    'Hediyeniz bir Google Play hediye kartı: kod = XYZW-1234-5678-ABCD',
    'Hediyeniz bir Starbucks hediye kartı: kod = STARB-UCKS-1234',
    'Hediyeniz bir Xbox Live Gold üyelik kodu: KOD123-456789-XYZ',
    'Hediyeniz bir PlayStation Plus abonelik kodu: PSPLUS-ABCDEF-12345',
    'Hediyeniz bir Steam cüzdan kodu: STEAM-1234-5678-ABCD'
]
hediye_seçim = random.choice(hedylist)#burda hediye listesinden bir hediye seçicek

#hediye scriptimizi yazalım:
def hediye_scripti():
    global bakiye
    if bakiye >= 4:
        bakiye -= 4
        bilgi_label.config(text="RichCoins: " + str(bakiye) + " RC")
        hediye_seçim = random.choice(hedylist)
        messagebox.showinfo("Hediyeniz", hediye_seçim)
    else:
        messagebox.showinfo("Mesaj!", "Yeterli bakiyeniz yok. Lütfen daha fazla coin kazanın.")

# Bakiye arttırma işlevimiz
def bakiye_arttirma_scripti():
    global bakiye
    bakiye += 5 
    bilgi_label.config(text="RichCoins: " + str(bakiye) + " RC")

def bakiye_çekme_scripti():
    global bakiye
    bakiye -= 5  
    bilgi_label.config(text="RichCoins: " + str(bakiye) + " RC")

def ingilizce_öğrenme_scripti():
    global bakiye
    if bakiye >= 5:  
        bakiye -= 5   
        bilgi_label.config(text="RichCoins: " + str(bakiye) + " RC")
        ing_seçim = random.choice(list_ing)  # Rastgele bir İngilizce kelime seçecek bir kod
        messagebox.showinfo("İngilizce kelimeniz hazır!", ing_seçim)
    else:
        messagebox.showinfo("Mesaj!", "Bakiyeniz yetersiz. Lütfen daha fazla coin kazanın.")

def github_reklam_scripti():
    global bakiye
    bakiye += 16000  # Bakiyeyi 16000 olarak ayarlama kodumuz
    bilgi_label.config(text="RichCoins: " + str(bakiye) + " RC")
    messagebox.showinfo("Teşekkürler", "GitHub hesabımı ziyaret ettiğiniz için teşekkürler! Hesabınıza 16000RC bakiye eklenmiştir.")
    time.sleep(2)
    webbrowser.open("https://github.com/LashCo")

# Arayüz oluşturma
pencere = tk.Tk()
pencere.title("CoinRust")
pencere.geometry("600x600")

# Etiket ve butonlar
bilgi_label = tk.Label(pencere, font=("Courier", 16, "bold"), text="RichCoins: 0 RC")
bakiye_button = tk.Button(pencere, text="Coin kazan", font="Courier 16 bold", width=15, justify="left", command=bakiye_arttirma_scripti)
çek_buton = tk.Button(pencere, font=("Courier", 16, "bold"), text="RC Coin çekimi", command=bakiye_çekme_scripti)
ingilizce_butonu = tk.Button(pencere, font=("Courier", 16, "bold"), text="İngilizce kelime öğren", command=ingilizce_öğrenme_scripti)
hediye_butonu = tk.Button(pencere, font=("Courier", 16, "bold"), text="bir hediye al", command=hediye_scripti)
github = tk.Button(pencere, font=("Courier", 16, "bold"), text="GitHub", command=github_reklam_scripti)

# Konumlar
bilgi_label.pack()
bakiye_button.pack()
çek_buton.pack()
ingilizce_butonu.pack()
hediye_butonu.pack()
github.place(x=30, y=50)

pencere.mainloop()
