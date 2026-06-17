# boot.py - Adalang'in En Basit Yorumlayıcısı
import sys

def adalang_yorumla(kod):
    """Verilen Adalang kodunu çalıştırır."""
    satirlar = kod.split('\n')
    for satir in satirlar:
        satir = satir.strip()
        # 'yaz' komutunu yakala
        if satir.startswith('yaz'):
            # "yaz" kelimesinden sonrasını al, tırnakları temizle
            icerik = satir.replace('yaz', '').strip()
            icerik = icerik.replace('"', '')
            print(icerik)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("🚀 Kullanım: python boot.py <dosya.adal>")
        sys.exit(1)
    
    dosya_adi = sys.argv[1]
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            adalang_kodu = f.read()
        adalang_yorumla(adalang_kodu)
    except FileNotFoundError:
        print(f"❌ Dosya bulunamadı: {dosya_adi}")
