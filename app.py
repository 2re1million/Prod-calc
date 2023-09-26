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

st.title('Kalkulator for besparelse ved digitalisering')

# Inputs fra bruker
X = st.slider('Minutter spart per dag:', 0, 120, 20)
Y = st.slider('Antall ansatte:', 1, 300, 5)
Z = st.slider('Antall år:', 1, 10, 2)
W = st.slider('Gjennomsnittlig årlig lønn (i NOK):', 300000, 1500000, 664680)

# Beregner besparelsen
savings = calculate_savings(X, Y, Z, W)

# Budskapet for markedsføring
st.write(f"🔍 **Analyseresultat:**")

if savings > 0:
    st.write(f"Ved å starte din digitaliseringsreise, kan din bedrift potensielt spare NOK {savings:,.2f} over {Z} år. Dette er ressurser som kan omdirigeres til andre nyttige arbeidsoppgaver, noe som kan gi stor verdi for organisasjonen din.")
    st.write("🚀 **WS er her for deg!**")
    st.write("WS er din pålitelige partner på denne reisen. Vi er eksperter på å digitalisere bort manuelt arbeid som krever unødig med tid. La oss hjelpe deg å omdanne disse besparelsene til reell vekst for din bedrift!")
else:
    st.write("Selv små forbedringer i effektivitet kan føre til store besparelser over tid. WS kan hjelpe deg med å identifisere og utnytte disse mulighetene. Start din digitaliseringsreise med oss!")

if st.button("Beregn på nytt"):
    st.experimental_rerun()

