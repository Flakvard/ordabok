# Ordabok
Orðabókin á terminalinum.
## Innihald av orðabøkrum
- fo-fo
- fo-en
- en-fo
- da-fo
- fo-da
- ru-fo
- navnbendingar

## Brúksháttur: 
```bash
Usage: ord [OPTIONS] SEARCH_TERM"
Options:
	      Search Faroese to Faroese (default)"
	-s    Search all words that can match SEARCH_TERM"
	-a    Search all words - regular expression"
	-A    Search all descriptions of words + words - regular expression"
	-e    Search English to Faroese"
	-E    Search Faroese to English"
	-d    Search Danish to Faroese"
	-D    Search Faroese to Danish"
	-r    Search Russian to Faroese"
	-n    Search Names in Faroese"
	-h    Display this help message"
```
## Brúksreglur
### Leita fo-fo
```bash
ord brúksreglur # orðið brúksreglur
```
### Leita fo-en og en-fo
```bash
ord -e instruction # orðið instruction á føroyskum
ord -E brúksreglur # orðið brúksreglur á enskum
ord -es instru # finnur orið instruction og nógv onnur
```
### Leita fo-da og da-fo
```bash
ord -d brugervejledning  # orðið brugervejledning á føroyskum
ord -D brúksreglur # orðið brúksreglur á donskum
ord -ds brugerve # finnur orið brugervejledning og onnur
```
### Leita nøvn
```bash
ord -n hørður # bending av Hørði = Hørð, Hørði, Haðar
```
### Leita øll orð
```bash
ord -Ea vápn # gevur nógv sum td. = vælvápnaður, álopsvápn, óvápnaður
ord -Ea vápn # sama sum -a og meira td. óskaðiligur, ótti, royndarspreinging, ragnarøk
```
