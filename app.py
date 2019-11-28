# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import datetime

app = Flask(__name__)


# Routing
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

