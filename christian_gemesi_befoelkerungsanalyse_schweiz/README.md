
##Bevoelkerungswachstum der Schweiz
Team: Christian Gémesi

## Ziel

Bevölkerungswachstum analysieren

Bevölkerungswachstum
-Welchen Stadt,Kanton am meisten personen zugezogen bzw am wenigsten.
	in Zahlen
	in Prozent

-Trendanalyse:
	in Zahlen
	in Prozent

-Grossstädte analysieren (wachstum) -> vielleicht sieht man Trends
	Zürich,Bern,Basel,Genf

-wo leben die meisten Personen, bzw die wenigsten
	Kanton,Stadt

- Entwicklung visualisiert auf Karte, in Relation zu grösse 

## Datenquelle

-Daten von 1850 - 2000 in excel

https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000

## Data Collection

-Die Daten wurden vom Bundesamt für Statistik BFS gesammelt, zuletzt aktualisiert am 1. November 2005

-Folgende Files liegen vor:
	1. ein fetch_data.py Skript, welches die daten von "https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000" herunterlädt, entpackt und für
	die weiterverarbeitung anpasst. (Bitte zu beachten, dass das Skript bereits ausgeführt wurde, und bei erneutem durchlauf alle CSV-Files erneut erstellt werden. Daher bitte
	zu Erst die Daten in data\raw löschen.) 
	2. CSV-Files der einzelnen Kantone
- Quellen:
	https://opendata.swiss/de/dataset/bevolkerungsentwicklung-der-gemeinden-1850-2000

Data Description - Raw:
	Eine Tabelle sieht wie folgt aus: Dabei ist der Kanton ganz Links eingetragen, gefolgt von der Stadt, gefolgt von der Anzahl Personen in dieser Stadt im jeweiligen Jahr
	(oben ersichtlich, z.B. 1850 waren 4657 Personen angemeldet in Aarau)

	Die CSV-Dateien wurden vorerst nicht zusammengemerged und sind somit pro Kanton abgelegt. Die Spalte Kanton in jedem CSV-File ist somit Redundant. 

	Beispiel:
	Kanton	Stadt	1850	1860	1870	1880	1888	1900	1910	1920	1930	1941	1950	1960	1970	1980	1990	2000
	AG	Aarau	4657	5094	5401	5914	6699	7831	9593	10701	11666	12900	14280	17045	16881	15788	16481	15470

