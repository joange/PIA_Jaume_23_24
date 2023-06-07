# 1. Preparant l'Entorn en Python

Abans de començar a programar en Python hem de preparar la nostra màquina per a tal tasca. Està clar que podem tenir un superordenador i instal·lar tot al complet, però al poc de temps ens adoanrem que perdrem el control del que tenim. Varies versions dels intèrprets de Python (2 o 3) i dins de la 3, 3.7, 3.9, etc... Ademés tenim tota la col·lecció de llibreries que podem instal·lar amb `pip` per a fer-les servir al nostre programa. Espai i més espai.. versions i més versions.

Per a evitar aquestes instal·lacions massives de incloure-ho tot, ens ajuden els gestors de dependències, com els que ja coneixereu `Maven`, `Ant`, `Gradle` per a `Java`, per exemple el _Node Package Manager_ de `node.js`. Els gestors de dependencies ens permeten crear una mena d'entorns aïllats on podem indicar quines llibreries i dependències ens calen per al nostre projecte. Aquestes llibreries no depenen del sistema anfitrió, i a més a més, permeten una exportació fàcil, ja que no hem de copiar ni d'exportar les llibreries, ja que al destí s'agafaran de nou.

Dins de python, cada entorn de treball aïllat és coneix com a _entorn virtual_, i els sistema que ens permet gestionar-lo s'anomena `conda`.

> No confondre amb `pip` (package installer for Python). `pip` ens permet instal·lar nous paquets (llibreries) de python, i aquestes s'instal·len de manera global (a la nostra màquina). Si estem dins d'un entorn virtual, i instal·lem qualssevol llibreria, aquesta s'instal·la dins de l'entorn.

En resum, els entorns virtuals ens permeten:

- Organitzar i tindre millor controlades totes les llibreries
- Estabilitat, ja que sempre tenim la llibreria exacta del nostre entorn i no la de la màquina real
- Version distintes 

!!! Success "Atenció"
    Recomanem per tant, crear un entorn virtual per a cadascun dels projectes que desenvoluparem.



## Python Anaconda vs Miniconda

Un  paquet que gestiona tant les dependències com l'entorn és conda. Podem instalar `miniconda` per a una instal·lació mínima o `Anaconda` per a una més completa, al voltant de 3GB de llibreries. Podeu seguir la discussió ací [miniconda vs anaconda](https://conda.io/projects/conda/en/latest/user-guide/install/download.html#anaconda-or-miniconda)

!!! tip "Consell"
    Recomanem `miniconda` per tindre sols el que necessitem i no arrastrar tantes llibreries al nostre sistema. En cada projecte afegirem el que necessitem.

Un cop instal·lat al teu sistema amfitrió seguint els passos que pots trobar (ací)[https://conda.io/projects/conda/en/stable/user-guide/install/index.html].

Per defefcte a partir d'ara, al obrir una terminal, estarem dins d'un entor, anomenat `base`. Si volem eixir d'ell hem d'executar `conda deactivate`

Si vols habilitar estar o no dins d'un entorn quan obrim una terminal, has de fer:

- `conda config --set auto_activate_base false`
- `conda config --set auto_activate_base true`

Per a crear un entorn , has d'executar:

```sh
conda create -n entorn python=x.x
```

!!! note
    La primera vegada descarregarrà els paquets bàsics de python, que encara no els tindria

amb `conda env list` podrem veure els entorns que tenim, i entrar al nou que hem creat amb `conda activate entorn`.

Per afegir nous paquets al entorn, `conda install nom_paquet`.

Per 

## 1.1. Estructura d’un programa en `Python`

Un programa en `Python` te una estructura molt simple, si ho comparm en altres llenguatges de programació; simplement hem d'escriure les nostres linies de codi i ja està, però pot tenir més coses

Qualsevol programa escrit en `Python` té la següent estructura:
```
[Descripció del programa]
[Directives]
[Importació de Libreria]
[Definició de classes]
[Funcions]
Entrada de dades
Processament de dades
Sortidad de dades
```


Els claudàtors indiquen que eixos apartats són opcionals. Per tant, veiem que l’única part necessària en un programa és l'entrada, el processament i la sortida de dades, com en qualssevol algorisme. Notar que en `Python` tots aquests poden canviar la posició. Vejam uns exemples i els analitzem.

El més simple, mostra un missatge per pantalla:

```Python
print("Hola món")
```
Altre una mica més complet:

```Python
# Programa que calcula el area de un rectangle
# Autor: Joan Gerard Camarena
# Data : 2019/07/11
import time

def areaRectangle(base,altura):
    return base*altura

base=int(input("Dis-me la base del rectangle: "))
altura=int(input("Dis-me l'altura del rectangle: "))
time.sleep(2)   # Espera dos segons

area=areaRectangle(base,altura)

print("L'area del rectangle és " + str(area))
```

Comentaris:

- Les 3 primeres línies sob una descripció del que fa el programa. Son comentaris, que no s'executen
- Al `import` indiquem que necessitem una llibreria. Això es veurà més endavant, però les llibreries són un conjunt de funcions que ja venen implementades i les podem fer servir als nostres programes. La funció que farem servir és `time.sleep()` que fa que el programa es pause durant una quantitat de segons.
- Desprès tenin la definició d'una funció, que comença amb la paraula reservada `def`. Notar que tot el que pertany a la funció està indentat una tabulació (al nostre cas sols la instrucció del `return`).
- Desprès ja tenim el nostre programa pròpiament dit:
  - Les línies no tenen cap indentació (pegades a l'esquerre)
  - La primera part és la que l'algorisme ha d'aconseguir la informació. En aquest cas a preguntem a l'usuari mitjançant `input`. 
  - La segona part  és el fer el càlcul. Pot veure's que es crida a la funció que hem definit anteriorment
  - Finalment mostrem a l'usuari el resultat (`print`).


## 1.2. Noms i paraules reservades en `Python`

Nosaltres per a programar, com hem vist abans, li hem posat nom a les variables i funcions. Per a posar nom a les variables hem de complir unes regles, que tenen tots els llenguatges de programació:

1. Són una combinació de lletres minúscules [a..z], majúscules [A..Z], dígits [0..9] i el caràcter subratllat[_]. 
2. No poden començar amb dígit.
3. Poden contenir accents i altes caràcters (ñ,ç,...)
4. No poden ser paraules reservades o `keywords` del sistema (veure taula a continuació)
5. No poden haver símbols especials ni operadors [!, @, #, $, %, ...] etc. 
6. Poden tenir qualssevol longitud

Paraules reservades:
||||||
|:-:|:-:|:-:|:-:|:-:|
|False|	class|	finally|	is|	return|
|None|	continue|	for	|lambda	|try|
|True|	def|	from|	nonlocal|	while|
|and|	del	|global|	not|	with|
|as|	elif|	if|	or|	yield|
|assert|	else|	import|	pass| |	 
|break	|except	|in	|raise	||

Existeixen algunes més, com els tipus de dades (`int`, `float`, `str`, `complex`, etc). La facilitat és que els editors ens colorejen les paraules reservades, llavors sabrem que no les podem utilitzar per als nostres identificadors.


Les variables són els llocs on es guarda la informació. Poden ser de distints tipus, segons el lloc on es fan servir i des d'on es poden accedir. Una primera distinció és entre globals i locals:

- Les globals són aquelles que es creen fora de qualssevol funció i, per tant, són accessibles des de qualsevol punt del fitxer o programa.
- Les locals són les que es creen dins d’alguna funció i, per tant, només són accessibles des de les instruccions de dins d’eixa funció. Dins de una funció es pot accedir a les variables locals seues, així com a les variables globals
- Les variables de classe són com les variables locals a les funcions. S'estudiaràn dins de la POO

## 1.3. Comentaris

Els comentaris, com ja s'ha dit abans, són sentències les quals no s'executen, però serveixen per a poder entrendre i recordar què voliem fer dins del nostre codi. Si escrivim un codi, i el tornem a revisar al cap d'unes setmanes, segur que no recordem certes coses. L'ús de comentaris ens ajudarà a recordar.

També servieix quan altre programador ens revisa el nostre codi poder entrendre el que voliem fer.

### 1.3.1. Tipus de comentaris

- D'una línia, venen precedits pel caràcter coixinet `#`
- De més d'una línia, quan tanquem diverses línies entre dos parelles de tres cometes simples `'''`
- De documentació _docstring_, són una línia o línies de text intercalades  al principi d'un mòdul, mètode, classe o funció. Pot ser:
  
  - Línia simple: com per exemple `'Documentació.'`
  - Línia múltiple: tancada entre tres parelles de cometes dobles `"""`

```python
'''
Programa que calcula el area de un rectangle
Autor: Joan Gerard Camarena
Data : 2019/07/11
'''
import time
# declarem una funció
def areaRectangle(base,altura):
    """
    Aquest funció calcula el àrea d'un rectangle
    Paràmetres:
        base -> La base del rectangle
        altura -> La altura del rectangel
    Errors: 
        No implentat
    """
    return base*altura

def areaQuadrat(base):
    'Calcula el area  de un quadrat de costat pasat.'
    return base*altura

#demanem les dades a l'usuari
base=int(input("Dis-me la base del rectangle: "))
altura=int(input("Dis-me l'altura del rectangle: "))
time.sleep(2)   # Espera dos segons

area=areaRectangle(base,altura)
#mostrem el resultat
print("L'area del rectangle és " + str(area))
```

## 1.4. Delimitadors

Són símbols especials que permeten al compilador separar i reconéixer les diferents unitats sintàctiques del llenguatge. En molts llenguatges de programació es fa servir un `;` (`C` i  en `Java` ) com  a finalitzador, però `Python` fa servir el bot de línia. De tota manera indiquem els més habituals per a tots els llenguatges.


|DELIMITADOR | NOM	|UTILITAT|
|:-:|:-:|:-:|
|;|	Finalitzador|	Finalitzar una instrucció simple o una declaració d’objectes|
|,|	Separador	|Separar els elements d’una llista|
|( )|	Parèntesis	|Agrupar operacions i per als paràmetres de les funcions|
|{ }|	Claus	|Delimitar l’inici i fi d’un bloc de codi|
|[ ]|	Claudàtors|	Per als vectors. llistes i demés|





