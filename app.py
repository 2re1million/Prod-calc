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

# Set title and intro message
st.title('Exponential Savings 🤑')

st.info("💡 Exponential growth is called the eight wonder of the world. It is a rapid increase in a quantity over time, characterized by a rate that is proportional to the current value of the quantity.")

st.markdown('## Din innsparingskalkulator: ')
st.markdown('### Hva koster manuelt arbeid bedriften virkelig?')
# Ingress
st.write("""
I en verden dominert av teknologi, hvorfor skal vi fortsatt utføre repetitive oppgaver manuelt? Føre inn samme data i to forskjellige system, er for eksempel en notorisk tidstyv. 
Heldigvis kan dette gjøres noe med! Med riktig teknologi kan manuelt arbeid digitaliseres bort!
""")
st.write("Bruk kalkulatoren under og avslør hvor mye du faktisk kan spare ved å digitalisere disse gjentagende arbeidsoppgavene")

st.info("💡 Exponential growth is called the eight wonder of the world. It is a rapid increase in a quantity over time, characterized by a rate that is proportional to the current value of the quantity.")


# Opprett to kolonner
col1, col2 = st.columns(2)

with col1:
    # Inputs fra bruker
    X = st.slider('Hvor mange **minutter** bruker en ansatt på repetitive manuelle oppgaver hver dag?', 0, 120, 30, step=5)
    Y = st.number_input('**Antall ansatte** som jevnlig utfører disse oppgavene?')
    W = st.number_input('Gjennomsnittlig **årlig lønn** for disse ansatte (i NOK):', value=700000.0, format='%f')
    Z = st.slider('Hvor mange **år** ønsker du å se potensielle besparelser for?', 1, 10, 3)

    # Kalkulere total kostnad for en ansatt
    total_kostnad_per_ansatt = totale_kostnader_for_bedriften(W)

    # Bruke den totale kostnaden for en ansatt i stedet for bare årslønnen
    savings = calculate_savings(X, Y, Z, total_kostnad_per_ansatt)

    if st.button("Beregn på nytt"):
        st.experimental_rerun()

with col2:


    # Resultat:
    st.write(f"🔍 **Ditt potensiale:**")

    savings_int = int(savings)

    if savings > 0:
        st.write(f" Besparelse: NOK {savings_int:,} over {Z} år!💸")
        st.write(f"Dette er verdifulle ressurser som kan reinvesteres i andre produktive områder av virksomheten din.")
        
        st.write("Hjelp til å komme i gang? 👉 post@webstep.no")
    else:
        st.write("Selv mindre effektivitetsøkninger kan akkumuleres til betydelige besparelser over tid. La WS være din guide på veien mot digitalisering.")
