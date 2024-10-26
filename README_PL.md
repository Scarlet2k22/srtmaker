
# CSV to SRT Subtitle Converter

### 📜 Opis projektu
CSV to SRT Subtitle Converter to skrypt Python, który pozwala na konwersję napisów zapisanych w pliku CSV do formatu SRT, popularnego w odtwarzaczach wideo. Skrypt automatycznie oblicza czas trwania napisów na podstawie liczby znaków, dba o odpowiednią długość linii oraz umożliwia wygodne wybieranie plików przez interfejs graficzny.

### 🎯 Funkcjonalności
- **Konwersja CSV do SRT:** Obsługuje pliki CSV zawierające napisy i konwertuje je do formatu SRT.
- **Wygodny interfejs wyboru pliku:** Dzięki Tkinter użytkownik może łatwo wybrać plik CSV do konwersji.
- **Informacja o sukcesie:** Skrypt wyświetla komunikaty o stanie konwersji.
- **Kontrola czasu wyświetlania napisów:** Uwzględnia prędkość czytania oraz ogranicza czas wyświetlania napisów.
- **Podział linii napisów:** Zapewnia lepszą czytelność przez automatyczne dzielenie zbyt długich linii.

### 📋 Parametry
- **FRAME_RATE** - liczba klatek na sekundę dla synchronizacji czasu (domyślnie: 25 FPS).
- **MIN_DURATION** - minimalny czas wyświetlania napisu w sekundach (domyślnie: 1 sekunda).
- **MAX_DURATION** - maksymalny czas wyświetlania napisu w sekundach (domyślnie: 7 sekund).
- **CHARS_PER_LINE** - maksymalna liczba znaków w jednej linii (domyślnie: 42 znaki).
- **READING_SPEED** - prędkość czytania w znakach na sekundę (domyślnie: 20 znaków/sekundę).

### 🛠️ Wymagania
- Python 3.x
- Biblioteki Python:
  - `csv`
  - `os`
  - `tkinter`
  - `re`
  - `sys`

### 🔧 Instalacja
1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/TwojeUzytkownikow/CSV-to-SRT-Converter.git
    cd CSV-to-SRT-Converter
    ```
2. Upewnij się, że posiadasz Python 3.x i zainstalowane wymagane biblioteki.
3. Uruchom skrypt.

### 🚀 Jak używać
1. Uruchom skrypt za pomocą:
   ```bash
   python script.py
   ```
2. Wybierz plik CSV, który chcesz przekonwertować, korzystając z interfejsu wyboru pliku.
3. Skrypt automatycznie przekonwertuje plik CSV na format SRT i zapisze go w folderze `converted` znajdującym się w lokalizacji pliku CSV.
4. Po zakończeniu konwersji zostanie wyświetlone powiadomienie o sukcesie.

### 📂 Struktura CSV
Plik CSV powinien mieć następujący format:
- **Kolumna 1**: Czas rozpoczęcia w formacie `HH:MM:SS:FF` (godziny:minuty:sekundy:klatki).
- **Kolumna 2**: Tekst napisu.

Przykład:
```csv
00:00:01:10, Witaj w naszym filmie.
00:00:05:20, Dziś omówimy temat napisów.
```

### 🎉 Przykładowe użycie
Oto, jak wygląda przykładowy plik CSV i jego konwersja na SRT:
- **Wejście CSV**:
  ```csv
  00:00:01:10, Przykładowy napis numer jeden.
  00:00:05:20, Drugi przykładowy napis do filmu.
  ```
- **Wyjście SRT**:
  ```
  1
  00:00:01,400 --> 00:00:03,500
  Przykładowy napis numer jeden.

  2
  00:00:05,800 --> 00:00:08,000
  Drugi przykładowy napis do filmu.
  ```


### 💡 Uwagi
- Jeśli Twój plik wideo ma inną liczbę klatek na sekundę, zmień wartość `FRAME_RATE`, aby uzyskać synchronizację czasów.
- Używaj parametrów `MIN_DURATION` i `MAX_DURATION` w celu kontroli czasu wyświetlania napisów.

### 📜 Licencja
Ten projekt jest objęty licencją Creative Commons Uznanie Autorstwa–Użycie Niekomercyjne 4.0 Międzynarodowa (CC BY-NC 4.0). Możesz używać, modyfikować i udostępniać kod do celów niekomercyjnych, pod warunkiem odpowiedniego uznania autorstwa. Szczegółowe informacje znajdziesz w [pełnej treści licencji](LICENSE).

---

Miłego używania i powodzenia z napisami! Jeśli masz pytania, nie wahaj się skontaktować.
