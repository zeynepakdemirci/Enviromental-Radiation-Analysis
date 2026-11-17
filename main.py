import pandas as pd
import matplotlib.pyplot as plt

veri = pd.read_csv("data.csv")

# Görünmez boşluklar varsa temizleyelim ve sayıları garantiye alalım
veri["Radiation_Level"] = pd.to_numeric(veri["Radiation_Level"])
veri["Location"] = veri["Location"].astype(str).str.strip()

plt.figure(figsize=(8, 5))
plt.bar(veri["Location"], veri["Radiation_Level"], color=['#4C72B0','#55A868','#C44E52'])

plt.title("İstanbul - Çevresel Radyasyon Anomali Analizi") 
plt.xlabel("İlçeler")
plt.ylabel("Radyasyon Seviyesi")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# plt.show() YERİNE FOTOĞRAF OLARAK KAYDEDİYORUZ:
plt.savefig("radyasyon_grafigi.png", dpi=300, bbox_inches='tight')

print("Hedef vuruldu: Grafik 'radyasyon_grafigi.png' olarak klasöre kaydedildi!") 


