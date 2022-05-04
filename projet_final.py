import yfinance as yf
import streamlit as st
import datetime as dt

#Settings de la page
st.set_page_config(layout='wide')

#Choisir l'action analysée
tickerSymbol = st.sidebar.text_input("Entrez votre symbole",value='MSFT')
#Choisir la période de temps pour l'analyse
start_date = st.sidebar.date_input("Départ de l'analyse", dt.date(2010,1,1))
end_date = dt.date.today()

#Aller chercher les données sur l'entreprise
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start= start_date, end= end_date)

#Titre de la page
st.markdown("<h1 style='text-align: center; color: red;'>Cette page permet d'obtenir les informations clés de l'entreprise de votre choix</h1>", unsafe_allow_html=True)

#Instruction de la page
st.markdown("<h1 style='text-align: left; color: black;'>Veuillez insérer le symbole de votre choix dans la barre à gauche</h1>", unsafe_allow_html=True)

#L'entreprise choisie
st.markdown(f"<h1 style='text-align: left; color: black;'>L'entreprise choisie est celle de {tickerData.info['shortName']} </h1>", unsafe_allow_html=True)
st.write(f'''Voici les données historiques du **cours de fermeture** ainsi que du **volume** de {tickerSymbol} selon la période choisie :''')

# Graphique 1
st.write("""
## Cours de fermeture
""")
st.line_chart(tickerDf.Close)

#Graphique 2
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

# Rendement de l'action
c1, c2, c3 = st.columns(3)

r = (tickerDf.Close[-1] - tickerDf.Close[-2]) / tickerDf.Close[-2]
r1 = (tickerDf.Close[-1] - tickerDf.Close[0]) / tickerDf.Close[0]

c1.metric(label="Secteur de l'entreprise", value = f"{tickerData.info['sector']}")
c2.metric(label=f"Rendement de la dernière journée", value = f"{tickerDf.Close[-1]:.2f}", delta = f"{r * 100:.2f} %")
c3.metric(label=f"Rendement depuis {start_date}", value=f"{tickerDf.Close[-1]:.2f}", delta=f"{r1 * 100:.2f} %")

#Metrics regroupant les principaux éléments financiers de l'entreprise jugés important
st.write("""
## Quelques données importantes
""")

d1, d2, d3, d4, d5 = st.columns(5)

d1.metric(label="Capitalisation boursière", value = f"{tickerData.info['marketCap']} $")
d2.metric(label="Cible basse des analystes", value = f"{tickerData.info['targetLowPrice']} $")
d3.metric(label="Cible haute des analystes", value = f"{tickerData.info['targetHighPrice']} $")
d4.metric(label="Cible moyenne des analystes", value = f"{tickerData.info['targetMedianPrice']} $")
d5.metric(label="Recommandation des analystes", value = f"{tickerData.info['recommendationKey']}")

f1, f2, f3, f4, f5 = st.columns(5)

f1.metric(label="BETA", value = f"{tickerData.info['beta']}")
f2.metric(label="Dernier dividende trimestriel ditribué", value = f"{tickerData.info['lastDividendValue']} $")
f3.metric(label="Rendement du dividende", value = f"{tickerData.info['dividendYield'] * 100:.2f} %")
f4.metric(label="Pourcentage des profits distribué en dividende", value = f"{tickerData.info['payoutRatio']* 100:.2f} %")
f5.metric(label="Nombre d'analystes", value = f"{tickerData.info['numberOfAnalystOpinions']}")

#Metrics pour voir certains des ratios importants
st.write("""
## Quelques ratios importants
""")

e1, e2, e3, e4, e5 = st.columns(5)

e1.metric(label="Marge brute", value = f"{tickerData.info['grossMargins'] * 100:.2f} %")
e2.metric(label="Marge avant intérêts/impôts/amortissement", value = f"{tickerData.info['ebitdaMargins'] * 100:.2f} %")
e3.metric(label="Marge nette", value = f"{tickerData.info['profitMargins'] * 100:.2f} %")
e4.metric(label="Cours/Bénéfices", value = f"{tickerData.info['priceToBook']:.2f}")
e5.metric(label="Forward PE", value = f"{tickerData.info['forwardPE']:.2f}")

g1, g2, g3, g4, g5 = st.columns(5)

g1.metric(label="Quick ratio", value = f"{tickerData.info['quickRatio']:.2f}")
g2.metric(label="Current ratio", value = f"{tickerData.info['currentRatio']:.2f}")
g3.metric(label="Dette sur fonds propres", value = f"{tickerData.info['debtToEquity']:.2f}")
g4.metric(label="Rendement des capitaux propres", value = f"{tickerData.info['returnOnEquity']:.2f}")
g5.metric(label="Croissance du revenu", value = f"{tickerData.info['revenueGrowth'] * 100:.2f} %")
