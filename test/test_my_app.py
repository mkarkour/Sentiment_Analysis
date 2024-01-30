import pytest
from src import my_app 

def test_printing():
    assert my_app.printing() == 'Hello World'