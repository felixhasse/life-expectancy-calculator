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
        'weights': np.array([55.47308369,  0.26737533]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.26737533
    },
    'americas': {
        'weights': np.array([66.48479853,  0.2635029]),
        'scaler': StandardScaler(), 
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.2635029
    },
    'asia': {
        'weights': np.array([63.79659836,  0.30434426]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.30434426
    },
    'europe': {
        'weights': np.array([69.08087097,  0.22166447]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.22166447
    }
}

# Pre-computed continent weights for females  
continent_weights_female = {
    'africa': {
        'weights': np.array([58.15750819,  0.29098361]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.29098361
    },
    'americas': {
        'weights': np.array([72.11229612,  0.24901639]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.24901639
    },
    'asia': {
        'weights': np.array([68.83770492,  0.32360656]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.32360656
    },
    'europe': {
        'weights': np.array([77.12491502,  0.20491803]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.20491803
    }
}

# Pre-computed Europe country weights for males
europe_weights_male = {
    'germany': {
        'weights': np.array([70.01491935,  0.23032258]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.23032258
    },
    'italy': {
        'weights': np.array([71.95483871,  0.2183871]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.2183871
    },
    'portugal': {
        'weights': np.array([66.29032258,  0.31451613]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.31451613
    },
    'russian federation': {
        'weights': np.array([65.61290323,  0.12258065]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.12258065
    }
}

# Pre-computed Europe country weights for females
europe_weights_female = {
    'germany': {
        'weights': np.array([76.91612903,  0.22258065]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.22258065
    },
    'italy': {
        'weights': np.array([78.49354839,  0.21612903]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.21612903
    },
    'portugal': {
        'weights': np.array([73.42903226,  0.28387097]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.28387097
    },
    'russian federation': {
        'weights': np.array([75.53548387,  0.07741935]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.07741935
    }
}

# Pre-computed Asia country weights for males
asian_weights_male = {
    'japan': {
        'weights': np.array([74.21612903,  0.23225806]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.23225806
    },
    'sri lanka': {
        'weights': np.array([66.34838710,  0.30322581]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.30322581
    },
    'indonesia': {
        'weights': np.array([62.12258065,  0.35806452]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.35806452
    },
    'china': {
        'weights': np.array([66.51612903,  0.32580645]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.32580645
    }
}

# Pre-computed Asia country weights for females
asian_weights_female = {
    'japan': {
        'weights': np.array([80.66451613,  0.24516129]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.24516129
    },
    'sri lanka': {
        'weights': np.array([71.17741935,  0.32903226]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.32903226
    },
    'indonesia': {
        'weights': np.array([65.98064516,  0.38709677]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.38709677
    },
    'china': {
        'weights': np.array([70.51290323,  0.33548387]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.33548387
    }
}

# Pre-computed Africa country weights for males
africa_weights_male = {
    'sierra leone': {
        'weights': np.array([37.69032258,  0.26451613]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.26451613
    },
    'congo': {
        'weights': np.array([54.34838710,  0.24516129]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.24516129
    },
    'madagascar': {
        'weights': np.array([53.38064516,  0.29032258]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.29032258
    }
}

# Pre-computed Africa country weights for females
africa_weights_female = {
    'sierra leone': {
        'weights': np.array([38.81935484,  0.27741935]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.27741935
    },
    'congo': {
        'weights': np.array([57.23225806,  0.28064516]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.28064516
    },
    'madagascar': {
        'weights': np.array([56.41935484,  0.31451613]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.31451613
    }
}

# Pre-computed America country weights for males
america_weights_male = {
    'brazil': {
        'weights': np.array([63.81612903,  0.27741935]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.27741935
    },
    'puerto rico': {
        'weights': np.array([68.91612903,  0.26451613]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.26451613
    },
    'cuba': {
        'weights': np.array([72.72903226,  0.17741935]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.17741935
    },
    'canada': {
        'weights': np.array([73.96774194,  0.20967742]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.20967742
    },
    'united states of america': {
        'weights': np.array([72.03548387,  0.15161290]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.15161290
    }
}

# Pre-computed America country weights for females
america_weights_female = {
    'brazil': {
        'weights': np.array([70.65806452,  0.27096774]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.27096774
    },
    'puerto rico': {
        'weights': np.array([75.30645161,  0.24516129]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.24516129
    },
    'cuba': {
        'weights': np.array([77.24516129,  0.19354839]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.19354839
    },
    'canada': {
        'weights': np.array([79.31612903,  0.20322581]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.20322581
    },
    'united states of america': {
        'weights': np.array([76.63548387,  0.15161290]),
        'scaler': StandardScaler(),
        'X_template': np.array([1., 0.]),
        'slope_raw': 0.15161290
    }
}

# Initialize scalers with proper parameters (approximated for year range 1950-2050)
for weights_dict in [continent_weights_male, continent_weights_female, 
                     europe_weights_male, europe_weights_female,
                     asian_weights_male, asian_weights_female,
                     africa_weights_male, africa_weights_female,
                     america_weights_male, america_weights_female]:
    for model_info in weights_dict.values():
        if model_info is not None:
            scaler = model_info['scaler']
            # Set scaler parameters for year range 1950-2050
            scaler.mean_ = np.array([2000.0])  # Middle of year range
            scaler.scale_ = np.array([28.87])   # Approx std of years 1950-2050
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

def predict_life_expectancy(country, continent, sex, year=2024, physical_activity=0, fast_food=0, alcohol=0, smoke="never", smoke_quit_age=25):
    """
    Predict life expectancy based on demographic and lifestyle factors.
    
    Parameters:
    - country: Country name (string)
    - continent: Continent name (africa, americas, asia, europe)  
    - sex: Gender (male/female)
    - year: Year for prediction (default 2024)
    - physical_activity: Hours of physical activity per week (0-7)
    - fast_food: Number of fast food meals per week (0-14)
    - alcohol: Number of alcoholic drinks per week
    - smoke: Smoking status ("never", "former", "current")
    - smoke_quit_age: Age when smoking was quit (if former smoker)
    
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

    # Lifestyle adjustments
    
    # Physical activity can increase life expectancy from 0.43 to 6.9 additional years
    pa_bonus = min(physical_activity, 7) * (6.9/7)

    # Eating fast food can decrease life expectancy by 15%
    ff_penalty = (min(fast_food, 14) / 14) * 0.15

    # Alcohol adjustment
    if alcohol > 0 and alcohol < 3:
        alcohol_penalty = 1
    elif alcohol >= 3:
        alcohol_penalty = 3
    else:
        alcohol_penalty = 0

    # Smoking can decrease life expectancy by up to 10-12 years
    smoke_penalty = 0
    if smoke != "never":
        smoke_penalty = 12 if sex == "male" else 11
        if smoke == "former":
            if smoke_quit_age <= 34:
                smoke_penalty -= 10
            elif smoke_quit_age <= 44:
                smoke_penalty -= 9
            elif smoke_quit_age <= 54:
                smoke_penalty -= 6
            elif smoke_quit_age <= 64:
                smoke_penalty -= 4

    # Calculate final adjusted life expectancy
    adjusted = (basic_le * (1 - ff_penalty)) + pa_bonus - alcohol_penalty - smoke_penalty
    return round(adjusted)

def get_available_countries():
    """Return dictionary of available countries by continent."""
    return countries.copy()

def get_continents():
    """Return list of available continents."""
    return list(countries.keys()) 