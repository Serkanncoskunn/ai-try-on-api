from google import genai

# Kendi API anahtarını buraya yapıştır
API_KEY = "AIzaSyDGl3o2osFCQRR-PHN-h3n45JoLJ9W3Qeg"

print("API test ediliyor, lütfen bekleyin...")

try:
    # Sistemi yormamak için en hafif metin modelini kullanıyoruz
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model='models/nano-banana-pro-preview', 
        contents='Merhaba, bu bir API bağlantı testidir. Bana sadece "Bağlantı başarılı" yaz.'
    )
    print("\n✅ BAŞARILI! Gelen Yanıt:", response.text)

except Exception as e:
    print("\n❌ HATA OLUŞTU:")
    print(str(e))