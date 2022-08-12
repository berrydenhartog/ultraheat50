"""Starting flask webserver from cli """
from uh50 import create_app

config = {"DEBUG": False, "SECRET_KEY": "2134sdafnh08b14"}

app = create_app(config)
app.run(host="0.0.0.0")
