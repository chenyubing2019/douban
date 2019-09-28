import flask
import os
app = flask.Flask(__name__)
app.config["UPLOAD_FOLDER"]="C:\\Users\\Administrator\\Desktop\\各种方法\\file_share\\templates\\uploaded_files"

@app.route("/")
def home():
    return flask.render_template("file_upload.html")

@app.route("/file_upload",methods=["POST"])
def file_upload():
    uploaded_file = flask.request.files["dj"]
    file_name = uploaded_file.filename
    file_path=os.path.join(app.config["UPLOAD_FOLDER"],file_name)
    uploaded_file.save(file_path)
    return flask.redirect(flask.url_for("download"))

@app.route("/download")
def download():
    file_names=os.listdir(app.config["UPLOAD_FOLDER"])
    return flask.render_template("download.html",file_names=file_names)

@app.route("/download/<file_name>")
def download_file(file_name):
    return flask.send_from_directory(app.config["UPLOAD_FOLDER"],file_name)

if __name__=="__main__":
    app.run(port=80, debug=True)

