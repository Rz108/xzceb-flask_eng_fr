    french_text=translator.english_to_french(textToTranslate)
    return french_text


@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    english_text=translator.french_to_english(textToTranslate)
    return english_text


@app.route("/")
def renderIndexPage():
    return render_template("result_html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
