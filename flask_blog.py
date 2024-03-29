from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Darshan Majithiya',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 3, 2019'
    },
    {
        'author': 'Vandit Mehta',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 4, 2019'
    }
]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html', posts=posts, title='My Blog')
@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True, port=8080)