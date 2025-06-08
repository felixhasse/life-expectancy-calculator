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
This calculator predicts life expectancy based on demographic information and individual factors. 
The predictions are based on linear regression models trained on historical data from various countries and continents as well as research on the impact of health and lifestyle factors on life expectancy.
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
# Add "Other" option to use continent-level weights
available_countries_with_other = available_countries + ["Other"]
country = st.sidebar.selectbox(
    "Select Country:",
    options=available_countries_with_other,
    help="Choose a specific country or 'Other' to use continent-level data"
)

# Sex selection
sex = st.sidebar.selectbox(
    "Select Sex:",
    options=["Male", "Female"],
    help="Choose the biological sex for the prediction"
)

# Year selection
year = st.sidebar.slider(
    "Prediction Year:",
    min_value=1950,
    max_value=2050,
    value=2025,
    step=1,
    help="Select the year for which you want to predict life expectancy"
)

# Lifestyle factors section
st.sidebar.subheader("🏃‍♀️ Lifestyle Factors")

# Physical activity
physical_activity = st.sidebar.selectbox(
    "Physical Activity Level:",
    options=[0, 1, 2, 3],
    format_func=lambda x: {0: "None", 1: "Low", 2: "Medium", 3: "High"}[x],
    index=1,
    help="Physical activity level based on regularity and intensity"
)

# Processed food consumption  
fast_food = st.sidebar.selectbox(
    "Processed Food Consumption:",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: {0: "None", 1: "Low", 2: "Medium", 3: "High", 4: "Very High"}[x],
    index=1,
    help="Level of ultra-processed food consumption"
)

# Alcohol consumption (drinks per week)
alcohol = st.sidebar.slider(
    "Alcohol Consumption (drinks/week):",
    min_value=0,
    max_value=50,
    value=0,
    step=1,
    help="Grams of alcohol per week (1 drink ≈ 10g). 100-200g = moderate, 200-350g = high, >350g = very high"
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
    "Family History of Cardiovascular Disease:",
    options=[0, 1, 2],
    format_func=lambda x: {0: "No family history", 1: "Some family history", 2: "Strong family history"}[x],
    help="Family history of heart disease, stroke, and related cardiovascular conditions"
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
stress_input = st.sidebar.checkbox("Include stress attitude", value=False)
stress_level = None
if stress_input:
    stress_level = st.sidebar.selectbox(
        "Attitude Towards Stress:",
        options=[0, 1, 2],
        format_func=lambda x: {0: "Positive influence", 1: "Neutral attitude", 2: "Overwhelming/negative"}[x],
        index=1,
        help="How you generally view and handle stress in your life"
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
                alcohol=alcohol * 10,
                smoke=smoke,
                smoke_quit_age=smoke_quit_age,
                family_history=family_history,
                bmi=bmi,
                stress_level=stress_level,
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
            
            # Calculate individual impacts using the predict_life_expectancy function
            # Get baseline (all factors at neutral/default values)
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
                doctor_visits=1  # Default to "when ill" as neutral
            )
            
            # Calculate impact of each factor by changing one at a time
            # Physical activity impact
            pa_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=physical_activity, fast_food=0, alcohol=0, smoke="never",
                smoke_quit_age=25, family_history=0, bmi=None, stress_level=None, doctor_visits=1
            )
            pa_impact = pa_prediction - baseline
            
            # Processed food impact
            ff_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=0, fast_food=fast_food, alcohol=0, smoke="never",
                smoke_quit_age=25, family_history=0, bmi=None, stress_level=None, doctor_visits=1
            )
            ff_impact = ff_prediction - baseline
            
            # Alcohol impact
            alcohol_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=0, fast_food=0, alcohol=alcohol, smoke="never",
                smoke_quit_age=25, family_history=0, bmi=None, stress_level=None, doctor_visits=1
            )
            alcohol_impact = alcohol_prediction - baseline
                
            # Smoking impact
            smoke_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=0, fast_food=0, alcohol=0, smoke=smoke,
                smoke_quit_age=smoke_quit_age, family_history=0, bmi=None, stress_level=None, doctor_visits=1
            )
            smoke_impact = smoke_prediction - baseline
            
            # Family history impact
            family_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=0, fast_food=0, alcohol=0, smoke="never",
                smoke_quit_age=25, family_history=family_history, bmi=None, stress_level=None, doctor_visits=1
            )
            family_impact = family_prediction - baseline
            
            # BMI impact
            if bmi is not None:
                bmi_prediction = predict_life_expectancy(
                    country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                    physical_activity=0, fast_food=0, alcohol=0, smoke="never",
                    smoke_quit_age=25, family_history=0, bmi=bmi, stress_level=None, doctor_visits=1
                )
                bmi_impact = bmi_prediction - baseline
            else:
                bmi_impact = 0
            
            # Stress impact
            if stress_level is not None:
                stress_prediction = predict_life_expectancy(
                    country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                    physical_activity=0, fast_food=0, alcohol=0, smoke="never",
                    smoke_quit_age=25, family_history=0, bmi=None, stress_level=stress_level, doctor_visits=1
                )
                stress_impact = stress_prediction - baseline
            else:
                stress_impact = 0
            
            # Doctor visits impact
            doctor_prediction = predict_life_expectancy(
                country=country, continent=continent.lower(), sex=sex.lower(), year=year,
                physical_activity=0, fast_food=0, alcohol=0, smoke="never",
                smoke_quit_age=25, family_history=0, bmi=None, stress_level=None, doctor_visits=doctor_visits
            )
            doctor_impact = doctor_prediction - baseline
            
            # Create impact DataFrame
            # Handle display name for "Other" option
            display_country = "continent-level" if country == "Other" else country
            
            impact_data = {
                'Factor': ['Baseline (Demographics)', 'Physical Activity', 'Processed Food', 'Alcohol', 'Smoking', 'Family History', 'BMI', 'Stress Attitude', 'Doctor Visits'],
                'Impact (years)': [
                    f"{baseline:.1f}", 
                    f"+{pa_impact:.1f}", 
                    f"{ff_impact:.1f}", 
                    f"{alcohol_impact:.1f}", 
                    f"{smoke_impact:.1f}",
                    f"{family_impact:+.1f}",
                    f"{bmi_impact:.1f}" if bmi is not None else "Not included",
                    f"{stress_impact:+.1f}" if stress_level is not None else "Not included",
                    f"{doctor_impact:+.1f}"
                ],
                'Description': [
                    f"Base life expectancy for {sex.lower()} in {display_country}, {continent} in {year}",
                    f"Physical activity level: +{pa_impact:.1f} years",
                    f"Processed food consumption: {ff_impact:.1f} years",
                    f"Alcohol consumption: {alcohol_impact:.1f} years",
                    f"Smoking status: {smoke_impact:.1f} years",
                    f"Family history of cardiovascular disease: {family_impact:+.1f} years",
                    f"BMI impact: {bmi_impact:.1f} years" if bmi is not None else "BMI not included in calculation",
                    f"Stress attitude impact: {stress_impact:+.1f} years" if stress_level is not None else "Stress attitude not included",
                    f"Regular healthcare: {doctor_impact:+.1f} years"
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
        <p>This calculator uses linear regression models trained on historical life expectancy data from the UN Population Division. The models consider demographic factors and apply adjustments based on lifestyle choices.</p>
        <p><strong>Country Selection:</strong> Choose a specific country for country-specific predictions, or select "Other" to use continent-level averages for countries not specifically modeled.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="lifestyle-impact">
        <strong>Lifestyle Impact Factors (based on research):</strong><br>
        • <strong>Physical Activity:</strong> 0.4 to 6.9 years increased life expectancy<br>
        • <strong>Processed Food:</strong> High consumption reduces life expectancy by up to 10%<br>
        • <strong>Alcohol:</strong> 100-200g/week (-0.5 years), 200-350g/week (-1.5 years), >350g/week (-4.5 years)<br>
        • <strong>Smoking:</strong> Current smokers lose 11-12 years; but quitting early can restore most of the lost lifespan<br>
        • <strong>Family History (CVD):</strong> No history (+2 years), some history (-1 year), strong history (-2 years)<br>
        • <strong>BMI:</strong> Overweight: -3.1 to -3.3 years; Obese: -5.8 to -7.1 years<br>
        • <strong>Stress Attitude:</strong> Positive view (+1 year), neutral (0), overwhelming (-1 year)<br>
        • <strong>Healthcare:</strong> Regular checkups (+1 year), never visiting doctor (-1 year)
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