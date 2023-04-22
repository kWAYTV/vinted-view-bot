import threading, requests, os, time
from itertools import cycle
from datetime import datetime
from colorama import Fore, Style
from fake_useragent import UserAgent
from pystyle import Colors, Colorate, Center

logo = """
██╗   ██╗██╗███╗   ██╗████████╗███████╗██████╗ 
██║   ██║██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
██║   ██║██║██╔██╗ ██║   ██║   █████╗  ██║  ██║
╚██╗ ██╔╝██║██║╚██╗██║   ██║   ██╔══╝  ██║  ██║
 ╚████╔╝ ██║██║ ╚████║   ██║   ███████╗██████╔╝
  ╚═══╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═════╝"""

# Clear the console.
clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

def check_files():
    if not os.path.exists("proxies.txt"):
        with open("proxies.txt", "w") as f:
            f.write("Put your proxies here. (user:pass@ip:port)")
        print(f"{Style.DIM}ERROR - {Style.RESET_ALL}You need to input proxies in proxies.txt")
        input(f"{Style.DIM}EXIT - {Style.RESET_ALL}Press enter to exit...")
        time.sleep(1)
        exit()

    if os.stat("proxies.txt").st_size == 0:
        print(f"{Style.DIM}ERROR - {Style.RESET_ALL}You need to input proxies in proxies.txt")
        input(f"{Style.DIM}EXIT - {Style.RESET_ALL}Press enter to exit...")
        time.sleep(1)
        exit()

class VintedViewer:
    def __init__(self, link, threads):
        self.link = link
        self.lock = threading.Lock()
        self.threads = threads
        self.ctr = 0
        self.session = requests.Session()
        self.proxy_pool = self.load_proxies()
        self.proxy = next(self.proxy_pool)
        self.set_proxy()
        self.user_agent = UserAgent()

    def load_proxies(self):
        with open("proxies.txt", "r") as f:
            proxies = f.read().splitlines()
        return cycle(proxies)

    def set_proxy(self):
        self.proxy = next(self.proxy_pool)
        self.session.proxies = {'http': f"http://{self.proxy}", 'https': f'http://{self.proxy}'}

    def safe_print(self, arg):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with self.lock:
            print(f"{current_time} • {arg}")

    def thread_starter(self):
        headers = {
            "User-Agent": self.user_agent.random
        }
        try:
            r = self.session.get(self.link, headers=headers)
            if r.status_code == 200:
                with self.lock:
                    self.ctr += 1
                self.safe_print(f"{Style.DIM}OK • {Style.RESET_ALL}Sent: {self.ctr}")
            else:
                self.safe_print(f"{Style.DIM}ERROR • {Style.RESET_ALL}Error: {r.status_code} for proxy {self.proxy}")
        except requests.exceptions.RequestException as e:
            self.safe_print(f"{Style.DIM}ERROR • {Style.RESET_ALL}Error: {e} for proxy {self.proxy}")

    def run(self):
        while True:
            if threading.active_count() <= self.threads:
                try:
                    threading.Thread(target=self.thread_starter).start()
                except:
                    pass
            self.set_proxy()

def main():
    clear()
    print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logo, 1)))
    print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, "────────────────────────────────────────────\n", 1)))
    print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, "Starting...", 1)))
    check_files()
    link = input(f"{Style.DIM}Input • {Style.RESET_ALL}Vinted link: ")
    threads = int(input(f"{Style.DIM}Input • {Style.RESET_ALL}Threads: "))
    viewer = VintedViewer(link, threads)
    viewer.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Style.DIM}EXIT - {Style.RESET_ALL}Detected Ctrl + C, exiting...")
        time.sleep(1)
        exit()