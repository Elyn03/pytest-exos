# 🌤️ Weather Data Fetcher

Un petit script Python pour récupérer les données météo horaires d'un lieu donné via l'API [Open-Meteo](https://open-meteo.com), les sauvegarder en JSON et tracer la température.

## 📦 Prérequis

- Python 3.8+
- Environnement virtuel recommandé (`.venv`)

## 🔧 Installation

WINDOWS :
```bash
# Créer un environnement virtuel
python -m venv .venv

# Activer l'environnement (Windows)
.\.venv\Scripts\activate

# Installer les dépendances
pip install pandas matplotlib openmeteo-requests
```

## ▶️ Utilisation

```bash
pytest