from litestar.config.app import AppConfig
from litestar.plugins import InitPluginProtocol

from .controller import Controller


class Plugin(InitPluginProtocol):
    def on_app_init(self, app_config: AppConfig) -> AppConfig:
        app_config.route_handlers.append(Controller)

        return app_config
