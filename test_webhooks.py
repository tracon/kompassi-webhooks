# encoding: utf-8

import json

import pytest


@pytest.fixture
def app():
    import webhooks
    return webhooks.app.test_client()


def test_root(app):
    resp = app.get('/')
    assert resp.status_code == 404


def test_unauthenticated(app):
    resp = app.post('/webhooks/ping')
    assert resp.status_code == 401


def test_ping(app):
    resp = app.post('/webhooks/ping',
        data=json.dumps(dict(token='secret')),
        headers={'content-type': 'application/json'}
    )
    assert resp.status_code == 200
