# 🌌 COSMOS Platform – Professional Landing Page & App

Ovaj repozitorijum sadrži dva glavna dela COSMOS platforme:
1. **Zvaničnu Landing Stranicu (Static Site)** - Profesionalna prezentacija COSMOS platforme, SIMPA i ORDO modula.
2. **Interaktivnu Streamlit Aplikaciju** - Analitički alati, kalkulatori i simulatori odluka.

---

## 🚀 Pokretanje Landing Stranice (Novo)

Nova profesionalna landing stranica nalazi se u folderu `site/`. S obzirom da je reč o statičkoj HTML/CSS/JS stranici, pokretanje je izuzetno jednostavno:

1. Otvorite folder `site/`.
2. Dvostrukim klikom otvorite fajl `index.html` u bilo kom modernom pretraživaču (Chrome, Firefox, Safari).

*Nije potrebno instalirati server niti pokretati Python skripte za pregled landing stranice.*

---

## 📊 Pokretanje Streamlit Aplikacije (Interaktivni alati)

### 1. Preduslovi
Ensure you have Python 3.9+ installed on your system.

### 2. Instalacija zavisnosti
Open your terminal in this directory and run:
```bash
pip install -r requirements.txt
```

### 3. Pokretanje Streamlit Aplikacije
Run the following command:
```bash
streamlit run app.py
```
The application will automatically open in your default browser at `http://localhost:8501`.

---

## ☁️ How to Publish on Streamlit Community Cloud

Deploying this application to **Streamlit Community Cloud** (free hosting) takes less than 2 minutes:

1. **Push to GitHub**:
   - Create a new public repository on GitHub (e.g. `cosmos-platform-app`).
   - Push all files from `/Users/branislavradomirovic/Applications/Python/COSMOS` to your GitHub repo.

2. **Deploy on Streamlit**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and log in with your GitHub account.
   - Click **"New app"**.
   - Select your repository (`cosmos-platform-app`), branch (`main`), and set Main file path to `app.py`.
   - Click **"Deploy!"**.

Your application will be live with a public URL (e.g. `https://cosmos-platform.streamlit.app`).

---

## 🏛️ Platform Features Included

- **COSMOS Architecture & 5 Pillars**: Data, Knowledge, Analytics, Artificial Intelligence, and Human Experience.
- **SIMPA Module**: Social Inclusion Decision Intelligence, Local Index of Social Inclusion (LISI), SOZIS integration details, and implementation packages.
- **ORDO Module**: Destination Intelligence & Development Lifecycle.
- **10 Core Principles & Standards**: Comprehensive interactive breakdown of COSMOS methodology.
- **Team & Vision**: Profiles of Dr. Goran Bašić, Dr. Branislav Radomirović, Lana Rašković, and Maja Anđelković.
- **Interactive Calculators**: Real-time financial/social ROI simulator for municipalities & tourism development scenario calculator.
