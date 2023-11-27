
import os 
from flask import Flask, render_template, request, redirect, url_for, session,send_from_directory, send_file

app = Flask(__name__)

@app.route('/', methods=['get'])
def index():
    return render_template('ind.html')

@app.route('/download', methods=['GET', 'POST'])
def download():

    return send_file('/home/smaron/Max Raabe - We Will Rock You.mp4', attachment_filename='rocku.mp4')


if __name__ == '__main__':
       app.run()
