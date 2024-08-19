from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)

# @app.route('/'): This is a route decorator that maps the URL path '/' to the index function. This means that when a user accesses the root URL (e.g., http://localhost:5000/), the index function will be called
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/analyze', methods=['GET', 'POST'])
# def analyze():
#     if request.method == 'POST':
#         rawtext = request.form['rawtext']
#         summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)
#         return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)

# if __name__ == "__main__": This condition ensures that the Flask application runs only if the script is executed directly, not when it is imported as a module.
if __name__ == "__main__":
    app.run(debug=True)


