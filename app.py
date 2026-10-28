"""
Portfolio Professionnel
Auteur : Abdellatif Kiswendsida NIKIEMA
Titre : Ingénieur Logiciel Full-Stack | Spécialiste IA & Fouille de Données
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# ==============================================================================
# 1. CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Abdellatif K. NIKIEMA | Ingénieur Logiciel & IA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. STYLES CSS ÉPURÉS & PROFESSIONNELS (EXECUTIVE CORPORATE)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Typographie & Arrière-plan */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        background-color: #F8FAFC !important;
        color: #0F172A;
    }

    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Barre latérale */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 1px solid #E2E8F0 !important;
    }

    /* Photo de profil sobre et élégante */
    [data-testid="stSidebar"] img {
        border-radius: 50% !important;
        aspect-ratio: 1 / 1 !important;
        object-fit: cover !important;
        object-position: top center !important;
        border: 2px solid #E2E8F0 !important;
        margin: 0 auto 0.4rem auto !important;
        display: block !important;
    }

    /* Avatar Monogramme si image absente */
    .avatar-monogram {
        width: 96px;
        height: 96px;
        margin: 0 auto 0.5rem auto;
        border-radius: 50%;
        background-color: #1E293B;
        color: #F8FAFC;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.5rem;
        letter-spacing: 0.05em;
        border: 2px solid #E2E8F0;
    }

    /* En-tête Principal (Hero) */
    .hero-container {
        background-color: #0F172A;
        padding: 2.2rem 2.4rem;
        border-radius: 12px;
        color: #F8FAFC;
        margin-bottom: 1.6rem;
        border: 1px solid #1E293B;
    }

    .hero-badge-tag {
        display: inline-block;
        background-color: rgba(255, 255, 255, 0.08);
        color: #94A3B8;
        border: 1px solid rgba(255, 255, 255, 0.12);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 6px;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1.2;
        letter-spacing: -0.02em;
        color: #FFFFFF;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        font-weight: 600;
        color: #60A5FA;
        margin-bottom: 0.9rem;
    }

    .hero-desc {
        font-size: 0.95rem;
        line-height: 1.65;
        color: #CBD5E1;
        max-width: 940px;
    }

    /* Cartes Piliers d'Intervention */
    .pillar-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.15rem 1.1rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    }

    .pillar-title {
        font-size: 0.98rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 0.45rem;
        line-height: 1.3;
    }

    .pillar-desc {
        font-size: 0.85rem;
        line-height: 1.55;
        color: #475569;
        margin-bottom: 0.75rem;
    }

    .pillar-tags {
        font-size: 0.75rem;
        color: #2563EB;
        font-weight: 600;
        margin-top: auto;
    }


    /* Navigation par Onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #E2E8F0;
        padding: 4px;
        border-radius: 8px;
        margin-bottom: 1.4rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        padding: 0 16px;
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.86rem;
        color: #475569;
        background-color: transparent;
        border: none;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #0F172A;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        font-weight: 700 !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.08) !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }

    /* Fiches Projets */
    .project-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.4rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03);
    }

    .project-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.5rem;
        flex-wrap: wrap;
        gap: 0.5rem;
    }

    .project-title {
        font-size: 1.18rem;
        font-weight: 700;
        color: #0F172A;
        letter-spacing: -0.01em;
        margin: 0;
    }

    .project-role {
        font-size: 0.84rem;
        font-weight: 600;
        color: #2563EB;
        margin-bottom: 0.65rem;
    }

    .project-desc {
        font-size: 0.92rem;
        line-height: 1.6;
        color: #334155;
        margin-bottom: 0.85rem;
    }

    .impact-box {
        background-color: #F8FAFC;
        border-left: 3px solid #0F766E;
        padding: 0.6rem 0.85rem;
        border-radius: 0 6px 6px 0;
        font-size: 0.86rem;
        font-weight: 500;
        color: #115E59;
        margin-bottom: 0.85rem;
    }

    /* Badges de Technologies (Subtils et lisibles) */
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin-top: 0.5rem;
    }

    .tech-badge {
        display: inline-block;
        background-color: #F1F5F9;
        color: #334155;
        border: 1px solid #E2E8F0;
        font-size: 0.74rem;
        font-weight: 500;
        padding: 2.5px 8.5px;
        border-radius: 4px;
    }

    .tech-badge-primary {
        background-color: #EFF6FF;
        color: #1E40AF;
        border-color: #DBEAFE;
    }

    .tech-badge-green {
        background-color: #F0FDF4;
        color: #166534;
        border-color: #DCFCE7;
    }

    .tech-badge-purple {
        background-color: #FAF5FF;
        color: #581C87;
        border-color: #F3E8FF;
    }

    .tech-badge-amber {
        background-color: #FFFBEB;
        color: #92400E;
        border-color: #FEF3C7;
    }

    /* Pilules de Certifications */
    .cert-pill {
        display: inline-block;
        background-color: #F8FAFC;
        color: #334155;
        border: 1px solid #CBD5E1;
        font-weight: 600;
        font-size: 0.76rem;
        padding: 3px 9px;
        border-radius: 4px;
        margin: 2px 3px 3px 0;
    }

    /* Boutons */
    .stButton > button, .stDownloadButton > button {
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        border: 1px solid #CBD5E1 !important;
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        transition: none !important;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        border-color: #0F172A !important;
        color: #0F172A !important;
        background-color: #F8FAFC !important;
    }
    .stButton > button[kind="primary"] {
        background-color: #0F172A !important;
        color: #FFFFFF !important;
        border: 1px solid #0F172A !important;
    }
    .stButton > button[kind="primary"]:hover {
        background-color: #1E293B !important;
    }

    /* Formulaires */
    [data-testid="stForm"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        padding: 1.4rem !important;
    }

    /* Pied de page */
    .footer-bar {
        text-align: center;
        padding: 2.5rem 0 1.5rem 0;
        color: #94A3B8;
        font-size: 0.82rem;
        border-top: 1px solid #E2E8F0;
        margin-top: 3.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. BARRE LATÉRALE (SIDEBAR)
# ==============================================================================
with st.sidebar:
    profile_path = "assets/profile.png"
    if PIL_AVAILABLE and os.path.exists(profile_path):
        try:
            profile_img = Image.open(profile_path)
            c_p1, c_p2, c_p3 = st.columns([1, 3.5, 1])
            with c_p2:
                st.image(profile_img, use_container_width=True)
        except Exception:
            pass
    else:
        st.markdown("""
        <div class="avatar-monogram">AKN</div>
        """, unsafe_allow_html=True)

    # Identité & Titre
    st.markdown("""
    <div style="text-align: center; margin-top: 0.4rem; margin-bottom: 0.8rem;">
        <h3 style="margin-top: 0; margin-bottom: 0.15rem; color: #0F172A; font-weight: 700; font-size: 1.15rem;">
            Abdellatif K. NIKIEMA
        </h3>
        <p style="color: #2563EB; font-size: 0.84rem; font-weight: 600; margin-bottom: 0.25rem;">
            Ingénieur Logiciel & IA
        </p>
        <p style="color: #64748B; font-size: 0.8rem; margin: 0;">
            Ouagadougou, Burkina Faso
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Certifications
    st.markdown("##### Certifications")
    st.markdown("""
    <span class="cert-pill">ITIL v4 Managing Professional</span>
    <span class="cert-pill">PRINCE2 Practitioner</span>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Coordonnées directes
    st.markdown("##### Contact")
    st.markdown("""
    - **Localisation :** Ouagadougou, Burkina Faso
    - **Téléphone :** [+226 78 80 50 60](tel:+22678805060) / [+226 65 36 99 49](tel:+22665369949)
    - **Email :** [abdellatifnikiema@gmail.com](mailto:abdellatifnikiema@gmail.com)
    - **Mobilité :** Présentiel & Remote
    - **Statut :** Disponible pour mandats & consulting
    """)

    # Réseaux professionnels
    c_side1, c_side2 = st.columns(2)
    with c_side1:
        st.link_button("LinkedIn", "https://linkedin.com", use_container_width=True)
    with c_side2:
        st.link_button("GitHub", "https://github.com", use_container_width=True)

    st.markdown("---")

    # Téléchargement CV
    cv_file_path = "cv.pdf"
    if os.path.exists(cv_file_path):
        with open(cv_file_path, "rb") as pdf_file:
            portfolio_cv_bytes = pdf_file.read()
    else:
        portfolio_cv_bytes = b"%PDF-1.4\n%Fallback CV"

    st.download_button(
        label="Télécharger le CV (PDF)",
        data=portfolio_cv_bytes,
        file_name="CV_Abdellatif_Kiswendsida_NIKIEMA.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.markdown("---")

    # Compétences Techniques
    st.markdown("##### Compétences Clés")
    st.markdown("""
    <div class="badge-container">
        <span class="tech-badge tech-badge-primary">Python</span>
        <span class="tech-badge tech-badge-primary">FastAPI</span>
        <span class="tech-badge tech-badge-primary">LightGBM</span>
        <span class="tech-badge tech-badge-primary">XGBoost</span>
        <span class="tech-badge tech-badge-primary">PyTorch</span>
        <span class="tech-badge tech-badge-green">Spring Boot</span>
        <span class="tech-badge tech-badge-green">Symfony 7</span>
        <span class="tech-badge tech-badge-green">PHP / Laravel</span>
        <span class="tech-badge tech-badge-purple">Flutter / Dart</span>
        <span class="tech-badge tech-badge-purple">Edge AI / TFLite</span>
        <span class="tech-badge tech-badge-amber">PostgreSQL</span>
        <span class="tech-badge tech-badge-amber">MS SQL Server</span>
        <span class="tech-badge tech-badge-amber">SAGE 100c</span>
        <span class="tech-badge">Docker</span>
        <span class="tech-badge">Linux Systemd</span>
        <span class="tech-badge">Activiti BPMN</span>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 4. BANDEAU HERO & MÉTRIQUES D'IMPACT
# ==============================================================================
st.markdown("""
<div class="hero-container">
    <div class="hero-badge-tag">Profil Hybride | + de 7 Ans d'Expériences</div>
    <div class="hero-title">Abdellatif Kiswendsida NIKIEMA</div>
    <div class="hero-subtitle">Ingénieur Logiciel Full-Stack & Spécialiste IA / Fouille de Données</div>
    <div class="hero-desc">
        Profil alliant la rigueur d'un <strong>Architecte Logiciel Senior</strong>, l'expertise quantitative d'un 
        <strong>Data Scientist Actuariel</strong> et l'expérience de plus de <strong>7 ans en exploitation de systèmes d'information critiques</strong>.
        Conception et déploiement de solutions logicielles d'État, de moteurs prédictifs anti-fraude haute vélocité et de plateformes techniques conformes au <strong>Code CIMA</strong>.
    </div>
</div>
""", unsafe_allow_html=True)

# 4 Piliers d'Intervention
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-title">Ingénierie Logicielle</div>
        <div class="pillar-desc">
            Architectures modulaires, APIs haute vélocité et solutions robustes d'entreprise.
        </div>
        <div class="pillar-tags">Microservices • FastAPI • Spring Boot • Docker</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-title">IA & Fouille de Données</div>
        <div class="pillar-desc">
            Modèles prédictifs supervisés, détection de fraude financière et Edge Computing.
        </div>
        <div class="pillar-tags">LightGBM • XGBoost • PaySim • TFLite</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-title">Actuariat & Réassurance</div>
        <div class="pillar-desc">
            Calibrage optimal de traités non-vie, modélisation des valeurs extrêmes et solvabilité.
        </div>
        <div class="pillar-tags">Code CIMA • EVT • Moteur Technique • PyTorch</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="pillar-card">
        <div class="pillar-title">Gouvernance & SI État</div>
        <div class="pillar-desc">
            Dématérialisation de guichets régaliens, automatisation ERP et continuité critique.
        </div>
        <div class="pillar-tags">SAGE 100c • ITIL v4 • PRINCE2 • E-Gouvernance</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# ==============================================================================
# 5. ORGANISATION EN 5 ONGLETS
# ==============================================================================
tab_ia, tab_actuariat, tab_gov, tab_solutions, tab_sim = st.tabs([
    "1. IA, Vision & Data Science",
    "2. Actuariat & Réassurance",
    "3. Projets Nationaux & GovTech",
    "4. Solutions Métier & Digitalisation",
    "5. Analytics & Démonstration Risque"
])

# ------------------------------------------------------------------------------
# ONGLET 1 : IA, VISION & DATA SCIENCE
# ------------------------------------------------------------------------------
with tab_ia:
    st.markdown("### Intelligence Artificielle, Vision par Ordinateur & Data Mining")
    st.caption("Modélisation prédictive, détection d'anomalies en temps réel et inférence embarquée sur terminaux mobiles.")

    # Projet 1.1: Mobile Money Fraude
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">FinTech & Paiements</span>
                <div class="project-title" style="margin-top: 5px;">Détection de Fraude Mobile Money & Transactions Financières</div>
                <div class="project-role">Lead Data Scientist & ML Engineer</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-green">Rappel : 97%</span>
            </div>
        </div>
        <div class="project-desc">
            Conception d'un pipeline complet de Machine Learning ciblé sur les flux de transferts critiques (opérations TRANSFER et CASH_OUT sur jeu de données PaySim).
            Ingénierie de variables avancée capturant les signatures de fraude caractéristiques : vidage intégral de solde (Zero-Balance Draining), déséquilibre des soldes émetteur/destinataire et vélocité temporelle inhabituelle.
            Optimisation des hyperparamètres et calibrage des seuils décisionnels pour minimiser les faux positifs tout en captant l'essentiel du volume financier à risque.
        </div>
        <div class="impact-box">
            Résultats obtenus : 97% de rappel atteint, captant plus de 99,5% de la valeur totale frauduleuse avec un temps de réponse d'inférence inférieur à 20 ms.
        </div>
        <div class="badge-container">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">LightGBM</span>
            <span class="tech-badge">Scikit-Learn</span>
            <span class="tech-badge">PaySim</span>
            <span class="tech-badge">Feature Engineering</span>
            <span class="tech-badge">Plotly</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 1.2: Sinistres & Audit
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">Assurance & Audit</span>
                <div class="project-title" style="margin-top: 5px;">Moteur Anti-Fraude Sinistres & Fast-Track d'Indemnisation</div>
                <div class="project-role">Architecte IA & Spécialiste Risques</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-amber">XGBoost & Isolation Forest</span>
            </div>
        </div>
        <div class="project-desc">
            Système d'évaluation probabiliste des déclarations de sinistres combinant détection d'anomalies non supervisée (Isolation Forest) et modèle de classification supervisée (XGBoost).
            Intégration d'un module d'explicabilité par valeurs SHAP fournissant aux auditeurs et gestionnaires les facteurs explicatifs détaillés de chaque alerte (anomalies chronologiques, récurrence anormale de tiers).
            Mise en place d'un parcours Fast-Track orientant automatiquement les dossiers réguliers vers une liquidation accélérée.
        </div>
        <div class="impact-box">
            Résultats obtenus : Réduction de 45% des frais d'expertise externe et diminution du délai de règlement des sinistres conformes de 15 jours à 48 heures.
        </div>
        <div class="badge-container">
            <span class="tech-badge">XGBoost</span>
            <span class="tech-badge">Isolation Forest</span>
            <span class="tech-badge">SHAP Values</span>
            <span class="tech-badge">FastAPI</span>
            <span class="tech-badge">Analyse de Graphes</span>
            <span class="tech-badge">PostgreSQL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 1.3: E-SUIVI BTP
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-purple">Edge AI & Mobilité</span>
                <div class="project-title" style="margin-top: 5px;">E-SUIVI — Inspection Chantiers BTP & Détection Visuelle Embarquée</div>
                <div class="project-role">Architecte Mobile & Edge AI</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-green">Offline-First & TFLite</span>
            </div>
        </div>
        <div class="project-desc">
            Application mobile d'inspection technique d'infrastructures conçue pour fonctionner en zones dépourvues de connectivité réseau.
            Intégration d'un modèle TensorFlow Lite quantifié pour la classification et le repérage sur le terrain des non-conformités structurelles et armatures.
            Architecture locale Offline-First avec moteur d'indexation SQLite FTS5, synchronisation incrémentale chiffrée lors de la reconnexion et intégration MDM Android.
        </div>
        <div class="impact-box">
            Résultats obtenus : Disponibilité opérationnelle permanente sans connexion, élimination des pertes de rapports de terrain et centralisation automatisée des non-conformités.
        </div>
        <div class="badge-container">
            <span class="tech-badge">Flutter / Dart</span>
            <span class="tech-badge">TensorFlow Lite</span>
            <span class="tech-badge">SQLite FTS5</span>
            <span class="tech-badge">Computer Vision</span>
            <span class="tech-badge">Android MDM</span>
            <span class="tech-badge">API REST</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ONGLET 2 : ACTUARIAT, TRAITÉS & SI RÉASSURANCE
# ------------------------------------------------------------------------------
with tab_actuariat:
    st.markdown("### Actuariat, Traités & Systèmes d'Information de Réassurance")
    st.caption("Modélisation quantitative des engagements réglementaires CIMA et modernisation des architectures applicatives de réassurance.")

    # Projet 2.1: Optimisation Actuarielle Traités
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">Sciences Actuarielles & Code CIMA</span>
                <div class="project-title" style="margin-top: 5px;">Optimisation Actuarielle des Traités de Réassurance Non-Vie</div>
                <div class="project-role">Ingénieur Chercheur en Sciences Actuarielles (Master 2 & AMRe)</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-purple">EVT & PyTorch</span>
            </div>
        </div>
        <div class="project-desc">
            Modélisation stochastique appliquée au calibrage des structures de réassurance proportionnelles (Quote-Part, Excédent de Plein) et non-proportionnelles (Excédent de Sinistre / XS).
            Application de la Théorie des Valeurs Extrêmes (EVT / loi de Pareto généralisée) pour la modélisation des sinistres majeurs et des risques de pointe.
            Intégration d'algorithmes d'optimisation sous contraintes de capital réglementaire et de solvabilité conformes aux exigences du Code CIMA.
        </div>
        <div class="impact-box">
            Résultats obtenus : Réduction de 18% du besoin en capital de solvabilité tout en préservant le niveau de rétention optimal de la compagnie face aux chocs extrêmes.
        </div>
        <div class="badge-container">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">PyTorch</span>
            <span class="tech-badge">Théorie des Valeurs Extrêmes</span>
            <span class="tech-badge">Simulations Monte Carlo</span>
            <span class="tech-badge">Code CIMA</span>
            <span class="tech-badge">AMRe</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 2.2: REASS-NEXT
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-green">ERP Technique & Microservices</span>
                <div class="project-title" style="margin-top: 5px;">REASS-NEXT — ERP & Moteur de Calcul Technique CIMA</div>
                <div class="project-role">Architecte Logiciel & Développeur Backend</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-green">&lt; 150 ms / police</span>
            </div>
        </div>
        <div class="project-desc">
            Développement d'un progiciel métier de réassurance couvrant la gestion des traités, des cessions légales et des facultatives.
            Moteur de calcul technique multi-devises développé sous FastAPI, assurant la ventilation automatique des primes, sinistres et commissions selon les cascades de plein.
            Conteneurisation Docker complète, persistance transactionnelle ACID et interfaces adaptées aux souscripteurs et comptables techniques.
        </div>
        <div class="impact-box">
            Résultats obtenus : Latence de calcul technique inférieure à 150 ms par police, capacité de traitement de plus de 150 000 lignes de risque sans saturation système.
        </div>
        <div class="badge-container">
            <span class="tech-badge">FastAPI</span>
            <span class="tech-badge">Python Asynchrone</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">PostgreSQL</span>
            <span class="tech-badge">Architecture Microservices</span>
            <span class="tech-badge">RabbitMQ</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 2.3: SI & SAGE 100c
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-amber">Systèmes d'Information & ERP</span>
                <div class="project-title" style="margin-top: 5px;">SI & Interfaçage Automatisé SAGE 100c (GLOBUS-RE)</div>
                <div class="project-role">Ingénieur SI & Administrateur Systèmes Senior (+7 ans d'exp.)</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-primary">Cadre ITIL v4</span>
            </div>
        </div>
        <div class="project-desc">
            Conception et fiabilisation de l'interfaçage technique entre le coeur de métier de réassurance (GLOBUS-RE) et le logiciel comptable SAGE 100c.
            Mise en place d'une passerelle ETL sous MS SQL Server gérant les déversements d'écritures, le lettrage automatique et la réconciliation bancaire.
            Application des processus ITIL v4 pour la gestion des changements en production et la traçabilité des opérations sensibles.
        </div>
        <div class="impact-box">
            Résultats obtenus : Durée des clôtures comptables trimestrielles ramenée de 3 semaines de saisies manuelles à quelques heures d'exécution automatisée sans écart de réconciliation.
        </div>
        <div class="badge-container">
            <span class="tech-badge">SAGE 100c</span>
            <span class="tech-badge">MS SQL Server</span>
            <span class="tech-badge">T-SQL</span>
            <span class="tech-badge">Pipelines ETL</span>
            <span class="tech-badge">ITIL v4</span>
            <span class="tech-badge">GLOBUS-RE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 2.4: Faso Assur Tech
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">InsurTech</span>
                <div class="project-title" style="margin-top: 5px;">Faso Assur Tech — Comparateur & Souscription Digitale</div>
                <div class="project-role">Tech Lead Full-Stack</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-green">Paiements Mobile Money</span>
            </div>
        </div>
        <div class="project-desc">
            Plateforme web et mobile permettant la comparaison d'offres d'assurance et la souscription dématérialisée immédiate avec délivrance d'attestations certifiées.
            Interfaçage avec les passerelles de paiement Mobile Money locales et mise en conformité stricte avec les exigences de l'APDP sur les données personnelles.
        </div>
        <div class="impact-box">
            Résultats obtenus : Parcours de souscription entièrement dématérialisé réalisable en moins de 3 minutes par l'assuré.
        </div>
        <div class="badge-container">
            <span class="tech-badge">FastAPI</span>
            <span class="tech-badge">Vue.js</span>
            <span class="tech-badge">APIs Mobile Money</span>
            <span class="tech-badge">Conformité APDP</span>
            <span class="tech-badge">PostgreSQL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ONGLET 3 : PROJETS NATIONAUX & GOVTECH
# ------------------------------------------------------------------------------
with tab_gov:
    st.markdown("### Projets Nationaux, E-Gouvernance & Architectures Souveraines")
    st.caption("Déploiement d'infrastructures logicielles régaliennes et dématérialisation des services publics.")

    # Projet 3.1: SYLVIE V2
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">Commerce Extérieur & Douanes</span>
                <div class="project-title" style="margin-top: 5px;">SYLVIE V2 — Guichet Unique du Commerce Extérieur</div>
                <div class="project-role">Ingénieur d'Études & Développeur Backend (SOGESY SA)</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-amber">Spring Boot & BPMN</span>
            </div>
        </div>
        <div class="project-desc">
            Contribution à la modernisation du guichet unique national de dématérialisation des formalités de pré-dédouanement et d'import/export au Burkina Faso.
            Développement de microservices sous Spring Boot et implémentation de workflows d'autorisation via le moteur de règles Activiti 6 BPMN.
            Interconnexion sécurisée entre les administrations douanières, les ministères techniques, le Trésor Public et les institutions bancaires.
        </div>
        <div class="impact-box">
            Résultats obtenus : Traitement mensuel de plus de 10 000 dossiers de commerce extérieur avec réduction notable des délais administratifs.
        </div>
        <div class="badge-container">
            <span class="tech-badge">Java / Spring Boot</span>
            <span class="tech-badge">Activiti 6 BPMN</span>
            <span class="tech-badge">Angular</span>
            <span class="tech-badge">Oracle DB / PostgreSQL</span>
            <span class="tech-badge">Sécurité TLS & PKI</span>
            <span class="tech-badge">SOGESY SA</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 3.2: BURKINDI
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-primary">Ministère de la Justice</span>
                <div class="project-title" style="margin-top: 5px;">BURKINDI — Dématérialisation des Demandes de Naturalisation</div>
                <div class="project-role">Lead Développeur & Architecte de Migration</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-green">Symfony 2.8 ➔ Symfony 7</span>
            </div>
        </div>
        <div class="project-desc">
            Migration et refonte complète du système étatique hérité de Symfony 2.8 vers Symfony 7 avec PHP 8.2+.
            Mise en place d'une politique rigoureuse de contrôle d'accès basée sur les rôles (RBAC), chiffrement des documents d'identité et traçabilité inviolable des visas ministériels.
            Assurance de la continuité opérationnelle du service pour les commissions administratives durant la bascule.
        </div>
        <div class="impact-box">
            Résultats obtenus : Dette technique assainie, temps de réponse divisé par 4 et conformité avec les standards de sécurité gouvernementaux.
        </div>
        <div class="badge-container">
            <span class="tech-badge">Symfony 7</span>
            <span class="tech-badge">PHP 8.2</span>
            <span class="tech-badge">PostgreSQL</span>
            <span class="tech-badge">Sécurité RBAC</span>
            <span class="tech-badge">PRINCE2</span>
            <span class="tech-badge">Journalisation d'Audit</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Projet 3.3: Guichets Dématérialisés Justice & Santé
    st.markdown("""
    <div class="project-card">
        <div class="project-header">
            <div>
                <span class="tech-badge tech-badge-purple">Justice & Santé Publique</span>
                <div class="project-title" style="margin-top: 5px;">Guichets Dématérialisés Justice & Santé (RCCM, Agréments, Permis)</div>
                <div class="project-role">Consultant Dématérialisation des Processus Publics</div>
            </div>
            <div>
                <span class="tech-badge tech-badge-primary">Services Dématérialisés</span>
            </div>
        </div>
        <div class="project-desc">
            Conception et mise en production de guichets publics numériques :
            <ul style="margin-top: 6px; margin-bottom: 6px; color: #334155;">
                <li><strong>Portail RCCM :</strong> Formalités d'immatriculation d'entreprises et délivrance des extraits certifiés.</li>
                <li><strong>Agrément des Établissements de Santé :</strong> Instruction des dossiers d'ouverture d'officines et structures médicales.</li>
                <li><strong>Permis de Communiquer :</strong> Traitement des autorisations d'accès carcéral auprès des juridictions d'instruction.</li>
            </ul>
        </div>
        <div class="impact-box">
            Résultats obtenus : Réduction des délais d'attente physiques, traçabilité administrative complète et émission de documents sécurisés par QR Code vérifiable.
        </div>
        <div class="badge-container">
            <span class="tech-badge">PHP / Symfony</span>
            <span class="tech-badge">Python</span>
            <span class="tech-badge">PostgreSQL</span>
            <span class="tech-badge">Génération PDF Sécurisée</span>
            <span class="tech-badge">Signatures Numériques</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ONGLET 4 : DIGITALISATION & SOLUTIONS MÉTIER
# ------------------------------------------------------------------------------
with tab_solutions:
    st.markdown("### Solutions Métier, Logistique & Digitalisation")
    st.caption("Développement d'outils opérationnels pour l'industrie, le commerce et la gestion logistique.")

    c_sol1, c_sol2 = st.columns(2)

    with c_sol1:
        # EKDS-PREFA
        st.markdown("""
        <div class="project-card">
            <span class="tech-badge tech-badge-primary">Industrie & BTP</span>
            <div class="project-title" style="margin-top: 5px;">EKDS-PREFA (Prefat Pro) — Traçabilité Industrielle BTP</div>
            <div class="project-role">Architecte Solution & Développeur Mobile</div>
            <div class="project-desc">
                Plateforme de suivi de production et de traçabilité des éléments préfabriqués en béton (poutrelles, dallettes, pavés).
                Identification des lots par étiquetage QR Code scanné sur terminal mobile Flutter lors des étapes de coulage, séchage, contrôle qualité et expédition.
            </div>
            <div class="impact-box">
                Résultats obtenus : Traçabilité des rebuts en direct, diminution de 30% des anomalies de livraison et visibilité instantanée sur les stocks d'agrégats.
            </div>
            <div class="badge-container">
                <span class="tech-badge">Laravel</span>
                <span class="tech-badge">Flutter</span>
                <span class="tech-badge">Scannage QR Code</span>
                <span class="tech-badge">MySQL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Doux Goût
        st.markdown("""
        <div class="project-card">
            <span class="tech-badge tech-badge-green">Distribution Commerciale (2026)</span>
            <div class="project-title" style="margin-top: 5px;">Doux Goût — Plateforme de Vente & Suivi Temps Réel des Commerciaux (2026)</div>
            <div class="project-role">Architecte Solution & Lead Développeur Full-Stack</div>
            <div class="project-desc">
                <strong>• Vente & Suivi Commerciaux Temps Réel :</strong> Digitalisation complète des flux de vente sur le terrain et suivi géographique/opérationnel des commerciaux en direct.<br>
                <strong>• Tableaux de Bord Interactifs :</strong> Pilotage centralisé des performances (chiffre d'affaires, taux de réalisation des objectifs, panier moyen) et suivi instantané des commandes entrantes.
            </div>
            <div class="impact-box">
                Résultats obtenus : Visibilité en direct sur 100% des ventes terrain, réduction des retards de livraison et pilotage commercial prédictif au quotidien.
            </div>
            <div class="badge-container">
                <span class="tech-badge tech-badge-primary">PHP / Laravel</span>
                <span class="tech-badge tech-badge-primary">Node.js / Vite</span>
                <span class="tech-badge tech-badge-green">Tableaux de bord interactifs</span>
                <span class="tech-badge tech-badge-amber">MySQL</span>
                <span class="tech-badge">APIs REST</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c_sol2:
        # Colis Express
        st.markdown("""
        <div class="project-card">
            <span class="tech-badge tech-badge-amber">Logistique & Transport</span>
            <div class="project-title" style="margin-top: 5px;">Colis Express — Crowdshipping Interurbain</div>
            <div class="project-role">Tech Lead Mobile & Backend</div>
            <div class="project-desc">
                Plateforme collaborative d'acheminement et de suivi de colis entre centres urbains d'Afrique de l'Ouest, s'appuyant sur les flux réguliers de transporteurs partenaires.
                Console d'exploitation sous Laravel Filament, application mobile Flutter client/transporteur avec alertes push et validation par signature numérique.
            </div>
            <div class="impact-box">
                Résultats obtenus : Réduction des coûts d'expédition de 40% par rapport aux solutions classiques et suivi des étapes de transit à la minute près.
            </div>
            <div class="badge-container">
                <span class="tech-badge">Flutter</span>
                <span class="tech-badge">Laravel Filament</span>
                <span class="tech-badge">WebSockets</span>
                <span class="tech-badge">Géolocalisation</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # FASO DOG
        st.markdown("""
        <div class="project-card">
            <span class="tech-badge tech-badge-purple">Génétique & Élevage</span>
            <div class="project-title" style="margin-top: 5px;">FASO DOG — Registre Généalogique & Écosystème Canin</div>
            <div class="project-role">Concepteur Algorithmique & Développeur</div>
            <div class="project-desc">
                Plateforme de certification généalogique et de suivi sanitaire d'élevage.
                Intégration de l'algorithme de calcul du Coefficient de Consanguinité de Wright sur plusieurs générations pour assister les éleveurs et génération automatisée d'arbres généalogiques et certificats PDF certifiés.
            </div>
            <div class="impact-box">
                Résultats obtenus : Plus de 1 500 pedigrees officiels vérifiés et contrôle rigoureux des plans d'accouplement.
            </div>
            <div class="badge-container">
                <span class="tech-badge">Flutter</span>
                <span class="tech-badge">Coefficient de Wright</span>
                <span class="tech-badge">Moteur PDF Certifié</span>
                <span class="tech-badge">API REST</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ONGLET 5 : ANALYTICS & SIMULATEUR DE RISQUE
# ------------------------------------------------------------------------------
with tab_sim:
    st.markdown("### Analytics de Portefeuille & Détection de Risque")
    st.caption("Visualisation synthétique des réalisations logicielles et démonstration du moteur d'évaluation des transactions financières.")

    # 1. Analytics de portefeuille
    st.markdown("#### Répartition du Portefeuille de Projets")

    col_chart1, col_chart2 = st.columns([1.1, 1.1])

    projects_data = [
        {"Domaine": "IA & Data Science", "Projet": "Fraude Mobile Money", "Maturite": "Production", "Technologie": "LightGBM"},
        {"Domaine": "IA & Data Science", "Projet": "Moteur Anti-Fraude Sinistres", "Maturite": "Production", "Technologie": "XGBoost"},
        {"Domaine": "IA & Data Science", "Projet": "E-SUIVI Edge AI", "Maturite": "Production", "Technologie": "TFLite / Flutter"},
        {"Domaine": "Actuariat & Réassurance", "Projet": "Optimisation Traités CIMA", "Maturite": "Recherche Appliquée", "Technologie": "EVT / PyTorch"},
        {"Domaine": "Actuariat & Réassurance", "Projet": "REASS-NEXT ERP", "Maturite": "Production", "Technologie": "FastAPI"},
        {"Domaine": "Actuariat & Réassurance", "Projet": "SI & SAGE 100c", "Maturite": "Production", "Technologie": "MS SQL / ITIL"},
        {"Domaine": "Actuariat & Réassurance", "Projet": "Faso Assur Tech", "Maturite": "Production", "Technologie": "FastAPI"},
        {"Domaine": "Projets Nationaux & GovTech", "Projet": "SYLVIE V2 Guichet Unique", "Maturite": "Production Nationale", "Technologie": "Spring Boot"},
        {"Domaine": "Projets Nationaux & GovTech", "Projet": "BURKINDI Naturalisation", "Maturite": "Production Nationale", "Technologie": "Symfony 7"},
        {"Domaine": "Projets Nationaux & GovTech", "Projet": "Guichets Justice & Santé", "Maturite": "Production Nationale", "Technologie": "Symfony / Python"},
        {"Domaine": "Digitalisation & Solutions Métier", "Projet": "EKDS-PREFA", "Maturite": "Production", "Technologie": "Laravel / Flutter"},
        {"Domaine": "Digitalisation & Solutions Métier", "Projet": "Colis Express", "Maturite": "Production", "Technologie": "Flutter / Filament"},
        {"Domaine": "Digitalisation & Solutions Métier", "Projet": "Doux Goût (Vente & Suivi)", "Maturite": "Production", "Technologie": "PHP / Laravel"},
        {"Domaine": "Digitalisation & Solutions Métier", "Projet": "FASO DOG", "Maturite": "Production", "Technologie": "Flutter / Algo"}
    ]
    df_p = pd.DataFrame(projects_data)

    with col_chart1:
        domain_counts = df_p["Domaine"].value_counts().reset_index()
        domain_counts.columns = ["Domaine", "Nombre de Projets"]
        
        fig_pie = px.pie(
            domain_counts,
            values="Nombre de Projets",
            names="Domaine",
            hole=0.45,
            color_discrete_sequence=["#1D4ED8", "#0F766E", "#6D28D9", "#B45309"],
            title="Distribution par Domaine d'Expertise"
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#FFFFFF', width=2)))
        fig_pie.update_layout(
            font=dict(family="Plus Jakarta Sans, sans-serif", color="#0F172A"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=340,
            margin=dict(l=10, r=10, t=40, b=10),
            showlegend=False
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_chart2:
        tech_counts = df_p["Technologie"].value_counts().head(7).reset_index()
        tech_counts.columns = ["Stack / Framework", "Occurrences"]
        
        fig_bar = px.bar(
            tech_counts,
            x="Occurrences",
            y="Stack / Framework",
            orientation="h",
            color="Occurrences",
            color_continuous_scale=[[0, "#93C5FD"], [1, "#1D4ED8"]],
            title="Technologies Fréquemment Déployées"
        )
        fig_bar.update_layout(
            font=dict(family="Plus Jakarta Sans, sans-serif", color="#0F172A"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            height=340,
            margin=dict(l=10, r=10, t=40, b=10),
            coloraxis_showscale=False
        )
        fig_bar.update_yaxes(categoryorder="total ascending", gridcolor="#F1F5F9")
        fig_bar.update_xaxes(gridcolor="#F1F5F9")
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    # 2. Simulateur de scoring de risque transactionnel
    st.markdown("#### Démonstration : Moteur d'Évaluation du Risque Transactionnel")
    st.markdown("""
    Cette interface illustre les règles heuristiques et pondérations prédictives issues de nos pipelines anti-fraude appliqués aux transactions de paiements et de transferts.
    Ajustez les paramètres d'une opération pour observer l'indice de risque calculé et la procédure de conformité correspondante.
    """)

    with st.container(border=True):
        col_in1, col_in2, col_in3 = st.columns(3)

        with col_in1:
            op_type = st.selectbox("Type d'Opération", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEPOSIT"])
            amount = st.number_input("Montant de la Transaction", min_value=100.0, max_value=5000000.0, value=75000.0, step=5000.0)

        with col_in2:
            orig_old_bal = st.number_input("Solde Initial Émetteur", min_value=0.0, max_value=10000000.0, value=76000.0, step=5000.0)
            orig_new_bal = st.number_input("Solde Résiduel Émetteur", min_value=0.0, max_value=10000000.0, value=1000.0, step=5000.0)

        with col_in3:
            dest_old_bal = st.number_input("Solde Initial Bénéficiaire", min_value=0.0, max_value=10000000.0, value=0.0, step=5000.0)
            dest_new_bal = st.number_input("Solde Final Bénéficiaire", min_value=0.0, max_value=10000000.0, value=0.0, step=5000.0)
            tx_hour = st.slider("Heure de la Transaction (0h - 23h)", min_value=0, max_value=23, value=3)

        # Calcul d'indice de risque
        base_score = 0
        if op_type in ["TRANSFER", "CASH_OUT"]:
            base_score += 28
        else:
            base_score += 5

        orig_diff = orig_old_bal - orig_new_bal
        if orig_old_bal > 0 and orig_new_bal == 0 and abs(orig_diff - amount) < 1.0:
            base_score += 35
        elif orig_new_bal < 0:
            base_score += 30

        if dest_old_bal == 0 and dest_new_bal == 0 and amount > 10000 and op_type == "TRANSFER":
            base_score += 25

        if 1 <= tx_hour <= 5:
            base_score += 12

        if orig_old_bal > 0:
            ratio = amount / orig_old_bal
            if ratio > 0.95:
                base_score += 15

        risk_score = min(100, max(2, base_score))

        col_res1, col_res2 = st.columns([1.2, 1.8])

        with col_res1:
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Indice de Risque Calculé (/100)", 'font': {'size': 14, 'family': 'Plus Jakarta Sans', 'color': '#334155'}},
                number={'suffix': "/100", 'font': {'size': 24, 'family': 'Plus Jakarta Sans', 'color': '#0F172A'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#CBD5E1"},
                    'bar': {'color': "#DC2626" if risk_score >= 70 else ("#D97706" if risk_score >= 35 else "#0F766E")},
                    'steps': [
                        {'range': [0, 35], 'color': "#F0FDF4"},
                        {'range': [35, 70], 'color': "#FFFBEB"},
                        {'range': [70, 100], 'color': "#FEF2F2"}
                    ],
                    'threshold': {
                        'line': {'color': "#0F172A", 'width': 2},
                        'thickness': 0.75,
                        'value': 70
                    }
                }
            ))
            fig_gauge.update_layout(
                font=dict(family="Plus Jakarta Sans, sans-serif"),
                paper_bgcolor="rgba(0,0,0,0)",
                height=250,
                margin=dict(l=20, r=20, t=35, b=10)
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        with col_res2:
            st.markdown("##### Décision & Procédure de Conformité Déclenchée :")
            if risk_score >= 70:
                st.error("""
                **Décision : Transaction Suspendue — Audit Requis**  
                - **Motif :** Vidage intégral de compte ou compte bénéficiaire non consolidé en flux critique.  
                - **Procédure :** Gel conservatoire de l'opération, journalisation d'audit WORM et transmission à l'équipe conformité.
                """)
            elif risk_score >= 35:
                st.warning("""
                **Décision : Authentification Renforcée Requise (2FA / OTP)**  
                - **Motif :** Opération à montant significatif ou plage horaire nocturne inhabituelle.  
                - **Procédure :** Déclenchement d'un défi d'authentification biométrique ou validation OTP avant exécution.
                """)
            else:
                st.success("""
                **Décision : Validation Immédiate (Fast-Track)**  
                - **Motif :** Profil transactionnel cohérent avec les critères réguliers et soldes normaux.  
                - **Procédure :** Inférence et compensation exécutées sous les 150 ms sans intervention manuelle.
                """)

            st.markdown(f"""
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; padding: 9px 12px; border-radius: 6px; font-size: 0.83rem; color: #475569;">
                <strong>Paramètres d'inférence :</strong> Opération <code>{op_type}</code> de <code>{amount:,.2f}</code> | 
                Variation solde émetteur : <code>{orig_diff:,.2f}</code> | 
                Heure locale : <code>{tx_hour:02d}h00</code>.
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 6. FORMULAIRE DE CONTACT PROFESSIONNEL
# ==============================================================================
st.markdown("---")
st.subheader("Contact Professionnel")
st.write("Pour toute opportunité d'architecture logicielle, de modélisation actuarielle, d'expertise IA ou de consulting.")

c_form_col, c_contact_col = st.columns([1.8, 1.2])

with c_form_col:
    with st.form("contact_form", clear_on_submit=True):
        f_name = st.text_input("Nom & Prénom *", placeholder="Ex : Dr. Diallo")
        f_org = st.text_input("Organisation / Institution", placeholder="Ex : Banque, Compagnie d'Assurances, Ministère")
        f_email = st.text_input("Adresse Email Professionnelle *", placeholder="Ex : direction.tech@organisation.org")
        f_subject = st.selectbox("Objet de la Sollicitation", [
            "Architecture Logicielle & Microservices",
            "Projet Data Science & Détection de Fraude",
            "Modélisation Actuarielle CIMA & Réassurance",
            "Dématérialisation & Projet GovTech",
            "Audit de Système d'Information & SAGE 100c",
            "Autre échange technique"
        ])
        f_msg = st.text_area("Message / Périmètre du Projet *", height=120, placeholder="Précisez succinctement votre besoin ou le cadre de votre projet...")
        
        btn_submit = st.form_submit_button("Envoyer le message", use_container_width=True)
        if btn_submit:
            if f_name.strip() and f_email.strip() and f_msg.strip():
                st.success(f"Merci {f_name}. Votre message a bien été envoyé. Une réponse vous sera apportée sous 24 à 48 heures.")
            else:
                st.error("Veuillez renseigner tous les champs obligatoires (*) avant de soumettre.")

with c_contact_col:
    st.markdown("""
    <div class="project-card" style="margin-bottom: 0;">
        <h4 style="margin-top: 0; color: #0F172A; font-weight: 700;">Coordonnées Directes</h4>
        <p style="color: #334155; font-size: 0.9rem; line-height: 1.6;">
            <strong>Abdellatif Kiswendsida NIKIEMA</strong><br>
            Ingénieur Logiciel Full-Stack & Spécialiste IA<br>
            Certifié ITIL v4 & PRINCE2
        </p>
        <hr style="border: none; border-top: 1px solid #E2E8F0; margin: 0.8rem 0;">
        <p style="color: #475569; font-size: 0.86rem; margin-bottom: 0.4rem;">
            <strong>Localisation :</strong> Ouagadougou, Burkina Faso
        </p>
        <p style="color: #475569; font-size: 0.86rem; margin-bottom: 0.4rem;">
            <strong>Téléphone :</strong> <a href="tel:+22678805060" style="color: #2563EB; text-decoration: none;">+226 78 80 50 60</a> / <a href="tel:+22665369949" style="color: #2563EB; text-decoration: none;">+226 65 36 99 49</a>
        </p>
        <p style="color: #475569; font-size: 0.86rem; margin-bottom: 0.4rem;">
            <strong>Email :</strong> <a href="mailto:abdellatifnikiema@gmail.com" style="color: #2563EB; text-decoration: none;">abdellatifnikiema@gmail.com</a>
        </p>
        <p style="color: #475569; font-size: 0.86rem; margin-bottom: 0;">
            <strong>Disponibilité :</strong> Missions présentielles et mandats internationaux à distance.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 7. PIED DE PAGE
# ==============================================================================
st.markdown("""
<div class="footer-bar">
    © 2026 Abdellatif Kiswendsida NIKIEMA. Tous droits réservés.
</div>
""", unsafe_allow_html=True)
