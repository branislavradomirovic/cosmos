# CODEX PROMPT — COSMOS LANDING PAGE V2

You already attempted the COSMOS landing page once. The previous result did not match the desired visual quality.

This iteration has a different workflow:

## 0. DO NOT START CODING IMMEDIATELY

First inspect the complete repository and the supplied PDF documentation.

Then inspect the new design-reference folder:

- `reference-design/index.html`
- `reference-design/cosmos.html`
- `reference-design/simpa.html`
- `reference-design/ordo.html`
- `reference-design/details.html`
- `reference-design/assets/css/style.css`
- `reference-design/screenshots/`

The HTML pages are NOT production code that you must copy verbatim.

They are the VISUAL AND INFORMATION-ARCHITECTURE REFERENCE.

Your Streamlit implementation must reproduce their:
- visual hierarchy
- whitespace
- typography scale
- color system
- section rhythm
- COSMOS/SIMPA/ORDO relationship
- serious institutional tone
- responsive behavior
- restrained use of cards
- radial / network / concentric-circle visual language

## 1. ABSOLUTE SCOPE

Build ONLY a public COSMOS landing experience.

No functional SIMPA app.
No functional ORDO app.
No dashboards.
No Plotly.
No pandas unless genuinely required.
No GIS.
No login.
No database.
No API.
No AI chat.
No fake analytics.
No fake screenshots.
No multipage Streamlit product in this phase.

SIMPA and ORDO are presented as specialized COSMOS applications/modules.

## 2. SOURCE OF TRUTH

Use the attached documents as authoritative content sources:
- `IDENTITET I KNJIGA STANDARDA.pdf`
- `ORDO OSNOVNI DOC.pdf`
- `SIMPA u sistemu socijalne zaštite.pdf`

Do not invent claims.

All public copy must be Serbian Latin script with correct diacritics.

## 3. TARGET

The final page should feel like:
institutional credibility + research/consulting sophistication + modern decision-intelligence technology.

It must NOT feel like:
a Streamlit demo, admin dashboard, crypto site, cyberpunk AI page, generic SaaS template or student project.

The runtime may be Streamlit, but the visitor should feel that they opened the official COSMOS platform website.

## 4. VISUAL REFERENCE PRIORITY

When implementation choices are ambiguous, follow this priority:

1. supplied PDF brand/identity documents
2. `reference-design/details.html`
3. `reference-design/index.html`
4. SIMPA and ORDO reference pages
5. existing project code

The existing project code is the LOWEST priority for visual decisions because the purpose of this iteration is a redesign.

## 5. REQUIRED PUBLIC STRUCTURE

Create one long-form public page with:

1. Sticky navigation
2. COSMOS hero
3. "Razumevanje prethodi odlučivanju"
4. Nauka / Podaci / Veštačka inteligencija
5. Human responsibility statement
6. COSMOS ecosystem
7. SIMPA overview
8. ORDO overview
9. COSMOS methodology / 5-step process
10. Trust / standards
11. Final CTA
12. Minimal footer

Default preference: one public page.

## 6. DESIGN TOKENS

Derive exact values from the reference CSS and supplied documents.

Core:
- warm off-white background
- white surfaces
- deep forest green
- fresh secondary green
- dark green/black ink
- restrained neutral borders

SIMPA:
- deep navy
- teal/cyan

ORDO:
- deep navy
- muted premium gold

Do not use the old generic blue gradient.

## 7. STREAMLIT-SPECIFIC GUARDRAILS

Avoid default-looking Streamlit widgets.

Do NOT use:
- emoji icons
- `st.info` cards as primary UI
- `st.metric`
- default sidebar
- expanders as main content architecture
- big dark `.stApp` dashboard theme
- Plotly for decorative visuals

Prefer:
- controlled HTML sections
- CSS variables
- custom grid/flex layout
- inline SVG/CSS visual motifs
- semantic headings
- local brand assets
- minimal Streamlit chrome

Do not rely heavily on fragile internal Streamlit DOM selectors.
Custom HTML should carry most of the visual styling.

## 8. BRAND ASSETS

Inspect `reference-design/assets/img/` and the PDFs.

Do not invent a new logo.

Use clean existing brand assets where technically appropriate.

## 9. RESPONSIVENESS

Test at least:
- 1440px desktop
- ~900px tablet
- ~390px mobile

No horizontal scroll.
No broken nav.
No 5-column microscopic cards on mobile.
Hero typography must scale properly.

## 10. CONTENT DISCIPLINE

Do not paste entire PDF chapters into the landing page.

Use concise editorial copy.

The landing page is a public narrative:
problem → COSMOS philosophy → platform → SIMPA/ORDO → methodology → trust → CTA.

It is NOT product documentation.

Do not expose SIMPA pricing/packages in this version.

## 11. IMPLEMENTATION

Keep architecture simple:
- `app.py`
- `styles.py`
- optionally `components.py`
- optionally `content.py`
- `.streamlit/config.toml`
- `assets/`

Remove unused dependencies and obsolete active `pages/` behavior.

The app must run with:
`streamlit run app.py`

## 12. VALIDATION BEFORE COMPLETION

Before reporting done:
- run the app
- fix all errors
- verify assets
- verify one public experience
- verify no sidebar
- verify no emoji
- verify no Plotly demo
- verify no fake product functionality
- compare visually against the reference screenshots
- inspect mobile layout
- verify Serbian diacritics
- verify all factual product claims against the PDFs

## 13. FINAL REPORT

Return:
- files changed
- files removed/archived
- dependencies removed/added
- how each reference page influenced the implementation
- any content intentionally omitted due insufficient source support
- exact local command
- Streamlit Community Cloud entrypoint
- remaining caveats

STOP after the landing page is complete. Do not continue into SIMPA/ORDO application development.
