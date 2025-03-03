from flask import Flask, request, send_file

from src.service.PptService import PptService

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ppt',methods=['POST','GET'])
def debug_demo( ):
   body=request.json
   p=PptService(body['words'])
   filePath=p.gernatePptFile()
   return  filePath;

@app.route('/download/<filename>')
def download_ppt(filename):
    file_path = f"doc/{filename}"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009)
