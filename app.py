import streamlit as st
import pandas as pd
import numpy as np

# # dataframe
# st.dataframe(df)

# # gráfico de linha
# st.line_chart(df)

# # gráfico de barras
# st.bar_chart(df)

if st.sidebar.button('Exibir gráfico'):
    df = pd.DataFrame(
        np.random.rand(10, 4),
        columns=['Preço', 'Taxa de ocupação', 'Taxa de inadimplência', 'Pessoas por casa']
    )

    st.bar_chart(df)


