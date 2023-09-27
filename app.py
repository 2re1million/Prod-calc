import streamlit as st

def totale_kostnader_for_bedriften(arslonn: float) -> float:
    # Feriepenger
    feriepenger = arslonn * 0.12

    # Arbeidsgiveravgift
    ekstra_avgift = 0
    if arslonn > 750000:
        ekstra_avgift = (arslonn - 750000) * 0.05
    arbeidsgiveravgift = (arslonn + feriepenger) * 0.141 + ekstra_avgift

    # Pensjonskostnader
    pensjonskostnader = max(0, arslonn - 500000) * 0.02

    # Arbeidsgiveravgift av pensjonskostnader
    arbeidsgiveravgift_pensjon = pensjonskostnader * 0.141

    # Yrkesskadeforsikring
    yrkesskadeforsikring = 3000

    # Total kostnad
    total_kostnad = (arslonn + feriepenger + arbeidsgiveravgift + pensjonskostnader 
                     + arbeidsgiveravgift_pensjon + yrkesskadeforsikring)

    return total_kostnad

def calculate_savings(hours_saved_per_week, num_employees, num_years, avg_salary):
    # Antall arbeidsuker i et år (vanligvis ca. 50)
    work_weeks_per_year = 50
    # Total antall timer spart per år
    total_hours_saved = hours_saved_per_week * work_weeks_per_year * num_employees
    # Konverter lønn fra årlig til timebasis
    avg_hourly_salary = avg_salary / (work_weeks_per_year * 7.5 * 5)  # assuming 7.5 hours/day and 5 days/week
    # Total besparelse
    total_savings = total_hours_saved * avg_hourly_salary * num_years
    return total_savings


st.markdown('## Din innsparingskalkulator: ')
st.markdown('### Hva koster manuelt arbeid bedriften virkelig?')

# Ingress
st.write("""
I en verden dominert av teknologi, hvorfor skal vi fortsatt utføre repetitive oppgaver manuelt? Føre inn samme data i to forskjellige system, er for eksempel en notorisk tidstyv. 
Heldigvis kan dette gjøres noe med! Med riktig teknologi kan manuelt arbeid digitaliseres bort!
""")
st.write("Bruk kalkulatoren under og avslør hvor mye du faktisk kan spare ved å digitalisere disse gjentagende arbeidsoppgavene")

# Inputs fra bruker
X = st.slider('**Timer** per uke en ansatt bruker på repetitiv oppgaveer?', 0.0, 25.0, 4.0, step=0.5)
Y = st.number_input('**Antall ansatte** som jevnlig utfører disse oppgaven hver uke?', 5)
W = st.number_input('**Gjennomsnittlig årlig lønn** for disse ansatte (i NOK):', value=700000.0, format='%f')
Z = st.slider('Hvor mange år ønsker du å se potensielle besparelser for?', 1, 10, 2)

# Kalkulere total kostnad for en ansatt
total_kostnad_per_ansatt = totale_kostnader_for_bedriften(W)

# Bruke den totale kostnaden for en ansatt i stedet for bare årslønnen
savings = calculate_savings(X, Y, Z, total_kostnad_per_ansatt)

if st.button("Beregn på nytt"):
    st.experimental_rerun()

# Resultat:
st.write(f"🔍 **Ditt potensiale:**")

if savings > 0:
    st.write(f"Tenk deg å kunne frigjøre opptil:")
    st.write(f" NOK {savings:,.2f} over {Z} år! 💸")
    st.write(f"Dette er verdifulle ressurser som kan reinvesteres i andre produktive områder av virksomheten din.")
    #st.write(" **La WS vise vei!** 🚀")
    st.write("Vi i WS er spesialister på å digitalisere manuelle oppgaver. Gi dine ansatte gaven av tid, og la oss hjelpe dere med å maksimere effektiviteten. Kontakt oss, og vi tar steget sammen - post@webstep.no")
else:
    st.write("Selv mindre effektivitetsøkninger kan akkumuleres til betydelige besparelser over tid. La WS være din guide på veien mot digitalisering.")

    st.write("* - Regnestykket inkl arb.avgift og andre sosiale kostnaderfor arb.giver.")
