
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/image1.jpeg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="font-size: 24px;text-align: center;"><p><strong>Manuel utilisateur du plugin
« Assistant complexe »</strong></p>
<p><strong>V1.3.2</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>

## Sommaire

- [1. Prérequis](#prerequis)

- [2. Résumé](#resume)

- [3. Installation](#installation)

- [4. Présentation](#presentation)

- [5. Mode de sélection](#mode-de-sélection)

	- [5.1 Sélection unique](#selection-unique)

	- [5.2 Sélection multiple](#selection-multiple)

- [6. Modifications d’un complexe](#modifications-dun-complexe)

- [7. A propos de](#a-propos-de)

	




<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>

- Version de QGIS : 3.28 ou supérieur

- Plugin « IGN Espace collaboratif » version 4.2.2 (minimum) auquel il
  fait accès pour modifier la BDTopo.

- Couche troncon_de_route  éditable de la BDTopo que l’on trouve dans
  les guichets en écriture directe BDTopo ‘sdis formation’, ‘sdis
  découverte’ et ‘sdis expert’.

- Package openpyxl (voir installation en annexe à la fin de ce
  document).

- Le plugin « PluginsManager » doit préalablement être installé : 
[PluginsManager-qgis-plugin sur GitHub](https://github.com/IGNF/maitre-qgis-plugin/releases/download/version_finale/PluginsManager.zip)

- Le fonctionnement de certaines fonctionnalités nécessite l’installation de :
[ShortestPath-qgis-plugin sur GitHub](https://github.com/IGNF/ShortestPath-qgis-plugin/releases/download/version_finale/IGN_ShortestPath.zip)  

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="resume" style="color: white;margin:0;" >2. Résumé</h2>
</div>

Rappel des spécifications de la BDTopo :

Le numéro ou le nom des routes (départementales, autoroutes, nationales,
intercommunales, communales, chemins ruraux) est affiché dans les
tronçons de route (CPX_Numéro, CPX_Numéro de route européenne,
CPX_Toponyme route nommée) mais ces routes numérotées ou nommées sont
gérées par des objets Route numérotées ou nommées.

Le lien entre les tronçons de route et les routes numérotées ou nommées
est construit par l’attribut Liens vers route nommée des tronçons. C’est
la notion d’objets complexes.

Pour plus de précisions se référer aux [spécifications
BDTopo](https://geoservices.ign.fr/bd-topor-explorer-descriptif-de-contenu).

Ce plugin facilite la gestion de ce lien et permet d’ajouter, de retirer
un ou plusieurs tronçons de ces routes numérotées ou nommées et de
sélectionner tous les tronçons qui les composent.

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="installation" style="color: white;margin:0;" >3. Installation</h2>
</div>
Ouvrir QGIS.

Allez dans Extensions/Installer/Gérer les extensions, cliquez sur
Installer depuis un ZIP, sélectionner le fichier ZIP puis cliquez sur
Installer le plugin.

<img src="images/image2.png"
style="width:6.83889in;height:1.525in" />

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >4. Présentation</h2>
</div>

<img src="images/image3.png"
style="width:4.83401in;height:2.10446in" />

Cette interface permet de lire les informations des routes numérotées ou
nommées auquel appartiennent les tronçons de route sélectionnés mais
aussi de les retirer ou ajouter.

Le bouton <img src="images/image4.PNG"
style="width:1.0625in;height:0.19318in" /> permet d’ajouter les tronçons
de route sélectionnés au complexe fixé dans la liste.

Le bouton <img src="images/image5.PNG"
style="width:1.07292in;height:0.19361in" /> permet de retirer les
tronçons de route sélectionnés au complexe fixé dans la liste.

Le bouton <img src="images/image6.PNG"
style="width:1.54167in;height:0.19503in" /> permet de sélectionner tous
les constituants (tronçons de route) du complexe choisi.

Le bouton à cliquer <img src="images/image7.PNG"
style="width:0.30208in;height:0.33307in" /> sert à fixer le complexe
choisi afin de permettre la sélection de tronçons de route pour ajout ou
retrait du complexe.

Le bouton <img src="images/image8.png"
style="width:0.21522in;height:0.22291in" /> permet d’afficher le suivi
des versions et permet également d’ouvrir la documentation du plugin

Le bouton <img src="images/image9.png"
style="width:0.78125in;height:0.40625in" /> permet de modifier la
couleur de la sélection

Le bouton <img src="images/image10.PNG"
style="width:1.03125in;height:0.2145in" /> permet de sélectionner tous
les tronçons compris entre 2 tronçons

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="mode-de-sélection" style="color: white;margin:0;" >5. Mode de sélection</h2>
</div>

L’interface permet de modifier la couleur de la sélection des tronçons
dans QGIS, en fonction de la symbologie des tronçons il peut être
judicieux d’en modifier la couleur



<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="selection-unique" style="color: white;margin:0;" >5.1 Sélection unique</h2>
</div>

- Sélection unique, on ne sélectionne qu’un seul tronçon avec l’outil de
  sélection de QGIS


<div  style="font-size: 10px;background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="selection-multiple" style="color: white;margin:0;" >5.2 Sélection multiple</h2>
</div>

- Sélection multiple avec l’outil de saisi. Dans QGIS on peut
  sélectionner manuellement un ensemble de tronçons

- Sélection multiple de tronçons contigües, on sélectionne
  <span class="mark">2 tronçons visibles à l’écran et connectés</span>
  par un réseau de tronçons. Ensuite en clique sur
  <img src="images/image10.PNG"
  style="width:0.90144in;height:0.1875in" />, le résultat est une
  sélection de tous les tronçons entre le premier et le deuxième
  sélectionnés respectant l’algorithme du chemin le plus court. Un
  contrôle visuel est toutefois nécessaire afin de vérifier si les
  tronçons sont bien ceux désirés.

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="modifications-dun-complexe" style="color: white;margin:0;" >6. Modifications d’un complexe</h2>
</div>

- Lors de la sélection d’un tronçon de route, l’interface affiche la
  liste des complexes associés s’ils sont dans l’emprise du projet.

> <img src="images/image3.png"
> style="width:4.1841in;height:1.82153in" />

- On sélectionne le complexe à modifier. La case à cocher passe
  automatiquement à « cochée »

> <img src="images/image11.png"
> style="width:4.19042in;height:1.82428in" />

- Le complexe étant fixé on peut :



- Sélectionner les constituants avec : <img src="images/image6.PNG"
  style="width:1.30208in;height:0.16472in" />

- Ajouter un ou plusieurs tronçon(s) au complexe avec :
  <img src="images/image4.PNG"
  style="width:0.86458in;height:0.1572in" />

- Retirer un ou plusieurs tronçon(s) au complexe avec :
  <img src="images/image5.PNG"
  style="width:0.86458in;height:0.15601in" />


- <span class="mark">Les modifications faites avec l’outil ne seront
  effectives (objets modifiés sur le serveur) que lorsqu’on enregistrera
  les modifications</span> par l’outil natif de QGis (disquette)
  <img src="images/image12.png"
  style="width:0.88041in;height:0.35216in" />

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="a-propos-de" style="color: white;margin:0;" >7. A propos de</h2>
</div>


Accessible via <img src="images/image13.PNG"
style="width:0.23962in;height:0.25003in" />.

<img src="images/image14.png"
style="width:3.50396in;height:4.30844in" />

Cette boite permet de suivre l’évolution des différentes versions ainsi
que d’afficher cette documentation.


