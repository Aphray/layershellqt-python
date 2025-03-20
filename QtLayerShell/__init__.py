__doc__ = 'LayerShellQt python bindings'
__version__ = '0.1.0'


# This try/except is to avoid errors during the metadata fetching process
# by `py-build-cmake`
try:
    from ._qlayershell import QLayerShell
except ImportError as e:
    pass