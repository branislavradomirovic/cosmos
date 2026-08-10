# COSMOS Reference Design Kit

Ovaj folder je namerno odvojen od produkcionog Streamlit koda. Njegova svrha je da Codex-u pruži
konkretne vizuelne i sadržajne reference pre implementacije javnog COSMOS landing page-a.

## Fajlovi
- `index.html` — referentni glavni landing page
- `cosmos.html` — referentni COSMOS / metodologija detalj
- `simpa.html` — referentni SIMPA detalj
- `ordo.html` — referentni ORDO detalj
- `details.html` — design system / guardrails
- `assets/css/style.css` — zajednički vizuelni sistem
- `assets/img/*_cover.png` — vizuelni izvor iz priložene dokumentacije
- `screenshots/` — renderovani pregledi referentnih stranica
- `CODEX_PROMPT.md` — prompt za sledeći Codex prolaz

## Važno
Reference nisu zamišljene kao zaseban produkcioni sajt niti kao zahtev da Streamlit bude pretvoren
u JS framework. Codex treba da reprodukuje kompoziciju, hijerarhiju, osećaj, paletu i ponašanje u
postojećoj Streamlit aplikaciji.

V1 ostaje samo javni landing page. SIMPA i ORDO su sekcije / detaljni sadržaj, ne funkcionalne aplikacije.
