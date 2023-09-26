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

st.title('Innsparingskalkulator - Kostnaden av manuelt, repetativt arbeid!')

# Ingress
st.write("""
# Digitalisering av manuelt arbeid
I dagens teknologiske verden kan nærmest all repetitivt manuelt arbeid digitaliseres bort på en eller annen måte. Spesielt dobbeltplotting er en "versting" det er enkelt å gjøre noe med, ved å få systemer til å prate sammen.
""")
st.write("Bruk kalkulatoren under for å se hvor mye du taper / kan spare ved å digitalisere enkelte arbeidsprosesser.")


# Inputs fra bruker
X = st.slider('Minutter på manuelt repetativt -  per dag:', 0, 120, 20)
Y = int(st.text_input('Antall ansatte som gjør disse oppgavene:', 10))
Z = st.slider('Antall år for potensiell besparelse:', 1, 10, 2)
W = int(st.text_input('Gjennomsnittlig årlig lønn (i NOK):', 664680))

# Beregner besparelsen
savings = calculate_savings(X, Y, Z, W)

# Resultat:
st.write(f"🔍 **Analyseresultat:**")

if savings > 0:
    st.write(f"Ved å digitalisere bort manuelt arbeid, kan di bedrift potensielt spare:")
    st.write(f"NOK {savings:,.2f} over {Z} år!")
    st.write(f"Dette er ressurser som kan omdirigeres til andre nyttige arbeidsoppgaver i organisasjonen din!")
    st.write("🚀 **WS er her for deg!**")
    st.write("Digitalisere bort manuelt arbeid er vi eksperter på i WS. La oss hjelpe dere med å få mer ut av arbeidsdagen. Ta kontakt, så setter vi i gang -  post@webstep.no")
else:
    st.write("Selv små forbedringer i effektivitet kan føre til store besparelser over tid. WS kan hjelpe deg med å identifisere og utnytte disse mulighetene. Start din digitaliseringsreise med oss!")

if st.button("Beregn på nytt"):
    st.experimental_rerun()

