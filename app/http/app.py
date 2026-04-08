import dotenv
from injector import Injector

from config import Config
from internel.router import Router
from internel.server import Http

dotenv.load_dotenv()
injector = Injector()
config = Config()

app = Http(__name__, config=config, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
