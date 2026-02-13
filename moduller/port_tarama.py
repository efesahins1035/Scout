import socket
from rich.progress import Progress
from core.base import ScoutModul
from core.utils import print_success, print_warning, console

class PortTaramaModulu(ScoutModul):
    def __init__(self):
        super().__init__()
        self.ad = "Port Tarama"
        self.aciklama = "Belirtilen portları tarar ve açık olanları listeler."

    def calistir(self, hedef, port_str, ayarlar):
        portlar = self._portlari_ayikla(port_str)
        acik_portlar = []
        
        console.print(f"[green]Scout[/green] {len(portlar)} port üzerinde tarama yapıyor...")
        
        with Progress() as progress:
            task = progress.add_task("[cyan]Taranıyor...", total=len(portlar))
            
            for port in portlar:
                if self._port_kontrol(hedef, port):
                    servis_bilgisi = ""
                    if ayarlar.get("servis"):
                        servis_bilgisi = f" ({self._servis_bul(hedef, port)})"
                    
                    progress.console.print(f"[+] Port {port} AÇIK{servis_bilgisi}")
                    acik_portlar.append(port)
                progress.update(task, advance=1)
                
        if not acik_portlar:
            print_warning("Açık port bulunamadı.")
        else:
            print_success(f"Tarama tamamlandı. {len(acik_portlar)} açık port bulundu.")

    def _portlari_ayikla(self, port_str):
        # "1-100" veya "80,443" gibi stringleri listeye çevirir
        portlar = []
        if "-" in port_str:
            bas, son = map(int, port_str.split("-"))
            return list(range(bas, son + 1))
        elif "," in port_str:
            return [int(p) for p in port_str.split(",")]
        else:
            return [int(port_str)]

    def _port_kontrol(self, ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False

    def _servis_bul(self, ip, port):
        try:
            return socket.getservbyport(port)
        except:
            return "Bilinmiyor"
