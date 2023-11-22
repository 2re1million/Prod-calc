import streamlit as st
import random



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

st.title('Digitaliseringskalkulatoren: 🔍 ')

st.info("🕰️ Utdaterte datasystemer er frustrerende, stjeler tid og bremser produktivitet. I en tid der teknologi burde være vår styrke, hvorfor holder vi fortsatt fast på med oppgaver som kan automatiseres? ")
st.write("Utforsk kalkulatoren under og se potensialet for sparing i kroner og øre. Utforsk hvordan digitalisering kan kutte kostnader ved å eliminere dobbelplotting pga systemer ikke kommuniserer, eller erstatte systemer bedriften din har vokst i fra for lengst") 

# Opprett to kolonner 
col1, col2 = st.columns(2)

with col1:
    # Inputs fra bruker
    X = st.slider('Ca hvor mange **minutter** hver dag går tapt på grunn av trege og ineffektive datasystemer?(pr. ansatt)', 0, 120, 30, step=5)
    Y = st.number_input('Antall **ansatte** som påvirkes av disse systembegrensningene?', step=1)
    W = int(st.number_input('Ca. gjennomsnittlig **årlig lønn** for disse ansatte:', value=700000, step=10000)) 
    Z = st.slider('Hvor mange **år** ønsker du å se potensielle besparelser for?', 1, 10, 3)

    # Kalkulere total kostnad for en ansatt
    total_kostnad_per_ansatt = totale_kostnader_for_bedriften(W)

    # Bruke den totale kostnaden for en ansatt i stedet for bare årslønnen
    savings = calculate_savings(X, Y, Z, total_kostnad_per_ansatt)
    savings_int = int(savings)
    
with col2:
    
    variant = random.choice(['A', 'B'])
    # Resultat:
    st.write(f"🔍 **Ditt potensiale:**")

    savings_int = int(savings)
    
    if savings > 0:
        st.write(f" Besparelse: NOK **{savings_int:,}** over **{Z}** år!💸")
        st.write(" ")
        st.write(f"Dette er verdifulle ressurser som kan reinvesteres i andre produktive områder av virksomheten din.")
        st.write("**Tenk også på den utilsiktede gevinsten av:**")
        st.write("* Mer motiverte ansatte som nå kan fokusere på mer spennende arbeidsoppgaver")
        st.write("* Nye nyttige funksjoner som følger med et skreddersydd system")
        
        if variant == 'A':
            st.write("Interessant?")
            st.link_button("DM meg!💡", "https://www.linkedin.com/in/thore-tollevik-434621b5/")
        elif variant == 'B':
            st.write("Interessant?")
            st.link_button("Mail meg!💡", "thore.tollevik@webstep.no")
    else:
        st.write("Selv mindre effektivitetsøkninger kan akkumuleres til betydelige besparelser over tid. Prosjekter kan med det betale seg ned av seg selv over tid")

st.write("Disclaimer: Selvsagt vil det være hundre ting som spiller inn på besparelse, men dette gir en ball-park") :)
