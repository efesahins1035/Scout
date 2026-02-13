from rich.console import Console
from rich.panel import Panel
from rich.text import Text

BANNER = r"""
███████╗ ██████╗ ██████╗ ██╗   ██╗████████╗
██╔════╝██╔════╝██╔═══██╗██║   ██║╚══██╔══╝
███████╗██║     ██║   ██║██║   ██║   ██║   
╚════██║██║     ██║   ██║██║   ██║   ██║   
███████║╚██████╗╚██████╔╝╚██████╔╝   ██║   
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝    ╚═╝   
"""

console = Console()

def print_banner():
    """Ekrana Scout banner'ını basar."""
    text = Text(BANNER, style="bold cyan")
    panel = Panel(text, border_style="blue", title="Scout v1.0", subtitle="Modüler Ağ Güvenlik Aracı")
    console.print(panel)

def print_error(msg):
    console.print(f"[bold red]HATA:[/bold red] {msg}")

def print_success(msg):
    console.print(f"[bold green]BAŞARILI:[/bold green] {msg}")

def print_info(msg):
    console.print(f"[bold blue]BİLGİ:[/bold blue] {msg}")

def print_warning(msg):
    console.print(f"[bold yellow]UYARI:[/bold yellow] {msg}")
