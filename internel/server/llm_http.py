from flask import Flask

from internel.router import Router


class Http(Flask):

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.register_router(self)
