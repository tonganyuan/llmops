from injector import Injector

from internel.router import Router
from internel.server import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
