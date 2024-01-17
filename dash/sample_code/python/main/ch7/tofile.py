import spacy

nlp = spacy.load('en')
doc = nlp(u"In 2011, Google launched Google +, its fourth foray into social networking.")
doc.user_data["title"] = "An example of an entity visualization"
# In the next block, you instruct displaCy to render the markup wrapped as a full HTML page.
from spacy import displacy

html = displacy.render(doc, style='ent', page=True)
# In the next block, you save the html file generated by displacy.render() to disk on your machine.
# Be sure you have /visualizations folder in your file system
from pathlib import Path

output_path = Path("/visualizations/ent_visual.html")
output_path.open("w", encoding="utf-8").write(html)
