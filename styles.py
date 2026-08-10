import streamlit as st


def apply_global_styles() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #f6f7f3;
                --paper: #ffffff;
                --ink: #0c231d;
                --muted: #66736e;
                --line: #dfe5e1;
                --cosmos: #0b5a46;
                --cosmos-dark: #063d31;
                --cosmos-2: #6ab64a;
                --cosmos-soft: #e8f2ec;
                --navy: #0a2d59;
                --simpa: #0b9c9a;
                --simpa-soft: #e6f6f5;
                --ordo: #c59a3b;
                --ordo-soft: #f7f0df;
                --shadow: 0 18px 60px rgba(16, 42, 33, 0.09);
                --max: 1180px;
            }

            html {
                scroll-behavior: smooth;
                background: var(--bg);
            }

            body,
            .stApp {
                margin: 0;
                background: var(--bg);
                color: var(--ink);
                font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
                font-size: 16px;
                line-height: 1.6;
            }

            header[data-testid="stHeader"],
            footer,
            #MainMenu,
            div[data-testid="stToolbar"],
            div[data-testid="stDecoration"],
            div[data-testid="collapsedControl"],
            section[data-testid="stSidebar"] {
                display: none !important;
            }

            .block-container {
                max-width: none !important;
                padding: 0 !important;
            }

            .main .block-container,
            [data-testid="stAppViewContainer"] > .main {
                background: var(--bg);
            }

            .element-container {
                margin: 0 !important;
            }

            div[data-testid="stMarkdownContainer"] > p {
                margin: 0;
            }

            .cosmos-page * {
                box-sizing: border-box;
            }

            .cosmos-page {
                background: var(--bg);
                color: var(--ink);
                min-height: 100vh;
                overflow-x: clip;
            }

            .cosmos-page a {
                color: inherit;
                text-decoration: none;
            }

            .cosmos-page img {
                display: block;
                max-width: 100%;
            }

            .cosmos-shell {
                width: min(var(--max), calc(100% - 40px));
                margin: 0 auto;
            }

            .cosmos-nav {
                position: sticky;
                top: 0;
                z-index: 50;
                background: rgba(246, 247, 243, 0.9);
                backdrop-filter: blur(18px);
                border-bottom: 1px solid rgba(12, 35, 29, 0.08);
            }

            .cosmos-nav-inner {
                height: 78px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 24px;
            }

            .brand {
                display: flex;
                align-items: center;
                gap: 12px;
                flex: 0 0 auto;
            }

            .brand img {
                width: auto;
                height: 52px;
                object-fit: contain;
            }

            .brand-fallback {
                width: 74px;
                height: 52px;
                display: grid;
                place-items: center;
                border: 1px solid var(--line);
                background: var(--paper);
                color: var(--cosmos);
                font-size: 13px;
                font-weight: 900;
                letter-spacing: 0.14em;
            }

            .nav-links {
                display: flex;
                align-items: center;
                justify-content: flex-end;
                gap: 26px;
                color: #375047;
                font-size: 14px;
                font-weight: 700;
                white-space: nowrap;
            }

            .nav-links a {
                transition: color 0.18s ease, transform 0.18s ease;
            }

            .nav-links a:hover {
                color: var(--cosmos);
                transform: translateY(-1px);
            }

            .btn {
                min-height: 46px;
                padding: 0 20px;
                border-radius: 999px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                border: 1px solid transparent;
                font-size: 14px;
                font-weight: 800;
                letter-spacing: 0.01em;
                transition: background 0.18s ease, border-color 0.18s ease, transform 0.18s ease;
            }

            .btn-primary {
                color: #ffffff;
                background: var(--cosmos);
                box-shadow: 0 10px 26px rgba(11, 90, 70, 0.18);
            }

            .btn-primary:hover {
                background: #084c3b;
            }

            .btn-secondary {
                background: transparent;
                border-color: #b9c8c1;
                color: var(--ink);
            }

            .btn-light {
                background: #ffffff;
                color: var(--cosmos);
            }

            .btn:hover {
                transform: translateY(-1px);
            }

            .hero {
                padding: 86px 0 74px;
                position: relative;
                overflow: hidden;
            }

            .hero-grid {
                display: grid;
                grid-template-columns: 1.08fr 0.92fr;
                gap: 64px;
                align-items: center;
            }

            .eyebrow,
            .kicker {
                display: inline-flex;
                align-items: center;
                gap: 10px;
                margin: 0 0 24px;
                color: var(--cosmos);
                font-size: 12px;
                font-weight: 900;
                letter-spacing: 0.18em;
                text-transform: uppercase;
            }

            .eyebrow::before {
                content: "";
                width: 34px;
                height: 1px;
                background: currentColor;
                flex: 0 0 auto;
            }

            .kicker {
                margin-bottom: 12px;
                color: var(--cosmos-2);
            }

            h1,
            h2,
            h3,
            h4,
            p {
                margin-top: 0;
            }

            .cosmos-page h1 {
                margin-bottom: 28px;
                color: var(--ink);
                font-size: clamp(52px, 7.1vw, 104px);
                font-weight: 900;
                letter-spacing: -0.055em;
                line-height: 0.91;
            }

            .cosmos-page h1 span {
                display: block;
                color: var(--cosmos-2);
            }

            .desktop-break {
                display: block;
            }

            .lead {
                max-width: 720px;
                color: #42584f;
                font-size: 20px;
                line-height: 1.65;
            }

            .hero-actions {
                display: flex;
                gap: 12px;
                flex-wrap: wrap;
                margin-top: 34px;
            }

            .micro {
                display: flex;
                flex-wrap: wrap;
                gap: 18px;
                margin-top: 28px;
                color: #6f7d77;
                font-size: 13px;
            }

            .micro span {
                display: inline-flex;
                align-items: center;
                gap: 7px;
            }

            .micro i {
                width: 7px;
                height: 7px;
                display: inline-block;
                background: var(--cosmos-2);
                border-radius: 999px;
            }

            .orbit-card {
                min-height: 560px;
                border: 1px solid #e0e7e2;
                border-radius: 38px;
                background: linear-gradient(145deg, #ffffff, #edf4ef);
                box-shadow: var(--shadow);
                position: relative;
                overflow: hidden;
            }

            .orbit-card .label {
                position: absolute;
                top: 28px;
                left: 28px;
                color: #5c7369;
                font-size: 12px;
                font-weight: 900;
                letter-spacing: 0.17em;
                text-transform: uppercase;
            }

            .orbit {
                width: 430px;
                height: 430px;
                border-radius: 50%;
                position: absolute;
                left: 50%;
                top: 52%;
                transform: translate(-50%, -50%);
                background:
                    radial-gradient(circle at center, var(--cosmos) 0 13%, transparent 13.3%),
                    radial-gradient(circle at center, transparent 0 23%, rgba(11, 90, 70, 0.15) 23.3% 23.8%, transparent 24.1%),
                    radial-gradient(circle at center, transparent 0 39%, rgba(11, 90, 70, 0.14) 39.3% 39.8%, transparent 40.1%),
                    radial-gradient(circle at center, transparent 0 57%, rgba(106, 182, 74, 0.18) 57.2% 58%, transparent 58.2%),
                    radial-gradient(circle at center, transparent 0 73%, rgba(11, 90, 70, 0.12) 73.2% 73.8%, transparent 74%);
            }

            .orbit::before,
            .orbit::after {
                content: "";
                position: absolute;
                border-radius: 50%;
                border: 1px dashed rgba(11, 90, 70, 0.25);
            }

            .orbit::before {
                inset: 72px;
            }

            .orbit::after {
                inset: 136px;
            }

            .core-mark {
                width: 112px;
                height: 112px;
                border-radius: 50%;
                position: absolute;
                left: 50%;
                top: 52%;
                transform: translate(-50%, -50%);
                display: grid;
                place-items: center;
                background: var(--cosmos);
                color: #ffffff;
                box-shadow: 0 18px 40px rgba(11, 90, 70, 0.28);
                font-size: 34px;
                font-weight: 900;
                letter-spacing: 0.08em;
            }

            .node {
                width: 13px;
                height: 13px;
                border-radius: 50%;
                position: absolute;
                background: #ffffff;
                border: 3px solid var(--cosmos);
                box-shadow: 0 0 0 5px rgba(11, 90, 70, 0.07);
            }

            .n1 { left: 22%; top: 29%; }
            .n2 { right: 16%; top: 38%; }
            .n3 { left: 19%; bottom: 22%; }
            .n4 { right: 22%; bottom: 16%; }
            .n5 { left: 47%; top: 14%; }

            .orbit-caption {
                position: absolute;
                left: 28px;
                right: 28px;
                bottom: 28px;
                padding-top: 18px;
                border-top: 1px solid #d9e4dd;
                display: flex;
                justify-content: space-between;
                gap: 20px;
                color: #4d6259;
                font-size: 13px;
            }

            .orbit-caption strong {
                color: var(--ink);
            }

            .section {
                padding: 94px 0;
            }

            .section.white {
                background: var(--paper);
            }

            .section.dark {
                background: #0a241c;
                color: #ffffff;
            }

            .section-title {
                display: grid;
                grid-template-columns: 0.9fr 1.1fr;
                gap: 80px;
                align-items: start;
                margin-bottom: 52px;
            }

            .section-title h2 {
                margin-bottom: 0;
                color: var(--ink);
                font-size: clamp(40px, 5vw, 72px);
                font-weight: 850;
                letter-spacing: -0.04em;
                line-height: 1.02;
            }

            .section-title p {
                max-width: 650px;
                color: #5c6e67;
                font-size: 18px;
            }

            .dark .section-title h2,
            .module-band .section-title h2 {
                color: #ffffff;
            }

            .dark .section-title p,
            .module-band .section-title p {
                color: rgba(255, 255, 255, 0.76);
            }

            .pillars {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 18px;
            }

            .pillar,
            .metric,
            .trust {
                border-radius: 22px;
            }

            .pillar,
            .metric {
                min-height: 210px;
                padding: 28px;
                background: #ffffff;
                border: 1px solid var(--line);
            }

            .num,
            .top,
            .snum {
                color: var(--cosmos);
                font-size: 12px;
                font-weight: 900;
                letter-spacing: 0.16em;
                text-transform: uppercase;
            }

            .pillar h3 {
                margin: 30px 0 8px;
                color: var(--ink);
                font-size: 24px;
                letter-spacing: -0.02em;
                line-height: 1.17;
            }

            .pillar p,
            .metric p,
            .step p {
                margin-bottom: 0;
                color: #687871;
                font-size: 14px;
            }

            .human-note {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-top: 18px;
                padding: 18px 22px;
                border: 1px solid #c9d7d0;
                border-radius: 18px;
                background: #edf5f0;
                color: var(--ink);
                font-weight: 800;
            }

            .human-note::before {
                content: "";
                width: 10px;
                height: 10px;
                flex: 0 0 auto;
                border-radius: 999px;
                background: var(--cosmos-2);
            }

            .ecosystem {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 22px;
            }

            .product {
                min-height: 430px;
                padding: 38px;
                border-radius: 30px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                color: #ffffff;
                position: relative;
                overflow: hidden;
            }

            .product::after,
            .module-band::after,
            .cta::after {
                content: "";
                position: absolute;
                border-radius: 50%;
                pointer-events: none;
            }

            .product::after {
                right: -120px;
                top: -120px;
                width: 280px;
                height: 280px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                box-shadow: 0 0 0 42px rgba(255, 255, 255, 0.035);
            }

            .product.simpa {
                background: linear-gradient(145deg, #092c58 0%, #087b84 100%);
            }

            .product.ordo {
                background: linear-gradient(145deg, #092c58 0%, #183862 58%, #a77d28 135%);
            }

            .product .tag {
                opacity: 0.78;
                font-size: 12px;
                font-weight: 900;
                letter-spacing: 0.18em;
                text-transform: uppercase;
            }

            .product h3 {
                margin: 18px 0 12px;
                font-size: 62px;
                font-weight: 850;
                letter-spacing: -0.04em;
                line-height: 1;
            }

            .product .motto {
                margin-bottom: 28px;
                font-size: 17px;
                font-weight: 800;
            }

            .product p {
                max-width: 520px;
                color: rgba(255, 255, 255, 0.82);
            }

            .chips,
            .outcome-row {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
            }

            .chips {
                margin-top: 30px;
            }

            .chip {
                padding: 8px 11px;
                border: 1px solid rgba(255, 255, 255, 0.25);
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.08);
                font-size: 12px;
                font-weight: 800;
            }

            .product .link {
                position: absolute;
                left: 38px;
                bottom: 34px;
                z-index: 1;
                font-size: 14px;
                font-weight: 900;
            }

            .product .link::after {
                content: " →";
            }

            .platform-note {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 20px;
                margin-top: 20px;
                padding: 24px;
                border: 1px dashed #cbd6d0;
                border-radius: 20px;
                background: #fbfcfa;
                color: #5e7069;
            }

            .platform-note strong {
                color: var(--ink);
            }

            .platform-note span:last-child {
                color: #8a9892;
                font-size: 13px;
                font-weight: 900;
                letter-spacing: 0.08em;
            }

            .module-overview {
                display: block;
            }

            .module-lead {
                max-width: 720px;
                margin-bottom: 42px;
            }

            .module-lead h2 {
                margin: 0 0 18px;
                color: var(--ink);
                font-size: clamp(50px, 7vw, 92px);
                font-weight: 850;
                letter-spacing: -0.055em;
                line-height: 0.95;
            }

            .module-lead .statement {
                color: var(--ink);
                font-size: 22px;
                font-weight: 800;
                line-height: 1.28;
            }

            .module-lead p {
                color: #596c64;
                font-size: 17px;
            }

            .module-simpa .eyebrow,
            .module-simpa .top {
                color: var(--simpa);
            }

            .module-ordo .eyebrow,
            .module-ordo .top {
                color: var(--ordo);
            }

            .module-simpa .module-lead h2,
            .module-ordo .module-lead h2 {
                color: var(--navy);
            }

            .metric-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 14px;
            }

            .metric-grid.five {
                grid-template-columns: repeat(5, 1fr);
            }

            .metric {
                min-height: 238px;
                padding: 24px;
            }

            .metric h3 {
                margin: 24px 0 8px;
                color: var(--ink);
                font-size: 21px;
                line-height: 1.22;
            }

            .module-band {
                position: relative;
                overflow: hidden;
                color: #ffffff;
            }

            .module-band::after {
                right: -160px;
                top: -210px;
                width: 440px;
                height: 440px;
                border: 1px solid rgba(255, 255, 255, 0.16);
                box-shadow: 0 0 0 48px rgba(255, 255, 255, 0.035), 0 0 0 96px rgba(255, 255, 255, 0.022);
            }

            .simpa-band {
                background: linear-gradient(135deg, #0a2d59, #0b9c9a);
            }

            .ordo-band {
                background: linear-gradient(135deg, #0a2d59, #304f70 60%, #b18a35);
            }

            .band-grid {
                display: grid;
                grid-template-columns: 0.8fr 1.2fr;
                gap: 70px;
                align-items: start;
                position: relative;
                z-index: 1;
            }

            .band-grid h2 {
                margin-bottom: 0;
                color: #ffffff;
                font-size: clamp(42px, 5vw, 58px);
                font-weight: 850;
                letter-spacing: -0.04em;
                line-height: 1.02;
            }

            .band-grid p {
                color: rgba(255, 255, 255, 0.82);
                font-size: 17px;
            }

            .simpa-band .kicker {
                color: #72e0da;
            }

            .ordo-band .kicker {
                color: #e1bf6e;
            }

            .flow {
                display: grid;
                grid-template-columns: repeat(6, 1fr);
                gap: 10px;
                margin-top: 42px;
                position: relative;
                z-index: 1;
            }

            .flow.five {
                grid-template-columns: repeat(5, 1fr);
            }

            .flow-card {
                min-height: 168px;
                padding: 18px 14px;
                border: 1px solid rgba(255, 255, 255, 0.18);
                border-radius: 16px;
                background: rgba(255, 255, 255, 0.08);
            }

            .flow-card .num {
                color: rgba(255, 255, 255, 0.72);
            }

            .flow-card h3 {
                margin: 34px 0 7px;
                color: #ffffff;
                font-size: 16px;
                line-height: 1.25;
            }

            .flow-card p {
                margin: 0;
                color: rgba(255, 255, 255, 0.72);
                font-size: 12px;
                line-height: 1.45;
            }

            .steps {
                display: grid;
                grid-template-columns: repeat(5, 1fr);
                gap: 10px;
            }

            .step {
                padding: 24px 12px 8px;
                border-top: 2px solid #bdd0c7;
            }

            .step h3 {
                margin: 12px 0 10px;
                color: var(--ink);
                font-size: 17px;
                line-height: 1.25;
            }

            .trust-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 14px;
            }

            .trust {
                padding: 26px;
                background: #12362b;
                border: 1px solid rgba(255, 255, 255, 0.08);
            }

            .trust .dot {
                width: 34px;
                height: 34px;
                display: grid;
                place-items: center;
                margin-bottom: 28px;
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                color: rgba(255, 255, 255, 0.78);
                font-size: 12px;
                font-weight: 900;
            }

            .trust h3 {
                margin-bottom: 10px;
                color: #ffffff;
                font-size: 18px;
            }

            .trust p {
                margin: 0;
                color: #c6d7d0;
                font-size: 13px;
            }

            .cta {
                min-height: 258px;
                margin: 0 auto;
                padding: 62px;
                border-radius: 34px;
                background: linear-gradient(125deg, #0a3e30, #0b5a46 70%, #5da34a);
                color: #ffffff;
                display: flex;
                align-items: flex-end;
                justify-content: space-between;
                gap: 50px;
                position: relative;
                overflow: hidden;
            }

            .cta::after {
                top: -90px;
                right: -70px;
                width: 330px;
                height: 330px;
                border: 1px solid rgba(255, 255, 255, 0.2);
                box-shadow: 0 0 0 42px rgba(255, 255, 255, 0.035), 0 0 0 84px rgba(255, 255, 255, 0.025);
            }

            .cta h2 {
                max-width: 760px;
                margin: 0;
                color: #ffffff;
                font-size: clamp(40px, 4.7vw, 54px);
                font-weight: 850;
                letter-spacing: -0.04em;
                line-height: 1.02;
                position: relative;
                z-index: 1;
            }

            .cta .btn {
                flex: 0 0 auto;
                position: relative;
                z-index: 1;
            }

            .cta .btn-light {
                min-width: 224px;
                background: #ffffff !important;
                color: #0b5a46 !important;
                font-size: 14px !important;
                font-weight: 800 !important;
            }

            .site-footer {
                padding: 44px 0 58px;
                background: var(--bg);
            }

            .footer-inner {
                display: flex;
                justify-content: space-between;
                gap: 30px;
                padding-top: 28px;
                border-top: 1px solid #d9e1dc;
                color: #63716c;
                font-size: 13px;
            }

            .footer-inner strong {
                color: var(--ink);
                letter-spacing: 0.16em;
            }

            @media (max-width: 1000px) {
                .hero-grid,
                .section-title,
                .band-grid {
                    grid-template-columns: 1fr;
                }

                .orbit-card {
                    min-height: 500px;
                }

                .pillars,
                .ecosystem {
                    grid-template-columns: 1fr 1fr;
                }

                .metric-grid,
                .metric-grid.five,
                .trust-grid {
                    grid-template-columns: repeat(2, 1fr);
                }

                .steps {
                    grid-template-columns: repeat(3, 1fr);
                }

                .flow,
                .flow.five {
                    grid-template-columns: repeat(3, 1fr);
                }

                .section-title {
                    gap: 28px;
                }
            }

            @media (max-width: 720px) {
                .cosmos-shell {
                    width: min(calc(100% - 24px), var(--max));
                }

                .cosmos-nav-inner {
                    height: 68px;
                    flex-direction: row;
                    align-items: center;
                    justify-content: space-between;
                    gap: 18px;
                    padding: 0;
                }

                .brand img,
                .brand-fallback {
                    width: auto;
                    height: 44px;
                }

                .nav-links {
                    display: none;
                }

                .hero {
                    padding: 56px 0;
                }

                .hero-grid {
                    gap: 34px;
                }

                .cosmos-page h1 {
                    font-size: clamp(48px, 15vw, 66px);
                    letter-spacing: -0.045em;
                }

                .desktop-break {
                    display: none;
                }

                .lead {
                    font-size: 16px;
                    line-height: 1.65;
                }

                .btn {
                    min-height: 42px;
                    padding: 0 16px;
                    font-size: 12px;
                }

                .orbit-card {
                    min-height: 420px;
                    border-radius: 26px;
                }

                .orbit {
                    width: min(330px, calc(100vw - 62px));
                    height: min(330px, calc(100vw - 62px));
                }

                .core-mark {
                    width: 88px;
                    height: 88px;
                    font-size: 26px;
                }

                .orbit-caption {
                    display: block;
                    font-size: 10px;
                }

                .section {
                    padding: 68px 0;
                }

                .section-title {
                    gap: 18px;
                    margin-bottom: 34px;
                }

                .section-title h2 {
                    font-size: clamp(38px, 12vw, 50px);
                }

                .section-title p {
                    font-size: 15px;
                }

                .pillars,
                .ecosystem,
                .metric-grid,
                .metric-grid.five,
                .trust-grid,
                .steps,
                .flow,
                .flow.five {
                    grid-template-columns: 1fr;
                }

                .product {
                    min-height: 390px;
                    padding: 28px;
                }

                .product h3 {
                    font-size: 52px;
                }

                .product .link {
                    left: 28px;
                }

                .platform-note {
                    align-items: flex-start;
                    flex-direction: column;
                }

                .module-lead h2 {
                    font-size: clamp(54px, 18vw, 72px);
                }

                .module-lead {
                    margin-bottom: 28px;
                }

                .module-lead .statement {
                    font-size: 19px;
                }

                .metric {
                    min-height: 0;
                }

                .band-grid h2 {
                    font-size: clamp(38px, 12vw, 48px);
                }

                .flow-card {
                    min-height: 142px;
                }

                .flow-card h3 {
                    margin-top: 24px;
                }

                .cta {
                    display: block;
                    min-height: 0;
                    padding: 38px;
                    border-radius: 24px;
                }

                .cta h2 {
                    margin-bottom: 28px;
                    font-size: clamp(34px, 10vw, 40px);
                }

                .footer-inner {
                    display: block;
                }

                .footer-inner > div + div {
                    margin-top: 10px;
                }
            }

            @media (max-width: 420px) {
                .cosmos-page h1 {
                    font-size: 45px;
                }

                .micro {
                    gap: 10px 14px;
                    font-size: 12px;
                }

                .pillar,
                .product,
                .metric,
                .trust {
                    border-radius: 18px;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
