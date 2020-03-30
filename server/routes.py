import os
from flask import redirect
from .extensions import app, sched
from .jobs import request_gog_data
from .settings import config


@app.route('/api/games')
def games_route():
    """
        Return all games data.
    """
    with open(config.GOG_JSON_PARSED_PATH) as file:
        return file.read(), 200
    return 405


@app.route('/api/jobs/gog/<token>')
def run_job_gog(token):
    """
        Run GOG data request.
    """
    if token == config.JOB_TOKEN:
        sched.add_job(request_gog_data)
        return 'JOB STARTED: Request GOG data.', 202
    return 'Invalid job token', 403


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
        Serve client on all routes.
    """
    with open(os.path.join(config.PUBLIC_DIR, 'index.html'), 'r') as file:
        return file.read(), 200
