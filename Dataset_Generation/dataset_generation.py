import pandas as pd
import numpy as np
import pdb
from googletrans import Translator


df = pd.read_csv("gz_recipe.csv")

df2 = df.iloc[: , 1:]

df2 = df2.dropna()

translator = Translator()
pdb.set_trace()


def translate_category(x):
    try:
        translated_text = translator.translate(str(x), dest='en').text
        return translated_text
    except Exception as e:
        print(f"Error translating '{x}': {e}")
        return None

df2['translate_Categoria'] = df2['Categoria'].apply(translate_category)


# df2['translate_Categoria'] = df2['Categoria'].apply(lambda x: translator.translate(x, dest='en').text)

print(df2.translate_Categoria)




