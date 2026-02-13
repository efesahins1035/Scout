# Scout - Modüler Ağ Güvenlik Aracı 🕵️♂️

Scout, Python ile geliştirilmiş, tamamen Türkçe arayüze sahip, modüler ve genişletilebilir bir ağ güvenlik aracıdır. Nmap benzeri yetenekleri modern bir terminal arayüzü (TUI) ile birleştirir.

```text
███████╗ ██████╗ ██████╗ ██╗   ██╗████████╗
██╔════╝██╔════╝██╔═══██╗██║   ██║╚══██╔══╝
███████╗██║     ██║   ██║██║   ██║   ██║   
╚════██║██║     ██║   ██║██║   ██║   ██║   
███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   
```

## 🚀 Özellikler

- **🔍 Gelişmiş Port Tarama:** TCP Connect, SYN (Yarı Açık) ve UDP tarama desteği.
- **🇹🇷 Tamamen Türkçe:** Arayüz, loglar ve yardım menüleri tamamen Türkçe.
- **🧩 Modüler Yapı:** Kolayca yeni araçlar ve modüller eklenebilir.
- **🖥️ Modern Arayüz:** `rich` kütüphanesi ile renklendirilmiş, canlı ilerleme çubuklu terminal arayüzü.
- **⚙️ Esnek Yapılandırma:** Parametre kısayollarını (`-ss` yerine `-gizli` gibi) kendiniz belirleyebilirsiniz.
- **⚡ Hız Profilleri:** Ağ durumuna göre 5 farklı hız profili (`gizli`'den `agresif`'e).
- **📝 Servis Tespiti:** Açık portlarda çalışan servisleri ve versiyon bilgilerini (banner grabbing) otomatik algılar.

## 🛠️ Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/efesahins1035/Scout.git
   cd Scout
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
   *(Not: SYN ve UDP taramaları için Windows'ta Npcap kurulumu gerekebilir)*

## 📖 Kullanım

### 1. Komut Satırı (CLI)

```bash
# Basit tarama
python scout.py -t 192.168.1.1

# Kritik portlar + Servis tespiti
python scout.py -t google.com -p 80,443 -sv
```

### 2. İnteraktif Mod

Parametresiz çalıştırın:
```bash
python scout.py
```

## 🔌 Parametreler

| Kısa | Uzun | Açıklama |
|------|------|----------|
| `-t` | `--hedef` | Hedef IP veya alan adı |
| `-p` | `--port` | Port aralığı (Ör: `1-100`, `80,443`) |
| `-st` | `--tam` | TCP Connect taraması |
| `-ss` | `--yari` | SYN taraması (Yönetici yetkisi gerektirir) |
| `-sv` | `--servis` | Servis ve versiyon tespiti |

## 📄 Lisans
MIT License
