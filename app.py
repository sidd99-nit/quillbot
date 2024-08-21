from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['left_text']
        text = text.replace('\n', ' ').replace('\r', ' ')
        # Split text into sentences at full stops, strip extra spaces, and remove empty sentences
        sentences = [sentence.strip() for sentence in text.split('.') if sentence.strip()]
        # Convert each sentence to a bullet point with a full stop at the end
        bullet_points = [f'• {sentence}.\n' for sentence in sentences]
        bullet_text = '\n'.join(bullet_points)
        return render_template('index.html', left_text=text, right_text=bullet_text)
    return render_template('index.html', left_text='', right_text='')

if __name__ == '__main__':
    app.run(debug=True)
