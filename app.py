from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import tempfile

from translate_docx import translate_docx


app = Flask(__name__)

@app.route("/", methods=["GET"])
def check():
    return jsonify({"status": "Translation API is running."}), 200

@app.route("/translate", methods=["POST"])
def translate_document():
    '''as translate_docx takes a bit time, we can run this function in celery task'''
    
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file chosen"}), 400

        file = request.files['file']
        source_lang = request.form.get('source_lang')
        target_lang = request.form.get('target_lang')

        if not file or file.filename == '' or not file.filename.endswith('.docx'):
            return jsonify({"error": "No selected file or plese select .docx file"}), 400

        if not source_lang or not target_lang:
            return jsonify({"error": "Missing source_lang or target_lang"}), 400

        filename = secure_filename(file.filename)
        input_path = os.path.join("sample_docs", filename)
        output_path = os.path.join("sample_docs", f"translated_to_{target_lang}_{filename}")
        file.save(input_path)

        translate_docx(input_path, output_path, source_lang, target_lang)

        return send_file(output_path, as_attachment=True, download_name=f"translated_to_{target_lang}_{filename}")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)