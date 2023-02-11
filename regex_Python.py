import re

Mesaj = "J'aime #apprendre, mais je #deteste #l'ecole #"
replacement = r'<a href="">\1</a>'
result = re.sub("(#[\w_0-9']+)", replacement, Mesaj)
print(result)