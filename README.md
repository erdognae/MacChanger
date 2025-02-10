# MAC Adresi Değiştirme Scripti

## 📌 Özet  
Bu Python scripti, **rastgele bir MAC adresi üretir ve `eth0` arayüzünün MAC adresini geçici olarak değiştirir**.

## ⚙️ Nasıl Çalışır?
1. **Rastgele bir MAC adresi oluşturur.**  
2. **Mevcut MAC adresini alır.**  
3. **Ağ arayüzünü devre dışı bırakır.**  
4. **Yeni MAC adresini atar.**  
5. **Ağ arayüzünü tekrar etkinleştirir.**  
6. **Eski ve yeni MAC adreslerini ekrana yazdırır.**  

## 🔧 Gereksinimler  
- **Python 3**  
- **Root yetkisi (`sudo`)**  
- **`net-tools` paketi (`ifconfig` komutu için)**  

## 🚀 Çalıştırma  
Terminalde scriptin bulunduğu dizine gidip çalıştır:  
```bash
sudo python3 script.py
