# Tutoriel : Créer une Carte Interactive Leaflet à partir d'un CSV

Ce guide explique comment transformer un fichier de données CSV (contenant des coordonnées GPS) en une carte interactive web utilisant la bibliothèque **Leaflet.js**.

---

## 1. Structure du Projet
Pour que la carte fonctionne, vous avez besoin de deux fichiers dans le même dossier :
1. `index.html` : La page web qui contient la carte.
2. `data.csv` : Votre fichier de données.

---

## 2. Préparation du Fichier CSV
Votre fichier CSV doit impérativement contenir deux colonnes nommées (sans accents de préférence) :
- `latitude` : Les coordonnées Nord/Sud (ex: 44.837)
- `longitude` : Les coordonnées Est/Ouest (ex: -0.579)

---

## 3. Le Code HTML & JavaScript (Modèle prêt à l'emploi)
Voici le code complet à copier dans votre fichier `index.html`.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ma Carte Interactive</title>
    
    <!-- 1. Import de Leaflet (CSS) -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    
    <style>
        #map { height: 100vh; width: 100%; } /* La carte prend tout l'écran */
        body { margin: 0; }
    </style>
</head>
<body>

    <div id="map"></div>

    <!-- 2. Import des Bibliothèques (JS) -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.2/papaparse.min.js"></script>

    <script>
        // 3. Initialisation de la carte (Coordonnées par défaut et Zoom)
        const map = L.map('map').setView([44.83, -0.57], 12);

        // 4. Choix du fond de carte (CartoDB Voyager)
        L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap'
        }).addTo(map);

        // 5. Lecture du fichier CSV avec PapaParse
        Papa.parse('data.csv', {
            download: true,
            header: true,
            complete: function(results) {
                results.data.forEach(row => {
                    const lat = parseFloat(row.latitude);
                    const lng = parseFloat(row.longitude);

                    if (!isNaN(lat) && !isNaN(lng)) {
                        // Ajout d'un marqueur pour chaque ligne
                        L.marker([lat, lng])
                            .addTo(map)
                            .bindPopup(`<b>${row.nom}</b><br>${row.description}`);
                    }
                });
            }
        });
    </script>
</body>
</html>
```

---

## 4. Personnalisation Avancée

### Changer les icônes (Symboles personnalisés)
Au lieu du marqueur bleu standard, vous pouvez utiliser des icônes SVG :
```javascript
const myIcon = L.divIcon({
    className: 'custom-div-icon',
    html: "<div style='background-color:red;'>X</div>",
    iconSize: [30, 30]
});
L.marker([lat, lng], {icon: myIcon}).addTo(map);
```

### Ajouter des contours (GeoJSON)
Pour afficher les frontières d'une ville ou d'une métropole :
```javascript
fetch('url_du_fichier_geojson')
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, { style: { color: 'fuchsia' } }).addTo(map);
    });
```

---

## 5. Publication avec GitHub Pages
1. Créez un dépôt sur GitHub.
2. Envoyez vos fichiers (`index.html` et `votre_data.csv`).
3. Allez dans **Settings > Pages**.
4. Sous **Build and deployment**, choisissez la branche `main` et cliquez sur **Save**.
5. Votre carte sera en ligne à l'adresse `https://votre-pseudo.github.io/nom-du-depot/`.

---

## 6. Erreurs Fréquentes
- **Chemin du CSV** : Vérifiez que le nom du fichier dans le code (`Papa.parse('nom.csv', ...)`) correspond exactement au nom du fichier réel.
- **Espaces dans les noms** : Évitez les espaces dans le nom du fichier CSV (utilisez `donnees.csv` plutôt que `mes donnees.csv`).
- **Nombres** : Assurez-vous que les coordonnées dans le CSV utilisent le point (`.`) comme séparateur décimal et non la virgule (`,`).
