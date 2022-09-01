Chapitre 1 : Etude technique du projet 
1.	Identification des besoins : 
Une application web de supervision s’adaptant aux différents types de machines et systèmes d’exploitation, s’avère la mieux convenante.
2.	Capteurs :
o	Bme280

Le Bme280 est un capteur qui permet de mesurer une température, une pression barométrique et le pourcentage d'humidité. Ce capteur est idéal pour tous les projets climatiques ou environnementaux et très modulable par sa connexion en I2C ou SPI.
Techniquement il est caractérisé par :

![image](https://user-images.githubusercontent.com/83168701/187957586-39f50d28-70a3-4deb-b4f9-55785d016595.png)

→	Tension d’alimentation : 3 à 5V
→	Plage de température : -40 à +85°C           
→	Plage d’humidité : 0-100%
→	Plage de pression : 300-1100 hPa
→	Dimensions : 19.0mm x 18.0mm x 3.0mm
→	Broche VIN : tension d’alimentation     comprise entre 3 et 5V
→	Broche GND : masse 
→	Broche SCL : broche d’horloge du bus I2C
→	Broche SDA : broche de donnée du bus I2C
o	DHT22

Le DHT22 est un capteur numérique de base, à faible coût permettant de mesurer de manière efficace la température et l’humidité de l’air ambiant grâce a sa combinaison deux en un d’un capteur humidité capacitif et d’une thermistance. 
Techniquement il est caractérisé par : 

![image](https://user-images.githubusercontent.com/83168701/187957692-6bc4a6fb-e0e9-45fe-a972-599195803240.png)

→	Tension d’alimentation : 3 à 5V
→	Plage de température : -40 à +80°C
→	Humidité de : 0 à 100% RH
→	Dimension : 15.1*25*7.7mm
→	Broche 1 : tension d’alimentation comprise entre 3 et 5V
→	Broche2 : entrée des données 
→	Broche3 : non connecté 
→	Broche 4 : Masse 

3.	Raspberry Pi :

La Raspberry Pi est un nano-ordinateur à faible coût qui se branche sur un écran d’ordinateur ou un téléviseur avec clavier et souris standard. C'est un petit appareil capable qui permet aux personnes de tous âges d'explorer l'informatique et d'apprendre à programmer dans des langages comme Scratch et Python. 
Techniquement elle est caractérisée par : 

![image](https://user-images.githubusercontent.com/83168701/187957738-6bbb1ef0-0770-4728-b12e-5fff42835dcf.png)

→	Carte mère Raspberry Pi 4
→	Processeur : Broadcom BCM2711, quad-core Cortex-A72 (ARM v8)
 64-bit SoC @ 1.5GHz
→	RAM : 8 Go LPDDR4
→	GPU : VideoCore VI prenant en charge OpenGL ES 3.0, décodage HEVC 4K à 60 i/s
→	Connexion sans fil : Bluetooth 5.0, Wi-Fi 802.11b/g/n/ac
→	Connexion filaire : Gigabit Ethernet (RJ45)
→	Lecteur de carte micro-SD (stockage non fourni)
→	Port caméra CSI pour connecter la caméra Raspberry Pi
→	Port d'affichage DSI pour connecter l'écran tactile Raspberry Pi
→	Audio : AV 3.5 mm
→	Ports : 2 x USB 3.0 / 2 x USB 2.0 / 1 x USB-C (alimentation seulement) / 1 x GPIO 40 pin / 1 x port quadripôle Audio/Vidéo composite / 2 x micro-HDMI
→	Alimentation : 5V DC via un connecteur USB-C (minimum 3A), 5V DC via un en-tête GPIO (minimum 3A), compatible Power over Ethernet (PoE) (nécessite un HAT pour PoE)



4.	Montage circuit et configuration :
o	Raspberry Pi + Bme280 :
•	Configuration de l’interface  I2C :
Avant d’entamer le montage du circuit Raspberry Pi + Bme280 il faut avant tout activer l’interface I2C dans le Raspberry pi :
→	Etape 1 : Activation de l’interface I2C :

      A partir du terminal on commence par exécuter la commande suivante :  Sudo raspi-config 
Cette commande lancera l’utilitaire raspi-config, puis on sélectionne  Interface Options :

 ![image](https://user-images.githubusercontent.com/83168701/187957873-8cad5215-a378-4221-b715-90bb9b8359ff.png)

On active ensuite l’option I2c :

 ![image](https://user-images.githubusercontent.com/83168701/187957922-20185476-3fc4-4ddb-8d0c-7580086d3eed.png)

 Après la Raspberry pi  va se redémarrer et l’interface I2C sera activé.
→	Etape 2 : Installation des utilitaires :

 Pour aider au débogage et permettre à l'interface d'être utilisée dans Python, nous pouvons installer « python-smbus » et « i2c-tools » en exécutant les commandes suivantes :
                            Sudo apt-get update
	                  Sudo apt-get install -y python-smbus i2c-tools 
→	Etape 3 : Arrêt :

Arrêt de la Raspberry Pi en exécutant la commande : Sudo halt 
Puis on attend  dix secondes, On débranche  l'alimentation de la Raspberry Pi et on est  maintenant prêt à connecter notre matériel I2C.
•	Circuit :
Le tableau ci-dessous montre comment le module est connecté à l'en-tête GPIO du Raspberry Pi (P1) :
Broches Bme280	Desc	     Broches en-tête GPIO
VCC	           3.3V	     P1-01
GND	           Masse	    P1-06
SCL 	          I2C SCL	  P1-05
ADD	           I2C SDA	  P1-03
                    
Voici un schéma d'une configuration de maquette. On connecte les quatre broches du module directement au Pi, On aura besoin que de quatre fils femelle-femelle.

 ![image](https://user-images.githubusercontent.com/83168701/187958258-ae99cb9d-ee74-4f20-9f5a-d3eb302dea59.png)
	               
Il nous reste maintenant que de télécharger le script BME280 en exécutant la commande : 
                                  Wget -O bme280.py http://bit.ly/bme280py

o	Raspberry Pi + DHT22 :
•	Circuit :
Le tableau ci-dessous montre comment le module est connecté à l'en-tête GPIO du Raspberry Pi :




Broche DHT22 	Broches en-tête GPIO
Pin           1	3v3
Pin2         	GPIO4
Pin4	         GND

Sans oubliant une résistance de 10K entre Pin1 et Pin2 du capteur DHT22.
 
![image](https://user-images.githubusercontent.com/83168701/187958392-78c19b26-1ea0-4dc7-9e4e-67fd92f9d186.png)

•	Installation de la bibliothèque Adafruit  DHT :
Avant notre code python, On doit télécharger et installer la bibliothèque DHT dans notre Raspberry Pi. Dans le terminal on exécute les commandes suivantes : 
                              Git clone https://github.com/adafruit/Adafruit_Python_DHT.git
		    Cd Adafruit_Python_DHT
		    Sudo apt-get update
                              Sudo apt-get install build essential python-dev 
                              Sudo python setup.py install  
Il nous reste maintenant qu’à redémarrer notre Raspberry  afin de récupérer le pilote Adafruit  .



Chapitre 2 : Déroulement du projet :
  Partie 1 : Partie préparation et création 
1.	Préparation de l’environnement sous Raspbian : 
o	Installation de Apache web server :
Apache est un des serveurs web les plus populaires disponibles pour la Raspberry Pi, il peut servir des fichier HTML via les protocoles Web HTTP et HTTPS. 
Avant d’installer Apache sur notre Raspberry Pi, nous devons d’abord nous assurer que la liste des packages est à jour en exécutant les deux commandes suivantes : 
			Sudo apt-get update
			Sudo apt-get upgrade 
Maintenant on peut entamer l’installation d’apache2 avec la commande suivante :
			Sudo apt install apache2 -y
Il nous reste qu’ajouter l’utilisateur pi au groupe www-data, puis donner la possession de tous les fichiers et  dossiers du répertoire /var/www/html au groupe www-data à travers les deux commandes suivantes :
			Sudo usermod -a -G www-data   pi
			Sudo chown -R -f www-data  /var/www/html
o	Mise en place de PHP :
PHP est un des langages les plus utilisés pour crée des sites dynamiques. La manière la plus classique et la plus simple d’installer PHP est de l’installer sous forme d’un module Apache. Pour cela, il suffit d’installer le module libapache2-mod-php :
Sudo apt install php7.3 libapache2-mod-php7.3 php7.3-mbstring php7.3-mysql php7.3-curl php7.3-gd php7.3-zip -y	
Maintenant après l’exécution de cette commande, PHP est installé sur notre Raspberry PI
o	Mise en place de MySQL :
MySQL est l’un des systèmes de gestion base de données relationnelles les plus populaires au monde qui permet de stocker et de gérer facilement de grandes quantités de données. C’est  l’une des technologies qui aident à piloter le WEB moderne.
Avant de commencer à installer MySQL sur notre Raspberry Pi, nous devons d’abord mettre à jour notre liste de packages et tous les packages installés. En exécutant les deux commandes suivantes : 
Sudo apt-get update
			Sudo apt-get upgrade 
L’etape suivante consiste à installer le logiciel du serveur MySQL sur notre Raspberry Pi en effectuant la commande suivante :  sudo apt install mariadb-server
Nous devrons maintenant lancer le processus de sécurisation MySQL : 
Sudo mysql_secure_installation 
o	Mise en place de PHPMYADMIN :
PHPMYADMIN est un outil qui a été conçu pour permettre une administration facile de MySQL.
Pour installer le package PHPMYADMIN sur notre Raspberry Pi, nous devons exécuter la commande suivante :  sudo apt install phpmyadmin  
Une fois le processus d’installation de PHPMYADMIN terminé , il reste a crée un nouvel utilisateur afin d’acceder à des tables de données dans PHPMYADMIN . Pour ce la nous devrons nous connecter a l’interface de ligne de commande MySQL en utilisant l’utilisateur « root » : sudo mysql -u root -p
Puis on execute la commande suivante : GRANT ALL PRIVILEGES ON *.* TO ‘username ‘@ ‘localhost’ IDENTIFIED BY ‘password’ WITH GRANT OPTION ; 
→	Configuration d’Apache pour PHPMYADMIN :

Avant de pouvoir charger l’interface PHPMYADMIN sur notre Raspberry Pi, nous devons apporter quelques modifications à la configuration d’Apache.
Pour commencer nous devons éditer le fichier « Apache2.conf » :
 sudo nano /etc/apache2/apache2.conf 
	Puis nous devons ajouter la ligne suivante au bas de ce fichier : 
Include /etc/phpmyadmin/apache.conf 
	Et finallement redemarer le service Apacher sur notre Raspberry Pi : 
sudo service apache2 restart 

 ![image](https://user-images.githubusercontent.com/83168701/187958769-bbd96c06-cb27-4fc7-80f7-9a859647e8cc.png)
 ![image](https://user-images.githubusercontent.com/83168701/187958821-2efc4cd3-97a4-46ca-93aa-da02c6d89c88.png)


o	Installation de Python :
Python est un langage de programmation interprété, multi-paradigme et multiplateformes. Il favorise  la programmation impérative structurée,fonctionnelle et orientée objet. Pour installer Python il faut executer les commandes suivantes :
	sudo apt-get update 
	sudo apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
→	Configurer un environement virtuel Python :
L’environement virtuel Python est un environement qui permet de separe un projet  des outils du système et de tout autre projet Python sur lequel nous pourrions travailler.
Nous devons installer la virtualenv commande pour créer ces environements . Nous pouvons obtenir ceci en utilisant pip : sudo pip3 install virtualenv
2.	Création d’un projet Django : 
o	Configuration de l’environnement virtuel :
Une fois virtualenv est installé , nous pouvons commencer à former notre projet .Pour commencer on doit crée un repertoire dans lequel on souhaite conserver notre projet : 
pi@raspberrypi:~/Desktop $  mkdir meteo
Puis on ce deplace dans le repertoire afin de crée un environnement virtuel Python :
pi@raspberrypi:~/Desktop $  cd meteo
pi@raspberrypi:~/Desktop/meteo $  virtualenv myenv
 
Il nous reste qu’ installer Django dans notre environnement , mais avant tout il faut activer l’environnement virtuel en executant : 
pi@raspberrypi:~/Desktop/meteo $  source myenv/bin/activate

o	Installation de Django et Configuration du projet :
Après la configuration de l’environnement virtuel de notre projet il nous reste qu’installer Django : 
(myenv) pi@raspberrypi:~/Desktop/meteo $  pip3 install django
Maintenant tout est pres , il nous faut que crée notre projet Django avec la commande suivante :
(myenv) pi@raspberrypi:~/Desktop/meteo $  django-admin.py startproject meteo
Apres la creation de notre projet Django , on ajuste les parametres dans le fichier settings.py :
-	On commance par saisir les adresses autorisées dans la ligne 29 du fichier :
-	En bad du fichier , on ajoute une ligne pour la configuration du repertoire static de notre projet sans oublier «  import os » en haut du fichier : 

 
  Partie  2: Partie réalisation et commandes 
1.	Création de l’application MeteoApp : 
Maintenant apres la configuration de notre environnement virtuel et de notre projet Django il nous reste la creation de notre application MeteoApp pour cela on execute la commande suivante : 
 (myenv) pi@raspberrypi:~/Desktop/meteo/meteo $  python3 manage.py startapp MeteoApp
Sans oubliant la creation des deux repertoires static et templates .
 

2.	Création de la bdd meteo (models+migration) :
Afin de stocker les valeurs récupères  des capteurs on doit crée un base de donées pour notre projet :

-	Django CRUD :

Une fois le projet créé, on modifie les paramètres dans ‘settings.py’. Django est configuré pour utiliser SQLite par défaut, mais comme on utilise MySQL, on doit configurer le type de base de données.

Et en utilisant la migration, on obtient les tables dans notre base de données  en executant la commande suivante : (python3 manage.py makemigrations & python3 manage.py migrate).

 ![image](https://user-images.githubusercontent.com/83168701/187959250-04450176-db24-4bc5-a540-c361e9927847.png)

3.	Script du capteur DHT22 :

o	Récupération des valeurs : 
On a deux types de valeurs, valeurs mesurer et calculer ces dernier on les recuperes a traver une boucle dans un script python ou on import les bibliotheques des capteurs bme280 et Adafruit_DHT du capteur dht22 , la bibliotheque datetime afin d’inserer la date et temps actuelle des valeurs mesurées sans oublier aussi la bibliotheque math qu’on utilisera lors du calcul des valeurs .
 
o	Insertion dans la bdd :
L’insertion des valeurs mesurées et calculées se fait aussi a traver le meme script python , premierement on doit importer mysql connector afin de lier et connecter notre base de donnée a notre script puis on implemente une fonction insertIntoDatabase dans la quelle on se connecte a notre base de donée et on prepare notre sql requette qui s’exutera lors de l’execution de la fonction insertIntoDatabase
 

o	Sélection et insertion des maxs et mins :
Pour la sélection et l’insertion elle se fait aussi a travers les fonctions max et min dans notre script , dans ces fonctions on se connecte a notre base de donée et on prepare notre sql requette qui s’exutera lors de l’execution des fonctions .
Example fonction max_temp() et min_temp() :
 

Meme structure pour les fonctiosn max_hum , min_hum , max_pres et min_pres .
L’execution de se script se fera automatiquement par la commande crontab -e  : 
   


4.	Urls et Views :
o	Ajout des views : 

-	valeurs-page :
 
Dans cette fonction on récupère la dernière ligne de notre base de données meteo (last_values), dernières valeurs max et min de temperature , humidite et pression afin de les afficher dans notre template « valeurs.html ».

-	 view d’ historiques :

Pour les pages d’historiques , on récupère la dernière valeur instantanée (last_val) , max et min de chaque historique , toutes les valeurs de la base de donée (date,time et la valeur de la page) order  by « -id » , un filtre pour filtrer les valeures  et labels et data pour notre chart 
      
-	view message  :
Pour les pages de messages , on récupère seulement la dernière ligne des  valeurs instantanées de notre base de donnée meteo (last_values).
Example metar_page ( meme structure pour synop_page ) 


 
  Partie 3 : Interfaces 
1.	Valeurs Instantanées :
 
![image](https://user-images.githubusercontent.com/83168701/187959532-8590b7bd-825f-4d76-a70a-9545660d15ea.png)

![image](https://user-images.githubusercontent.com/83168701/187959539-549ca11b-a829-4cac-8ad1-8005f91050e2.png)

 La page d’accueil (valeurs instantanées) de notre application web se compose de :
-  Une nav bar a gauche qui permet a l’utilisateur de passer d’une page a une autre par un simple clique
- L’entete de la page ( Valeurs instantanées de +date +time de la recuperation des valeurs ) 
- Un div qui contient l’affichage des valeurs instantanées 
- Un div qui contient une horloge 
- Un div qui contient l’affichage des valeurs mins et maxs  
- Footer 
2.	Historique : « Example température  , même structure pour les autres pages de l’historique »

 ![image](https://user-images.githubusercontent.com/83168701/187959590-7176ae00-b5a5-49d5-a482-a735779157df.png)

 ![image](https://user-images.githubusercontent.com/83168701/187959610-835aa052-d6d8-46f4-9def-065eec11642b.png)

Les pages d’historiques de notre application web visualise les anciennes valeurs en fonction du temps et date . C’est pages ce compose de :
-	Graffe d’evolution des valeurs en fonction de datetime 
-	Filtre des valeurs du tableau en fonction de la date
-	Tableau des anciennes valeurs 
3.	Message : « Example metar  , même structure pour les autres pages de l’historique »
 
![image](https://user-images.githubusercontent.com/83168701/187959650-8081b2cd-7ce6-4a60-b5a7-832375a00c19.png)
![image](https://user-images.githubusercontent.com/83168701/187959681-d06e2462-5391-41bb-86d8-438ddaa47f43.png)

Les pages messages de notre application web permettent d’envoyer un message spécifique par FTP , ce message est recupere en cliquant sur le button donnée qui declenche en fonction par methode onclick cette dernière remplit l’innerText de la page par les données recuperer de notre base de donnée










 
