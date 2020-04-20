#pip install autocorrect
# pip install google-cloud-translate
from flask import Flask, request, render_template, jsonify
from autocorrect import Speller
import wordninja
import time
from google.cloud import translate_v2 as translate
import mysql.connector
import os
import json







os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./GoogleAPICredentials.json"



insert_query = """INSERT INTO cloud_project.preprocess (id, job, original_text, processed_text)
                           VALUES
                           ('{}', '{}', '{}', '{}') """

app = Flask(__name__)




@app.route('/api/spell', methods=['POST','GET'])
def spell():
    if request.method == 'POST':
        id = request.form.get('id')
        id = str(id) + '-' + time.asctime()
        original_text=request.form.get('text')
        spell = Speller()
        corrected_text = spell(original_text)
        query=insert_query.format(id,'spell',original_text,corrected_text)
        db_connection = mysql.connector.connect(host=os.environ["DB_HOST"], database=os.environ["DB_NAME"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        db_connection.close()

        return '''<h3> the corrected text is: {}, (the id is: {} )</h3>'''.format(corrected_text,id)


    return '''<form method = 'POST'>
    id <input type="text" name="id">
    text <input type="text" name="text">
    <input type="submit">
    </form>'''



@app.route('/api/space', methods=['POST','GET'])
def space():
    if request.method == 'POST':
        id = request.form.get('id')
        id = str(id) + '-' + time.asctime()
        original_text=request.form.get('text')


        split_text = wordninja.split(request.form.get('text'))
        corrected_text = str(' '.join(split_text))

        query=insert_query.format(id,'space',original_text,corrected_text)
        db_connection = mysql.connector.connect(host=os.environ["DB_HOST"], database=os.environ["DB_NAME"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        db_connection.close()

        return '''<h3> the corrected text is: {}, (the id is: {} )</h3>'''.format(corrected_text,id)


    return '''<form method = 'POST'>
    id <input type="text" name="id">
    text <input type="text" name="text">
    <input type="submit">
    </form>'''



@app.route('/api/translate', methods=['POST','GET'])
def translate_text():
    translator  = translate.Client()
    if request.method == 'POST':
        id = request.form.get('id')
        id = str(id) + '-' + time.asctime()
        original_text=request.form.get('text')

        corrected_text = translator.translate(request.form.get('text'),target_language="en")['translatedText']

        query=insert_query.format(id,'translate',original_text,corrected_text)
        db_connection = mysql.connector.connect(host=os.environ["DB_HOST"], database=os.environ["DB_NAME"], user=os.environ["DB_USER"], password=os.environ["DB_PASSWORD"])
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        cursor.close()
        db_connection.close()

        return '''<h3> the corrected text is: {}, (the id is: {})</h3>'''.format(corrected_text,id)


    return '''<form method = 'POST'>
    id <input type="text" name="id">
    text <input type="text" name="text">
    <input type="submit">
    </form>'''





if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',debug=True,port=8088)
