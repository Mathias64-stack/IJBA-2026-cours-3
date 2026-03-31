TUTORIEL : CREER UNE CARTE INTERACTIVE A PARTIR D'UN CSV (SANS CODAGE)

Ce guide vous explique comment transformer un fichier de données CSV (contenant des coordonnées GPS) en une carte interactive professionnelle en utilisant l'outil libre uMap (basé sur Leaflet).

-------------------------------------------------------------------------------

1. PREPARATION DE VOS DONNEES (LE CSV)

Avant de commencer, assurez-vous que votre fichier CSV est bien structuré. Il doit impérativement contenir :
- Une colonne pour le Nom du lieu.
- Une colonne latitude (exemple : 44.837)
- Une colonne longitude (exemple : -0.579)

Conseils :
- Utilisez le point (.) pour les décimales.
- Enregistrez votre fichier au format .csv (Séparateur point-virgule ou virgule).

-------------------------------------------------------------------------------

2. CREATION DE LA CARTE AVEC UMAP

1. Rendez-vous sur le site : umap.openstreetmap.fr
2. Cliquez sur "Créer une carte".
3. Dans la barre d'outils à droite, cliquez sur l'icône "Importer des données" (une flèche pointant vers le haut).
4. Choisissez votre fichier CSV sur votre ordinateur.
5. uMap détecte automatiquement vos colonnes latitude et longitude et place les points sur la carte.

-------------------------------------------------------------------------------

3. PERSONNALISATION VISUELLE

Une fois les points importés, vous pouvez tout modifier sans code :
- Changer les icônes : Cliquez sur un point, puis sur le bouton "Editer". Vous pouvez choisir des symboles (maison, étoile, etc.) et des couleurs.
- Modifier le fond de carte : Cliquez sur l'icône des calques à droite pour choisir un rendu (épuré, satellite, artistique).
- Configurer les Popups : Vous pouvez choisir quelles colonnes du CSV s'affichent quand on clique sur un point.

-------------------------------------------------------------------------------

4. AJOUTER LES CONTOURS DE LA METROPOLE

1. Trouvez un fichier GeoJSON du contour souhaité (disponible sur les sites Open Data).
2. Utilisez à nouveau le bouton "Importer des données" et sélectionnez le fichier GeoJSON.
3. Le contour s'affichera automatiquement comme un nouveau calque que vous pourrez colorer (exemple : en fuchsia).

-------------------------------------------------------------------------------

5. PARTAGER LA CARTE

1. Cliquez sur "Enregistrer" en haut à droite.
2. Cliquez sur l'icône "Partager et intégrer" dans la barre latérale gauche.
3. Vous obtiendrez un lien direct vers votre carte ou un code pour l'insérer dans un site web.

-------------------------------------------------------------------------------

6. AVANTAGES DE CETTE METHODE

- Aucune installation : Tout se fait dans le navigateur.
- Zero maintenance : Vous n'avez pas de fichiers techniques à gérer vous-même.
- Collaboratif : Vous pouvez autoriser d'autres personnes à modifier la carte.
