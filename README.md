# Vitalisync

Vitalisync è un progetto sviluppato per il corso di Editoria Digitale tenuto dal prof Paolo Ceravolo.

L'anteprima del WebBook è disponibile qui: https://filippozuccarini.github.io/vitalisync_site/

## Requisiti

* requests
* beautifulsoup
* mkdocs
* mkdocs-material

## Processo

* usa lo script python `./scripts/source_download.py` per estrarre le fonti in markdown nella cartella `./docs` (modificando il link a ogni iterazione)
* crea il file `./mkdocs.yaml` impostando tema material ed eventuali estensioni
* inserisci i tuoi grafici eCharts in un file javascript dedicato da richiamare in mkdocs.yaml
* inserisci la stringa html necessaria a caricare i grafici nei file di markdown
* esegui da terminale `python3 -m mkdocs serve --dev-addr=0.0.0.0:8000` nella cartella root `./` per visualizzare un'anteprima live
* esegui `mkdocs build` in cartella root `./` per generare la cartella site