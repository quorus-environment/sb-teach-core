from flask import Blueprint, Response
from flask_cors import cross_origin

image_view = Blueprint('image', __name__, url_prefix="/image")


@image_view.route('/image_proxy', methods=["GET"])
@cross_origin(supports_credentials=True)
def get_image_proxy():
    key = request.args.get('key')
    # get the file from s3
    try:
        file = S3Controller().get_file(key)
    except S3Exception:
        return 'Failed to get file', 500

    # return the file
    return Response(file, mimetype='video/mp4')


@video_view.route('/upload', methods=["POST"])
@cross_origin(supports_credentials=True)
def upload():
    # Get the uploaded file data from the request object
    file = request.files['video']
    # Upload the file to S3
    try:
        S3Controller().upload_video(file)
    except S3Exception:
        return 'Failed to upload video', 500

    return 'File uploaded successfully!', 200


# proxy for videos and images
# unauthorized!!!
@image_view.route('/s3')
@cross_origin(supports_credentials=True)
def s3proxy():
    # get the key from the request
    key = request.args.get('key')
    # get the file from s3
    try:
        file = S3Controller().get_file(key)
    except S3Exception:
        return 'Failed to get file', 500

    # return the file
    return Response(file, mimetype='video/mp4')
