import os
import openai
import deepl
from flask import Flask, render_template, request

# Create a Translator object providing your DeepL API authentication key
translator = deepl.Translator("996a53f2-ad47-d724-50e9-0619de95e1b1:fx")
openai.api_key = "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"

app = Flask(__name__)

@app.route("/api/ficheproduit", methods=["POST"])
def fiche_produit():
    
    question = request.form['text']
    lenght = request.form['taille']
    question_en = translator.translate_text(question, target_lang="EN-US")
    print(question_en)
    question_complete = "Write a creative description for the following product\n\"\"\"\"\"\"\n" + str(question_en) + "\n\"\"\"\"\"\"\nThis is the description I wrote for an online shop\n\"\"\"\"\"\n"

    response = openai.Completion.create(
    engine="davinci-instruct-beta",
    prompt=question_complete,
    temperature=0.5,
    max_tokens=int(lenght),
    top_p=1,
    frequency_penalty=0.99,
    presence_penalty=0,
    stop=["\"\"\"\"\"\""]
    )
    response_fr = translator.translate_text(response.choices[0].text, target_lang="FR")
    return str(response_fr)


@app.route("/")
def ficheproduit():
    return render_template('ficheproduit.html')

if __name__ == "__main__":
    app.run()