# Template Global pour Applications Data & Machine Learning

Ce template fournit une architecture complète pour développer, déployer et surveiller des applications de Machine Learning et Data Science avec Docker, MLflow, Prometheus et Grafana. Il inclut trois projets distincts (API de gestion des données, API de Machine Learning, et interface utilisateur Streamlit), ainsi que des outils de monitoring.

---

## 1. Structure du Projet

```
📦 template-global
├── 📂 Projet-1  (API de gestion des données)
│   ├── 📂 models         # Modèles ML sauvegardés
│   ├── 📂 modules        # Fonctions et classes réutilisables
│   ├── 📂 routes         # Fichiers contenant les endpoints de l’API
│   ├── 📂 tests          # Tests unitaires et d’intégration
│   │   ├── test_main.py
│   ├── 📂 data           # Données (ex: CSV, JSON)
│   ├── 📂 fig            # Visualisations et graphiques
│   ├── .gitignore
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── Readme.md
├── 📂 Projet-2  (API Machine Learning)
│   ├── 📂 models
│   ├── 📂 modules
│   ├── 📂 tests
│   │   ├── test_main.py
│   ├── 📂 data
│   ├── 📂 fig
│   ├── .gitignore
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── Readme.md
├── 📂 Projet-3  (Interface Utilisateur Streamlit)
│   ├── 📂 modules
│   ├── 📂 tests
│   │   ├── test_main.py
│   ├── 📂 fig
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   ├── Readme.md
├── 📂 monitoring  (Prometheus & Grafana)
│   ├── 📂 grafana
│   │   ├── 📂 provisioning
│   │   │   ├── dashboards.yml
│   │   │   ├── datasources.yml
│   │   ├── Dockerfile
│   ├── 📂 prometheus
│   │   ├── prometheus.yml
│   ├── docker-compose.monitoring.yml
├── .github
│   ├── 📂 workflows
│   │   ├── ci.yml  # Pipeline CI/CD
├── docker-compose.yml
├── Readme.md
```

---

## 2. Installation et Exécution

### **Prérequis**
- **Docker & Docker Compose**
- **Python 3.9+** (si exécution locale)
- **MLflow, Prometheus, Grafana** pour le suivi des modèles et monitoring

### **Exécution avec Docker Compose**

#### **Démarrer l’ensemble des services**
```sh
docker-compose up --build
```

#### **Démarrer uniquement le monitoring (Grafana & Prometheus)**
```sh
docker-compose -f docker-compose.monitoring.yml up --build
```

#### **Accès aux services :**
- API Projet 1 : http://localhost:8001
- API Projet 2 : http://localhost:8002
- Interface Streamlit : http://localhost:8501
- MLflow Tracking UI : http://localhost:5000
- Prometheus : http://localhost:9090
- Grafana : http://localhost:3000

---

## 3. Développement & Tests

### **Lancer un projet en local (sans Docker)**
```sh
cd Projet-1  # ou Projet-2, Projet-3
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8001  # Adapter le port selon le projet
```

### **Exécuter les tests**
```sh
pytest tests/
```

### **Déploiement sur DockerHub**
```sh
docker build -t mon-image:latest .
docker tag mon-image:latest mon-dockerhub/mon-template:latest
docker push mon-dockerhub/mon-template:latest
```

---

## 4. Monitoring avec Prometheus & Grafana

### **Accès à Grafana**
- Ouvrir Grafana : [http://localhost:3000](http://localhost:3000)
- Identifiants par défaut : `admin / admin`
- Ajouter une source de données Prometheus : `http://prometheus:9090`
- Importer les dashboards via `provisioning/dashboards.yml`

### **Suivi des performances des modèles avec MLflow**
```sh
docker-compose up mlflow
```
Accès : [http://localhost:5001](http://localhost:5001)

---

## 5. Fonctionnalités à venir
✅ Intégration d’Airflow pour orchestrer les tâches ML
✅ Intégration d’Alertmanager pour recevoir des notifications sur l’état des APIs
✅ Intégration d’une base de données PostgreSQL pour le stockage des prédictions

---

## 6. Utilisation du Template sur GitHub
Si vous voulez réutiliser ce projet pour un nouveau développement :
1. **Créer un nouveau repo GitHub**
2. **Utiliser l’option** `Use this template` **sur GitHub**
3. **Cloner le projet**
```sh
git clone https://github.com/votre-repo/template-global.git
```
4. **Adapter et personnaliser selon votre projet !**

---

### 📌 **Auteur & Contributeurs**
Ce projet a été conçu et optimisé pour faciliter le développement et le suivi de projets ML.
- **Mathieu Soussignan** : [Mon site web](https://www.mathieu-soussignan.com/)