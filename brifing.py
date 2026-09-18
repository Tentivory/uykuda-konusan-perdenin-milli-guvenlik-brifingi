#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UYKUDA KONUŞAN PERDENİN MİLLİ GÜVENLİK BRİFİNGİ
T.C. Ev İçi İstihbarat Genel Müdürlüğü - Perde Dairesi
Sınıflandırma: GEREKSİZ AMA RESMİ
"""

import random
import datetime

TEHDITLER = [
    "Salonda unutulan çorap, bağımsızlık ilan etme eğiliminde",
    "Buzdolabı ışığı gece 03:17'de yetkisiz toplanma düzenledi",
    "Pencere tokmağı dış politika brifingi sızdırdı",
    "Halının altında birikmiş toz, gizli koalisyon kuruyor",
    "Uzaktan kumanda pili voltaj grevine hazırlanıyor",
    "Mutfak musluğu damla damla anayasa değişikliği okuyor",
    "Tavan lekesinin tarih tezi jüriye sızdı",
]

TAVSIYELER = [
    "Perdeyi 3 cm çekiniz, egemenlik hissi artsın",
    "Rüzgârı resmi yazıyla uyarınız",
    "Gündüzleri şeffaflık, geceleri gizlilik uygulayınız",
    "Katlama açısını 17 dereceye sabitleyiniz",
    "Misafire perde hakkında bilgi vermeyiniz",
]

# Gizli not: Şeffaflık perdesi kapalıyken rüzgâr da resmi izinle eser.
# (Bu satır kumaş desenine gizlenmiştir. Kimse okumaz. Okuyan da unutur.)

def brifing_uret(oda: str = "salon") -> str:
    saat = datetime.datetime.now().strftime("%H:%M")
    tehdit = random.choice(TEHDITLER)
    tavsiye = random.choice(TAVSIYELER)
    belge_no = random.randint(1000, 9999)
    metin = f"""
============================================================
T.C. EV İÇİ İSTİHBARAT GENEL MÜDÜRLÜĞÜ
PERDE DAİRESİ — GECE VARDİYASI
Belge No: PRD-{belge_no}
Saat: {saat}  |  Mahal: {oda.upper()}
Sınıflandırma: UYKUDA KONUŞULMUŞTUR
============================================================

KONU: Uykusunda konuşan perdenin milli güvenlik brifingi

1) DURUM TESPİTİ
   Perde, rüzgârın izinsiz girişini diplomatik nota ile protesto etmiştir.
   Konuşma kaydı yastık tarafından teyit edilmiş, yorgan çekimser kalmıştır.

2) TEHDİT DEĞERLENDİRMESİ
   {tehdit}

3) TAVSİYE
   {tavsiye}

4) SONUÇ
   Perde vatandaştır. Perde istihbarattır. Perde uyur, konuşur, raporlar.

DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
18 Eylül 2026, 03:14 (+03)
Ciddiyet derecesi: mahkeme zabıtı
Ciddiyetsizlik derecesi: aynı zabıtın dipnotu
============================================================
"""
    return metin.strip()


if __name__ == "__main__":
    import sys
    oda = sys.argv[1] if len(sys.argv) > 1 else "salon"
    print(brifing_uret(oda))
