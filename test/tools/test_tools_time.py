# coding=utf-8
"""Tools for getting and displaying the time."""
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest

from sopel.tools import time


def test_validate_timezone():
    assert time.validate_timezone('Europe/Paris') == 'Europe/Paris'
    assert time.validate_timezone('America/New York') == 'America/New_York'
    assert time.validate_timezone('Paris, Europe') == 'Europe/Paris'
    assert time.validate_timezone('New York, America') == 'America/New_York'
    assert time.validate_timezone('Israel') == 'Israel'


def test_validate_timezone_none():
    assert time.validate_timezone(None) is None


def test_validate_timezone_invalid():
    with pytest.raises(ValueError):
        time.validate_timezone('Invalid/Timezone')

    with pytest.raises(ValueError):
        time.validate_timezone('Europe Paris')

    with pytest.raises(ValueError):
        time.validate_timezone('Paris/Europe')

    with pytest.raises(ValueError):
        time.validate_timezone('Paris,Europe')


def test_validate_format():
    assert time.validate_format('%Y') == '%Y'
    assert time.validate_format('%Y%m%d') == '%Y%m%d'
    assert time.validate_format('%b %d %Y %H:%M:%S') == '%b %d %Y %H:%M:%S'
    assert time.validate_format('some text') == 'some text'


def test_validate_format_none():
    with pytest.raises(ValueError):
        time.validate_format(None)
