import streamlit as st
def add_logo():
    st.markdown(    
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "";
                background-image: url('data:image/png;base64,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')
                background-size:139px, 76px;
                background-repeat: no-repeat;
                width:139px;
                height:76px;
                display:inline-block;
                margin-left: 20px;
                font-size: 30px;
                position: relative;
                top: 30px;
            }
        </style>
        """,unsafe_allow_html=True)
