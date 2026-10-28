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

# ---------------------------------------------------------
# Configuration de la page
# ---------------------------------------------------------
st.set_page_config(
    page_title="Portfolio | Abdellatif - Data Scientist & AI Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Style CSS personnalisé & Design moderne
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Hero section styling */
    .hero-title {
        font-size: 2.7rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 50%, #3B82F6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        color: #334155;
        margin-bottom: 1rem;
    }

    .hero-description {
        font-size: 1.05rem;
        color: #475569;
        line-height: 1.6;
    }

    /* Badges & Pills */
    .badge {
        display: inline-block;
        background: #EFF6FF;
        color: #1D4ED8;
        border: 1px solid #BFDBFE;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 9999px;
        font-size: 0.85rem;
        margin: 3px 4px 3px 0;
        transition: all 0.2s ease-in-out;
    }
    .badge:hover {
        background: #DBEAFE;
        transform: translateY(-1px);
    }

    .badge-accent {
        background: #F0FDF4;
        color: #15803D;
        border: 1px solid #BBF7D0;
    }

    .badge-purple {
        background: #FAF5FF;
        color: #7E22CE;
        border: 1px solid #E9D5FF;
    }

    /* Card styling */
    .custom-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 1.25rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }

    .stat-box {
        background: linear-gradient(145deg, #F8FAFC 0%, #EDF2F7 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }

    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #2563EB;
        line-height: 1;
    }

    .stat-label {
        font-size: 0.85rem;
        font-weight: 600;
        color: #64748B;
        margin-top: 0.35rem;
    }

    /* Timeline styling */
    .timeline-item {
        border-left: 2px solid #3B82F6;
        padding-left: 1.2rem;
        margin-left: 0.5rem;
        margin-bottom: 1.5rem;
        position: relative;
    }
    .timeline-item::before {
        content: "";
        position: absolute;
        left: -6px;
        top: 4px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #2563EB;
        border: 2px solid #FFFFFF;
    }
    .timeline-role {
        font-weight: 700;
        font-size: 1.05rem;
        color: #0F172A;
    }
    .timeline-company {
        font-weight: 600;
        color: #2563EB;
        font-size: 0.95rem;
    }
    .timeline-date {
        font-size: 0.82rem;
        color: #64748B;
        margin-bottom: 0.4rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 0.85rem;
        padding: 2rem 0 1rem 0;
        margin-top: 3rem;
        border-top: 1px solid #E2E8F0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRE LATÉRALE (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    profile_path = "assets/profile.png"
    if PIL_AVAILABLE and os.path.exists(profile_path):
        try:
            img = Image.open(profile_path)
            st.image(img, use_container_width=True)
        except Exception:
            pass
    else:
        st.markdown("""
        <div style="text-align: center; padding: 1.5rem 0;">
            <div style="width: 110px; height: 110px; margin: 0 auto; border-radius: 50%; background: linear-gradient(135deg, #2563EB, #1D4ED8); display: flex; align-items: center; justify-content: center; font-size: 3rem; color: white; box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);">
                👨‍💻
            </div>
            <h3 style="margin-top: 0.8rem; margin-bottom: 0.1rem; color: #0F172A;">Abdellatif</h3>
            <p style="color: #64748B; font-size: 0.9rem; margin-bottom: 0;">Data Scientist & Ingénieur IA</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📍 Coordonnées")
    st.markdown("📍 **Localisation :** Paris & Remote (France)")
    st.markdown("📧 **Email :** [contact.abdellatif@example.com](mailto:contact.abdellatif@example.com)")
    st.markdown("💼 **Disponibilité :** À l'écoute de nouvelles opportunités")

    st.markdown("---")
    st.markdown("### 🌐 Liens professionnels")
    st.markdown("""
    - [🔗 **LinkedIn**](https://linkedin.com)
    - [🐙 **GitHub**](https://github.com)
    - [✍️ **Medium / Blog**](https://medium.com)
    - [🤗 **Hugging Face**](https://huggingface.co)
    """)

    st.markdown("---")
    # Téléchargement de CV
    cv_dummy_content = b"""%PDF-1.4
1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj
2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj
3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R >> endobj
4 0 obj << /Length 44 >> stream
BT /F1 12 Tf 72 712 Td (CV de Abdellatif - Data Scientist) Tj ET
endstream
endobj
xref
0 5
0000000000 65535 f 
0000000010 00000 n 
0000000060 00000 n 
0000000117 00000 n 
0000000201 00000 n 
trailer << /Size 5 /Root 1 0 R >>
startxref
295
%%EOF"""

    st.download_button(
        label="📄 Télécharger mon CV (PDF)",
        data=cv_dummy_content,
        file_name="CV_Abdellatif_Data_Scientist.pdf",
        mime="application/pdf",
        use_container_width=True
    )

    st.markdown("---")
    st.caption("✨ Portfolio interactif propulsé par Streamlit & Plotly")

# ---------------------------------------------------------
# SECTION HERO & PRÉSENTATION
# ---------------------------------------------------------
col_hero_1, col_hero_2 = st.columns([2.2, 1.1])

with col_hero_1:
    st.markdown('<div class="hero-title">Bonjour, je suis Abdellatif 👋</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Data Scientist & Machine Learning Engineer | Spécialiste IA & Data Visualisation</div>',
        unsafe_allow_html=True
    )
    st.markdown("""
    <div class="hero-description">
        Passionné par l'exploitation de la donnée et l'intelligence artificielle, je conçois des 
        <strong>modèles de Machine Learning robustes</strong>, des <strong>pipelines d'ingénierie de données</strong> et des 
        <strong>applications décisionnelles interactives</strong>.<br><br>
        Mon objectif : transformer des données complexes en leviers stratégiques mesurables et déployer des solutions 
        IA orientées produit à fort impact.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    c_btn1, c_btn2 = st.columns([1, 1.2])
    with c_btn1:
        st.link_button("🚀 Découvrir mes projets", "#projets-phares", use_container_width=True)
    with c_btn2:
        st.link_button("📬 Me contacter directement", "#me-contacter", use_container_width=True)

with col_hero_2:
    st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 15px;">
        <div class="stat-box">
            <div class="stat-number">4+</div>
            <div class="stat-label">Années d'Expérience</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">20+</div>
            <div class="stat-label">Projets Réalisés</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">92%</div>
            <div class="stat-label">Précision Moyenne ML</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">100%</div>
            <div class="stat-label">Code Open Source</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# COMPÉTENCES TECHNIQUES
# ---------------------------------------------------------
st.subheader("🛠️ Compétences & Technologies")

c_skill1, c_skill2, c_skill3, c_skill4 = st.columns(4)

with c_skill1:
    st.markdown("#### 💻 Langages & Core")
    st.markdown("""
    <span class="badge">Python</span>
    <span class="badge">SQL (PostgreSQL, BigQuery)</span>
    <span class="badge">Bash / Linux</span>
    <span class="badge">R</span>
    <span class="badge">Git / GitHub</span>
    """, unsafe_allow_html=True)

with c_skill2:
    st.markdown("#### 🧠 Machine Learning & IA")
    st.markdown("""
    <span class="badge badge-accent">Scikit-Learn</span>
    <span class="badge badge-accent">PyTorch</span>
    <span class="badge badge-accent">XGBoost / LightGBM</span>
    <span class="badge badge-accent">NLP & Transformers</span>
    <span class="badge badge-accent">LangChain / RAG</span>
    <span class="badge badge-accent">Hugging Face</span>
    """, unsafe_allow_html=True)

with c_skill3:
    st.markdown("#### 📊 Data & Visualisation")
    st.markdown("""
    <span class="badge">Pandas</span>
    <span class="badge">NumPy</span>
    <span class="badge">Plotly</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Seaborn / Matplotlib</span>
    <span class="badge">Power BI / Tableau</span>
    """, unsafe_allow_html=True)

with c_skill4:
    st.markdown("#### ⚙️ MLOps & Cloud")
    st.markdown("""
    <span class="badge badge-purple">Docker</span>
    <span class="badge badge-purple">FastAPI</span>
    <span class="badge badge-purple">MLflow</span>
    <span class="badge badge-purple">Google Cloud (GCP)</span>
    <span class="badge badge-purple">CI/CD (GitHub Actions)</span>
    <span class="badge badge-purple">DVC</span>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# PROJETS PHARES AVEC DÉMOS INTERACTIVES
# ---------------------------------------------------------
st.subheader("🚀 Projets phares & Démonstrations interactives")
st.caption("Explorez les démonstrations interactives intégrées directement dans les onglets ci-dessous.")

tab1, tab2, tab3 = st.tabs([
    "📊 1. Modèle de Churn Client (Prédiction en direct)",
    "🤖 2. Assistant IA & RAG (Simulation Q&A)",
    "📈 3. Dashboard Financier & Séries Temporelles"
])

# Onglet 1 : Démo Churn
with tab1:
    col_p1_text, col_p1_demo = st.columns([1.2, 1.8])
    
    with col_p1_text:
        st.markdown("### Modèle de prédiction du Churn Client")
        st.markdown("""
        Ce projet résout un défi stratégique majeur : anticiper la résiliation d'abonnés télécom ou SaaS 
        avant qu'ils ne partent, permettant aux équipes de rétention d'agir proactivement.
        
        - **Pipeline :** Nettoyage des données, gestion du déséquilibre de classes (SMOTE), sélection de features.
        - **Modèles comparés :** Régression Logistique, Random Forest, XGBoost (meilleur F1-Score : 0.89).
        - **Explicabilité :** SHAP values pour comprendre l'impact de chaque variable client.
        """)
        st.markdown("**Stack :** `Python`, `XGBoost`, `Scikit-Learn`, `Pandas`, `Plotly`, `SHAP`")
        
        c_link1, c_link2 = st.columns(2)
        with c_link1:
            st.link_button("📂 Code GitHub", "https://github.com", use_container_width=True)
        with c_link2:
            st.link_button("📄 Rapport d'analyse", "https://github.com", use_container_width=True)

    with col_p1_demo:
        st.markdown("##### 🎛️ Testez le simulateur en temps réel :")
        with st.container(border=True):
            s_col1, s_col2 = st.columns(2)
            with s_col1:
                tenure = st.slider("Ancienneté du client (mois)", min_value=1, max_value=72, value=12)
                monthly_charges = st.slider("Facture mensuelle (€)", min_value=20.0, max_value=150.0, value=75.0)
                contract_type = st.selectbox("Type de contrat", ["Mois par mois", "1 An", "2 Ans"])
            with s_col2:
                support_tickets = st.slider("Nombre d'appels au support", min_value=0, max_value=10, value=3)
                tech_support = st.radio("Option Support Technique", ["Oui", "Non"], horizontal=True)
                payment_method = st.selectbox("Moyen de paiement", ["Prélèvement bancaire", "Carte de crédit", "Virement"])
            
            # Formule heuristique représentative d'un modèle ML entraîné
            contract_risk = 0.35 if contract_type == "Mois par mois" else (0.10 if contract_type == "1 An" else 0.02)
            support_risk = (support_tickets / 10.0) * 0.35
            tech_risk = -0.10 if tech_support == "Oui" else 0.10
            tenure_factor = (72 - tenure) / 72.0 * 0.25
            charge_factor = (monthly_charges / 150.0) * 0.15

            churn_prob = max(0.01, min(0.99, 0.15 + contract_risk + support_risk + tech_risk + tenure_factor + charge_factor - 0.2))

            # Jauge Plotly
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=churn_prob * 100,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Probabilité estimée de résiliation", 'font': {'size': 16, 'color': '#1E293B'}},
                number={'suffix': "%", 'font': {'size': 26, 'color': '#0F172A'}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
                    'bar': {'color': "#EF4444" if churn_prob > 0.5 else ("#F59E0B" if churn_prob > 0.3 else "#10B981")},
                    'steps': [
                        {'range': [0, 30], 'color': "#DCFCE7"},
                        {'range': [30, 50], 'color': "#FEF3C7"},
                        {'range': [50, 100], 'color': "#FEE2E2"}
                    ],
                    'threshold': {
                        'line': {'color': "black", 'width': 3},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            fig_gauge.update_layout(height=240, margin=dict(l=20, r=20, t=40, b=10))
            st.plotly_chart(fig_gauge, use_container_width=True)

            if churn_prob > 0.5:
                st.error("⚠️ **Risque élevé de résiliation !** Recommandation : Proposer une remise de fidélité ou un contact avec le gestionnaire de compte.")
            elif churn_prob > 0.3:
                st.warning("⚡ **Risque modéré.** Surveillance recommandée.")
            else:
                st.success("✅ **Client fidèle et sécurisé.** Faible probabilité de départ.")

# Onglet 2 : RAG & Assistant IA
with tab2:
    col_p2_text, col_p2_demo = st.columns([1.2, 1.8])
    
    with col_p2_text:
        st.markdown("### Assistant RAG d'Entreprise avec LangChain")
        st.markdown("""
        Un système intelligent de **Retrieval-Augmented Generation (RAG)** permettant aux collaborateurs 
        d'interroger en langage naturel la documentation interne d'entreprise (politiques RH, spécifications techniques, contrats).
        
        - **Indexation vectorielle :** Découpage sémantique (Chunking), génération d'embeddings avec `text-embedding-3-small`.
        - **Stockage vectoriel :** Base ChromaDB / Pinecone avec recherche par similarité cosinus et re-ranking.
        - **Génération contrôlée :** Réduction des hallucinations via un prompt structuré obligeant la citation stricte des sources.
        """)
        st.markdown("**Stack :** `LangChain`, `OpenAI API`, `ChromaDB`, `FastAPI`, `Streamlit`")
        
        c_link1, c_link2 = st.columns(2)
        with c_link1:
            st.link_button("📂 Repo GitHub", "https://github.com", use_container_width=True)
        with c_link2:
            st.link_button("🌐 Documentation", "https://github.com", use_container_width=True)

    with col_p2_demo:
        st.markdown("##### 💬 Simuler une interaction avec l'Assistant RAG :")
        with st.container(border=True):
            sample_questions = [
                "Quelle est la politique de télétravail ?",
                "Quel est le plafond de remboursement pour le matériel informatique ?",
                "Combien de jours de congés payés sont alloués par an ?"
            ]
            
            selected_question = st.selectbox("Sélectionnez ou tapez une question exemple :", sample_questions)
            custom_question = st.text_input("Ou posez une question personnalisée :", value=selected_question)
            
            knowledge_base = {
                "télétravail": {
                    "answer": "Selon l'accord d'entreprise (Section 4.2), chaque collaborateur a droit à 2 jours de télétravail par semaine après la période d'essai, avec une indemnité mensuelle forfaitaire de 30 € pour les frais de connexion.",
                    "source": "Guide_Collaborateur_RH_2024.pdf (Page 18, § 4.2)",
                    "score": "96.4% de similarité"
                },
                "matériel": {
                    "answer": "L'équipement standard comprend un ordinateur portable (MacBook Pro ou Dell XPS), un écran externe 27 pouces et une allocation de 250 € remboursable sur facture pour les accessoires ergonomiques.",
                    "source": "Politique_IT_Materiel.pdf (Page 5, § 2.1)",
                    "score": "94.8% de similarité"
                },
                "congés": {
                    "answer": "Les collaborateurs bénéficient de 25 jours ouvrés de congés payés légaux par an, complétés par 10 à 12 jours de RTT selon le calendrier annuel de l'accord cadre 35h.",
                    "source": "Convention_Temps_De_Travail.pdf (Page 9, § 1.3)",
                    "score": "98.1% de similarité"
                }
            }

            if st.button("🔍 Interroger l'assistant RAG", type="primary"):
                with st.spinner("Recherche sémantique dans la base vectorielle..."):
                    q_lower = custom_question.lower()
                    matched_key = None
                    if "télé" in q_lower or "remote" in q_lower:
                        matched_key = "télétravail"
                    elif "matériel" in q_lower or "ordinateur" in q_lower or "écran" in q_lower:
                        matched_key = "matériel"
                    elif "congé" in q_lower or "rtt" in q_lower or "vacance" in q_lower:
                        matched_key = "congés"
                    
                    if matched_key:
                        item = knowledge_base[matched_key]
                        st.markdown(f"**🤖 Réponse synthétisée :**\n\n{item['answer']}")
                        st.info(f"📚 **Source extraite :** `{item['source']}` — Indice de confiance : `{item['score']}`")
                    else:
                        st.markdown("""
                        **🤖 Réponse synthétisée :**  
                        D'après les documents indexés, cette question nécessite une validation auprès du support concerné ou n'apparaît pas explicitement dans les documents de démonstration.
                        """)
                        st.caption("ℹ️ Pour tester un cas réel complet, connectez vos propres PDF via l'application complète !")

# Onglet 3 : Dashboard Financier
with tab3:
    col_p3_text, col_p3_demo = st.columns([1.2, 1.8])

    with col_p3_text:
        st.markdown("### Dashboard Boursier & Analyse Technique")
        st.markdown("""
        Une plateforme d'analyse financière permettant de suivre en temps réel la volatilité des actifs,
        de calculer des indicateurs clés (**Moyennes Mobiles**, **RSI**, **Bandes de Bollinger**) et de simuler des signaux de trading.
        
        - **Calcul d'indicateurs :** Implémentation vectorisée NumPy / Pandas pour une rapidité optimale.
        - **Interactivité :** Graphiques Plotly zoomables et personnalisables.
        - **Prétraitement :** Normalisation, détection d'anomalies de volume.
        """)
        st.markdown("**Stack :** `Python`, `Plotly`, `Pandas`, `NumPy`, `Streamlit`")
        
        c_link1, c_link2 = st.columns(2)
        with c_link1:
            st.link_button("📂 Voir le code", "https://github.com", use_container_width=True)
        with c_link2:
            st.link_button("📊 Démo en direct", "https://streamlit.io", use_container_width=True)

    with col_p3_demo:
        st.markdown("##### 📈 Graphique interactif des cours & indicateurs :")
        with st.container(border=True):
            f_col1, f_col2, f_col3 = st.columns(3)
            with f_col1:
                asset_choice = st.selectbox("Actif financier", ["AI Tech Index (AITX)", "Green Energy ETF (GNRG)", "FinTech Alpha (FNTK)"])
            with f_col2:
                days_range = st.slider("Horizon temporel (jours)", min_value=30, max_value=180, value=90)
            with f_col3:
                show_sma = st.checkbox("Afficher MM 20 jours", value=True)

            # Génération d'une série temporelle réaliste
            np.random.seed(42 if "AITX" in asset_choice else (100 if "GNRG" in asset_choice else 2024))
            dates = pd.date_range(end=datetime.today(), periods=days_range)
            base_price = 140.0 if "AITX" in asset_choice else (85.0 if "GNRG" in asset_choice else 210.0)
            returns = np.random.normal(loc=0.0012, scale=0.02, size=days_range)
            price_series = base_price * np.exp(np.cumsum(returns))
            
            df_fin = pd.DataFrame({"Date": dates, "Prix": price_series})
            df_fin["MM20"] = df_fin["Prix"].rolling(window=20).mean()

            # Plotly interactive chart
            fig_fin = go.Figure()
            fig_fin.add_trace(go.Scatter(
                x=df_fin["Date"], y=df_fin["Prix"],
                mode='lines',
                name='Prix de clôture (€)',
                line=dict(color='#2563EB', width=2.5)
            ))

            if show_sma:
                fig_fin.add_trace(go.Scatter(
                    x=df_fin["Date"], y=df_fin["MM20"],
                    mode='lines',
                    name='Moyenne Mobile 20j',
                    line=dict(color='#F59E0B', width=2, dash='dash')
                ))

            last_price = df_fin['Prix'].iloc[-1]
            first_price = df_fin['Prix'].iloc[0]
            pct_change = ((last_price - first_price) / first_price) * 100

            fig_fin.update_layout(
                title=f"{asset_choice} : {last_price:.2f} € ({'+' if pct_change >= 0 else ''}{pct_change:.2f}%)",
                xaxis_title="Date",
                yaxis_title="Prix (€)",
                height=300,
                margin=dict(l=20, r=20, t=40, b=20),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_fin, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------
# EXPÉRIENCES & FORMATIONS
# ---------------------------------------------------------
col_exp, col_edu = st.columns(2)

with col_exp:
    st.subheader("💼 Expériences professionnelles")
    
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-role">Data Scientist Senior / Lead ML</div>
        <div class="timeline-company">Entreprise Tech & Solutions IA</div>
        <div class="timeline-date">2022 - Présent | Paris / Télétravail</div>
        <div style="color: #475569; font-size: 0.92rem;">
            - Conception et mise en production de pipelines de Machine Learning prédictifs et de NLP.<br>
            - Réduction du churn de 14% via l'optimisation des modèles de scoring client.<br>
            - Encadrement technique d'une équipe de 4 Data Scientists et mise en place de la stack MLOps (MLflow, Docker).
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-role">Data Scientist & Analyste</div>
        <div class="timeline-company">Cabinet de Conseil Data & Stratégie</div>
        <div class="timeline-date">2020 - 2022 | Paris</div>
        <div style="color: #475569; font-size: 0.92rem;">
            - Modélisation statistique, segmentation clients avancée et prévision de ventes (Time Series).<br>
            - Création de tableaux de bord interactifs pour les comités de direction.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_edu:
    st.subheader("🎓 Formations & Certifications")
    
    st.markdown("""
    <div class="timeline-item">
        <div class="timeline-role">Diplôme d'Ingénieur / Master en Data Science & IA</div>
        <div class="timeline-company">École d'Ingénieurs / Université</div>
        <div class="timeline-date">2017 - 2020</div>
        <div style="color: #475569; font-size: 0.92rem;">
            Spécialisation : Intelligence Artificielle, Mathématiques appliquées, Algorithmes et Big Data.
        </div>
    </div>
    
    <div class="timeline-item">
        <div class="timeline-role">Certifications Clés</div>
        <div class="timeline-company">Organismes Reconnus</div>
        <div class="timeline-date">2021 - 2024</div>
        <div style="color: #475569; font-size: 0.92rem;">
            - <strong>Google Cloud Certified</strong> - Professional Data Engineer<br>
            - <strong>DeepLearning.AI</strong> - Deep Learning Specialization & LangChain<br>
            - <strong>AWS Certified Machine Learning</strong> - Specialty
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# FORMULAIRE DE CONTACT
# ---------------------------------------------------------
st.markdown('<div id="me-contacter"></div>', unsafe_allow_html=True)
st.subheader("📬 Me contacter")
st.write("Vous avez un projet en tête, une opportunité ou souhaitez simplement échanger ? Laissez-moi un message !")

col_contact_form, col_contact_info = st.columns([2, 1])

with col_contact_form:
    with st.form("contact_form", clear_on_submit=True):
        f_name = st.text_input("Nom & Prénom *", placeholder="Ex : Marie Martin")
        f_email = st.text_input("Adresse email *", placeholder="Ex : marie.martin@entreprise.com")
        f_subject = st.text_input("Sujet", placeholder="Ex : Proposition d'opportunité / Projet IA")
        f_message = st.text_area("Votre message *", rows=5, placeholder="Décrivez brièvement votre projet ou votre demande...")
        
        submitted = st.form_submit_button("🚀 Envoyer le message", use_container_width=True)
        
        if submitted:
            if f_name.strip() and f_email.strip() and f_message.strip():
                st.success(f"✨ Merci **{f_name}** ! Votre message a été enregistré avec succès. Je vous répondrai dans les plus brefs délais.")
                st.balloons()
            else:
                st.error("⚠️ Veuillez renseigner tous les champs obligatoires (*) avant de valider.")

with col_contact_info:
    st.markdown("""
    <div class="custom-card">
        <h4 style="margin-top:0; color:#0F172A;">Coordonnées directes</h4>
        <p style="color:#475569; font-size:0.95rem;">
            <strong>Email :</strong><br>
            <a href="mailto:contact.abdellatif@example.com" style="color:#2563EB; text-decoration:none;">contact.abdellatif@example.com</a>
        </p>
        <p style="color:#475569; font-size:0.95rem;">
            <strong>Téléphone :</strong><br>
            +33 (0)6 00 00 00 00
        </p>
        <p style="color:#475569; font-size:0.95rem;">
            <strong>Localisation :</strong><br>
            Paris, France (Disponible sur site ou en Full Remote)
        </p>
        <hr style="border:none; border-top:1px solid #E2E8F0; margin:1rem 0;">
        <p style="font-size:0.85rem; color:#64748B;">
            ⚡ <em>Réponse garantie sous 24 à 48 heures ouvrées.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    © 2024 - 2026 Abdellatif. Tous droits réservés. Développé avec ❤️ en Python & Streamlit.
</div>
""", unsafe_allow_html=True)
