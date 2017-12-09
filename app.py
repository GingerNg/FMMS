from daemon.daemon import app
from utils.constants import APP_HOST, APP_PORT, USE_RELOADER


def daemon_entrypoint():
    app.run(host=app.config[APP_HOST], port=app.config[APP_PORT],
            use_reloader=app.config[USE_RELOADER])


if __name__ == '__main__':   # entry
    daemon_entrypoint()
