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
```
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
	-r    Search Russian to Faroese" # riggar ikki heilt, hygg niðanfyri!
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
ord -e instruction # orðið instruction á føroyskum = brúksreglur
ord -E brúksreglur # orðið brúksreglur á enskum = instruction
ord -es instru # finnur orðið instruction og nógv onnur
```
### Leita fo-da og da-fo
```bash
ord -d brugervejledning  # orðið brugervejledning á føroyskum = brúksreglur
ord -D brúksreglur # orðið brúksreglur á donskum = brugervejledning
ord -ds brugerve # finnur orðið brugervejledning og onnur
```
### Leita nøvn
```bash
ord -n hørður # bending av Hørði = Hørð, Hørði, Haðar
```
### Leita øll orð
```bash
ord -Ea vápn # gevur nógv sum td. = vælvápnaður, álopsvápn, óvápnaður í fo-en orðabókini
ord -EA vápn # sama sum -a og meira td. óskaðiligur, ótti, royndarspreinging, ragnarøk í ensku orðabókini
```
### Leita ru-fo
Virkar ikki heilt, tí orðini eru ikki formatera ordiligt
```bash
ord -r Привет # virkar tíanverri IKKI
ord -rs При # virkar og finnur øll orð við hesari byrjan
ord -ra рив # finnur øll orð við рив í sær
ord -rA matur # finnur øll orð við mat í sær
```
