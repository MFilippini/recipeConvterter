import pdfplumber 

ingredients = ["milk", "flour", "yeast", "sour cream", "sugar", "salt", "eggs", "butter", "chives", "pepper"]

text = ""
with pdfplumber.open("rolls.pdf") as pdf:
   for page in pdf.pages:
      text += (page.extract_text())


# parse ingredients between makes and preparaton

ingList = text.lower().split("makes")[1].split("preparation")[0].split("\n")
ingList.pop(0)
print(ingList)

