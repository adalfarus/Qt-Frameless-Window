"""
PySide6-Frameless-Window
========================
A cross-platform frameless window based on pyside6, support Win32, Linux and macOS.

Documentation is available in the docstrings and
online at https://pyqt-frameless-window.readthedocs.io.

Examples are available at https://github.com/zhiyiYo/PyQt-Frameless-Window/tree/PySide6/examples.

:copyright: (c) 2021 by zhiyiYo.
:license: LGPLv3, see LICENSE for more details.
"""

__version__ = "0.3.12"
__author__ = "zhiyiYo"

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow

from .titlebar import TitleBar, TitleBarButton, SvgTitleBarButton, StandardTitleBar, TitleBarBase

if sys.platform == "win32":
    from .windows import AcrylicWindow as QAcrylicWindow
    from .windows import WindowsFramelessWindow as QFramelessWindow
    from .windows import WindowsFramelessMainWindow as QFramelessMainWindow
    from .windows import WindowsFramelessDialog as QFramelessDialog
    from .windows import WindowsWindowEffect as QWindowEffect
elif sys.platform == "darwin":
    from .mac import AcrylicWindow as QAcrylicWindow
    from .mac import MacFramelessWindow as QFramelessWindow
    from .mac import MacFramelessMainWindow as QFramelessMainWindow
    from .mac import MacFramelessDialog as QFramelessDialog
    from .mac import MacWindowEffect as QWindowEffect
else:
    from .linux import LinuxFramelessWindow as QFramelessWindow
    from .linux import LinuxFramelessMainWindow as QFramelessMainWindow
    from .linux import LinuxFramelessDialog as QFramelessDialog
    from .linux import LinuxWindowEffect as QWindowEffect

    QAcrylicWindow = QFramelessWindow
