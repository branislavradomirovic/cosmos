import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration - No Sidebar (collapsed & hidden via CSS)
st.set_page_config(
    page_title="COSMOS Platforma | Inteligencija za bolje odluke",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for landing page styling (100% Serbian, no sidebar, modern luxury aesthetic)
st.markdown("""
<style>
    /* Hide Streamlit Sidebar Completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Main container background */
    .stApp {
        background-color: #0b132b;
        color: #e0e1dd;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Top Header / Navigation Bar */
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background: #1c2541;
        border-bottom: 1px solid rgba(0, 180, 216, 0.2);
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }
    .brand-logo {
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: 1px;
        color: #ffffff;
    }
    .brand-slogan {
        font-size: 0.85rem;
        color: #d4af37;
        font-weight: 600;
    }
    .cta-button {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%);
        color: white !important;
        padding: 0.6rem 1.4rem;
        border-radius: 30px;
        font-weight: 700;
        text-decoration: none;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.4);
    }
    
    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 60%, #1e3a8a 100%);
        padding: 3.5rem 2rem;
        border-radius: 20px;
        border: 1px solid rgba(0, 180, 216, 0.3);
        box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ffffff 0%, #48cae4 50%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 1.35rem;
        color: #90e0ef;
        max-width: 850px;
        margin: 0 auto 1.5rem auto;
        line-height: 1.6;
    }
    .hero-slogan-bar {
        font-size: 1.05rem;
        color: #d4af37;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    /* Cards */
    .cosmos-card {
        background: #1c2541;
        padding: 1.8rem;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1.5rem;
        height: 100%;
    }
    .card-title-cyan {
        color: #48cae4;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    .card-title-gold {
        color: #d4af37;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }
    
    /* Highlight box */
    .quote-box {
        background: rgba(212, 175, 55, 0.08);
        border-left: 5px solid #d4af37;
        padding: 1.2rem 1.8rem;
        border-radius: 6px;
        margin: 1.8rem 0;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* Metric overrides */
    div[data-testid="stMetricValue"] {
        color: #48cae4 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #e0e1dd !important;
        font-size: 1rem !important;
    }

    /* Custom Footer */
    .footer {
        text-align: center;
        padding: 2.5rem;
        margin-top: 3rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        color: #8d99ae;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Top Navigation / Header
st.markdown("""
<div class="top-header">
    <div>
        <div class="brand-logo">COSMOS</div>
        <div class="brand-slogan">Inteligencija za bolje odluke</div>
    </div>
    <div>
        <a class="cta-button" href="#kontakt">Zatražite Demo</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">COSMOS PLATFORMA</div>
    <div class="hero-subtitle">Jedinstvena platforma za inteligentno odlučivanje, održivi razvoj i dokazima zasnovano upravljanje složenim društvenim i ekonomskim procesima</div>
    <div class="hero-slogan-bar">Podaci • Znanje • Razumevanje • Odgovornost • Bolje Odluke</div>
</div>
""", unsafe_allow_html=True)

# Key Metrics Row
col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric(label="Naučno-istraživački rad", value="25+ Godina", delta="Četvrt veka razvoja")
with col_m2:
    st.metric(label="Standardizovani indikatori", value="500+", delta="U 10+ javnih sektora")
with col_m3:
    st.metric(label="Efikasnost upravljanja", value="15–30%", delta="Društveni i finansijski efekat")
with col_m4:
    st.metric(label="Tehnološka spremnost", value="TRL 8", delta="Provereno u praksi")

st.markdown("<br>", unsafe_allow_html=True)

# Top Navigation Tabs for Landing Page Sections
tab_overview, tab_simpa, tab_ordo, tab_principles, tab_team, tab_contact = st.tabs([
    "🌌 O Platformi",
    "🤝 SIMPA Modul",
    "🏔️ ORDO Modul",
    "📜 10 Načela",
    "👥 Tim & Vizija",
    "✉️ Kontakt & Demo"
])

# ==================== SECTION 1: O PLATFORMI ====================
with tab_overview:
    st.subheader("💡 Ideja i Vizija Platforme COSMOS")
    
    st.markdown("""
    <div class="quote-box">
        <b>Red u haosu:</b> Naziv <i>COSMOS</i> potiče od antičkog shvatanja kosmosa kao uređene celine u kojoj svaka pojava dobija svoje mesto i značenje, u suprotnosti sa haosom. 
        COSMOS razvija metodologiju koja različite izvore znanja organizuje u jedinstven sistem inteligencije odlučivanja.
    </div>
    """, unsafe_allow_html=True)

    c_left, c_right = st.columns(2)
    with c_left:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-cyan">Izazov Savremenog Upravljanja</div>
            <p>Savremene institucije i organizacije raspolažu ogromnim količinama podataka. Međutim, <b>paradoks našeg vremena jeste u tome što nikada nismo znali više, a često smo sigurni manje</b>.</p>
            <p>Količina informacija raste mnogo brže od naše sposobnosti da ih povežemo u smislenu celinu. Između podataka i odluka otvorio se prostor koji nije moguće ispuniti samo bržim računarima ili složenijim algoritmima.</p>
        </div>
        """, unsafe_allow_html=True)

    with c_right:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-gold">COSMOS Rešenje</div>
            <p>COSMOS polazi od pretpostavke: <b>razumevanje prethodi odlučivanju</b>. Veštačka inteligencija u COSMOS-u je sredstvo koje pomaže da se prepoznaju obrasci, procene posledice različitih scenarija i smanji neizvesnost.</p>
            <p>Konačna odgovornost za odluku uvek ostaje u rukama čoveka. Tehnologija proširuje ljudsku sposobnost razumevanja.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🧩 5 Stubova Inteligencije Odlučivanja")
    col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
    with col_p1:
        st.markdown("#### 1. Podaci\nPolazna osnova iz svih relevantnih izvora (statistika, registri, prostorni podaci).")
    with col_p2:
        st.markdown("#### 2. Znanje\nDaje podacima značenje povezivanjem sa ciljevima i lokalnim kontekstom.")
    with col_p3:
        st.markdown("#### 3. Analitika\nPretvara podatke u kompozitne indikatore i uzročno-posledične modele.")
    with col_p4:
        st.markdown("#### 4. AI Logika\nProširuje analizu, prepoznaje skrivene obrasce i simulira 'šta-ako' scenarije.")
    with col_p5:
        st.markdown("#### 5. Čovek\nNezamenljivi završni element – čovek snosi etičku i stručnu odgovornost za odluku.")

# ==================== SECTION 2: SIMPA ====================
with tab_simpa:
    st.subheader("🤝 SIMPA – Sistem Inteligencije za Socijalnu Zaštitu i Inkluziju")
    st.caption("Podaci. Znanje. Odluke. Rezultati.")
    
    st.write("""
    **SIMPA** je specijalizovani alat platforme COSMOS namenjen planiranju, praćenju i evaluaciji lokalnih javnih politika u oblasti socijalne zaštite i inkluzije. 
    Pretvara administrative podatke iz svakodnevnog rada centara za socijalni rad (CSR), SOZIS-a i opština u pouzdane indikatore i prediktivne scenarije.
    """)
    
    st.markdown("### 📊 LISI – Lokalni Indeks Socijalne Inkluzije")
    st.write("Metodološki instrument koji objedinjuje 6 ključnih dimenzija u jedinstvenu ocenu razvijenosti socijalne zaštite:")
    
    df_lisi = pd.DataFrame({
        "Dimenzija": [
            "1. Socijalne potrebe stanovništva",
            "2. Dostupnost i razvijenost usluga",
            "3. Obuhvat građana sistemom",
            "4. Kvalitet i rezultati usluga",
            "5. Efikasnost upravljanja resursima",
            "6. Razvojni kapacitet sistema"
        ],
        "Značaj (%)": [20, 20, 15, 15, 15, 15]
    })
    fig_lisi = px.pie(df_lisi, values="Značaj (%)", names="Dimenzija", title="Dimenzije LISI Indeksa", color_discrete_sequence=px.colors.sequential.Tealgrn)
    fig_lisi.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#e0e1dd")
    st.plotly_chart(fig_lisi, use_container_width=True)

    st.markdown("### 🔄 Odnos SOZIS i SIMPA")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.info("**SOZIS (Operativni nivo)**: Prikuplja i čuva administrativne podatke, vodi pojedinačne predmete i elektronske evidencije.")
    with col_s2:
        st.success("**SIMPA (Strateški nivo)**: Pretvara SOZIS podatke u indikatore, analitičke modele, prediktivne scenarije i strateške odluke.")

    st.markdown("### 📦 Paketi Implementacije za Lokalne Samouprave")
    pk1, pk2, pk3, pk4 = st.columns(4)
    with pk1:
        st.markdown("**Paket I: Osnovna Analiza**  \n• Trajanje: 6–8 nedelja  \n• LISI indeks & socijalna mapa  \n• Osnovni komandni dashboard")
    with pk2:
        st.markdown("**Paket II: Planiranje Razvoja**  \n• Trajanje: 2–3 meseca  \n• 300+ indikatora  \n• Projekcija buduće tražnje usluga")
    with pk3:
        st.markdown("**Paket III: Inteligentno Upravljanje**  \n• Trajanje: 3–5 meseci  \n• 500+ indikatora  \n• AI analitika & CSR dashboard")
    with pk4:
        st.markdown("**Paket IV: Nacionalni Sistem**  \n• Trajanje: 6–9 meseci  \n• 1000+ indikatora  \n• GIS analitika & SOZIS integracija")

# ==================== SECTION 3: ORDO ====================
with tab_ordo:
    st.subheader("🏔️ ORDO – Razvoj i Upravljanje Turističkim Destinacijama")
    st.caption("Podaci. Znanje. Razvoj. Destinacija.")
    
    st.write("""
    **ORDO** (od latinske reči za red, poredak i sklad) objedinjuje podatke o prostoru, turizmu, lokalnoj privredi, infrastrukturi i kulturnom nasleđu radi donošenja održivih i merljivih investicionih i razvojnih odluka.
    """)
    
    st.markdown("### 🗺️ Životni Ciklus Strategije Turizma u 7 Koraka")
    
    steps = [
        ("1. Upoznaj destinaciju", "Prikupljanje i povezivanje podataka o prostoru, ljudima, privredi i infrastrukturnim kapacitetima."),
        ("2. Otkrij potencijale", "Prepoznavanje autentičnih i inkluzivnih lokalnih resursa, zanatlija i porodičnih gazdinstava."),
        ("3. Razumi odnose", "Dubinsko razumevanje uzročno-posledičnih veza ekonomije, društva i zaštite životne sredine."),
        ("4. Razvij scenarije", "Modelovanje više održivih razvojnih opcija i procena njihovih efekata pre primene."),
        ("5. Izaberi razvojni pravac", "Donosioci odluka biraju scenario koji najbolje odgovara razvojnoj viziji destinacije."),
        ("6. Oblikuj strategiju", "Pretvaranje izabranog pravca u konkretan plan sa merljivim indikatorima i projektima."),
        ("7. Prati razvoj i uči", "Kontinuirano merenje ostvarenih rezultata u odnosu na planirane i prilagođavanje novim ciklusu.")
    ]
    
    for title, desc in steps:
        st.markdown(f"✅ **{title}** — *{desc}*")

# ==================== SECTION 4: 10 NAČELA ====================
with tab_principles:
    st.subheader("📜 10 Načela Platforme COSMOS")
    st.write("Svaka analiza i alat u okviru platforme COSMOS zasniva se na istim metodološkim i etičkim pravilima:")
    
    principles = [
        ("1. Razumevanje prethodi odlučivanju", "Svaka odluka počinje pokušajem da se razume stvarnost. Podaci predstavljaju njen opis, a značenje nastaje tek kada se činjenice povežu u kontekst."),
        ("2. Inteligencija nastaje povezivanjem znanja", "COSMOS razvija inteligenciju odlučivanja povezivanjem naučnog znanja, empirijskih podataka i mogućnosti veštačke inteligencije."),
        ("3. Čovek snosi odgovornost za odluke", "Konačna odluka uvek pripada čoveku. Naši sistemi nikada nisu projektovani da odlučuju umesto ljudi, već da ljudima omoguće bolje odlučivanje."),
        ("4. Svaka preporuka mora biti objašnjiva", "Poverenje proizlazi iz razumljivosti. Korisnik mora znati zbog čega je sistem došao do određene preporuke – ne postoje 'crne kutije'."),
        ("5. Društvo i tržište čine jedinstven sistem", "Javne politike, demografski trendovi, regulatorni okvir i ekonomsko ponašanje čine jedinstven sistem međusobno povezanih odnosa."),
        ("6. Složenost je izvor znanja", "Svet nije moguće svesti na nekoliko jednostavnih pokazatelja. COSMOS tehnologija pomaže da se u složenosti prepoznaju obrasci koji omogućavaju odgovornije odluke."),
        ("7. Dokazi imaju prednost nad pretpostavkama", "Intuicija i iskustvo postaju pouzdaniji kada su zasnovani na proverljivim činjenicama. Svaki model i preporuka moraju biti utemeljeni u dokazima."),
        ("8. Tehnologija razvija ljudske sposobnosti", "Napredak nije cilj sam po sebi. Veštačka inteligencija treba da povećava ljudske sposobnosti i osnažuje institucije, a ne da ih zamenjuje."),
        ("9. Poverenje je temelj svakog alata", "Poverenje se gradi doslednošću, transparentnošću i odgovornošću. Zato je poverenje najvažniji rezultat koji želimo da ostvarimo kod korisnika."),
        ("10. Red u haosu nije cilj, već trajni proces", "Društvo, tržište i tehnologija neprestano se menjaju. COSMOS omogućava da se svet iznova razume i da se odluke donose na osnovu najboljeg raspoloživog znanja.")
    ]
    
    for title, desc in principles:
        with st.expander(f"📌 {title}"):
            st.write(desc)

# ==================== SECTION 5: TIM & VIZIJA ====================
with tab_team:
    st.subheader("👥 Tim koji je stvorio COSMOS")
    st.markdown("*Velike platforme ne grade algoritmi. Grade ih ljudi koji veruju u istu ideju.*")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-cyan">Dr Goran Bašić</div>
            <p><b>Idejni tvorac platforme COSMOS</b></p>
            <p>Autor metodologije i vizije. Više od 25 godina istraživanja odnosa između društvenih procesa, javnih politika i donošenja odluka. Razvio je koncept inteligentnog odlučivanja koji povezuje društvene nauke, indikatore i AI.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-cyan">Lana Rašković</div>
            <p><b>Menadžerka sistema</b></p>
            <p>Brine o operativnom funkcionisanju sistema, organizaciji procesa, koordinaciji implementacije i podršci korisnicima, obezbeđujući dostupnost i primenljivost metodoloških rešenja.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-gold">Dr Branislav Radomirović</div>
            <p><b>Glavni arhitekta sistema</b></p>
            <p>Pretvorio je metodološku ideju u funkcionalnu tehnološku platformu. Njegov doprinos ogleda se u razvoju arhitekture sistema, projektovanju analitičkih modula i spajanju metodologije sa softverskim rešenjima.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title-gold">Maja Anđelković</div>
            <p><b>Projektna menadžerka</b></p>
            <p>Koordinirala je razvojni proces, povezujući istraživački tim, partnere i korisnike platforme. Obezbeđuje da se razvoj COSMOS-a odvija planski, dosledno i po najvišim standardima upravljanja.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== SECTION 6: KONTAKT & DEMO ====================
with tab_contact:
    st.markdown("<a id='kontakt'></a>", unsafe_allow_html=True)
    st.subheader("✉️ Zatražite Prezentaciju i Demo Platforme COSMOS")
    st.write("Zainteresovani ste za primenu SIMPA ili ORDO alata u Vašoj jedinici lokalne samouprave, ministarstvu ili organizaciji?")
    
    with st.form("demo_form"):
        f_name = st.text_input("Ime i prezime / Funkcija")
        f_org = st.text_input("Naziv institucije / Opštine / Organizacije")
        f_email = st.text_input("Službena email adresa")
        f_module = st.selectbox("Oblast interesovanja", [
            "COSMOS Platforma (Opšta prezentacija)",
            "SIMPA (Socijalna zaštita, inkluzija & SOZIS integracija)",
            "ORDO (Održivi razvoj turističkih destinacija)",
            "Strateško savetovanje i analitika javnih politika"
        ])
        f_msg = st.text_area("Dodatne informacije / Specifični zahtevi")
        
        btn_submit = st.form_submit_button("Pošalji Upit za Demo")
        if btn_submit:
            st.success("Hvala Vam na interesovanju! Stručni tim COSMOS platforme će Vam odgovoriti u najkraćem roku.")

# Footer
st.markdown("""
<div class="footer">
    <b>COSMOS Platforma</b> • Inteligencija za bolje odluke<br>
    Znanje • Razumevanje • Odgovornost • Bolje Odluke • Bolja Budućnost<br>
    © 2026 COSMOS • <a href="http://www.cosmos.rs" style="color: #48cae4;">www.cosmos.rs</a>
</div>
""", unsafe_allow_html=True)
