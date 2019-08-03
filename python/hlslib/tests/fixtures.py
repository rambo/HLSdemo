"""Test fixtures"""
import os.path

import numpy as np
import pytest

import hlslib

COLOR_MAX = 2**16 - 1
RED = np.array((COLOR_MAX, 0, 0), dtype=np.uint16)
GREEN = np.array((0, COLOR_MAX, 0), dtype=np.uint16)
BLUE = np.array((0, 0, COLOR_MAX), dtype=np.uint16)


@pytest.fixture()
def one_big_panel_array():
    """One panel array with big panel"""
    configfile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'panelconfig_singlepanel.txt'
    )
    return hlslib.PanelArray(configfile)


@pytest.fixture()
def multi_panel_array():
    """Multi panel array"""
    configfile = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'panelconfig_multipanel.txt'
    )
    return hlslib.PanelArray(configfile)


def fill_squares(panel_array, side_len=30):
    """Put some base color squares on the array (in-place)"""
    panel_array.pixeldata[-side_len:, -side_len:] = BLUE
    panel_array.pixeldata[-2 * side_len:-side_len, -2 * side_len:-side_len] = GREEN
    panel_array.pixeldata[-3 * side_len:-2 * side_len, -3 * side_len:-2 * side_len] = RED
    panel_array.pixeldata[:side_len, :side_len] = BLUE
    panel_array.pixeldata[side_len:2 * side_len, side_len:2 * side_len] = GREEN
    panel_array.pixeldata[2 * side_len:3 * side_len, 2 * side_len:3 * side_len] = RED
