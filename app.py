import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="COSMOS Platforma | Inteligencija za bolje odluke",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for premium look & feel
st.markdown("""
<style>
    /* Main background and fonts */
    .stApp {
        background-color: #0b132b;
        color: #e0e1dd;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Header hero styling */
    .hero-container {
        background: linear-gradient(135deg, #1c2541 0%, #0b132b 60%, #3a506b 100%);
        padding: 3rem 2rem;
        border-radius: 16px;
        border: 1px solid rgba(0, 180, 216, 0.2);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 2rem;
        text-align: center;
    }
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #ffffff 0%, #48cae4 50%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    .hero-subtitle {
        font-size: 1.4rem;
        color: #90e0ef;
        font-weight: 400;
        margin-bottom: 1.5rem;
    }
    .hero-slogan {
        font-size: 1.1rem;
        color: #d4af37;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Card styling */
    .cosmos-card {
        background: #1c2541;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 1.2rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .cosmos-card:hover {
        border-color: #00b4d8;
        transform: translateY(-2px);
    }
    .card-title {
        color: #48cae4;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .card-gold-title {
        color: #d4af37;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Pillar badge */
    .pillar-badge {
        display: inline-block;
        background: rgba(0, 180, 216, 0.15);
        color: #48cae4;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    /* Highlight box */
    .highlight-box {
        background: rgba(212, 175, 55, 0.1);
        border-left: 4px solid #d4af37;
        padding: 1rem 1.5rem;
        border-radius: 4px;
        margin: 1.5rem 0;
    }

    /* Metric styling */
    div[data-testid="stMetricValue"] {
        color: #48cae4 !important;
        font-weight: 700;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #070d1e;
        border-right: 1px solid rgba(255,255,255,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Navigation Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/space.png", width=64)
    st.title("COSMOS")
    st.caption("Inteligencija za bolje odluke")
    st.divider()
    
    page = st.radio(
        "Navigacija",
        [
            "🏠 Početna",
            "🌌 O Platformi COSMOS",
            "🤝 SIMPA (Socijalna Inkluzija)",
            "🏔️ ORDO (Razvoj Destinacija)",
            "📜 10 Načela & Standardi",
            "👥 Tim & Ekosistem",
            "🧮 Interaktivni Simulatori",
            "✉️ Kontakt & Demo"
        ]
    )
    
    st.divider()
    st.info("💡 **COSMOS Web App**  \nPripremljeno za objavu na *Streamlit Community Cloud*.")

# ==================== PAGE 1: POČETNA ====================
if page == "🏠 Početna":
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title">COSMOS PLATFORMA</div>
        <div class="hero-subtitle">Platforma za inteligentno odlučivanje, održivi razvoj i dokazima zasnovano upravljanje</div>
        <div class="hero-slogan">Podaci • Znanje • Razumevanje • Odgovornost • Bolje Odluke</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Godina naučnog rada", value="25+", delta="Četvrt veka iskustva")
    with col2:
        st.metric(label="Standardizovanih indikatora", value="500+", delta="U 10+ domena")
    with col3:
        st.metric(label="Povećanje efikasnosti", value="15-30%", delta="Društveni & finansijski efekat")
    with col4:
        st.metric(label="Nivo tehnološke spremnosti", value="TRL 8", delta="Dokazano u praksi")

    st.markdown("### 🌟 Specijalizovani alati platforme COSMOS")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title">🤝 SIMPA</div>
            <p><b>Sistem inteligencije za planiranje, monitoring i evaluaciju javnih politika socijalne zaštite i inkluzije.</b></p>
            <p>Povezuje administrativne podatke centara za socijalni rad, SOZIS-a i lokalnih samouprava u jedinstven analitički okvir koji pretvara podatke u znanje i pravednije usluge za građane.</p>
            <span class="pillar-badge">LISI Indeks</span>
            <span class="pillar-badge">Preventivno delovanje</span>
            <span class="pillar-badge">SOZIS Nadogradnja</span>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-gold-title">🏔️ ORDO</div>
            <p><b>Sistem inteligencije za razvoj, upravljanje i unapređenje turističkih destinacija.</b></p>
            <p>Objedinjuje podatke o prostoru, turizmu, lokalnoj privredi, infrastrukturi i kulturnom nasleđu radi donošenja održivih i merljivih investicionih i razvojnih odluka.</p>
            <span class="pillar-badge">5 Stubova Odlučivanja</span>
            <span class="pillar-badge">Virtuelni Scenariji</span>
            <span class="pillar-badge">Održivi Turizam</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧩 5 Stubova Inteligencije Odlučivanja")
    
    col_p1, col_p2, col_p3, col_p4, col_p5 = st.columns(5)
    with col_p1:
        st.markdown("**1. Podaci**  \nPolazna osnova iz svih relevantnih izvora (prostorni, privredni, demografski).")
    with col_p2:
        st.markdown("**2. Znanje**  \nDaje podacima značenje povezivanjem sa ciljevima i lokalnim kontekstom.")
    with col_p3:
        st.markdown("**3. Analitika**  \nPretvara podatke u kompozitne indikatore i uzročno-posledične modele.")
    with col_p4:
        st.markdown("**4. Veštačka Inteligencija**  \nProširuje analizu, prepoznaje skrivene obrasce i simulira scenarije.")
    with col_p5:
        st.markdown("**5. Ljudsko Iskustvo**  \nNezamenljivi završni element – čovek donosi konačnu odluku.")

# ==================== PAGE 2: O PLATFORMI ====================
elif page == "🌌 O Platformi COSMOS":
    st.header("🌌 O Platformi COSMOS")
    st.caption("Jedna platforma. Više oblasti odlučivanja. Jedinstvena metodologija.")
    
    st.markdown("""
    <div class="highlight-box">
        <b>Filozofska osnova:</b> Naziv <i>COSMOS</i> potiče od latinske i antičke grčke reči koja označava uređenu celinu, poredak i sklad u suprotnosti sa haosom. U tom izvornom značenju, kosmos označava razumljivu celinu u kojoj događaji nisu nasumični, već povezani odnosima koji se mogu otkriti i razumeti.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Zašto nastaje COSMOS?")
    st.write("""
    Savremene organizacije raspolažu ogromnim količinama podataka. Međutim, **paradoks našeg vremena jeste u tome što nikada nismo znali više, a često smo sigurni manje**. 
    Količina informacija raste mnogo brže od naše sposobnosti da ih povežemo u smislenu celinu. 

    COSMOS premošćuje taj jaz povezivanjem **naučnog znanja**, **empirijskih podataka** i **veštačke inteligencije** u jedinstven sistem podrške ljudskom odlučivanju.
    """)
    
    st.subheader("🏗️ Metodološki tok nastanka znanja")
    
    steps_df = pd.DataFrame({
        "Faza": ["1. Definisati problem", "2. Integracija izvora", "3. Poslovni indikatori", "4. Analitičko modelovanje", "5. Prediktivna logika", "6. Sinteza znanja", "7. Podrška odlučivanju"],
        "Opis": [
            "Problem određuje analizu – postavljanje jasnog cilja.",
            "Objedinjavanje podataka (statistika, registri, AI, prostorni podaci).",
            "Pretvaranje podataka u merljive i uporedive pokazatelje.",
            "Otkrivanje uzročno-posledičnih veza i razvojnih obrazaca.",
            "Simulacija 'šta-ako' scenarija i procena verovatnoća.",
            "Integracija svih nalaza u celovitu sliku.",
            "Jasne, objašnjive preporuke za donosioce odluka."
        ]
    })
    st.table(steps_df)

# ==================== PAGE 3: SIMPA ====================
elif page == "🤝 SIMPA (Socijalna Inkluzija)":
    st.header("🤝 SIMPA – Sistem Inteligencije za Socijalnu Zaštitu i Inkluziju")
    st.markdown("*Podaci. Znanje. Odluke. Rezultati.*")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📌 Pregled & Vrednosti", "📊 LISI Indeks", "⚙️ SOZIS Nadogradnja", "📦 Paketi Usluga"])
    
    with tab1:
        st.subheader("Šta je SIMPA?")
        st.write("""
        **SIMPA** je specijalizovani alat platforme COSMOS namenjen planiranju, praćenju i evaluaciji lokalnih javnih politika u oblasti socijalne zaštite i inkluzije. 
        Pretvara administrative podatke iz svakodnevnog rada centara za socijalni rad, ustanova i opština u pouzdane indikatore i razvojne projekcije.
        """)
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("#### 💚 Društvena Vrednost")
            st.caption("Dostupnije i kvalitetnije usluge za svakog građanina.")
        with c2:
            st.markdown("#### 🏛️ Profesionalna Vrednost")
            st.caption("Manje administracije, jača stručna podrška za CSR.")
        with c3:
            st.markdown("#### 📈 Razvojna Vrednost")
            st.caption("Planiranje usluga tamo gde su potrebe najveće.")
        with c4:
            st.markdown("#### 💶 Finansijska Vrednost")
            st.caption("Veći efekat ulaganja (15-30% više efikasnosti).")
            
    with tab2:
        st.subheader("📊 LISI – Lokalni Indeks Socijalne Inkluzije")
        st.write("LISI predstavlja jedinstveni metodološki instrument koji objedinjuje 6 ključnih dimenzija razvoja:")
        
        dims = {
            "Dimenzija": ["1. Socijalne potrebe stanovništva", "2. Dostupnost i razvijenost usluga", "3. Obuhvat građana sistemom", "4. Kvalitet i rezultati usluga", "5. Efikasnost upravljanja resursima", "6. Razvojni kapacitet sistema"],
            "Udeo u indeksu (%)": [20, 20, 15, 15, 15, 15]
        }
        df_lisi = pd.DataFrame(dims)
        
        fig = px.pie(df_lisi, values="Udeo u indeksu (%)", names="Dimenzija", title="Struktura LISI Indeksa", color_discrete_sequence=px.colors.sequential.Tealgrn)
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#e0e1dd")
        st.plotly_chart(fig, use_container_width=True)
        
    with tab3:
        st.subheader("🔄 Odnos SOZIS i SIMPA")
        st.write("""
        * **SOZIS**: Operativni informacioni sistem (prikuplja i čuva administrativne podatke, vodi evidencije i predmete).
        * **SIMPA**: Strateški sistem inteligencije (pretvara SOZIS podatke u indikatore, analitičke modele, simulative scenarije i strateške odluke).
        """)
        st.success("SOZIS obezbeđuje podatke ➡️ SIMPA iz njih razvija znanje za upravljanje!")

    with tab4:
        st.subheader("📦 Paketi Implementacije SIMPA")
        p1, p2, p3, p4 = st.columns(4)
        with p1:
            st.markdown("**Paket I: Osnovna analiza**  \n- Trajanje: 6-8 nedelja  \n- Orijentaciono: 15k-20k EUR  \n- Osnovni dashboard & LISI")
        with p2:
            st.markdown("**Paket II: Planiranje razvoja**  \n- Trajanje: 2-3 meseca  \n- Orijentaciono: 30k-40k EUR  \n- 300+ indikatora & projekcije")
        with p3:
            st.markdown("**Paket III: Inteligentno upravljanje**  \n- Trajanje: 3-5 meseci  \n- Orijentaciono: 50k-70k EUR  \n- AI analitika & CSR dashboard")
        with p4:
            st.markdown("**Paket IV: Nacionalni sistem**  \n- Trajanje: 6-9 meseci  \n- Orijentaciono: 80k-150k EUR  \n- GIS analitika & SOZIS sinhronizacija")

# ==================== PAGE 4: ORDO ====================
elif page == "🏔️ ORDO (Razvoj Destinacija)":
    st.header("🏔️ ORDO – Razvoj i Upravljanje Turističkim Destinacijama")
    st.markdown("*Podaci. Znanje. Razvoj. Destinacija.*")
    
    st.markdown("""
    **ORDO** (od latinske reči za red, poredak i sklad) objedinjuje podatke, analitiku, veštačku inteligenciju i stručno iskustvo u sistem inteligencije odlučivanja za održivi razvoj opština, gradova i turističkih regija.
    """)
    
    st.subheader("🗺️ Put od podataka do razvoja – Životni ciklus strategije")
    
    ordo_steps = [
        "1. Upoznaj destinaciju (Prikupljanje podataka o prostoru, kulturi, privredi, demografiji)",
        "2. Otkrij potencijale (Identifikovanje autentičnih i inkluzivnih lokalnih resursa)",
        "3. Razumi odnose (Analiza uzročno-posledičnih veza ekonomije i zaštite sredine)",
        "4. Razvij scenarije (Modelovanje održivih razvojnih opcija)",
        "5. Izaberi pravac (Donosioci odluka biraju optimalni scenario)",
        "6. Oblikuj strategiju (Konkretan plan realizacije i merljivi ciljevi)",
        "7. Prati i uči (Kontinuirana evaluacija i unapređenje)"
    ]
    for step in ordo_steps:
        st.markdown(f"✅ **{step}**")

# ==================== PAGE 5: NAČELA & STANDARDI ====================
elif page == "📜 10 Načela & Standardi":
    st.header("📜 10 Načela COSMOS Platforme")
    
    principles = [
        ("1. Razumevanje prethodi odlučivanju", "Podaci su opis, a značenje nastaje tek kada se činjenice stope u kontekst."),
        ("2. Inteligencija nastaje povezivanjem znanja", "Spajanje naučnog znanja, empirije i veštačke inteligencije."),
        ("3. Čovek snosi odgovornost za odluke", "AI daje procene i scenarije, ali konačni izbor i etička odgovornost pripadaju čoveku."),
        ("4. Svaka preporuka mora biti objašnjiva", "Ne postoje 'crne kutije' – svaka preporuka je proverljiva i prozirna."),
        ("5. Društvo i tržište čine jedinstven sistem", "Javne politike, ekonomija i demografija deluju u međusobnoj sprezi."),
        ("6. Složenost je izvor znanja", "Svet se ne pojednostavljuje veštački, već se u njegovoj složenosti otkrivaju obrasci."),
        ("7. Dokazi imaju prednost nad pretpostavkama", "Intuicija dobija pravu snagu kada se utemelji u proverljivim podacima."),
        ("8. Tehnologija razvija ljudske sposobnosti", "Cilj je osnaživanje donosilaca odluka, a ne njihova zamena."),
        ("9. Poverenje je temelj svakog alata", "Poverenje se gradi doslednošću, transparentnošću i proverljivošću."),
        ("10. Red u haosu nije cilj, već trajni proces", "Svet se neprestano menja, pa je razumevanje kontinuirani rad.")
    ]
    
    for title, desc in principles:
        with st.expander(f"📌 {title}"):
            st.write(desc)

# ==================== PAGE 6: TIM & EKOSISTEM ====================
elif page == "👥 Tim & Ekosistem":
    st.header("👥 Tim koji je stvorio COSMOS")
    st.write("Velike platforme ne grade algoritmi. Grade ih ljudi koji veruju u istu ideju.")
    
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title">Dr Goran Bašić</div>
            <p><b>Idejni tvorac platforme COSMOS</b></p>
            <p>Autor metodologije i vizije. Više od 25 godina istraživanja odnosa između društvenih procesa, javnih politika i odlučivanja.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-title">Lana Rašković</div>
            <p><b>Menadžerka sistema</b></p>
            <p>Brine o operativnom funkcionisanju sistema, organizaciji procesa, koordinaciji implementacije i podršci korisnicima.</p>
        </div>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown("""
        <div class="cosmos-card">
            <div class="card-gold-title">Dr Branislav Radomirović</div>
            <p><b>Glavni arhitekta sistema</b></p>
            <p>Pretvorio je metodološku ideju u funkcionalnu tehnološku platformu, projektujući analitičke module i napredne softverske arhitekture.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="cosmos-card">
            <div class="card-gold-title">Maja Anđelković</div>
            <p><b>Projektna menadžerka</b></p>
            <p>Koordinira istraživački tim, razvojne partnere i međunarodnu saradnju, obezbeđujući planski i dosledan razvoj.</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== PAGE 7: INTERAKTIVNI SIMULATORI ====================
elif page == "🧮 Interaktivni Simulatori":
    st.header("🧮 Interaktivni Simulatori Inteligencije Odlučivanja")
    st.caption("Isprobajte democikle odlučivanja za SIMPA i ORDO modele.")
    
    sim_type = st.radio("Izaberite simulator:", ["🤝 SIMPA: Efekat ulaganja u socijalnu zaštitu", "🏔️ ORDO: Turistički i ekonomski scenario destinacije"], horizontal=True)
    
    if "SIMPA" in sim_type:
        st.subheader("📊 SIMPA Simulator društvenog i finansijskog učinka")
        budget = st.slider("Godišnji budžet opštine za socijalnu zaštitu (€)", 100000, 5000000, 800000, step=50000)
        population = st.number_input("Broj stanovnika opštine", 10000, 500000, 50000)
        
        # Calculation based on SIMPA whitepaper (15-30% value return)
        min_eff = budget * 0.15
        max_eff = budget * 0.30
        avg_eff = (min_eff + max_eff) / 2
        
        st.markdown("---")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Godišnja izdvajanja po stanovniku", f"€{budget/population:.2f}")
        with col_m2:
            st.metric("Procenjena oslobođena vrednost (Min)", f"€{min_eff:,.0f}")
        with col_m3:
            st.metric("Procenjena oslobođena vrednost (Max)", f"€{max_eff:,.0f}")
            
        st.success(f"Primena SIMPA platforme u opštini sa {population:,} stanovnika može osloboditi **€{min_eff:,.0f} do €{max_eff:,.0f}** dodate vrednosti bez smanjenja obima usluga!")

        # Chart
        df_sim = pd.DataFrame({
            "Kategorija": ["Efikasnije planiranje budžeta (5%)", "Razvoj inkluzivnih usluga (4%)", "Upravljanje kapacitetima (3%)", "Automatizacija administracije (3%)"],
            "Procjena uštede/efekta (€)": [budget*0.05, budget*0.04, budget*0.03, budget*0.03]
        })
        fig_sim = px.bar(df_sim, x="Kategorija", y="Procjena uštede/efekta (€)", color="Kategorija", title="Struktura ostvarenih efekata po oblastima")
        fig_sim.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="#e0e1dd", showlegend=False)
        st.plotly_chart(fig_sim, use_container_width=True)

    else:
        st.subheader("🏔️ ORDO Scenario Razvoja Destinacije")
        tourists = st.slider("Trenutni godišnji broj turista", 5000, 500000, 50000)
        invest = st.slider("Planirane investicije u infrastrukturu i kulturu (€)", 50000, 2000000, 300000)
        
        est_growth = (invest / 100000) * 1.5
        new_tourists = int(tourists * (1 + est_growth/100))
        
        st.markdown("---")
        c_o1, c_o2 = st.columns(2)
        with c_o1:
            st.metric("Očekivani rast turističkog prometa", f"+{est_growth:.1f}%")
        with c_o2:
            st.metric("Procenjeni novi godišnji broj posetilaca", f"{new_tourists:,}")

# ==================== PAGE 8: KONTAKT ====================
elif page == "✉️ Kontakt & Demo":
    st.header("✉️ Kontaktirajte COSMOS Tim")
    st.write("Zainteresovani ste za primenu SIMPA ili ORDO alata u Vašoj jedinici lokalne samouprave ili organizaciji?")
    
    with st.form("contact_form"):
        name = st.text_input("Ime i prezime / Organizacija")
        email = st.text_input("Email adresa")
        interest = st.selectbox("Zainteresovani ste za:", ["COSMOS Platforma (Opšte)", "SIMPA (Socijalna inkluzija & SOZIS)", "ORDO (Razvoj turističkih destinacija)", "Međunarodna saradnja / Partnerstvo"])
        message = st.text_area("Poruka / Upit za demo")
        
        submitted = st.form_submit_request if hasattr(st, 'form_submit_request') else st.form_submit_button("Pošalji Upit")
        
        if submitted:
            st.success("Hvala Vam na interesovanju! COSMOS tim će Vas kontaktirati u najkraćem roku.")
            
    st.divider()
    st.markdown("📍 **COSMOS Platforma** | www.cosmos.rs")
