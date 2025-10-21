import openai
from datetime import date
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


hoy = date.today()


tema = "Estrategias de marketing digital para redes sociales"


prompt = f"""
Generá un post para Instagram sobre {tema}.
Incluí un copy atractivo, hashtags relevantes y una frase final inspiradora.
Fecha: {hoy}.
"""


response = openai.ChatCompletion.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": prompt}]
)


contenido = response["choices"][0]["message"]["content"]


os.makedirs("posts", exist_ok=True)
with open(f"posts/{hoy}.txt", "w", encoding="utf-8") as f:
f.write(contenido)
