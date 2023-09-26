import streamlit as st

def calculate_savings(minutes_saved, num_employees, num_years, avg_salary):
    # Konverterer minutter til timer
    hours_saved_per_day = minutes_saved / 60
    # Antall arbeidsdager i et år (vanligvis ca. 250)
    work_days_per_year = 230
    # Total antall timer spart per år
    total_hours_saved = hours_saved_per_day * work_days_per_year * num_employees
    # Konverter lønn fra årlig til timebasis
    avg_hourly_salary = avg_salary / (work_days_per_year * 7.5)
    # Total besparelse
    total_savings = total_hours_saved * avg_hourly_salary * num_years
    return total_savings

st.markdown('## Din innsparingskalkulator:')
st.markdown('### Hva koster manuelt arbeid bedriften virkelig?')

# Ingress
st.write("""
I en verden dominert av teknologi, hvorfor skal vi fortsatt utføre repetitive oppgaver manuelt? Føre inn samme data i to forskjellige system, for eksempel, er en notorisk tidstyv. Men den gode nyheten? Med riktig teknologi kan slike oppgaver effektivt elimineres ved å la systemene dine kommunisere sammen.
""")
st.write("Bruk kalkulatoren under og avslør hvor mye du faktisk kan spare ved å digitalisere disse gjentagende arbeidsoppgavene")


# Inputs fra bruker
X = st.slider('Hvor mange minutter bruker en ansatt på repetitive manuelle oppgaver hver dag?', 0, 120, 30, step=5)
Y = int(st.text_input('Hvor mange ansatte utfører disse oppgavene regelmessig?', 5))
W = int(st.text_input('Gjennomsnittlig årlig lønn for disse ansatte (i NOK):', 664680))
st.write("")
Z = st.slider('Hvor mange år ønsker du å se potensielle besparelser for?', 1, 10, 2)


# Beregner besparelsen
savings = calculate_savings(X, Y, Z, W)

if st.button("Beregn på nytt"):
    st.experimental_rerun()

# Resultat:
st.write(f"🔍 **Ditt potensiale:**")

if savings > 0:
    st.write(f"Tenk deg å kunne frigjøre opptil:")
    st.write(f" NOK {savings:,.2f} over {Z} år! 💸")
    st.write(f"Dette er verdifulle ressurser som kan reinvesteres i andre produktive områder av virksomheten din.")
    st.write(" **La WS vise vei!** 🚀")
    st.write("Vi i WS er spesialister på å digitalisere manuelle oppgaver. Gi dine ansatte gaven av tid, og la oss hjelpe dere med å maksimere effektiviteten. Kontakt oss, og vi tar steget sammen - post@webstep.no")
else:
    st.write("Selv mindre effektivitetsøkninger kan akkumuleres til betydelige besparelser over tid. La WS være din guide på veien mot digitalisering.")



