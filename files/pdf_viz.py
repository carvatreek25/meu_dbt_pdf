import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from unidecode import unidecode

# Seu comando do Ghostscript
os.environ['PATH'] += r';C:\Program Files\gs\gs10.06.0\bin'

# Seu arquivo (como o professor fez)
file_name = 'Redrex - Fatura (1)'
path = os.path.abspath(f"meu_dbt_pdf/files/redrex/{file_name}.pdf")

# Usar a variável 'path' no camelot
tables = camelot.read_pdf(
    path,
    pages='1-end',
    flavor='stream',
    table_areas=['65 , 558 , 500 , 298'],
    columns=["65,107,156,212,336,383,450"],
    strip_text='\n'
    )

# Exibe o relatório de acurácia (Parsing Report)
print(tables[0].parsing_report)
print(tables[0].df)

#camelot.plot(tables[0], kind='contour')

#plt.show()

print("Pause")


#python meu_dbt_pdf/files/pdf_viz.py