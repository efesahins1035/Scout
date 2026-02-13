from abc import ABC, abstractmethod

class ScoutModul(ABC):
    """
    Tüm Scout modülleri bu sınıftan türetilmelidir.
    """
    
    def __init__(self):
        self.ad = "Temel Modül"
        self.aciklama = "Açıklama yok"
    
    @abstractmethod
    def calistir(self, hedef, portlar, ayarlar):
        """
        Modülün ana çalışma mantığı burada olmalı.
        """
        pass
