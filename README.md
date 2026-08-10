# COSMOS Platforma

V1 javna landing stranica za COSMOS Platformu inteligencije odlučivanja.

Implementacija je jedna Streamlit stranica sa prilagođenim HTML/CSS slojem. SIMPA i ORDO su predstavljeni kao specijalizacije COSMOS platforme, bez funkcionalnih aplikacija, dashboarda, baze, autentifikacije ili analitičkih modula.

## Pokretanje lokalno

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud

Entrypoint:

```text
app.py
```

## Struktura

- `app.py` pokreće landing stranicu
- `styles.py` sadrži vizuelni sistem i responsive pravila
- `components.py` renderuje semantičke HTML sekcije
- `content.py` čuva javni sadržaj zasnovan na dokumentaciji
- `assets/` sadrži COSMOS, SIMPA i ORDO PDF dokumentaciju
- `reference-design/` je trajni vizuelni referentni kit
- `archive/future-pages/` čuva prethodne SIMPA/ORDO Streamlit module van aktivnog rutiranja
