import base64
import html
import mimetypes
from pathlib import Path
from textwrap import dedent

import streamlit as st

from content import (
    CONCEPT_PILLARS,
    ECOSYSTEM_COPY,
    HERO_COPY,
    METHODOLOGY_STEPS,
    ORDO_FLOW,
    ORDO_PILLARS,
    PRODUCT_CARDS,
    SIMPA_FLOW,
    SIMPA_METRICS,
    TRUST_ITEMS,
    UNDERSTANDING_COPY,
)


ROOT = Path(__file__).parent


def _escape(value: str) -> str:
    return html.escape(value, quote=True)


def _asset_uri(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.exists():
        return ""

    mime, _ = mimetypes.guess_type(path.name)
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime or 'application/octet-stream'};base64,{encoded}"


def _brand_markup() -> str:
    brand_uri = _asset_uri("reference-design/assets/img/core_brand.png")
    if not brand_uri:
        return '<span class="brand-fallback">COSMOS</span>'
    return f'<img src="{brand_uri}" alt="COSMOS">'


def _pillar_cards() -> str:
    return "\n".join(
        f"""
        <div class="pillar">
            <div class="num">{_escape(item["number"])}</div>
            <h3>{_escape(item["title"])}</h3>
            <p>{_escape(item["text"])}</p>
        </div>
        """
        for item in CONCEPT_PILLARS
    )


def _product_cards() -> str:
    cards = []
    for product in PRODUCT_CARDS:
        chips = "".join(f'<span class="chip">{_escape(chip)}</span>' for chip in product["chips"])
        cards.append(
            f"""
            <div class="product {_escape(product["theme"])}">
                <div class="tag">{_escape(product["tag"])}</div>
                <h3>{_escape(product["title"])}</h3>
                <div class="motto">{_escape(product["motto"])}</div>
                <p>{_escape(product["text"])}</p>
                <div class="chips">{chips}</div>
                <a class="link" href="{_escape(product["href"])}">{_escape(product["link"])}</a>
            </div>
            """
        )
    return "\n".join(cards)


def _metrics(items: list[tuple[str, str, str]], extra_class: str = "") -> str:
    cards = "\n".join(
        f"""
        <div class="metric">
            <div class="top">{_escape(top)}</div>
            <h3>{_escape(title)}</h3>
            <p>{_escape(text)}</p>
        </div>
        """
        for top, title, text in items
    )
    return f'<div class="metric-grid {extra_class}">{cards}</div>'


def _flow_cards(items: list[tuple[str, str, str]], extra_class: str = "") -> str:
    cards = "\n".join(
        f"""
        <div class="flow-card">
            <div class="num">{_escape(number)}</div>
            <h3>{_escape(title)}</h3>
            <p>{_escape(text)}</p>
        </div>
        """
        for number, title, text in items
    )
    return f'<div class="flow {extra_class}">{cards}</div>'


def _methodology_steps() -> str:
    return "\n".join(
        f"""
        <div class="step">
            <div class="snum">{_escape(number)}</div>
            <h3>{_escape(title)}</h3>
            <p>{_escape(text)}</p>
        </div>
        """
        for number, title, text in METHODOLOGY_STEPS
    )


def _trust_cards() -> str:
    return "\n".join(
        f"""
        <div class="trust">
            <div class="dot">{_escape(number)}</div>
            <h3>{_escape(title)}</h3>
            <p>{_escape(text)}</p>
        </div>
        """
        for number, title, text in TRUST_ITEMS
    )


def render_landing_page() -> None:
    brand = _brand_markup()
    html_page = f"""
    <div class="cosmos-page">
        <nav class="cosmos-nav" aria-label="Glavna navigacija">
            <div class="cosmos-shell cosmos-nav-inner">
                <a class="brand" href="#top" aria-label="COSMOS početak">{brand}</a>
                <div class="nav-links">
                    <a href="#platforma">Platforma</a>
                    <a href="#simpa">SIMPA</a>
                    <a href="#ordo">ORDO</a>
                    <a href="#metodologija">Metodologija</a>
                    <a class="btn btn-primary nav-cta" href="#ekosistem">Upoznajte platformu</a>
                </div>
            </div>
        </nav>

        <div id="top">
            <div class="hero" aria-labelledby="hero-title">
                <div class="cosmos-shell hero-grid">
                    <div>
                        <div class="eyebrow">Platforma inteligencije odlučivanja</div>
                        <h1 id="hero-title">INTELIGENTNE ODLUKE.<span>ODRŽIVI<br class="desktop-break">SVET.</span></h1>
                        <p class="lead">{_escape(HERO_COPY)}</p>
                        <div class="hero-actions">
                            <a class="btn btn-primary" href="#platforma">Upoznajte COSMOS</a>
                            <a class="btn btn-secondary" href="#ekosistem">SIMPA i ORDO</a>
                        </div>
                        <div class="micro">
                            <span><i></i>Pouzdano</span>
                            <span><i></i>Transparentno</span>
                            <span><i></i>Objašnjivo</span>
                            <span><i></i>Odgovorno</span>
                        </div>
                    </div>
                    <div class="orbit-card" aria-label="Apstraktni prikaz COSMOS sistema">
                        <div class="label">Red u haosu</div>
                        <div class="orbit" aria-hidden="true"></div>
                        <div class="core-mark">C</div>
                        <span class="node n1"></span>
                        <span class="node n2"></span>
                        <span class="node n3"></span>
                        <span class="node n4"></span>
                        <span class="node n5"></span>
                        <div class="orbit-caption">
                            <span>NAUKA · PODACI · AI</span>
                            <strong>INTELIGENCIJA ODLUČIVANJA</strong>
                        </div>
                    </div>
                </div>
            </div>

            <div class="section white" id="platforma">
                <div class="cosmos-shell">
                    <div class="section-title">
                        <div>
                            <div class="kicker">Filozofija</div>
                            <h2>Razumevanje prethodi odlučivanju.</h2>
                        </div>
                        <p>{_escape(UNDERSTANDING_COPY)}</p>
                    </div>
                    <div class="pillars">{_pillar_cards()}</div>
                    <div class="human-note">Odgovornost za odluku ostaje u rukama čoveka.</div>
                </div>
            </div>

            <div class="section" id="ekosistem">
                <div class="cosmos-shell">
                    <div class="section-title">
                        <div>
                            <div class="kicker">COSMOS ekosistem</div>
                            <h2>Jedna metodologija. Jedna platforma. Više oblasti odlučivanja.</h2>
                        </div>
                        <p>{_escape(ECOSYSTEM_COPY)}</p>
                    </div>
                    <div class="ecosystem">{_product_cards()}</div>
                    <div class="platform-note">
                        <div><strong>COSMOS je matična platforma</strong><br><span>SIMPA i ORDO su specijalizacije iste metodološke osnove.</span></div>
                        <span>ZAJEDNIČKI STANDARDI</span>
                    </div>
                </div>
            </div>

            <div class="section white module-simpa" id="simpa">
                <div class="cosmos-shell module-overview">
                    <div class="module-lead">
                        <div class="eyebrow">COSMOS / socijalna uključenost</div>
                        <h2>SIMPA</h2>
                        <p class="statement">Podaci. Znanje. Odluke. Rezultati.</p>
                        <p>SIMPA je specijalizovani alat platforme COSMOS namenjen planiranju, praćenju i evaluaciji lokalnih javnih politika u oblasti socijalne zaštite.</p>
                    </div>
                    <div>
                        {_metrics(SIMPA_METRICS)}
                    </div>
                </div>
            </div>

            <div class="section module-band simpa-band">
                <div class="cosmos-shell">
                    <div class="band-grid">
                        <div>
                            <div class="kicker">Tok inteligencije odlučivanja</div>
                            <h2>Podaci postaju znanje tek kada mogu da objasne potrebe i usmere akciju.</h2>
                        </div>
                        <p>Administrativni i drugi relevantni izvori povezuju se u metodološki okvir koji pomaže institucijama da razumeju potrebe građana, planiraju usluge i prate efekte mera.</p>
                    </div>
                    {_flow_cards(SIMPA_FLOW)}
                </div>
            </div>

            <div class="section white module-ordo" id="ordo">
                <div class="cosmos-shell module-overview">
                    <div class="module-lead">
                        <div class="eyebrow">COSMOS / razvoj destinacija</div>
                        <h2>ORDO</h2>
                        <p class="statement">Podaci. Znanje. Razvoj. Destinacija.</p>
                        <p>ORDO je alat platforme COSMOS razvijen za podršku planiranju, razvoju i upravljanju turističkim destinacijama kroz pet stubova inteligencije odlučivanja.</p>
                    </div>
                    <div>
                        {_metrics(ORDO_PILLARS, "five")}
                    </div>
                </div>
            </div>

            <div class="section module-band ordo-band">
                <div class="cosmos-shell">
                    <div class="band-grid">
                        <div>
                            <div class="kicker">Arhitektura ORDO</div>
                            <h2>Od razvojne ambicije do odluke zasnovane na znanju.</h2>
                        </div>
                        <p>ORDO posmatra destinaciju kao jedinstven razvojni sistem u kojem se priroda, prostor, ljudi, kultura, privreda, infrastruktura i institucije razumeju zajedno.</p>
                    </div>
                    {_flow_cards(ORDO_FLOW, "five")}
                </div>
            </div>

            <div class="section white" id="metodologija">
                <div class="cosmos-shell">
                    <div class="section-title">
                        <div>
                            <div class="kicker">Metodologija</div>
                            <h2>Od problema do odgovorne odluke.</h2>
                        </div>
                        <p>Metodologija ostaje jasna i proverljiva: analiza ne počinje od podataka koje imamo, već od problema koji treba razumeti.</p>
                    </div>
                    <div class="steps">{_methodology_steps()}</div>
                </div>
            </div>

            <div class="section dark" id="poverenje">
                <div class="cosmos-shell">
                    <div class="section-title">
                        <div>
                            <div class="kicker">Poverenje</div>
                            <h2>Platforma kojoj korisnik može da veruje.</h2>
                        </div>
                        <p>Poverenje ne proizlazi iz složenosti algoritma, već iz metodološke doslednosti, proverljivosti podataka i sposobnosti da se svaki rezultat objasni.</p>
                    </div>
                    <div class="trust-grid">{_trust_cards()}</div>
                </div>
            </div>

            <div class="section">
                <div class="cosmos-shell">
                    <div class="cta">
                        <h2>Od podataka do razumevanja.<br>Od razumevanja do odgovornih odluka.</h2>
                        <span class="btn btn-light">Istražite COSMOS metodologiju</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="site-footer">
            <div class="cosmos-shell footer-inner">
                <div><strong>COSMOS</strong> Platforma inteligencije odlučivanja</div>
                <div>SIMPA · ORDO · © 2026 COSMOS</div>
            </div>
        </div>
    </div>
    """
    st.html(dedent(html_page))
