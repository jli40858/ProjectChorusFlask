import flask
import werkzeug

app = flask.Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def handle_request():
    files_ids = list(flask.request.files)
    print("\nNumber of Received Files : ", len(files_ids))
    file_num = 1
    for file_id in files_ids:
        print("\nSaving File ", str(file_num), "/", len(files_ids))
        uploaded_file = flask.request.files[file_id]
        filename = werkzeug.utils.secure_filename(uploaded_file.filename)
        print("Filename : " + uploaded_file.filename)
        uploaded_file.save(filename)
        file_num = file_num + 1
    print("\n")
    return "File(s) Uploaded Successfully. Come Back Soon."


app.run(host="0.0.0.0", port=5000, debug=True)
