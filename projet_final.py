import yfinance as yf
import streamlit as st
import datetime as dt

st.set_page_config(layout='wide')

#Choisir l'action analysée
tickerSymbol = st.sidebar.text_input("Entrez votre symbole",value='AAPL')
#Choisir la période de temps pour l'analyse
start_date = st.sidebar.date_input("Départ de l'analyse",dt.date(2010,1,1))
end_date = dt.date.today()


st.title(f"Informations concernant l'action: {tickerSymbol} ")

st.write(f'''Voici les données historiques du **cours de fermeture** ainsi que du ***volume*** de {tickerSymbol} selon la période choisie''')

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

#Aller chercher les données sur l'entreprise
tickerData = yf.Ticker(tickerSymbol)

#Aller chercher les données historiques de l'entreprise choisie
tickerDf = tickerData.history(period='1d', start= start_date, end= end_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# Graphique 1
st.write("""
## Cours de fermeture
""")
st.line_chart(tickerDf.Close)

#Graphique 2
st.write("""
## Prix de volume
""")
st.line_chart(tickerDf.Volume)

# Rendement de l'action
c1, c2 = st.columns(2)

r = (tickerDf.Close[-1] - tickerDf.Close[0]) / tickerDf.Close[0]
r1 = (tickerDf.Close[-1] - tickerDf.Close[-2]) / tickerDf.Close[-2]

c1.metric(label=f"Rendement de la dernière journée", value = f"{tickerDf.Close[-1]:.2f}", delta = f"{r * 100:.2f} %")
c2.metric(label=f"Rendement depuis {start_date}", value=f"{tickerDf.Close[-1]:.2f}", delta=f"{r1 * 100:.2f} %")

#Tableau d'information, faire un tableau qui résume les principaux éléments financiers de l'entreprise

#st.write(f"Voici quelques données importantes de base concernant {tickerSymbol}.")

#Tableau 1
#Colonne 1 = ['Capitalisation boursière', '52 week high', '52 week low', 'Volume de la journée', 'BETA']
#Colonne 2 = [f'{tickerData.info['marketCap']}', f'{tickerData.info['52WeekHigh']}', f'{tickerData.info['52WeekLow']}', f'{tickerData.info['Volume']}', f'{tickerData.info['beta']}']

#Tableau de ratios
#Colonne 1 = ['Marge brute', 'Marge nette', 'Cours/Bénéfices', 'Cours/Valeur comptable']
#Colonne 2 = [f'{tickerData.info['grossMargins'] * 100}', f'{tickerSymbol} est de {tickerData.info['profitMargins'] * 100}', f'{tickerData.info['forwardPE']}', f'{tickerData.info['priceToBook']}']

# ou faire un plein de metric comme en haut
# Avec recommandation, Prix cible, Dividend yield, Earning P/S et toute les données qu'on peut sortir comme en bas      

st.write(f"{tickerSymbol} a une capitalisation boursière représentant {tickerData.info['marketCap']} $.")
st.write(f"{tickerSymbol} a un BETA de {tickerData.info['beta']} .")

st.write(f"La marge bénéficiaire brute de {tickerSymbol} est de {tickerData.info['grossMargins'] * 100} %.")
st.write(f"La marge bénéficiaire nette de {tickerSymbol} est de {tickerData.info['profitMargins'] * 100} %.")

st.write(f"Le ratio cours/valeur comptable de {tickerSymbol} est de {tickerData.info['priceToBook']} .")
st.write(f"Le ratio cours/bénéfice de {tickerSymbol} est de {tickerData.info['forwardPE']} .")

tickerData.info

