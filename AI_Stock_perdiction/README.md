# AI Stock Prediction

Python-project met historische S&P 500-data en candlestick-features.

## Dataset herstellen

De CSV is 143 MB. Daarom is de dataset lossless gecomprimeerd en verdeeld in twee uploadbestanden in `Data/`. Voer dit Python-script uit vanuit `AI_Stock_perdiction`:

```python
from pathlib import Path
from zipfile import ZipFile

archive = Path('Data/SP500_Historical_Data.zip')
with archive.open('wb') as output:
    for part in sorted(Path('Data').glob('SP500_Historical_Data.zip.part*')):
        output.write(part.read_bytes())
with ZipFile(archive) as dataset:
    dataset.extractall('data')
```

Installeer pandas met `python -m pip install pandas` en start `python SRC/data_loader.py` vanuit deze map. De code verwacht de CSV op `data/SP500_Historical_Data.csv` (kleine letters).

De originele Python-bestanden zijn ongewijzigd overgenomen. De lokale `.venv` en caches zijn weggelaten.
