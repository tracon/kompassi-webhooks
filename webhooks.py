# encoding: utf-8

from __future__ import unicode_literals, print_function

from functools import wraps
from os import environ

from flask import Flask, Response, request, jsonify


app = Flask(__name__)


TOKEN = environ.get('KOMPASSI_WEBHOOKS_TOKEN', 'secret')


def check_token_authentication():
    payload = request.get_json()
    if not isinstance(payload, dict):
        return False

    return payload.get('token') == TOKEN


def token_authentication_required(controller_function):
    @wraps(controller_function)
    def wrapped(*args, **kwargs):
        if not check_token_authentication():
            return jsonify(
                code=401,
                result='Unauthorized',
                reason='Token missing or wrong. Hint: {"token": "secret"}',
            ), 401

        return controller_function(*args, **kwargs)

    return wrapped


@app.route('/webhooks/ping', methods=['POST'])
@token_authentication_required
def ping():
    """
    This endpoint returns a JSON response and does nothing else. Useful for monitoring.
    """

    return jsonify(
        code=200,
        result='OK',
        message='Pong!',
    )


@app.route('/webhooks/aliases', methods=['POST'])
@token_authentication_required
def update_aliases():
    print("TODO put actual implementation here")

    return jsonify(
        code=200,
        result='OK',
    )


if __name__ == '__main__':
    app.run('0.0.0.0', 33001)
