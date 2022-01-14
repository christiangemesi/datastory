#Bevoelkerungswachstum der Schweiz
Team: Christian Gémesi

## Ziel
Mein Ziel ist es das Bevölkerungswachstum der Schweiz zu analysieren:

Bevölkerungswachstum
-Welchen Stadt,Kanton am meisten personen zugezogen bzw am wenigsten.
	in Zahlen

-Trendanalyse:
	in Zahlen

-Grossstädte analysieren (wachstum) -> vielleicht sieht man Trends
	Zürich,Bern,Basel,Genf

-wo leben die meisten Personen, bzw die wenigsten
	Kanton,Stadt

-Entwicklung visualisiert auf Karte, in Relation zu grösse 

## Datenquelle

-Daten von 1850 - 2000 in excel

https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000

## Data Collection

### Data Description - Raw

-Die Daten wurden vom Bundesamt für Statistik BFS gesammelt, zuletzt aktualisiert am 1. November 2005

-Folgende Files liegen vor:
	1. ein fetch_data.py Skript, welches die daten von "https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000" herunterlädt, entpackt und für
	die weiterverarbeitung anpasst. (Bitte zu beachten, dass das Skript bereits ausgeführt wurde, und bei erneutem durchlauf das merged.CSV-File in data\raw gelöscht werden muss.  

- Quellen:
	https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000

Alle CSV-Dateien wurden zusammengemerged.

### Data Description - Preprocessing

Attribute:
	Die Tabelle sieht wie folgt aus: Dabei ist der Kanton ganz Links eingetragen, gefolgt von der Stadt, gefolgt von der Anzahl Personen in dieser Stadt im jeweiligen Jahr
	(oben ersichtlich, z.B. 1850 waren 4657 Personen angemeldet in Aarau)

	Beispiel:
	Kanton	Stadt	1850	1860	1870	1880	1888	1900	1910	1920	1930	1941	1950	1960	1970	1980	1990	2000
	AG	Aarau	4657	5094	5401	5914	6699	7831	9593	10701	11666	12900	14280	17045	16881	15788	16481	15470

	Datentypen liegen wie folgt vor:

	Kanton     object
	Stadt      object
	1850      float64
	1860      float64
	1870      float64
	1880      float64
	1890      float64
	1900      float64
	1910      float64
	1920      float64
	1930      float64
	1940      float64
	1950      float64
	1960      float64
	1970      float64
	1980      float64
	1990      float64
	2000      float64



Wer hat die Daten erhoben?
Christian Gémesi

Wie wurden die Daten erhoben?
Via Downloadlink (genauer bereits oben beschrieben)

Wann wurden die Daten erhoben?

https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000

Gemäss Link am 1. November 2005

Wie viele Datenpunkte (n) wurden erfasst?

Es wurde für jede Stadt in der Schweiz ein Wert für die Jahre von 1850-2000 erhoben
2896 rows × 18 columns

Wurden Attribute präprozessiert? Falls ja, wie?
Daten wurden nicht präprozessiert

Wurden die Daten gefiltert? Falls ja, wie?
Daten wurden nicht gefiltert

Welche Merkmale, Variablen, Attribute wurden erfasst?
Siehe oben unter Data Description - Raw

Was für Dimensionen / Masseinheiten haben die Variablen?

Von was für einem Variablentyp sind die Variablen?

kategorische (nominale) Variablen
-Kanton
-Stadt

quantitiative (kardinale) Variablen
-1850
-1860
-...
-2000




