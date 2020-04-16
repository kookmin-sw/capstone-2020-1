import functools

from flask import request
from db import Database


def api(f):
    @functools.wraps(f)
    def deco(*args, **kwargs):
        if request.method in ['GET', 'DELETE']:
            data = request.args.to_dict()
        elif request.method in ['POST', 'PUT']:
            data = request.form
        else:
            data = {}
        with Database() as db:
            return f(data, db, *args, **kwargs)

    return deco
