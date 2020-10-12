"""
~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~
Don't push these keys to version control.
Set them as environment variables and get
them with the os module.
~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~+~

import os

if os.environ.get("BINANCE_KEY", None) is None:
    raise KeyError(
        "Set BINANCE_KEY on as an environment variable."
    ) from None
else:
    API_KEY = os.environ["BINANCE_KEY"]

if os.environ.get("BINANCE_SECRET", None) is None:
    raise KeyError(
        "Set BINANCE_SECRET on as an environment variable."
    ) from None
else:
    API_SECRET = os.environ["BINANCE_SECRET"]
"""
API_KEY = "k2av5iKzXKDBbtD2TQ9c7jU6LoimCuyw6Hv5Eh51WwxQETqV9xthdeMV70nneJDX"
SECRET_KEY = "BVxDahg0GtqxrysiW3pTMT1zg0z9q9UtpXhk9sfzBnhRPsuiYCk7RhHOtuGrnBaD"
