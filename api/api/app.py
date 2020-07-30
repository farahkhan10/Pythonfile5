from pecan import make_app
from api import model
from api.errors import JSONErrorHook


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=[JSONErrorHook()],
        **app_conf
    )
