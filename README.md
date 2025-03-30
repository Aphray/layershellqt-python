qtlayershell-python
-
Python wrapper for the [LayerShellQt](https://github.com/KDE/layer-shell-qt) library for creating shell windows/layers in Wayland-based compositors.

This module uses CMake and Shiboken to build a python wrapper for the LayerShellQt C++ bindings.

**This module is only intended for Linux systems!**

Build dependencies:
--
- CMake
- Ninja
- PySide6
- LayerShellQt
- Shiboken6
- py-build-cmake

Building
-
**It is highly recommended to install this module within a python virtualenv, as to not collide with system-wide packages.** 
```
python -m venv qtlayershell-env (or some other name)
source qtlayershell-env/bin/activate
```


To build the bindings, you will need to install PySide6 and Shiboken6 from the Qt official releases (**the PySide6/Shiboken6 distributions on pypi likely won't work**). py-build-cmake can be install from pypi:
```
pip install --index-url=http://download.qt.io/official_releases/QtForPython/ --trusted-host download.qt.io shiboken6 pyside6 shiboken6_generator

pip install py-build-cmake
```
Clone this repository:
```
git clone https://github.com/Aphray/layershellqt-python.git qtlayershell-python
```
Build and install the bindings. **NOTE: `--no-build-isolation` flag is required for proper references to the PySide6 libraries!**
```
cd qtlayershell-python
pip install . --no-build-isolation
```
Using the bindings
-
To use the bindings:
```python
import sys
from QtLayerShell import QLayerShell
from PySide6.QtWidgets import QWidget, QApplication


app = QApplication(sys.argv)

widget = QWidget()
shell = QLayerShell(widget)

shell.show()

sys.exit(app.exec())
```
See the `examples` folder for a more detailed usage case.
