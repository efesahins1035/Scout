from scout_v2.core.base import ScoutModul
from scout_v2.core.utils import print_success, print_warning, print_info, console
import requests
from rich.progress import Progress

class DizinTaramaModulu(ScoutModul):
    def __init__(self):
        super().__init__()
        self.ad = "Dir Scout (Dizin Tarama)"
        self.aciklama = "Web sitelerinde gizli dizin ve dosyaları (fuzzing) arar."
        # Küçük bir varsayılan wordlist
        self.default_wordlist = [
            "admin", "login", "wp-admin", "dashboard", "backup", "config", 
            "uploads", "images", "js", "css", "api", "test", "dev", ".env", 
            "robots.txt", "sitemap.xml", "administrator", "manage"
        ]

    def calistir(self, hedef, portlar=None, ayarlar=None):
        if not hedef.startswith("http"):
            hedef = f"http://{hedef}"
        
        wordlist_path = ayarlar.get("wordlist")
        if wordlist_path:
            try:
                with open(wordlist_path, "r") as f:
                    kelimeler = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print_warning(f"Wordlist dosyası bulunamadı: {wordlist_path}. Varsayılan liste kullanılıyor.")
                kelimeler = self.default_wordlist
        else:
            print_info("Wordlist belirtilmedi, varsayılan (kısa) liste kullanılıyor.")
            kelimeler = self.default_wordlist

        console.print(f"[green]Dir Scout[/green] {hedef} üzerinde {len(kelimeler)} dizin taranıyor...")

        with Progress() as progress:
            task = progress.add_task("[cyan]Fuzzing...", total=len(kelimeler))
            
            for kelime in kelimeler:
                url = f"{hedef}/{kelime}"
                try:
                    res = requests.get(url, timeout=3, allow_redirects=False)
                    status = res.status_code
                    
                    if status in [200, 301, 302, 403]:
                        renk = "green" if status == 200 else "yellow" if status in [301, 302] else "red"
                        progress.console.print(f"[{renk}][{status}] {url}[/{renk}]")
                        
                except requests.RequestException:
                    pass
                
                progress.update(task, advance=1)
