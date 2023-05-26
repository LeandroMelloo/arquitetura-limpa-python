import streamlit as st
import pandas as pd
import numpy as np

if st.sidebar.button('Exibir gráfico'):
    df = pd.DataFrame(
        np.random.rand(10, 4),
        columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casa']
    )

    st.bar_chart(df)


