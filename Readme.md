# 📌 Guide d'utilisation du Template Global

Ce document décrit comment utiliser le template global pour créer et déployer rapidement un projet basé sur ce modèle. Il inclut la structure du projet, l'utilisation de Docker Compose, l'intégration de Prometheus et Grafana pour la supervision, ainsi que MLflow pour le suivi des expériences de Machine Learning.

---

## 🚀 1. Cloner le Template

Ce template est conçu pour être utilisé comme point de départ pour de nouveaux projets.

### Option 1 : Utiliser "Use this template" sur GitHub
1. Aller sur la page du dépôt GitHub du template.
2. Cliquer sur **"Use this template"**.
3. Donner un nom à votre nouveau projet et créer le repository.

### Option 2 : Clonage classique
Si vous souhaitez simplement récupérer le template et l'utiliser localement sans créer un nouveau repo GitHub immédiatement :

```bash
# Cloner le repo
git clone https://github.com/votre-repo/template-global.git mon-nouveau-projet

# Se déplacer dans le dossier
cd mon-nouveau-projet

# Supprimer l'historique Git pour repartir de zéro
rm -rf .git

# Initialiser un nouveau dépôt
git init

git add .
git commit -m "Initialisation du projet depuis le template global"
```

---

## 🏗️ 2. Structure du Projet

```
mon-nouveau-projet/
│── .github/workflows/    # CI/CD avec GitHub Actions
│── grafana/              # Configuration Grafana
│── prometheus/           # Configuration Prometheus
│── Project-1/             # Service API 1
│── Project-2/             # Service API 2
│── Project-3/             # Interface Streamlit
│── docker-compose.yml    # Déploiement multi-services
│── Readme.md             # Documentation du projet
│── requirements.txt      # Dépendances générales
```

---

## 🏗️ 3. Déploiement avec Docker Compose

### Prérequis
- **Docker** & **Docker Compose** installés
- Un fichier **.env** si nécessaire

### Lancer les services

```bash
docker-compose up --build
```
Cela démarre :
✅ **Project-1** (API 1 sur le port 8001)
✅ **Project-2** (API 2 sur le port 8002)
✅ **Project-3** (Interface utilisateur Streamlit sur 8501)
✅ **Prometheus** (Monitoring sur 9090)
✅ **Grafana** (Visualisation sur 3000)
✅ **MLflow** (Tracking des expériences sur 5001)

### Arrêter les services

```bash
docker-compose down
```

---

## 📊 4. Accès aux services

| Service       | URL |
|--------------|----------------|
| Project-3 (UI) | [http://localhost:8501](http://localhost:8501) |
| Project-1 (API) | [http://localhost:8001](http://localhost:8001) |
| Project-2 (API) | [http://localhost:8002](http://localhost:8002) |
| Prometheus | [http://localhost:9090](http://localhost:9090) |
| Grafana | [http://localhost:3000](http://localhost:3000) |
| MLflow | [http://localhost:5001](http://localhost:5001) |

---

## 🔥 5. Supervision avec Prometheus & Grafana

- **Prometheus** collecte les métriques des services.
- **Grafana** permet de visualiser ces métriques.
- Un dashboard Grafana par défaut est provisionné.

### Accès à Grafana
1. Ouvrir [http://localhost:3000](http://localhost:3000)
2. Identifiants par défaut : `admin` / `admin`
3. Ajouter **Prometheus** comme datasource : `http://prometheus:9090`
4. Importer le dashboard fourni dans `grafana/provisioning`

---

## 🎯 6. Suivi des Expériences avec MLflow

- MLflow est utilisé pour suivre les entraînements de modèles.
- Par défaut, il est accessible sur [http://localhost:5001](http://localhost:5001).
- Un serveur de tracking est activé via Docker Compose.

### Lancer une expérience MLflow
Dans votre script d'entraînement, ajoutez :

```python
import mlflow
mlflow.set_tracking_uri("http://mlflow:5001")
mlflow.set_experiment("mon-experience")
```

---

## 📌 7. Bonnes Pratiques
✅ **Versionner le projet avec Git**
✅ **Utiliser les volumes Docker pour la persistance des données**
✅ **Personnaliser le `docker-compose.override.yml` si nécessaire**
✅ **Configurer les alertes Grafana pour la surveillance des APIs**

---

## 📬 8. Contributions & Améliorations
Si vous souhaitez contribuer à l'amélioration de ce template, vous pouvez :
- Proposer des améliorations via des **Pull Requests**.
- Ouvrir des **Issues** pour signaler des problèmes ou des suggestions.
- Discuter sur Slack/Discord si un espace communautaire existe.

---
** Ce template est conçu pour accélérer la mise en place de nouveaux projets tout en garantissant une architecture scalable et supervisée. Bonne utilisation ! **