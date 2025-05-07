from flask import Flask, request, jsonify, render_template
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-xml', methods=['POST'])
def process_xml():
    try:
        xml_data = request.data.decode('utf-8')
        root = ET.fromstring(xml_data)

        result = []
        for elem in root.iter():
            result.append({elem.tag: elem.text})

        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
