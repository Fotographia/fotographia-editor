from internal.app import app
import os

PORT = os.getenv("PORT")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
