## Article de blog

Présentation et comparaison des trois approches : <a href = https://rlgmachinelearning.wordpress.com/2022/06/09/detectez-les-bad-buzz-grace-au-deep-learning/>https://rlgmachinelearning.wordpress.com</a>

## Résultats des Notebooks sous format HTML

Les résultats des notebooks en pages HTML :

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_00_notebook_analyse>Analyse du jeu de données</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_01_notebook_text_analytics_api>Approche API sur étagère (service cognitif Azure)</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_02_notebook_designer>Approche modèle sur mesure simple (Concepteur / Designer d'Azure Machine Learning)</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_03_notebook_advanced_models>Approche modèle sur mesure avancé (service notebooks d'Azure Machine Learning)</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_04_notebook_azure_model_training>Azure ML - Entraînement du modèle avancé</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_05_notebook_azure_model_deployment>Azure ML - Déploiement du modèle avancé</a>

<a href = https://deviluna29.github.io/oc_ingenieur-ia_p7/P07_06_notebook_azure_modelDeployed_test>Azure ML - Test Web Service du modèle avancé</a>

## Configuration

Renommer le fichier .env_sample en .env et renseigner les valeurs des variables d'environnement ("Endpoints" et "Key" des web services Azure déployés)

## Installation de l'environnement virtuel

Créer l'environnement à partir du fichier yaml
```bash
conda env create -f environment.yml
```

Activer l'environnement
```bash
conda activate projet_ml
```

## Téléchargement du jeu de données

Récupérer le jeu de données <a href = https://www.kaggle.com/datasets/kazanova/sentiment140>à cette adresse</a>

Dezipper le fichier dans le dossier "data/"
