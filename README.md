# 🌍 Life Expectancy Calculator

A Streamlit web application that predicts life expectancy based on demographic information and lifestyle factors. The app uses machine learning models trained on historical UN Population Division data.

## Features

- **Country-Specific Predictions**: Covers 16 countries across 4 continents
- **Comprehensive Health Analysis**: Includes lifestyle, genetic, and behavioral factors
- **Interactive Interface**: User-friendly Streamlit interface with real-time predictions
- **Impact Breakdown**: Shows how each factor affects life expectancy
- **BMI Calculator**: Built-in BMI calculation from height and weight
- **Historical Data**: Based on UN Population Division statistics from 1950-2050

## Available Countries

### Africa
- Sierra Leone
- Congo
- Madagascar

### Americas
- Brazil
- Puerto Rico
- Cuba
- Canada
- United States of America

### Asia
- Japan
- Sri Lanka
- Indonesia
- China

### Europe
- Germany
- Italy
- Portugal
- Russian Federation

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Use the sidebar to input:
   - **Demographics**: Continent, country, sex, and year
   - **Lifestyle factors**: Physical activity, fast food consumption, alcohol intake, smoking status
   - **Health factors**: Family history, BMI, stress level, driving risk, healthcare visits

4. Click "Calculate Life Expectancy" to get your prediction

## How It Works

### Base Prediction Model
- Uses linear regression models fitted with Singular Value Decomposition (SVD)
- Country-specific models when available, falls back to continent-level models
- Trained on historical life expectancy trends from 1950-2050

### Lifestyle Adjustments
The app applies research-based adjustments for lifestyle factors:

- **Physical Activity**: Up to +6.9 years for regular exercise (7+ hours/week)
- **Fast Food**: Up to -15% reduction for frequent consumption (14+ meals/week)
- **Alcohol**: -1 year for moderate drinking (1-2 drinks/week), -3 years for heavy drinking (3+ drinks/week)
- **Smoking**: -10 to -12 years for current smokers, with recovery benefits for quitters based on quit age

### Health Factor Adjustments
Additional health-related factors that affect predictions:

- **Family History**: -2 years for some family history, -5 years for strong family history of chronic diseases
- **BMI (Body Mass Index)**: -2 years for underweight (<18.5) or overweight (25-30), -5 years for obesity (>30)
- **Stress Level**: -0.3 years per stress level point (scale 0-10)
- **Driving Risk**: -1 year for moderate risk, -3 years for high-risk driving behaviors
- **Healthcare Access**: +1 year for occasional checkups, +2 years for regular preventive care

### Sources for Lifestyle Impacts
- Physical activity benefits: Based on studies showing 0.43-6.9 year increases
- Fast food impacts: Research indicating 14-15% life expectancy reduction
- Smoking effects: Well-documented 10+ year reduction, with age-dependent recovery for quitters

## File Structure

```
├── streamlit_app.py              # Main Streamlit application
├── life_expectancy_predictor.py  # Core prediction functions and models
├── requirements.txt              # Python dependencies
└── README.md                    # This file
```

## Model Details

### Data Sources
- UN Population Division life expectancy statistics
- Historical data spanning 1950-2050
- Country and continent-level aggregations

### Methodology
- **Linear Regression**: Models life expectancy trends over time
- **SVD Fitting**: Robust parameter estimation using Singular Value Decomposition  
- **Standardization**: Years are standardized for numerical stability
- **Lifestyle Adjustments**: Evidence-based modifications applied to base predictions

### Limitations
- Predictions are statistical estimates based on population trends
- Individual health conditions and genetic factors not considered
- Lifestyle impacts are population-level averages
- Future events (pandemics, medical breakthroughs, policy changes) not predicted
- Limited to countries/regions with available training data

## Development

The models were originally developed in a Jupyter notebook (`p2_m4ml-2.ipynb`) and extracted into the modular Python files for the Streamlit app. The pre-computed model weights eliminate the need for the original training data during app execution.

## Disclaimer

This tool is for educational and informational purposes only. The predictions should not be used for medical decisions or insurance purposes. Consult healthcare professionals for personalized health advice.

## License

This project is for educational use. Please respect the data sources and research cited in the lifestyle factor calculations.