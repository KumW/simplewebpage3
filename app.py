from flask import Flask
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure App Service Test</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                margin-top: 100px;
            }}
            .card {{
                background: white;
                padding: 30px;
                width: 600px;
                margin: auto;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Azure App Service</h1>
            <h3>Deployment Successful</h3>
            <p><b>Hostname:</b> {socket.gethostname()}</p>
            <p><b>Time:</b> {datetime.now()}</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()