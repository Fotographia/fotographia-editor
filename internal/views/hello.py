from internal.app import app
from internal.lib.hello import get_hello_message


@app.route("/hello")
def hello():
    hello_message = get_hello_message()
    return hello_message
