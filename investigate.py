import webbrowser 
import time 

def logo():
    print("██╗░░░░░███████╗████████╗░██████╗")
    print("██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
    print("██║░░░░░█████╗░░░░░██║░░░╚█████╗░")
    print("██║░░░░░██╔══╝░░░░░██║░░░░╚═══██╗")
    print("███████╗███████╗░░░██║░░░██████╔╝")
    print("╚══════╝╚══════╝░░░╚═╝░░░╚═════╝░")
    print("██╗███╗░░██╗██╗░░░██╗███████╗░██████╗████████╗██╗░██████╗░░█████╗░████████╗███████╗")
    print("██║████╗░██║██║░░░██║██╔════╝██╔════╝╚══██╔══╝██║██╔════╝░██╔══██╗╚══██╔══╝██╔════╝")
    print("██║██╔██╗██║╚██╗░██╔╝█████╗░░╚█████╗░░░░██║░░░██║██║░░██╗░███████║░░░██║░░░█████╗░░")
    print("██║██║╚████║░╚████╔╝░██╔══╝░░░╚═══██╗░░░██║░░░██║██║░░╚██╗██╔══██║░░░██║░░░██╔══╝░░")
    print("██║██║░╚███║░░╚██╔╝░░███████╗██████╔╝░░░██║░░░██║╚██████╔╝██║░░██║░░░██║░░░███████╗")
    print("╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝\n\n")

def search():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #chrome_path = '/bin/google-chrome %s' 
    rozhodnuti = int(input("Jedna se o IP - 1 nebo domenu - 2?: "))
    if rozhodnuti == 1:
        ipaddress = input("Vloz IP kterou chces vyhledat: ")
        vti =  f'https://www.virustotal.com/gui/ip-address/{ipaddress}'
        webbrowser.get(chrome_path).open(vti) 
        time.sleep(2) 
        abuseip = f'https://www.abuseipdb.com/check/{ipaddress}'
        webbrowser.get(chrome_path).open(abuseip) 
        time.sleep(2) 
        random = f'https://www.google.com/search?q=what+is+ip+{ipaddress}'
        webbrowser.get(chrome_path).open(random) 
        time.sleep(2) 
        alien = f'https://otx.alienvault.com/indicator/ip/{ipaddress}'
        webbrowser.get(chrome_path).open(alien) 
        time.sleep(2) 
        whois = f'https://whois.domaintools.com/{ipaddress}'
        webbrowser.get(chrome_path).open(whois) 
        time.sleep(2) 
        urlscan = "https://urlscan.io/"
        webbrowser.get(chrome_path).open(urlscan)
        time.sleep(2)
        shodanip = f'https://www.shodan.io/host/{ipaddress}'
        webbrowser.get(chrome_path).open(shodanip)
        time.sleep(2)
        cisco = f'https://talosintelligence.com/reputation_center/lookup?search={ipaddress}'
        webbrowser.get(chrome_path).open(cisco)

    elif rozhodnuti == 2:
        domain = input("Vloz domenu kterou chces vyhledat: ")
        vtd = f'https://www.virustotal.com/gui/domain/{domain}/detection'
        webbrowser.get(chrome_path).open(vtd) 
        time.sleep(2) 
        abuseipd = f'https://www.abuseipdb.com/check/{domain}'
        webbrowser.get(chrome_path).open(abuseipd) 
        time.sleep(2) 
        randomd = f'https://www.google.com/search?q=what+is+domain+{domain}'
        webbrowser.get(chrome_path).open(randomd) 
        time.sleep(2) 
        aliend = f'https://otx.alienvault.com/indicator/domain/{domain}'
        webbrowser.get(chrome_path).open(aliend) 
        time.sleep(2) 
        urlvoid = f'https://www.urlvoid.com/scan/{domain}/'
        webbrowser.get(chrome_path).open(urlvoid) 
        time.sleep(2) 
        whoisd = f'https://whois.domaintools.com/{domain}'
        webbrowser.get(chrome_path).open(whoisd) 
        time.sleep(2) 
        urlscand = "https://urlscan.io/" 
        webbrowser.get(chrome_path).open(urlscand)
        time.sleep(2) 
        shodand = f'https://www.shodan.io/search?query={domain}'
        webbrowser.get(chrome_path).open(shodand)
        time.sleep(2)
        cisco = f'https://talosintelligence.com/reputation_center/lookup?search={domain}'
        webbrowser.get(chrome_path).open(cisco)
        
    else:
        print("Zadal jsi mimo rozsah... Zkus to znovu... \n")
        search()

def main():
    logo()
    search()
main()
