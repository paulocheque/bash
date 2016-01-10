import pytest

from bash.os import *


def test_run():
    run('ls')

def test_wait_for():
    wait_for(1, 1, lambda:None)

def test_read_config_file():
    read_config_file('test.json')

def test_str2bool():
    str2bool('t')

def test_is_mac():
    assert is_mac() == True

def test_is_linux():
    assert is_linux() == False

