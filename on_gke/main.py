"""
A toy flask app to host on google cloud GKE 

To host locally:
    flask --app main run --port=5000
"""
import logging
import time

import flask

app = flask.Flask(__name__)

# set up python logger #
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@app.route("/system_pause/<nsecs>", methods=["GET"])
def system_pause(nsecs: str) -> flask.Response:
    logger.info("sleeping %s seconds", nsecs)
    time.sleep(int(nsecs))

    return flask.Response("OK", status=200)
