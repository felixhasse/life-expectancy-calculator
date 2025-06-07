import numpy as np
from sklearn.preprocessing import StandardScaler
from numpy.linalg import svd

def svd_weights(X, y):

    # Solve SVD problem
    U, d, VT = svd(X, full_matrices=False)

    # X^+ = V D^-1 U (weights are given by pseudo-inverse)
    w = VT.T @ np.diag(1 / d) @ U.T @ y

    return w

def get_weights
    continent_weights_male = {}

    for i, (continent, mean_series) in enumerate(continent_means_male.items()):

        years = mean_series.index.values.reshape(-1, 1)
        values = mean_series.values

        scaler = StandardScaler()
        years_scaled = scaler.fit_transform(years)
        X_scaled = np.hstack([np.ones_like(years_scaled), years_scaled])

        w = svd_weights(X_scaled, values)
        # Calculate slope in raw year units
        slope_raw = w[1] / scaler.scale_[0]

        continent_weights_male[continent] = {
            'weights': w,
            'scaler': scaler,
            'X_template': X_scaled[0],
            'slope_raw': slope_raw
    }



def predict_life_expectancy(country, continent, sex, year=2024, physical_activity = 0, fast_food = 0, alchool = 0, smoke = "never", smoke_quit_age=25):

    country = country.lower()
    continent = continent.lower()
    sex = sex.lower()

    if sex == "male":
        model_info = cont_weights_male(country, continent)
    else:
        model_info = cont_weights_female(country, continent)

    basic_le = predict_model(year, model_info)

    # adjustments based on life style

    # physical activity can increase life expectation from 0.43 to 6.9 additional years
    pa_bonus = min(physical_activity, 7)*(6.9/7)

    # eating fast food can decrease life expectancy of 15%
    ff_penalty = (min(fast_food, 14) / 14) * 0.15

    # alchool
    if(alchool > 0 & alchool < 3):
        alchool_penalty = 1
    elif (alchool >= 3):
        alchool_penalty = 3
    else:
        alchool_penalty = 0

    # smoking can decrease your life expectancy even of 10 years
    smoke_penalty = 0
    if(smoke != "never"):
        smoke_penalty = 12 if sex == "male" else 11
        if (smoke == "former"):
            if (smoke_quit_age <= 34):
                smoke_penalty -= 10
            elif (smoke_quit_age <= 44):
                smoke_penalty -= 9
            elif (smoke_quit_age <= 54):
                smoke_penalty -= 6
            elif (smoke_quit_age <= 64):
                smoke_penalty -= 4

    adjusted = (basic_le * (1 - ff_penalty)) + pa_bonus - alchool_penalty - smoke_penalty
    return round(adjusted)

def cont_weights_female(country, continent):

  if continent == "europe" and country in europe_countries:
    return europe_weights_female.get(country)

  elif continent == "africa" and country in africa_countries:
    return africa_weights_female.get(country)

  elif continent == "america" and country in america_countries:
    return america_weights_female.get(country)

  elif continent == "asia" and country in asian_countries:
    return asian_weights_female.get(country)

  return continent_weights_female.get(continent)

def cont_weights_male(country, continent):

    if continent == "europe" and country in europe_countries:
        return europe_weights_male.get(country)

    elif continent == "africa" and country in africa_countries:
        return africa_weights_male.get(country)

    elif continent == "america" and country in america_countries:
        return america_weights_male.get(country)

    elif continent == "asia" and country in asian_countries:
        return asian_weights_male.get(country)

    return continent_weights_male.get(continent)

def predict_model(year, model_info):
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