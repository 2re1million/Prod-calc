import streamlit as st

def calculate_savings(minutes_saved, num_employees, num_years, avg_salary):
    # Konverterer minutter til timer
    hours_saved_per_day = minutes_saved / 60
    # Antall arbeidsdager i et år (vanligvis ca. 250)
    work_days_per_year = 250
    # Total antall timer spart per år
    total_hours_saved = hours_saved_per_day * work_days_per_year * num_employees
    # Konverter lønn fra årlig til timebasis
    avg_hourly_salary = avg_salary / (work_days_per_year * 8)
    # Total besparelse
    total_savings = total_hours_saved * avg_hourly_salary * num_years
    return total_savings

st.title('Kalkulator for besparelse ved digitalisering')

# Inputs fra bruker
X = st.slider('Minutter spart per dag:', 0, 300, 30)
Y = st.slider('Antall ansatte:', 1, 500, 10)
Z = st.slider('Antall år:', 1, 30, 5)
W = st.slider('Gjennomsnittlig årlig lønn (i NOK):', 300000, 3000000, 600000)

# Beregner besparelsen
savings = calculate_savings(X, Y, Z, W)

# Viser resultatet
st.write(f'Total besparelse over {Z} år: NOK {savings:,.2f}')

if st.button("Beregn på nytt"):
    st.experimental_rerun()

