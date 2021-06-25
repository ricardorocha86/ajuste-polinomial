import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.image('bannerflai.jpg', use_column_width = 'always' )

st.title('Minha Página WEB')

dispersao = st.sidebar.number_input('Dispersão dos dados gerado [0-10]', 0, 10, 3)
cor1 = st.sidebar.color_picker('Escolha a cor dos pontos', '#0f54c8')
cor2 = st.sidebar.color_picker('Escolha a cor do ajuste')

modelo = st.sidebar.selectbox('Selecione o grau do ajuste', ['Grau 1', 'Grau 2'])

x = np.random.uniform(low = 1, high = 10, size = 500)
y = x**2 - 8*x +50 + np.random.normal(0, dispersao, len(x))



c2, c1, c0 = np.polyfit(x, y, deg = 2)

plt.plot(x, y, '.', marker = '^', alpha = 0.5, color = cor1)

ex = np.arange(1, 10, 0.05)

if modelo == 'Grau 1':
	b1, b0 = np.polyfit(x, y, deg = 1)
	plt.plot(ex, b0 + b1*ex, color = cor2)

if modelo == 'Grau 2':
	c2, c1, c0 = np.polyfit(x, y, deg = 2)
	plt.plot(ex, c0 + c1*ex + c2*ex**2, color = cor2)


st.pyplot()