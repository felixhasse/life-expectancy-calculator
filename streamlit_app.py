import streamlit as st
import pandas as pd
from life_expectancy_predictor import predict_life_expectancy, get_available_countries, get_continents

# Page configuration
st.set_page_config(
    page_title="Life Expectancy Calculator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-result {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        padding: 1rem;
        background-color: #f0f8ff;
        border-radius: 10px;
        border: 2px solid #1f77b4;
        margin: 1rem 0;
    }
    .explanation-box {
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .lifestyle-impact {
        background-color: #fff3cd;
        padding: 0.75rem;
        border-radius: 5px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🌍 Life Expectancy Calculator</h1>', unsafe_allow_html=True)

st.markdown("""
This calculator predicts life expectancy based on demographic information and lifestyle factors. 
The predictions are based on machine learning models trained on historical data from various countries and continents.
""")

# Get available data
countries_data = get_available_countries()
continents = get_continents()

# Sidebar for inputs
st.sidebar.header("📋 Input Parameters")

# Demographics section
st.sidebar.subheader("👤 Demographics")

# Continent selection
continent = st.sidebar.selectbox(
    "Select Continent:",
    options=continents,
    help="Choose the continent for the prediction"
)

# Country selection based on continent
available_countries = countries_data.get(continent, [])
country = st.sidebar.selectbox(
    "Select Country:",
    options=available_countries,
    help="Choose a specific country (if not listed, continent-level data will be used)"
)

# Sex selection
sex = st.sidebar.selectbox(
    "Select Sex:",
    options=["Male", "Female"],
    help="Choose the biological sex for the prediction"
)

# Year selection
year = st.sidebar.number_input(
    "Prediction Year:",
    min_value=1950,
    max_value=2100,
    value=2024,
    help="Year for which to predict life expectancy"
)

# Lifestyle factors section
st.sidebar.subheader("🏃‍♀️ Lifestyle Factors")

# Physical activity
physical_activity = st.sidebar.slider(
    "Physical Activity (hours/week):",
    min_value=0.0,
    max_value=7.0,
    value=2.0,
    step=0.5,
    help="Hours of physical activity per week (0-7 hours)"
)

# Fast food consumption
fast_food = st.sidebar.slider(
    "Fast Food Meals (per week):",
    min_value=0,
    max_value=14,
    value=2,
    help="Number of fast food meals consumed per week"
)

# Alcohol consumption
alcohol = st.sidebar.slider(
    "Alcoholic Drinks (per week):",
    min_value=0,
    max_value=20,
    value=0,
    help="Number of alcoholic drinks consumed per week"
)

# Smoking status
smoke = st.sidebar.selectbox(
    "Smoking Status:",
    options=["never", "former", "current"],
    help="Current smoking status"
)

# Smoking quit age (only if former smoker)
smoke_quit_age = 25
if smoke == "former":
    smoke_quit_age = st.sidebar.slider(
        "Age When Quit Smoking:",
        min_value=15,
        max_value=80,
        value=25,
        help="Age at which you quit smoking"
    )

# Health factors section
st.sidebar.subheader("🏥 Health Factors")

# Family history
family_history = st.sidebar.selectbox(
    "Family History of Chronic Diseases:",
    options=[0, 1, 2],
    format_func=lambda x: {0: "None", 1: "Some family history", 2: "Strong family history"}[x],
    help="Family history of heart disease, diabetes, cancer, etc."
)

# BMI input
bmi_input = st.sidebar.checkbox("Include BMI in calculation", value=False)
bmi = None
if bmi_input:
    # BMI calculator option
    bmi_method = st.sidebar.radio(
        "BMI Input Method:",
        options=["Direct BMI", "Height & Weight"],
        help="Choose how to input your BMI"
    )
    
    if bmi_method == "Direct BMI":
        bmi = st.sidebar.number_input(
            "BMI (Body Mass Index):",
            min_value=10.0,
            max_value=50.0,
            value=22.0,
            step=0.1,
            help="BMI = weight(kg) / height(m)²"
        )
    else:
        col_h, col_w = st.sidebar.columns(2)
        with col_h:
            height = st.number_input(
                "Height (cm):",
                min_value=100,
                max_value=250,
                value=170,
                help="Your height in centimeters"
            )
        with col_w:
            weight = st.number_input(
                "Weight (kg):",
                min_value=30,
                max_value=200,
                value=70,
                help="Your weight in kilograms"
            )
        
        if height > 0:
            bmi = weight / ((height / 100) ** 2)
            st.sidebar.write(f"Calculated BMI: {bmi:.1f}")

# Stress level
stress_input = st.sidebar.checkbox("Include stress level", value=False)
stress_level = None
if stress_input:
    stress_level = st.sidebar.slider(
        "Stress Level (0-10):",
        min_value=0,
        max_value=10,
        value=3,
        help="Average stress level: 0=very low, 10=extremely high"
    )

# Driving risk
driving_risk = st.sidebar.selectbox(
    "Driving Risk Level:",
    options=[0, 1, 2],
    format_func=lambda x: {0: "Safe driver", 1: "Moderate risk", 2: "High risk driver"}[x],
    help="Driving habits and risk factors (speeding, aggressive driving, etc.)"
)

# Doctor visits
doctor_visits = st.sidebar.selectbox(
    "Regular Doctor Visits:",
    options=[0, 1, 2],
    format_func=lambda x: {0: "Rarely/Never", 1: "Occasional checkups", 2: "Regular checkups"}[x],
    help="Frequency of preventive healthcare visits"
)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔮 Prediction Results")
    
    # Make prediction button
    if st.button("Calculate Life Expectancy", type="primary", use_container_width=True):
        try:
            # Make the prediction
            predicted_age = predict_life_expectancy(
                country=country,
                continent=continent.lower(),
                sex=sex.lower(),
                year=year,
                physical_activity=physical_activity,
                fast_food=fast_food,
                alcohol=alcohol,
                smoke=smoke,
                smoke_quit_age=smoke_quit_age,
                family_history=family_history,
                bmi=bmi,
                stress_level=stress_level,
                driving_risk=driving_risk,
                doctor_visits=doctor_visits
            )
            
            # Display the result
            st.markdown(f"""
            <div class="prediction-result">
                🎯 Predicted Life Expectancy: {predicted_age} years
            </div>
            """, unsafe_allow_html=True)
            
            # Show breakdown of factors
            st.subheader("📊 Factors Impact Analysis")
            
            # Get baseline prediction (without lifestyle factors)
            baseline = predict_life_expectancy(
                country=country,
                continent=continent.lower(),
                sex=sex.lower(),
                year=year,
                physical_activity=0,
                fast_food=0,
                alcohol=0,
                smoke="never",
                smoke_quit_age=25,
                family_history=0,
                bmi=None,
                stress_level=None,
                driving_risk=0,
                doctor_visits=0
            )
            
            # Calculate individual impacts
            pa_impact = min(physical_activity, 7) * (6.9/7)
            ff_impact = -(baseline * (min(fast_food, 14) / 14) * 0.15)
            
            alcohol_impact = 0
            if alcohol > 0 and alcohol < 3:
                alcohol_impact = -1
            elif alcohol >= 3:
                alcohol_impact = -3
                
            smoke_impact = 0
            if smoke != "never":
                smoke_impact = -(12 if sex.lower() == "male" else 11)
                if smoke == "former":
                    if smoke_quit_age <= 34:
                        smoke_impact += 10
                    elif smoke_quit_age <= 44:
                        smoke_impact += 9
                    elif smoke_quit_age <= 54:
                        smoke_impact += 6
                    elif smoke_quit_age <= 64:
                        smoke_impact += 4
            
            # New health factors impacts
            if family_history == 0:
                family_impact = 0
            elif family_history == 1:
                family_impact = -2
            else:
                family_impact = -5
            
            bmi_impact = 0
            if bmi is not None:
                if bmi < 18.5:
                    bmi_impact = -2
                elif bmi < 25:
                    bmi_impact = 0
                elif bmi < 30:
                    bmi_impact = -2
                else:
                    bmi_impact = -5
            
            stress_impact = -(stress_level * 0.3) if stress_level is not None else 0
            
            if driving_risk == 0:
                driving_impact = 0
            elif driving_risk == 1:
                driving_impact = -1
            else:
                driving_impact = -3
            
            if doctor_visits == 2:
                doctor_impact = 2
            elif doctor_visits == 1:
                doctor_impact = 1
            else:
                doctor_impact = 0
            
            # Create impact DataFrame
            impact_data = {
                'Factor': ['Baseline (Demographics)', 'Physical Activity', 'Fast Food', 'Alcohol', 'Smoking', 'Family History', 'BMI', 'Stress Level', 'Driving Risk', 'Doctor Visits'],
                'Impact (years)': [
                    baseline, 
                    f"+{pa_impact:.1f}", 
                    f"{ff_impact:.1f}", 
                    f"{alcohol_impact:.1f}", 
                    f"{smoke_impact:.1f}",
                    f"{family_impact:.1f}",
                    f"{bmi_impact:.1f}" if bmi is not None else "Not included",
                    f"{stress_impact:.1f}" if stress_level is not None else "Not included",
                    f"{driving_impact:.1f}",
                    f"+{doctor_impact:.1f}"
                ],
                'Description': [
                    f"Base life expectancy for {sex.lower()} in {country}, {continent} in {year}",
                    f"Regular exercise: +{pa_impact:.1f} years",
                    f"Fast food consumption: {ff_impact:.1f} years",
                    f"Alcohol consumption: {alcohol_impact:.1f} years",
                    f"Smoking status: {smoke_impact:.1f} years",
                    f"Family history of chronic diseases: {family_impact:.1f} years",
                    f"BMI impact: {bmi_impact:.1f} years" if bmi is not None else "BMI not included in calculation",
                    f"Stress level impact: {stress_impact:.1f} years" if stress_level is not None else "Stress level not included",
                    f"Driving safety: {driving_impact:.1f} years",
                    f"Regular healthcare: +{doctor_impact:.1f} years"
                ]
            }
            
            impact_df = pd.DataFrame(impact_data)
            st.dataframe(impact_df, use_container_width=True, hide_index=True)
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.info("Please check your input parameters and try again.")

with col2:
    st.subheader("ℹ️ Information")
    
    st.markdown("""
    <div class="explanation-box">
        <h4>How it works:</h4>
        <p>This calculator uses machine learning models trained on historical life expectancy data from the UN Population Division. The models consider demographic factors and apply adjustments based on lifestyle choices.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="lifestyle-impact">
        <strong>Lifestyle Impact Factors:</strong><br>
        • <strong>Physical Activity:</strong> Can add up to 6.9 years<br>
        • <strong>Fast Food:</strong> Can reduce life expectancy by up to 15%<br>
        • <strong>Alcohol:</strong> Moderate consumption (-1 year), heavy (-3 years)<br>
        • <strong>Smoking:</strong> Can reduce by 10-12 years, but quitting helps significantly<br>
        • <strong>Family History:</strong> Some history (-2 years), strong history (-5 years)<br>
        • <strong>BMI:</strong> Underweight (-2 years), overweight (-2 years), obese (-5 years)<br>
        • <strong>Stress:</strong> Each stress level point reduces by 0.3 years<br>
        • <strong>Driving Risk:</strong> Moderate risk (-1 year), high risk (-3 years)<br>
        • <strong>Healthcare:</strong> Regular checkups can add up to 2 years
    </div>
    """, unsafe_allow_html=True)

# Additional information section
with st.expander("📖 About the Data and Methodology"):
    st.markdown("""
    ### Data Sources
    - **Primary Data:** UN Population Division life expectancy statistics
    - **Countries Included:** 16 countries across 4 continents
    - **Time Period:** Historical data from 1950-2050
    
    ### Methodology
    - **Base Prediction:** Linear regression models fitted using SVD
    - **Country-Specific Models:** Available for countries with sufficient data
    - **Continent Fallback:** Uses continent-level models when country data unavailable
    - **Lifestyle Adjustments:** Based on peer-reviewed medical research
    
    ### Limitations
    - Predictions are estimates based on historical trends
    - Individual health conditions are not considered
    - Lifestyle impacts are population-level averages
    - Future events (pandemics, medical breakthroughs) not predicted
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    📈 Life Expectancy Calculator | Based on UN Population Data | For Educational Purposes Only
</div>
""", unsafe_allow_html=True) 