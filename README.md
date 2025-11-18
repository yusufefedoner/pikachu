📘 README.md (Tek Dosya – Tam Açıklamalı)
# 🎮 Pokémon Discord Botu

Bu Discord botu, kullanıcıların kendi Pokémon’larını oluşturup eğittebildiği, savaştırabildiği, iyileştirebildiği ve liderlik tablosunda yarışabildiği bir oyun sunar. Bot; normal, büyücü (Wizard) ve dövüşçü (Fighter) Pokémon türlerini destekler ve PokeAPI üzerinden gerçek Pokémon isimleri ve sprite görüntüleri alır.

---

# 🧩 Özellikler

- 🐾 Normal Pokémon oluşturma
- 🧙‍♂️ Wizard sınıfı (büyü gücü bonuslu)
- 🥊 Fighter sınıfı (güç bonuslu)
- ⚔️ Gerçek zamanlı Pokémon savaşı
- 📜 Savaş geçmişi kaydı
- 🏆 Liderlik tablosu
- 🎨 Resimli Pokémon kartı (PokeAPI entegrasyonu)
- 💖 Pokémon iyileştirme sistemi
- 👥 Her kullanıcı maksimum 3 Pokémon sahibi olabilir

---

# 📂 Proje Yapısı



project/
│── logic.py # Pokémon mantığı, sınıflar ve saldırı sistemi
│── bot.py # Discord bot komutları
│── config.py # Bot tokeninin bulunduğu dosya
│── README.md # Bu dosya


---

# ⚙️ Kurulum

## 1) Gerekli kütüphaneler
```bash
pip install discord
pip install aiohttp

2) config.py oluşturun
token = "DISCORD_BOT_TOKENINIZ"

3) Botu çalıştırın
python bot.py


Bot başarıyla bağlanınca:

Giriş yapıldı: BotAdı


yazacaktır.

🧠 Pokémon Mantığı (logic.py)

Bu dosya, Pokémon sisteminin tamamını yönetir: Pokémon oluşturma, API’den isim/resim alma, savaş sistemi, iyileştirme ve geçmiş kaydı.

🔹 Pokemon Sınıfı (Temel Sınıf)

Her Pokémon rastgele:

1–1000 arası Pokémon ID

50–100 arası güç

100–500 arası can

değerleri ile oluşturulur.

Ayrıca:

pokemons = {trainer: [pokemonlar]}

battle_history = {trainer: [savaş kayıtları]}

şeklinde global kayıt tutulur.

🔹 API'den isim alma

PokeAPI’den gerçek Pokémon ismi:

data['forms'][0]['name']


Başarısız olursa: "Pikachu"

🔹 API'den resim alma

Pokémon sprite:

data['sprites']['front_default']

🔹 Saldırı Mekaniği (Normal Pokémon)

10–50 arası hasar verir.

Rakibin gücü 0 olursa yenilmiş sayılır.

Savaş geçmişi her iki kullanıcıya da kaydedilir.

🧙‍♂️ Wizard Sınıfı

+20 ile +40 arası büyü gücü bonusu alır.

30–70 arası büyü hasarı verir.

🥊 Fighter Sınıfı

+20 ile +50 arası güç bonusu alır.

20–60 arası hasar verir.

Dövüşçü stiliyle nakavt etme mesajı gösterir.

🤖 Discord Bot Komutları (bot.py)
🎒 Pokémon Oluşturma
!go
!go wizard
!go fighter


Kullanıcı en fazla 3 Pokémon oluşturabilir.

Pokémon bilgisi + resmi embed olarak gönderilir.

⚔️ Saldırı Yapma
!attack @Kullanıcı


Her iki kullanıcının da Pokémon’u olmalıdır.

En güçlü Pokémon otomatik seçilir.

Sonuç metni kanala gönderilir ve geçmişe kaydedilir.

💖 Pokémon İyileştirme
!heal


Sahip olunan tüm Pokémon’lara:

+20 ile +50 güç verilir.

ℹ️ Pokémon Bilgisi Görüntüleme
!info


Kullanıcının tüm Pokémon’larının:

İsmi

Gücü

Can değeri
gösterilir.

📜 Savaş Geçmişi
!history


Kullanıcının son 10 savaş sonucu listelenir.

🏆 Liderlik Tablosu
!leaderboard


Sunucudaki en güçlü 10 Pokémon sıralanır.

🌐 API Kullanımı

Bot Pokémon adı ve sprite almak için PokeAPI kullanır:

https://pokeapi.co/api/v2/pokemon/{id}

📄 Lisans

Bu proje eğitim ve eğlence amaçlıdır. Dilediğiniz gibi geliştirebilir ve düzenleyebilirsiniz.

🎉 İyi eğlenceler! Pokémon savaşları başlasın!


---

Hazır!  
İstersen **daha profesyonel badge’li**, **GIF’li**, **tablolı**, **renkli ikonlu**, ya da **İngilizce sürüm** de hazırlayabilirim.
