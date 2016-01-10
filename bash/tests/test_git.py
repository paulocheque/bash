import pytest

from bash.git import *


def test_autoincrement_tag():
    assert '2' == autoincrement_tag('1')
    assert '1.3' == autoincrement_tag('1.2')
    assert '1.2.4' == autoincrement_tag('1.2.3')

def test_current_git_branch():
    current_git_branch()

def test_last_git_tag():
    last_git_tag()

# def test_create_tag():
#     create_tag()

# def test_auto_create_tag():
#     auto_create_tag()

# def test_reset_tag():
#     reset_tag(tag)

# def test_reset_last_tag():
#     reset_last_tag()
