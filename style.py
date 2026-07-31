import streamlit as st

COLOR = {
    "primary": "#1565C0",
    "accent": "#2E7D32",
    "warning": "#EF6C00",
    "danger": "#C62828",
    "background": "#F7F9FC",
    "text": "#1F2937",
    "muted": "#6B7280",
}

def apply_global_style():
    st.markdown(
        """
        <style>
        .main {
            background-color: #F7F9FC;
        }

        h1, h2, h3 {
            color: #1F2937;
        }

        section[data-testid="stSidebar"] {
            background-color: #FFFFFF;
            border-right: 1px solid #E5E7EB;
        }

        div[data-testid="stMetric"] {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 14px;
            border: 1px solid #E5E7EB;
            box-shadow: 0px 1px 4px rgba(0,0,0,0.04);
        }

        div[data-testid="stAlert"] {
            border-radius: 12px;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .small-muted {
            color: #6B7280;
            font-size: 0.95rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def page_header(title, subtitle):
    st.title(title)
    st.markdown(f"<p class='small-muted'>{subtitle}</p>", unsafe_allow_html=True)
    st.divider()

def sidebar_summary():
    st.sidebar.title("EquiCure")
    st.sidebar.markdown("ML-based ED wait-time analysis")
    st.sidebar.divider()
    st.sidebar.markdown("**Best model:** Linear Regression")
    st.sidebar.markdown("**Best RMSE:** 44.73 min")
    st.sidebar.markdown("**Valid facilities:** 58")
