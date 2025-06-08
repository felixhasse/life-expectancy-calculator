import numpy as np
from sklearn.preprocessing import StandardScaler

# Countries by continent
countries = {
    'Africa': ['Sierra Leone', 'Congo', 'Madagascar'],
    'Americas': ['Brazil', 'Puerto Rico', 'Cuba', 'Canada', 'United States of America'],
    'Asia': ['Japan', 'Sri Lanka', 'Indonesia', 'China'],
    'Europe': ['Germany', 'Italy', 'Portugal', 'Russian Federation']
}

# Extract country lists
europe_countries = countries.get('Europe', [])
africa_countries = countries.get('Africa', [])
america_countries = countries.get('Americas', [])
asian_countries = countries.get('Asia', [])

# Pre-computed continent weights for males
continent_weights_male = {
    'africa': {
        'weights': np.array([48.80995999999999, 7.427797663635824]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.34310577809388354
    },
    'americas': {
        'weights': np.array([65.68893333333332, 6.095013555204009]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.28154164438122337
    },
    'asia': {
        'weights': np.array([59.29728399999999, 9.206187619878207]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.4252533940256046
    },
    'europe': {
        'weights': np.array([68.60288933333332, 3.593142724935098]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.16597490753911814
    }
}

# Pre-computed continent weights for females  
continent_weights_female = {
    'africa': {
        'weights': np.array([52.345453333333325, 7.342837591796632]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3391812916073966
    },
    'americas': {
        'weights': np.array([71.76667066666667, 6.1826456876559845]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.28558955903271693
    },
    'asia': {
        'weights': np.array([62.89476133333332, 10.227587577702595]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.4724340312944523
    },
    'europe': {
        'weights': np.array([75.83362399999999, 4.119186558463535]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.19027399146514914
    }
}

# Pre-computed Europe country weights for males
europe_weights_male = {
    'germany': {
        'weights': np.array([71.87143733333335, 4.587225890236901]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.2118937240398295
    },
    'italy': {
        'weights': np.array([73.03381199999998, 5.376565529051979]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.24835500142247505
    },
    'portugal': {
        'weights': np.array([69.313596, 6.778808123988059]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3131275704125178
    },
    'russian federation': {
        'weights': np.array([62.05815333333332, 1.6053944638817943]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.07415658605974408
    }
}

# Pre-computed Europe country weights for females
europe_weights_female = {
    'germany': {
        'weights': np.array([77.58053733333333, 4.482722237121892]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.20706647795163602
    },
    'italy': {
        'weights': np.array([78.54601733333332, 5.35285775826014]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.24725988904694168
    },
    'portugal': {
        'weights': np.array([75.74587066666665, 6.984728872246191]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3226394879089615
    },
    'russian federation': {
        'weights': np.array([72.75473999999997, 2.7612556404887654]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.12754827311522102
    }
}

# Pre-computed Asia country weights for males
asian_weights_male = {
    'japan': {
        'weights': np.array([73.66671333333332, 6.084929936909473]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.2810758605974396
    },
    'sri lanka': {
        'weights': np.array([65.00730933333332, 5.218823354737371]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.24106855476529154
    },
    'indonesia': {
        'weights': np.array([57.45450133333332, 9.04073326951489]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.4176107055476531
    },
    'china': {
        'weights': np.array([62.094491999999995, 10.704405754137152]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.49445927738264545
    }
}

# Pre-computed Asia country weights for females
asian_weights_female = {
    'japan': {
        'weights': np.array([79.32922933333333, 6.857907400256124]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3167813342816501
    },
    'sri lanka': {
        'weights': np.array([71.21257333333331, 6.811560682917558]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.31464048079658596
    },
    'indonesia': {
        'weights': np.array([61.29604133333332, 9.02926844501308]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.4170811209103843
    },
    'china': {
        'weights': np.array([66.70746933333334, 11.387949099336106]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.5260335988620198
    }
}

# Pre-computed Africa country weights for males
africa_weights_male = {
    'sierra leone': {
        'weights': np.array([42.28548533333333, 8.493151586584709]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.39231674253200555
    },
    'congo': {
        'weights': np.array([53.93806533333332, 5.957411826044415]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.27518552773826455
    },
    'madagascar': {
        'weights': np.array([51.46081333333332, 7.4008190590773815]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3418595789473682
    }
}

# Pre-computed Africa country weights for females
africa_weights_female = {
    'sierra leone': {
        'weights': np.array([45.109029333333325, 8.3094688987945]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3838320483641535
    },
    'congo': {
        'weights': np.array([56.76254666666666, 5.822295171764747]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.268944201991465
    },
    'madagascar': {
        'weights': np.array([54.23456133333332, 7.721151302301849]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.3566564068278804
    }
}

# Pre-computed America country weights for males
america_weights_male = {
    'brazil': {
        'weights': np.array([61.29868399999998, 7.972486056456338]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.36826609388335685
    },
    'puerto rico': {
        'weights': np.array([70.08885066666664, 4.219312491253628]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.1948990213371267
    },
    'cuba': {
        'weights': np.array([69.755504, 5.358231811984468]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.24750812802275962
    },
    'canada': {
        'weights': np.array([73.47906133333333, 4.517824066075921]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.20868790611664279
    },
    'united states of america': {
        'weights': np.array([71.22021733333332, 3.70491923616979]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.17113810241820782
    }
}

# Pre-computed America country weights for females
america_weights_female = {
    'brazil': {
        'weights': np.array([66.86967466666664, 8.806194958418565]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.4067768819345662
    },
    'puerto rico': {
        'weights': np.array([76.66809599999999, 5.384124716773799]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.24870417638691306
    },
    'cuba': {
        'weights': np.array([73.80328666666665, 5.609472765325014]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.2591134822190615
    },
    'canada': {
        'weights': np.array([79.18660799999998, 3.9433650933207063]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.18215242389758185
    },
    'united states of america': {
        'weights': np.array([77.49545199999999, 3.0327809736541753]),
        'scaler': StandardScaler(),
        'X_template': np.array([1.0, -1.709108724329423]),
        'slope_raw': 0.1400906059743955
    }
}

# Initialize scalers with proper parameters from actual data (1950-2024, mean=1987.0, std=21.65)
for weights_dict in [continent_weights_male, continent_weights_female, 
                     europe_weights_male, europe_weights_female,
                     asian_weights_male, asian_weights_female,
                     africa_weights_male, africa_weights_female,
                     america_weights_male, america_weights_female]:
    for model_info in weights_dict.values():
        if model_info is not None:
            scaler = model_info['scaler']
            # Set scaler parameters from actual dataset
            scaler.mean_ = np.array([1987.0])  # Mean year from actual data
            scaler.scale_ = np.array([21.64871050817269])   # Standard deviation from actual data
            scaler.n_features_in_ = 1

def predict_model(year, model_info):
    """Predict life expectancy for a given year using model weights."""
    weights = model_info.get('weights')
    scaler = model_info.get('scaler')
    X_template = model_info.get('X_template')

    if weights is None or scaler is None or X_template is None:
        raise ValueError("Model info incomplete")

    # Prepare input vector
    year_scaled = scaler.transform(np.array([[year]])).flatten()[0]
    X = X_template.copy()
    X[1] = year_scaled

    return float(np.dot(X, weights))

def cont_weights_male(country, continent):
    """Get model weights for male life expectancy by country/continent."""
    country = country.lower()
    continent = continent.lower()
    
    if continent == "europe" and country in [c.lower() for c in europe_countries]:
        return europe_weights_male.get(country)
    elif continent == "africa" and country in [c.lower() for c in africa_countries]:
        return africa_weights_male.get(country)
    elif continent == "americas" and country in [c.lower() for c in america_countries]:
        return america_weights_male.get(country)
    elif continent == "asia" and country in [c.lower() for c in asian_countries]:
        return asian_weights_male.get(country)
    
    return continent_weights_male.get(continent)

def cont_weights_female(country, continent):
    """Get model weights for female life expectancy by country/continent."""
    country = country.lower()
    continent = continent.lower()
    
    if continent == "europe" and country in [c.lower() for c in europe_countries]:
        return europe_weights_female.get(country)
    elif continent == "africa" and country in [c.lower() for c in africa_countries]:
        return africa_weights_female.get(country)
    elif continent == "americas" and country in [c.lower() for c in america_countries]:
        return america_weights_female.get(country)
    elif continent == "asia" and country in [c.lower() for c in asian_countries]:
        return asian_weights_female.get(country)
    
    return continent_weights_female.get(continent)

def predict_life_expectancy(
    country, continent, sex, year=2024,
    physical_activity=0, fast_food=0, alcohol=0, smoke="never", smoke_quit_age=25,
    family_history=0, bmi=None, stress_level=None,
    doctor_visits=0
):
    """
    Predict life expectancy based on demographic and lifestyle factors.
    
    Parameters:
    - country: Country name (string)
    - continent: Continent name (africa, americas, asia, europe)  
    - sex: Gender (male/female)
    - year: Year for prediction (default 2024)
    - physical_activity: Physical activity level (0=none, 1=low, 2=medium, 3=high)
    - fast_food: Processed food consumption level (0=none, 1=low, 2=medium, 3=high, 4=very high)
    - alcohol: Grams of alcohol per week
    - smoke: Smoking status ("never", "former", "current")
    - smoke_quit_age: Age when smoking was quit (if former smoker)
    - family_history: Family history of cardiovascular disease (0=none, 1=some, 2=strong)
    - bmi: Body Mass Index (optional)
    - stress_level: Stress attitude (0=positive, 1=neutral, 2=overwhelming)
    - doctor_visits: Doctor visit frequency (0=never, 1=when ill, 2=regular checkups)
    
    Returns:
    - Predicted life expectancy in years (rounded integer)
    """
    
    country = country.lower()
    continent = continent.lower()
    sex = sex.lower()

    # Get appropriate model weights
    if sex == "male":
        model_info = cont_weights_male(country, continent)
    else:
        model_info = cont_weights_female(country, continent)

    if model_info is None:
        raise ValueError(f"No model available for {country} in {continent}")

    # Get baseline life expectancy prediction
    basic_le = predict_model(year, model_info)

    # Lifestyle adjustments based on Sources.md
    
    # Physical activity adjustment (0.4 to 6.9 years)
    if physical_activity == 0:
        pa_bonus = 0
    elif physical_activity == 1:
        pa_bonus = 0.4  # Little bit of activity
    elif physical_activity == 2:
        pa_bonus = 3.6  # Medium activity
    else:  # physical_activity == 3
        pa_bonus = 6.9  # High activity

    # Processed food consumption (0% to 10% reduction in life expectancy)
    if fast_food == 0:
        ff_penalty_percent = 0.0  # No consumption
    elif fast_food == 1:
        ff_penalty_percent = 0.025  # Low consumption: 2.5%
    elif fast_food == 2:
        ff_penalty_percent = 0.05   # Medium consumption: 5%
    elif fast_food == 3:
        ff_penalty_percent = 0.075  # High consumption: 7.5%
    else:  # fast_food == 4
        ff_penalty_percent = 0.10   # Very high consumption: 10%

    # Alcohol adjustment (grams per week to years lost)
    # 100-200g: -0.5 years, 200-350g: -1 to -2 years, >350g: -4 to -5 years
    if alcohol < 100:
        alcohol_penalty = 0
    elif alcohol <= 200:
        alcohol_penalty = 0.5
    elif alcohol <= 350:
        alcohol_penalty = 1.5  # Average of 1-2 years
    else:
        alcohol_penalty = 4.5  # Average of 4-5 years

    # Smoking adjustment (10 years shorter life expectancy)
    smoke_penalty = 0
    if smoke == "current":
        smoke_penalty = 10  # At least 10 years shorter
    elif smoke == "former":
        # Adults who quit at different ages gained years back
        if smoke_quit_age <= 34:
            smoke_penalty = 0  # Gained about 10 years back (full recovery)
        elif smoke_quit_age <= 44:
            smoke_penalty = 1  # Gained about 9 years back
        elif smoke_quit_age <= 54:
            smoke_penalty = 4  # Gained about 6 years back
        else:
            smoke_penalty = 10  # No significant recovery after 54

    # Family history of cardiovascular disease
    if family_history == 0:
        family_history_bonus = 2  # No family history: +2 years
    elif family_history == 1:
        family_history_penalty = 1  # Some family history: -1 year
        family_history_bonus = 0
    else:  # family_history == 2
        family_history_penalty = 2  # Strong family history: -2 years
        family_history_bonus = 0

    # BMI adjustment
    bmi_penalty = 0
    if bmi is not None:
        if 25 <= bmi < 30:  # Overweight
            if sex == "female":
                bmi_penalty = 3.3
            else:  # male
                bmi_penalty = 3.1
        elif bmi >= 30:  # Obese
            if sex == "female":
                bmi_penalty = 7.1
            else:  # male
                bmi_penalty = 5.8

    # Stress adjustment
    stress_adjustment = 0
    if stress_level is not None:
        if stress_level == 0:  # Positive attitude to stress
            stress_adjustment = 1
        elif stress_level == 1:  # Neutral attitude
            stress_adjustment = 0
        else:  # stress_level == 2, overwhelming stress
            stress_adjustment = -1

    # Doctor visits adjustment
    if doctor_visits == 0:  # Never visiting doctor
        doctor_adjustment = -1
    elif doctor_visits == 1:  # Going when ill
        doctor_adjustment = 0
    else:  # doctor_visits == 2, regular checkups
        doctor_adjustment = 1

    # Calculate final adjusted life expectancy
    family_penalty = family_history_penalty if family_history > 0 else 0
    family_bonus = family_history_bonus if family_history == 0 else 0
    
    adjusted = (basic_le * (1 - ff_penalty_percent)) + pa_bonus - alcohol_penalty - smoke_penalty \
               - family_penalty + family_bonus - bmi_penalty + stress_adjustment + doctor_adjustment

    return round(adjusted)

def get_available_countries():
    """Return dictionary of available countries by continent."""
    return countries.copy()

def get_continents():
    """Return list of available continents."""
    return list(countries.keys()) 