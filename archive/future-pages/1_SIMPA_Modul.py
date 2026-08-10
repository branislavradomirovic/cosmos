import streamlit as st
import pandas as pd
import plotly.express as px
from styles import apply_global_styles

st.set_page_config(page_title="SIMPA Modul | COSMOS", page_icon="🤝", layout="wide")

# Apply SIMPA Theme (Tealish)
apply_global_styles(theme="simpa")

st.markdown("""
<div class="hero-banner">
    <div class="hero-tagline">SOCIJALNA UKLJUČENOST</div>
    <div class="hero-title">SIMPA</div>
    <div class="hero-subtitle">Sistem inteligencije za planiranje, monitoring i evaluaciju javnih politika socijalne zaštite.</div>
</div>
""", unsafe_allow_html=True)

st.header("🤝 SIMPA u sistemu socijalne zaštite")
st.write("SIMPA omogućava da se podaci iz različitih izvora objedine u jedinstven analitički okvir koji lokalnoj samoupravi pruža pouzdanu osnovu za razvoj inkluzivnih i efikasnih socijalnih usluga.")

st.markdown("### Vrednosti koje stvara SIMPA")
col_v1, col_v2, col_v3, col_v4 = st.columns(4)
with col_v1:
    st.info("**👥 Društvena vrednost**\n\nGrađani ostvaruju dostupnije i kvalitetnije usluge. Bolji kvalitet života.")
with col_v2:
    st.info("**🏢 Profesionalna vrednost**\n\nCentri za socijalni rad raspolažu pouzdanim pokazateljima i analitičkim alatima.")
with col_v3:
    st.info("**📈 Razvojna vrednost**\n\nLokalne samouprave planiraju sistem planski, usmeren prema potrebama.")
with col_v4:
    st.info("**💰 Finansijska vrednost**\n\nJavna sredstva ostvaruju veći društveni efekat. Isti budžet - veći efekat.")

st.markdown("---")
st.header("📊 Koji podaci su važni?")
st.write("Razvoj kvalitetnog i inkluzivnog sistema socijalne zaštite zahteva pouzdane podatke. SIMPA povezuje sledeće grupe podataka:")

col_d1, col_d2 = st.columns(2)
with col_d1:
    st.markdown("""
    - **Socijalne potrebe stanovništva** (broj korisnika, starosna i polna struktura)
    - **Siromaštvo i materijalna ugroženost** (korišćenje novčane pomoći)
    - **Porodica, deca i mladi** (mere zaštite, hraniteljstvo)
    - **Nasilje i krizne situacije** (prijave nasilja, procene rizika)
    """)
with col_d2:
    st.markdown("""
    - **Starije osobe i invaliditet** (pomoć u kući, personalna asistencija)
    - **Dostupnost socijalnih usluga** (liste čekanja, teritorijalna dostupnost)
    - **Kapaciteti lokalnog sistema** (stručni kapaciteti, finansijska izdvajanja)
    - **Međusektorska saradnja** (zajednički programi podrške)
    """)

st.markdown("---")
st.header("📈 LISI – Lokalni Indeks Socijalne Inkluzije")
st.markdown("""
<div class="highlight-box">
    LISI predstavlja jedinstveni metodološki instrument koji objedinjuje veliki broj administrativnih podataka, indikatora i analitičkih modela u jednu sveobuhvatnu ocenu razvijenosti sistema socijalne zaštite u jedinici lokalne samouprave.
</div>
""", unsafe_allow_html=True)

df_lisi = pd.DataFrame({
    "Dimenzija": [
        "Socijalne potrebe", "Dostupnost usluga", "Obuhvat građana",
        "Kvalitet usluga", "Efikasnost sredstava", "Razvojni kapacitet"
    ],
    "Značaj (%)": [20, 20, 15, 15, 15, 15]
})
fig = px.pie(df_lisi, values="Značaj (%)", names="Dimenzija", hole=0.4, color_discrete_sequence=px.colors.sequential.Tealgrn)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#fff")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.header("🔄 SIMPA kao nadogradnja sistema SOZIS")
col_s1, col_s2 = st.columns(2)
with col_s1:
    st.markdown("""
    <div class="info-card">
        <div class="card-title" style="color: #8d99ae;">SOZIS (Operativni sistem)</div>
        <div class="card-text">Prikuplja i čuva administrativne podatke, vodi evidenciju i upravlja predmetima. Fokusiran je na pojedinačne predmete i korisnike.</div>
    </div>
    """, unsafe_allow_html=True)
with col_s2:
    st.markdown("""
    <div class="info-card">
        <div class="card-title" style="color: #20b2aa;">SIMPA (Strateški sistem)</div>
        <div class="card-text">Pretvara te podatke u pokazatelje, analize i razvojne projekcije radi donošenja javnih politika. Sagledava stanje sistema u celini.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.header("🛤️ Standardna Metodologija Implementacije (10 faza)")

phases = [
    ("0. Definisanje prioriteta", "Radionice sa Ministarstvom, CSR, lokalnim akterima."),
    ("1. Analiza sistema", "Mapa lokalnog sistema i katalog podataka."),
    ("2. Modelovanje", "Jedinstveni model podataka SIMPA."),
    ("3. Integracija", "Povezivanje administrativnih podataka."),
    ("4. Kontrola kvaliteta", "Standardizacija i validacija podataka."),
    ("5. Razvoj indikatora", "Katalog SIMPA indikatora."),
    ("6. Analitičko modelovanje", "Razvoj modela za analizu socijalnih potreba."),
    ("7. Prediktivno modelovanje", "AI modeli za procenu budućih potreba."),
    ("8. Inteligencija odlučivanja", "Komandne table, socijalne mape."),
    ("9. Jačanje kapaciteta", "Obuka korisnika i pilot primena."),
    ("10. Kontinuirano unapređenje", "Evaluacija efekata lokalnih politika.")
]

for title, desc in phases:
    st.markdown(f"""
    <div class="timeline-step">
        <div class="step-title">{title}</div>
        <div class="card-text">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    <b>COSMOS Platforma</b> • Inteligentno razumevanje. Odgovorne odluke.<br>
    © 2026 COSMOS • www.cosmos.rs
</div>
""", unsafe_allow_html=True)
