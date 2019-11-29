# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import datetime

from tkinter import filedialog
import tkinter as tk
import os

app = Flask(__name__)


def get_folder_path():
    dir_path = "./"
    path = filedialog.askdirectory(initialdir=dir_path)
    print(path)
    return path


# Routing
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dir_folder", methods=["POST"])
def dir_folder():
    path = get_folder_path()
    return render_template("index.html", path=path)


@app.route("/execution", methods=["POST"])
def execution():
    return render_template("index.html", path="未実装です")


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)

