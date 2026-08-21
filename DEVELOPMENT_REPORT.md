# 📊 Geliştirme Raporu: Thracian Skills (Antigravity Çoklu Yetenek Deposu)

Bu rapor, Google Antigravity için tasarlanan **Thracian Skills** deposunda yapılan mimari dönüşümü, yeni geliştirilen yetenekleri ve araştırma sentezlerini detaylandırmaktadır.

---

## 1. Mimari Yapı: Thracian Skills Koleksiyonu (Multi-Skill Monorepo)
Proje, modüler ve genel amaçlı bir **Thracian Skills** koleksiyonu halinde yapılandırılmıştır:
*   **Klasör Yapısı:** Tüm yetenekler `skills/` dizini altında bağımsız klasörler halinde barındırılır:
    *   `skills/style-extractor/`: Yazım Tarzı Çıkarma & Antigravity Kural Üretim Yeteneği.
    *   `skills/gemini-spark/`: Gemini Spark Playwright otomasyon motoru.
*   **Esnek Kurulum Aracı (`setup.bat`):**
    *   `setup.bat` veya `setup.bat all`: Depodaki tüm yetenekleri otomatik kurar.
    *   `setup.bat <yetenek_adi>`: Sadece belirtilen yeteneği (ör. `setup.bat style-extractor`) hedef Antigravity dizinine (`.gemini/config/skills/<yetenek_adi>`) kurar.
    *   `setup.bat list`: Depoda mevcut tüm yetenekleri listeler.

---

## 2. Yazım Tarzı Çıkarma Yeteneği (`skills/style-extractor`)
*   **Örnek Doküman Analizi:** Kullanıcının sunduğu makale, rapor, e-posta veya kod yorumlarından yazarın özgün sesini ve üslubunu çıkarır.
*   **6 Boyutlu Stil Analizi:** Leksikal (kelime seçimi), Sözdizimsel (cümle yapısı), Noktalama/Biçimlendirme, Ton/Kadans, Retorik Yaklaşımlar ve Yapay Zeka Kalıplarını Temizleme (Anti-AI Purge Matrix).
*   **Kural Üretim Hedefleri:**
    1.  **Çalışma Alanı Kural Dosyası:** `.gemini/config/rules/*.md` formatında yeniden kullanılabilir RFC 2119 emredici kuralları.
    2.  **Özel Yetenek Rehberi:** İstendiğinde bağımsız bir `SKILL.md` stil rehberi sentezi.
*   **Rehber Doküman:** `skills/style-extractor/references/STYLOMETRIC_RESEARCH_GUIDE.md`.

---

## 3. Gemini Spark Yeteneği Özellikleri (`skills/gemini-spark`)
*   **Çoklu Hesap Desteği (`--account`):** Profil izoleli çalışma (`work`, `personal`, `research`).
*   **CDP Paralel Sekme Desteği (`--cdp`):** Eşzamanlı paralel sekmeler.
*   **Birebir Yanıt Modu (`verbatim`):** Yanıtların tam kopyası.
*   **Başlık Yeniden Adlandırma (`rename`):** Sohbet ve görev kartı başlıklarını güncelleme.
*   **Toplu Silme (`delete`):** Çoklu ID silme ve güncel liste çıktısı.
*   **Workspace Exporters:** Docs (.txt), Sheets (.xlsx), Slides (.pptx) ve görselleri indirme.
