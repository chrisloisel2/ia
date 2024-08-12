import numpy as np
import pandas as pd

# Définir la fonction


def f(x):
    return 0.6 * (x - 4)**2 + 4


# Générer 10 000 valeurs pour x dans un intervalle choisi
np.random.seed(42)  # Pour la reproductibilité
x_values = np.random.uniform(-10, 20, 10000)

# Appliquer la fonction f(x) à chaque valeur de x pour obtenir y
y_values = f(x_values)

# Ajouter un peu de bruit aux valeurs de y
noise = np.random.normal(0, 2, y_values.shape)
y_values_noisy = y_values + noise

# Ajouter des valeurs extrêmes pour simuler des outliers
n_extremes = 50  # Nombre de valeurs extrêmes à ajouter
extreme_indices = np.random.choice(range(10000), n_extremes, replace=False)
y_values_noisy[extreme_indices] += np.random.uniform(-15, 15, n_extremes)

# Créer un DataFrame pour le dataset
dataset = pd.DataFrame({
    'x': x_values,
    'y': y_values_noisy
})

dataset.to_csv('dataset.csv', index=False)
