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
        /* Main page background */
        .main {
            background-color: #F7F9FC;
        }

        /* Main content spacing */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }

        /* Sidebar container */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFFFFF 0%, #F3F7FB 100%);
            border-right: 1px solid #E5E7EB;
        }

        /* Sidebar title text */
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #1F2937;
        }

        /* Sidebar navigation links */
        section[data-testid="stSidebar"] a {
            border-radius: 10px;
            padding: 6px 10px;
            margin-bottom: 4px;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 14px;
            border: 1px solid #E5E7EB;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
        }

        /* Alert boxes */
        div[data-testid="stAlert"] {
            border-radius: 12px;
        }

        /* Dataframes */
        div[data-testid="stDataFrame"] {
            border-radius: 12px;
            overflow: hidden;
        }

        /* Custom reusable card */
        .info-card {
            background-color: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 18px 20px;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
            min-height: 150px;
            margin-bottom: 16px;
        }

        .info-card-title {
            color: #1565C0;
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 6px;
        }

        .info-card-name {
            color: #111827;
            font-size: 1.0rem;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .info-card-body {
            color: #4B5563;
            font-size: 0.95rem;
            line-height: 1.45;
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
    st.sidebar.markdown(
        """
        <div style="
            background-color: #1565C0;
            padding: 14px 16px;
            border-radius: 14px;
            margin-bottom: 16px;
        ">
            <div style="color: white; font-size: 1.25rem; font-weight: 700;">
                EquiCure
            </div>
            <div style="color: #DBEAFE; font-size: 0.9rem;">
                ED Wait-Time Equity Dashboard
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("### Project Snapshot")
    st.sidebar.markdown("**Best model:** Linear Regression")
    st.sidebar.markdown("**Best RMSE:** 44.73 min")
    st.sidebar.markdown("**Valid facilities:** 58")
    st.sidebar.markdown("**Scope:** LA County")

    st.sidebar.divider()

    st.sidebar.markdown("### How to Read")
    st.sidebar.caption(
        "Start with Findings, then review Model Performance, Data & Methods, and About."
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "Research demo only. Not intended for real-time clinical or patient navigation decisions."
    )
