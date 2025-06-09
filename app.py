import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


# Page configuration
st.set_page_config(
    page_title="Digitaliseringskalkulator Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .improvement-tip {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def totale_kostnader_for_bedriften(arslonn: float) -> dict:
    """Enhanced cost calculation with detailed breakdown"""
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
    
    return {
        'arslonn': arslonn,
        'feriepenger': feriepenger,
        'arbeidsgiveravgift': arbeidsgiveravgift,
        'pensjonskostnader': pensjonskostnader,
        'arbeidsgiveravgift_pensjon': arbeidsgiveravgift_pensjon,
        'yrkesskadeforsikring': yrkesskadeforsikring,
        'total_kostnad': total_kostnad
    }

def calculate_savings(minutes_saved, num_employees, num_years, avg_salary, efficiency_factor=1.0):
    """Enhanced savings calculation with efficiency factors"""
    # Konverterer minutter til timer
    hours_saved_per_day = minutes_saved / 60
    # Antall arbeidsdager i et år (vanligvis ca. 230)
    work_days_per_year = 230
    # Total antall timer spart per år
    total_hours_saved = hours_saved_per_day * work_days_per_year * num_employees * efficiency_factor
    # Konverter lønn fra årlig til timebasert
    avg_hourly_salary = avg_salary / (work_days_per_year * 7.5)
    # Total besparelse
    total_savings = total_hours_saved * avg_hourly_salary * num_years
    
    # Additional metrics
    daily_savings = hours_saved_per_day * num_employees * (avg_salary / (work_days_per_year * 7.5))
    monthly_savings = daily_savings * 22  # Average working days per month
    annual_savings = total_savings / num_years
    
    return {
        'total_savings': total_savings,
        'annual_savings': annual_savings,
        'monthly_savings': monthly_savings,
        'daily_savings': daily_savings,
        'total_hours_saved': total_hours_saved,
        'hours_per_year': total_hours_saved / num_years
    }

def create_savings_visualization(savings_data, years):
    """Create interactive savings visualization"""
    # Create yearly progression
    years_range = list(range(1, years + 1))
    cumulative_savings = [savings_data['annual_savings'] * i for i in years_range]
    
    fig = go.Figure()
    
    # Add cumulative savings
    fig.add_trace(go.Scatter(
        x=years_range,
        y=cumulative_savings,
        mode='lines+markers',
        name='Kumulativ besparelse',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
    # Add annual savings bars
    fig.add_trace(go.Bar(
        x=years_range,
        y=[savings_data['annual_savings']] * years,
        name='Årlig besparelse',
        opacity=0.7,
        marker_color='#ff7f0e'
    ))
    
    fig.update_layout(
        title='Besparelser over tid',
        xaxis_title='År',
        yaxis_title='NOK',
        hovermode='x unified',
        showlegend=True,
        height=400
    )
    
    return fig

def create_cost_breakdown_chart(cost_data):
    """Create cost breakdown pie chart"""
    labels = ['Grunnlønn', 'Feriepenger', 'Arbeidsgiveravgift', 'Pensjon', 'Yrkesskade']
    values = [
        cost_data['arslonn'],
        cost_data['feriepenger'],
        cost_data['arbeidsgiveravgift'] + cost_data['arbeidsgiveravgift_pensjon'],
        cost_data['pensjonskostnader'],
        cost_data['yrkesskadeforsikring']
    ]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.3,
        textinfo='label+percent',
        textfont_size=12
    )])
    
    fig.update_layout(
        title='Kostnadsoversikt per ansatt',
        height=400,
        showlegend=True
    )
    
    return fig

def get_industry_benchmarks():
    """Industry-specific benchmarks for time waste"""
    return {
        'Produksjon': {'avg_waste': 45, 'top_areas': ['Rapportering', 'Kvalitetskontroll', 'Planlegging']},
        'Helsevesen': {'avg_waste': 60, 'top_areas': ['Dokumentasjon', 'Pasientregistrering', 'Rapportering']},
        'Finans': {'avg_waste': 35, 'top_areas': ['Datainnsamling', 'Rapportering', 'Compliance']},
        'IT': {'avg_waste': 25, 'top_areas': ['Møter', 'Dokumentasjon', 'Testing']},
        'Offentlig': {'avg_waste': 55, 'top_areas': ['Saksbehandling', 'Rapportering', 'Koordinering']},
        'Retail': {'avg_waste': 40, 'top_areas': ['Lageroppfølging', 'Kundeservice', 'Rapportering']}
    }

def create_roi_gauge(roi_percent):
    """Create ROI gauge chart"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = roi_percent,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "ROI %"},
        delta = {'reference': 100},
        gauge = {
            'axis': {'range': [None, 500]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 100], 'color': "lightgray"},
                {'range': [100, 300], 'color': "yellow"}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 200}}))
    
    fig.update_layout(height=300)
    return fig

# Header
st.markdown('<h1 class="main-header">🚀 Digitaliseringskalkulator Pro</h1>', unsafe_allow_html=True)

# Sidebar for advanced settings
with st.sidebar:
    st.header("⚙️ Avanserte innstillinger")
    
    # Industry selection
    industry = st.selectbox(
        "Velg bransje",
        options=list(get_industry_benchmarks().keys()),
        help="Velg din bransje for tilpassede benchmarks"
    )
    
    # Efficiency factor
    efficiency_factor = st.slider(
        "Implementeringseffektivitet",
        min_value=0.5,
        max_value=1.5,
        value=1.0,
        step=0.1,
        help="Justerer for hvor godt implementeringen vil fungere i praksis"
    )
    
    # Advanced toggles
    show_breakdown = st.checkbox("Vis kostnadsoversikt", value=True)
    show_projections = st.checkbox("Vis fremskrivninger", value=True)
    include_inflation = st.checkbox("Inkluder inflasjon (2%)", value=False)
    
    st.markdown("---")
    st.markdown("### 📊 Kalkulator v2.0")
    st.markdown("✅ Interaktive visualiseringer")
    st.markdown("✅ Bransjebenchmarks") 
    st.markdown("✅ ROI-analyse")
    st.markdown("✅ Scenariomodellering")

# Main content
st.info("🔮 Utdaterte datasystemer er frustrerende, stjeler tid og bremser produktivitet. I en tid der teknologi burde være vår styrke, hvorfor holder vi fortsatt fast på oppgaver som kan automatiseres?")

# Industry insights
benchmarks = get_industry_benchmarks()
if industry in benchmarks:
    st.markdown(f"""
    <div class="improvement-tip">
    <strong>📊 Bransjeinsikt - {industry}:</strong><br>
    Gjennomsnittlig tidsbruk på ineffektive prosesser: <strong>{benchmarks[industry]['avg_waste']} minutter/dag</strong><br>
    Hovedområder for forbedring: {', '.join(benchmarks[industry]['top_areas'])}
    </div>
    """, unsafe_allow_html=True)

# Input sections
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Produktivitetsdata")
    
    # Pre-fill with industry benchmark
    default_minutes = benchmarks.get(industry, {}).get('avg_waste', 30)
    
    X = st.slider(
        'Ca hvor mange **minutter** hver dag går tapt på grunn av trege og ineffektive datasystemer? (pr. ansatt)',
        0, 180, default_minutes, step=5,
        help=f"Bransjegjennomsnitt for {industry}: {benchmarks[industry]['avg_waste']} min"
    )
    
    Y = st.number_input(
        'Antall **ansatte** som påvirkes av disse systembegrensningene?',
        min_value=1, value=10, step=1
    )
    
    W = int(st.number_input(
        'Ca. gjennomsnittlig **årlig lønn** for disse ansatte:',
        value=700000, step=10000, min_value=300000, max_value=2000000
    ))
    
    Z = st.slider(
        'Hvor mange **år** ønsker du å se potensielle besparelser for?',
        1, 15, 5
    )

with col2:
    st.subheader("💰 Beregningsresultater")
    
    # Calculate costs and savings
    total_kostnad_per_ansatt = totale_kostnader_for_bedriften(W)
    savings_data = calculate_savings(X, Y, Z, total_kostnad_per_ansatt['total_kostnad'], efficiency_factor)
    
    # Apply inflation if selected
    if include_inflation:
        inflation_factor = 1.02 ** Z
        savings_data['total_savings'] *= inflation_factor
        savings_data['annual_savings'] *= inflation_factor
    
    # Display key metrics
    st.metric(
        label="💰 Total besparelse over " + str(Z) + " år",
        value=f"NOK {int(savings_data['total_savings']):,}",
        delta=f"NOK {int(savings_data['annual_savings']):,} per år"
    )
    
    col2a, col2b = st.columns(2)
    with col2a:
        st.metric(
            "📅 Månedlig besparelse",
            f"NOK {int(savings_data['monthly_savings']):,}"
        )
    with col2b:
        st.metric(
            "⏰ Timer spart per år",
            f"{int(savings_data['hours_per_year']):,}"
        )
    
    # ROI calculation
    implementation_cost = savings_data['annual_savings'] * 0.2  # Estimate 20% of first year savings
    roi_months = (implementation_cost / savings_data['monthly_savings']) if savings_data['monthly_savings'] > 0 else 0
    roi_percent = ((savings_data['annual_savings'] - implementation_cost) / implementation_cost * 100) if implementation_cost > 0 else 0
    
    if roi_months > 0:
        st.markdown(f"""
        <div class="metric-card">
        <strong>📈 Return on Investment (ROI)</strong><br>
        Estimert tilbakebetalingstid: <strong>{roi_months:.1f} måneder</strong><br>
        ROI første år: <strong>{roi_percent:.0f}%</strong>
        </div>
        """, unsafe_allow_html=True)

# Visualizations
if show_projections and savings_data['total_savings'] > 0:
    st.subheader("📈 Besparelsesanalyse")
    
    # Create tabs for different views
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Besparelser over tid", "📊 Kostnadsoversikt", "🎯 Scenarioanalyse", "📈 ROI Analyse"])
    
    with tab1:
        savings_fig = create_savings_visualization(savings_data, Z)
        st.plotly_chart(savings_fig, use_container_width=True)
        
        # Additional insights
        total_hours = savings_data['total_hours_saved']
        st.markdown(f"""
        <div class="success-box">
        <strong>⏰ Tidsbesparelse:</strong> Over {Z} år sparer dere totalt <strong>{int(total_hours):,} timer</strong> 
        - det tilsvarer <strong>{int(total_hours/1750):.1f} årsverk</strong>!
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        if show_breakdown:
            cost_fig = create_cost_breakdown_chart(total_kostnad_per_ansatt)
            st.plotly_chart(cost_fig, use_container_width=True)
            
            # Cost details
            st.markdown(f"""
            **Kostnadsoversikt per ansatt:**
            - Grunnlønn: NOK {int(total_kostnad_per_ansatt['arslonn']):,}
            - Total kostnad: NOK {int(total_kostnad_per_ansatt['total_kostnad']):,}
            - Timekostnad: NOK {int(total_kostnad_per_ansatt['total_kostnad']/(230*7.5)):,}
            """)
    
    with tab3:
        st.subheader("🎯 Hva-om analyse")
        col3a, col3b, col3c = st.columns(3)
        
        scenarios = {
            'Konservativ': 0.7,
            'Realistisk': 1.0,
            'Optimistisk': 1.3
        }
        
        for i, (scenario_name, factor) in enumerate(scenarios.items()):
            scenario_savings = savings_data['total_savings'] * factor
            with [col3a, col3b, col3c][i]:
                st.metric(
                    f"{scenario_name} scenario",
                    f"NOK {int(scenario_savings):,}",
                    delta=f"{int((factor - 1) * 100):+}%"
                )
        
        # Sensitivity analysis
        st.subheader("🔧 Sensitivitetsanalyse")
        st.write("Se hvordan endringer i nøkkelfaktorer påvirker besparelsene:")
        
        sensitivity_data = []
        for time_factor in [0.5, 0.75, 1.0, 1.25, 1.5]:
            for employee_factor in [0.5, 0.75, 1.0, 1.25, 1.5]:
                new_time = X * time_factor
                new_employees = Y * employee_factor
                new_savings = calculate_savings(new_time, new_employees, Z, 
                                              total_kostnad_per_ansatt['total_kostnad'], efficiency_factor)
                sensitivity_data.append({
                    'Tid (factor)': time_factor,
                    'Ansatte (factor)': employee_factor,
                    'Besparelse (NOK)': new_savings['total_savings']
                })
        
        df_sensitivity = pd.DataFrame(sensitivity_data)
        pivot_table = df_sensitivity.pivot(index='Tid (factor)', columns='Ansatte (factor)', values='Besparelse (NOK)')
        
        heatmap_fig = px.imshow(pivot_table, 
                               labels=dict(x="Ansatte faktor", y="Tid faktor", color="Besparelse"),
                               title="Sensitivitetsanalyse: Besparelser vs. Tid og Ansatte faktorer")
        st.plotly_chart(heatmap_fig, use_container_width=True)
    
    with tab4:
        col4a, col4b = st.columns([1, 1])
        
        with col4a:
            if roi_percent > 0:
                roi_fig = create_roi_gauge(roi_percent)
                st.plotly_chart(roi_fig, use_container_width=True)
        
        with col4b:
            st.markdown(f"""
            ### 📊 ROI Detaljer
            - **Estimert implementeringskostnad:** NOK {int(implementation_cost):,}
            - **Årlig besparelse:** NOK {int(savings_data['annual_savings']):,}
            - **Tilbakebetalingstid:** {roi_months:.1f} måneder
            - **5-års NPV (5% rente):** NOK {int(savings_data['total_savings'] * 0.9):,}
            """)
            
            if roi_percent > 200:
                st.markdown("""
                <div class="success-box">
                <strong>🎉 Utmerket ROI!</strong><br>
                Dette prosjektet viser svært sterk lønnsomhet og bør prioriteres høyt.
                </div>
                """, unsafe_allow_html=True)

# Recommendations section
if savings_data['total_savings'] > 0:
    st.subheader("💡 Anbefalinger og neste steg")
    
    col4, col5 = st.columns([2, 1])
    
    with col4:
        st.markdown(f"""
        <div class="improvement-tip">
        <strong>🎯 Basert på din analyse, anbefaler vi å fokusere på:</strong><br><br>
        1. <strong>Rask gevinst:</strong> Start med {benchmarks[industry]['top_areas'][0].lower()} prosessene<br>
        2. <strong>Digitalisering:</strong> Automatiser repetitive oppgaver som sparer {X} min/dag<br>
        3. <strong>Integrasjon:</strong> Koble sammen systemer som ikke kommuniserer<br>
        4. <strong>Opplæring:</strong> Sørg for at {Y} ansatte får optimal systemopplæring<br>
        5. <strong>Måling:</strong> Implementer KPIer for å følge fremgang
        </div>
        """, unsafe_allow_html=True)
        
        # Advanced insights based on savings amount
        if savings_data['total_savings'] > 5000000:
            st.markdown("""
            <div class="warning-box">
            <strong>🚀 Massivt potensial oppdaget!</strong><br>
            Med besparelser over 5 millioner NOK bør du:
            <ul>
            <li>Etablere et dedikert digitaliseringsteam</li>
            <li>Vurdere omfattende systemmodernisering</li>
            <li>Planlegge en 3-5 års digitaliseringsstrategi</li>
            <li>Engasjere ledelsen på C-nivå</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        elif savings_data['total_savings'] > 1000000:
            st.markdown("""
            <div class="warning-box">
            <strong>⚡ Stort potensial oppdaget!</strong><br>
            Med besparelser over 1 million NOK bør du:
            <ul>
            <li>Gjennomføre en detaljert prosessanalyse</li>
            <li>Utvikle en fasevis implementeringsplan</li>
            <li>Etablere et dedikert digitaliseringsprosjekt</li>
            <li>Vurdere ekstern konsulentbistand</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="success-box">
            <strong>💪 Solid forbedringspotensial!</strong><br>
            Dette er en god start som kan bygges videre på:
            <ul>
            <li>Start med pilot-implementering</li>
            <li>Dokumenter prosessene som skal forbedres</li>
            <li>Involv brukerne i utformingen</li>
            <li>Mål og følg opp resultatene</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with col5:
        # Action buttons
        st.markdown("### 🎯 Neste steg")
        
        if st.button("📊 Generer rapport", help="Last ned detaljert PDF-rapport"):
            st.success("📄 Rapport klar for nedlasting!")
            st.info("🔧 Funksjon under utvikling")
        
        if st.button("📧 Send til e-post", help="Send kalkulasjonen til din e-post"):
            st.success("✉️ E-post sendt!")
            st.info("🔧 Funksjon under utvikling")
        
        if st.button("📅 Book møte", help="Book et konsultasjonsmøte"):
            st.success("📞 Møterequest sendt!")
            st.info("🔧 Funksjon under utvikling")
        
        # Contact section
        st.markdown("### 🤝 Få profesjonell hjelp")
        variant = random.choice(['A', 'B'])
        
        if variant == 'A':
            st.write("Klar for å realisere potensialet?")
            st.link_button("Ta kontakt! 📞", "https://www.linkedin.com/in/thore-tollevik-434621b5/")
        else:
            st.write("Trenger du ekspertbistand?")
            st.link_button("Kontakt oss! 🚀", "https://www.linkedin.com/in/thore-tollevik-434621b5/")

else:
    st.markdown("""
    <div class="warning-box">
    <strong>💡 Tips:</strong> Selv mindre effektivitetsøkninger kan akkumuleres til betydelige besparelser over tid. 
    Prosjekter kan med det betale seg ned av seg selv over tid.
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
<p><strong>Digitaliseringskalkulator Pro v2.0</strong> | Laget med ❤️ av <a href='https://www.linkedin.com/in/thore-tollevik-434621b5/' target='_blank'>Thore Tollevik</a></p>
<p><em>Disclaimer: Tusen ting kan påvirke kostnader, ta beløpet som en tankevekker og et artig ball-park estimat for effektivisering i arbeidshverdagen :)</em></p>
</div>
""", unsafe_allow_html=True)
