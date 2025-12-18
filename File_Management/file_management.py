import os 
print(f"{os.getlogin()} adli kullanici olarak giriş yaptiniz!")

def path_check(path):
    try:
        if os.path.exists(path) == True:
            return True
    except:
        return FileNotFoundError

def newFile(name):
        open(name,"x", encoding="utf-8")
        print(f"{name} adli dosyaniz oluşturuldu.")


def newFolder(name):
    os.mkdir(name)
    print(f"{name} adli klasör oluşturuldu.")
    ask = input("Klasörün içine dosya yada klasör açmak istermisiniz? 1-dosya 2-klasör (boş bırakmak atlatır)")
    if ask == "1":
        newFile(ask)  
    elif ask == "2":
        newFolder(ask)  

def showFolders():
    folder = os.listdir(os.getcwd())
    folders = []
    files = []
    for i in folder:
        if os.path.isfile(i) == True:
            files.append(i)
        elif os.path.isdir(i) == True:
                folders.append(i)
    print(f"""-----{su_an}-----
          Klasörler: {folders}
          Dosyalar: {files}""")
    x = input("Açmak istediğiniz dosyayi ya da klasörü giriniz (Çikiş için boş birakin): ")
    path_check(x)
    if len(x)> 0:
        if os.path.isfile(x) == True:
            with open(x,"r",encoding="utf-8") as f:
                print(f"-----{x}-----")
                print(f.read())
        elif os.path.isdir(x) == True:
            os.chdir(x)

def del_file():
    name = input("Dosya/Klasör adini giriniz: ")
    path_check(name)
    if os.path.isfile(name) == True:
        os.remove(name)
    elif os.path.isdir(name) == True:
        if len(os.listdir(name)) == 0:
            os.rmdir(name)
        else:
            for file in os.listdir(name):
                os.chdir(name)
                os.remove(file)
            os.chdir("..")
            os.rmdir(name)
            
def menu():
    global name
    name = None
    global su_an
    su_an = os.getcwd()
    print(f"Şuan {su_an} dizininde işlem yapiyorsunuz. Farkli bir dizinde işlem yapmak için '1' tuşlayin")
    x = input()
    path_check(x)
    if x == "1":
        new_path = input("Lütfen gitmek istediğiniz dizini giriniz: ")
        os.chdir(new_path)
    while True:
        print("""Lütfen yapmak istediğiniz işlemi seçiniz: 
          1- Yeni dosya oluştur
          2- Yeni klasör oluştur
          3- Mevcut klasör ve dosyalari görüntüle
          4- Dosya/Klasör sil
          5- Çikiş yap""")
        secim = input()
        if secim == "1":
            name = input("Dosya adını giriniz: ")
            newFile(name)
        elif secim == "2":
            name = input("Klasör adini giriniz: ")
            newFolder(name)
        elif secim =="3":
            showFolders()
        elif secim == "4":
            del_file()
        elif secim == "5":
            çikiş()
menu()