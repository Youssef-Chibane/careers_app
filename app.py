#!/usr/bin/python3

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS= [
    {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Florida, USA',
    'salary': '$140,000',
    },
    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': '$130,000',
    },
    {
    'id': 3,
    'title': 'Frontend',
    'location': 'Remote',
    'salary': '$100,000',
    },
    {
    'id': 4,
    'title': 'Backend',
    'location': 'San Francisco, USA',
    'salary': '$120,000',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
