from dotenv import load_dotenv, find_dotenv
import os
import pytest


def test_fun():
    load_dotenv(find_dotenv("manjesh.env"))
    cname = os.getenv("cname")
    apikey = os.getenv("apikey")
    print(cname)
    print(apikey)
    assert (apikey) == "apikeyfound"
