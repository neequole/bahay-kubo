from flask import Flask


app = Flask(__name__)
app.config.update(
    ENV='development',
    DEBUG=True,
)


@app.route('/')
def hello():
    return 'Excited to see you on PyCon APAC 2019!'


if __name__ == "__main__":
    app.run()
