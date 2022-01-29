from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_dict=language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    frenchtext = french_dict.get("translations")[0].get("translation")
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_dict=language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    englishtext=english_dict.get("translations")[0].get("translation")
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    textToTranslate=request.args.get('textToTranslate')
    return render_template("result_html",username=textToTranslate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
