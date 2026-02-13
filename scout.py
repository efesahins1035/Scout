import argparse
import sys
from core.utils import print_banner, print_error, print_info
from moduller.port_tarama import PortTaramaModulu

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Scout - Modüler Ağ Güvenlik Aracı")
    parser.add_argument("-t", "--hedef", help="Hedef IP veya Alan Adı")
    parser.add_argument("-p", "--port", help="Port aralığı (Ör: 1-100 veya 80,443)", default="1-1000")
    parser.add_argument("-sv", "--servis", help="Servis versiyon tespiti yap", action="store_true")
    
    args = parser.parse_args()
    
    if not args.hedef:
        print_info("Hedef belirtilmedi. İnteraktif mod başlatılıyor... (Yakında)")
        # Burada interaktif menü çağrılabilir
        sys.exit(0)
        
    print_info(f"Hedef: {args.hedef}, Portlar: {args.port}")
    
    # Port tarama modülünü başlat
    tarayici = PortTaramaModulu()
    tarayici.calistir(args.hedef, args.port, {"servis": args.servis})

if __name__ == "__main__":
    main()
