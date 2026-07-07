from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Saytda ko'rinadigan kinolar ro'yxati (baza)
    movies = [
        {
            "title": "Betmen",
            "image": "batman.jpg",
            "trailer_url": "https://www.youtube.com/embed/mqqft22276M"
        },
        {
            "title": "O'RGIMCHAK ODAM: YANGI KUN",
            "image": "spiderman.jpg",
            "trailer_url": "https://www.youtube.com/embed/rk-dF1lFi34"
        }
    ]
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)