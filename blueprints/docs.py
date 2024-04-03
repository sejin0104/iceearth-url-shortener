from flask import Blueprint
from utils import *
from .limiter import limiter
import os

docs = Blueprint("docs", __name__)


@docs.route("/docs/<path:file_path>")
@limiter.exempt
def serve_docs(file_path):
    try:
        if not os.path.exists(f"templates/docs/{file_path}.html"):
            raise FileNotFoundError
        return render_template(f"docs/{file_path}.html", host_url=request.host_url)
    except:
        return (
            render_template(
                "error.html",
                error_code="404",
                error_message="URL NOT FOUND",
                host_url=request.host_url,
            ),
            404,
        )

@docs.route("/legal/privacy-policy")
@limiter.exempt
def serve_privacy_policy():
    return render_template("docs/privacy-policy.html", host_url=request.host_url)
