import argparse
import sys
from rich.prompt import Prompt
from rich.table import Table
from scout_v2.core.utils import print_banner, print_error, print_info, console
from scout_v2.moduller.port_tarama import PortTaramaModulu
from scout_v2.moduller.dizin_tarama import DizinTaramaModulu

def interaktif_menu():
    while True:
        print_banner()
        
        table = Table(title="Scout Modülleri")
        table.add_column("No", style="cyan", no_wrap=True)
        table.add_column("Modül Adı", style="magenta")
        table.add_column("Açıklama", style="green")
        
        table.add_row("1", "Port Scout", "Port tarama ve servis tespiti")
        table.add_row("2", "Dir Scout", "Dizin tarama ve fuzzing")
        table.add_row("q", "Çıkış", "Uygulamadan çık")
        
        console.print(table)
        
        secim = Prompt.ask("Seçiminiz", choices=["1", "2", "q"], default="1")
        
        if secim == "q":
            print_info("Görüşmek üzere! 👋")
            sys.exit(0)
            
        elif secim == "1":
            hedef = Prompt.ask("Hedef IP/Domain")
            portlar = Prompt.ask("Portlar", default="1-1000")
            servis = Prompt.ask("Servis Tespiti?", choices=["e", "h"], default="h") == "e"
            
            tarayici = PortTaramaModulu()
            tarayici.calistir(hedef, portlar, {"servis": servis})
            
        elif secim == "2":
            hedef = Prompt.ask("Hedef URL (http://...)")
            wordlist = Prompt.ask("Wordlist Dosyası (Boş bırakırsan varsayılan kullanılır)", default="")
            
            tarayici = DizinTaramaModulu()
            tarayici.calistir(hedef, ayarlar={"wordlist": wordlist})
            
        Prompt.ask("\nDevam etmek için Enter'a basın...")
        console.clear()

def main():
    parser = argparse.ArgumentParser(description="Scout - Modüler Ağ Güvenlik Aracı")
    parser.add_argument("-t", "--hedef", help="Hedef IP veya Alan Adı")
    # CLI argümanları şimdilik sadece Port Scout'u tetikliyor, 
    # ileride sub-command (scout port / scout dir) yapısı eklenebilir.
    
    if len(sys.argv) == 1:
        interaktif_menu()
    else:
        # CLI kullanımı için basit yönlendirme
        # (Şu anlık sadece eski mantığı koruyoruz, ama interaktif menü ana odak)
        args, unknown = parser.parse_known_args()
        if args.hedef:
            # Varsayılan olarak port tarama
            print_info("CLI modunda varsayılan olarak Port Scout çalıştırılıyor.")
            from scout_v2.moduller.port_tarama import PortTaramaModulu
            tarayici = PortTaramaModulu()
            tarayici.calistir(args.hedef, "1-1000", {"servis": False})

if __name__ == "__main__":
    main()
