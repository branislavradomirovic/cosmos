import streamlit as st
from styles import apply_global_styles

st.set_page_config(page_title="ORDO Modul | COSMOS", page_icon="🏔️", layout="wide")

# Apply ORDO Theme (Navy/Gold)
apply_global_styles(theme="ordo")

st.markdown("""
<div class="hero-banner">
    <div class="hero-tagline">RAZVOJ DESTINACIJA</div>
    <div class="hero-title">ORDO</div>
    <div class="hero-subtitle">Sistem inteligencije za razvoj, upravljanje i unapređenje turističkih destinacija.</div>
</div>
""", unsafe_allow_html=True)

st.header("🏔️ Šta je ORDO?")
st.write("**ORDO** (od latinske reči za red, poredak i sklad) je alat platforme COSMOS razvijen za podršku planiranju, razvoju i upravljanju turističkim destinacijama. Njegova svrha je da objedini podatke, znanje, analitiku, veštačku inteligenciju i ljudsko iskustvo u jedinstven sistem inteligencije odlučivanja.")

st.markdown("### 5 Stubova Inteligencije Odlučivanja")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.info("**🗺️ Podaci**\n\nPrirodni resursi, turistički tokovi, privreda, infrastruktura, životna sredina.")
with col2:
    st.info("**📚 Znanje**\n\nDaje podacima značenje povezivanjem sa ciljevima i lokalnim iskustvom.")
with col3:
    st.info("**📈 Analitika**\n\nOrganizacija u pokazatelje, otkrivanje uzročno-posledičnih odnosa.")
with col4:
    st.info("**🤖 AI**\n\nPrepoznaje obrasce, simulira scenarije i procenjuje buduće efekte.")
with col5:
    st.info("**👥 Ljudi**\n\nZavršni element: tehnologija podržava, čovek donosi odluku.")

st.markdown("---")
st.header("💡 Filozofija: Razvoj počinje razumevanjem")
st.markdown("""
<div class="highlight-box">
    Razvoj turističkih destinacija dugo je bio usmeren na povećanje broja posetilaca. Dugoročno uspešne destinacije stvaraju ekonomsku vrednost, unapređuju kvalitet života lokalne zajednice i čuvaju kulturno nasleđe.
</div>
""", unsafe_allow_html=True)
st.write("Jedno od osnovnih načela ORDO jeste razvojna inkluzija. Lokalni proizvođači, zanatlije, porodična gazdinstva i kreativne industrije predstavljaju ključni kapital koji obogaćuje turističku ponudu i jača autentičnost destinacije.")

st.markdown("---")
st.header("⚙️ Arhitektura ORDO")
st.write("Metodološki okvir koji razvojnu filozofiju pretvara u inteligenciju odlučivanja:")

steps = [
    ("1. Poslovni cilj", "Definiše razvojnu ambiciju i usmerava analizu."),
    ("2. Integracija izvora", "Objedinjuje tržište, prostor, privredu i ekologiju."),
    ("3. Poslovni indikatori", "Pretvara podatke u merljiv jezik razvoja."),
    ("4. Analitičko modelovanje", "Otkriva obrasce i uzročno-posledične odnose."),
    ("5. Prediktivna logika", "Procena efekata različitih razvojnih scenarija."),
    ("6. Sinteza znanja", "Pouzdana osnova za strateško planiranje."),
    ("7. Poslovno odlučivanje", "Strategije i planovi zasnovani na znanju, a ne na pretpostavkama.")
]

c1, c2 = st.columns(2)
for i, (title, desc) in enumerate(steps):
    col = c1 if i % 2 == 0 else c2
    with col:
        st.markdown(f"""
        <div class="info-card" style="margin-bottom: 1rem; padding: 1.5rem;">
            <div class="card-title" style="color: #d4af37; font-size: 1.1rem;">{title}</div>
            <div class="card-text">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.header("🔄 Životni Ciklus Strategije Turizma (7 koraka)")
st.write("Put od podataka do razvoja – ORDO vodi proces, Vi donosite odluke.")

lifecycle = [
    ("1. Upoznaj destinaciju", "Prikupljanje i povezivanje podataka o prostoru, ljudima, privredi i turizmu."),
    ("2. Otkrij potencijale", "Prepoznavanje prirodnih, kulturnih, ekonomskih i inkluzivnih potencijala."),
    ("3. Razumi odnose", "Analiza međusobnih uticaja ekonomskih, društvenih i ekoloških činilaca."),
    ("4. Razvij scenarije", "Modelovanje opcija i procena efekata na konkurentnost, zapošljavanje i održivost."),
    ("5. Izaberi razvojni pravac", "Donosioci odluka biraju scenario sa najvećom ukupnom vrednošću."),
    ("6. Oblikuj strategiju", "Pretvaranje izabranog pravca u ciljeve, mere, projekte i indikatore."),
    ("7. Prati razvoj i uči", "Merenje rezultata, poređenje efekata i kontinuirano unapređenje strategije.")
]

for title, desc in lifecycle:
    st.markdown(f"""
    <div class="timeline-step">
        <div class="step-title" style="color: #d4af37;">{title}</div>
        <div class="card-text">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="custom-footer">
    <b>COSMOS Platforma</b> • Inteligentno razumevanje. Odgovorne odluke.<br>
    © 2026 COSMOS • www.cosmos.rs
</div>
""", unsafe_allow_html=True)
