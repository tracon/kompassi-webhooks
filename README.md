# Kompassi WebHooks example

We plan to do updating mailing lists, e-mail aliases etc. via webhooks. This is a rough sample
application for those webhooks.

## Requirements

* Python (3.5 preferred, 2.7 works too)
* `virtualenv` or `venv` recommended
* `pip`

## Getting started

    # one-time setup
    python3 -m venv venv3-webhooks
    source venv3-webhooks/bin/activate
    git clone git@github.com:tracon/kompassi-webhooks
    cd kompassi-webhooks
    pip install -r requirements.txt

    # run tests
    py.test

    # start app
    python webhooks.py

    # try it (in another terminal)
    curl -H 'Content-Type: application/json' -d '{"token": "secret"}' http://localhost:33001/webhooks/ping

When you return to the project in a new terminal, remember to run `python3 -m venv venv3-webhooks`
first.

## License

    The MIT License (MIT)

    Copyright © 2016 Santtu Pajukanta

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
