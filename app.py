from flask import Flask, render_template

app = Flask(__name__)

# Saytda ko'rinadigan kinolar ro'yxati (baza)
# "image" -> static/images/ ichida, "video" -> static/videos/ ichida joylashadi.
# "video" ixtiyoriy: agar mavjud bo'lsa, kartaga sichqoncha olib borilganda
# ovozsiz oldindan ko'rish (preview) sifatida ishga tushadi.
MOVIES = [
    {
        "title": "Betmen",
        "image": "batman.jpg",
        "video": None,
        "trailer_url": "https://www.youtube.com/embed/mqqft22276M",
        "genre": "Boevik",
        "year": 2022,
        "rating": 8.2,
        "description": "Gotham shahrini qamrab olgan jinoyatchilikka qarshi "
                        "yolg'iz kurashayotgan qorong'u qahramon haqida hikoya.",
    },
    {
        "title": "O'rgimchak odam: Yangi kun",
        "image": "spiderman.jpg",
        "video": "spiderman.mp4",
        "trailer_url": "https://www.youtube.com/embed/rk-dF1lFi34",
        "genre": "Animatsiya",
        "year": 2023,
        "rating": 8.7,
        "description": "Multivselenlar orasida yangi qahramon o'z yo'lini "
                        "topishga urinayotgan animatsion sarguzasht.",
    },
    {
        "title": "Dyuna: Ikkinchi qism",
        "image": "dune.jpg",
        "video": None,
        "trailer_url": "https://www.youtube.com/embed/Way9Dexny3w",
        "genre": "Fantastika",
        "year": 2024,
        "rating": 8.9,
        "description": "Pol Atreydes o'ch olish va imperiyaning taqdirini "
                        "hal qilish yo'lida davom etgan sayyoralararo eposning davomi.",
    },
    {
        "title": "Interstellar",
        "image": "interstellar.jpg",
        "video": None,
        "trailer_url": "https://www.youtube.com/embed/zSWdZVtXT7E",
        "genre": "Fantastika",
        "year": 2014,
        "rating": 9.3,
        "description": "Insoniyatni qutqarish uchun galaktikalararo sayohatga "
                        "chiqqan ekipaj haqidagi klassik ilmiy-fantastik film.",
    },
    {
        "title": "Ko'k Zindon",
        "image": "blue_lock.webp",
        "video": None,
        "trailer_url": "https://www.youtube.com/embed/-nxwbNI8-Uc",
        "genre": "Anime",
        "year": 2022,
        "rating": 8.4,
        "description": "Yaponiya terma jamoasi uchun eng shafqatsiz va xudbin "
                        "forvardni tarbiyalash maqsadida yaratilgan maxsus "
                        "'Ko'k Zindon' dasturi haqidagi sport-anime.",
        # Serial bo'lgani uchun qismlar (episodlar) ro'yxati beriladi.
        # Har bir qism uchun "file" — static/videos/ papkasidagi haqiqiy video
        # fayl nomi (masalan: bluelock_ep1.mp4). Shu nomdagi faylni
        # static/videos/ ichiga qo'ying — sayt ularni to'g'ridan-to'g'ri
        # pleyerda ijro etadi (YouTube shart emas).
        "episodes": [
            {"number": 1, "title": "1-qism", "file": "bluelock_ep1.mp4"},
            {"number": 2, "title": "2-qism", "file": "bluelock_ep2.mp4"},
            {"number": 3, "title": "3-qism", "file": "bluelock_ep3.mp4"},
            {"number": 4, "title": "4-qism", "file": "bluelock_ep4.mp4"},
        ],
    },
]


@app.route("/")
def home():
    """Bosh sahifa — barcha kinolar ro'yxatini ko'rsatadi."""
    return render_template("index.html", movies=MOVIES)


if __name__ == "__main__":
    app.run(debug=True)