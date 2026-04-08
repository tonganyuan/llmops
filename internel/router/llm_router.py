from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internel.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """创建一个蓝图"""
        blueprint = Blueprint("llmops", __name__, url_prefix="")
        """将url与控制器绑定"""
        blueprint.add_url_rule("/ping", view_func=self.app_handler.ping)
        blueprint.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.completion)
        blueprint.add_url_rule("/app/balance", view_func=self.app_handler.balance)

        app.register_blueprint(blueprint)
