import enum
from PySide6.QtGui import QScreen
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QWidget

from .QtLayerShell import QLayerShell as QLayerShell_CPP


class QLayerShell(QLayerShell_CPP):
    
    class Anchor(enum.Flag):
        Top = QLayerShell_CPP.Anchor.AnchorTop
        Bottom = QLayerShell_CPP.Anchor.AnchorBottom
        Right = QLayerShell_CPP.Anchor.AnchorRight
        Left = QLayerShell_CPP.Anchor.AnchorLeft
        NoAnchor = QLayerShell_CPP.Anchor.AnchorNone
        
    class Layer(enum.Flag):
        Overlay = QLayerShell_CPP.Layer.LayerOverlay
        Top = QLayerShell_CPP.Layer.LayerTop
        Bottom = QLayerShell_CPP.Layer.LayerBottom
        Background = QLayerShell_CPP.Layer.LayerBackground

    def __init__(
        self, 
        parent: QWidget, 
        scope: str | None = None,
        screen: QScreen | None = None,
        layer: Layer | None = None,
        margins: QMargins | None = None,
        exclusiveZone: int | None = None,
        exclusiveEdge: Anchor | None = None,
    ):
        
        assert isinstance(parent, QWidget) or issubclass(parent, QWidget)
        
        super().__init__(parent)
        
        if scope:
            self.setScope(scope)
        if screen:
            self.setScreen(screen)
        if layer:
            self.setLayer(layer)
        if margins:
            self.setMargins(margins)
        if exclusiveZone:
            self.setExclusiveZone(exclusiveZone)
        if exclusiveEdge:
            self.setExclusiveEdge(exclusiveEdge)
        
    def setScreen(self, screen: QScreen):
        assert isinstance(screen, QScreen)
        super().setScreen(screen)
        
    def setScope(self, scope: str):
        assert isinstance(scope, str)
        super().setScope(scope)
        
    def setLayer(self, layer: Layer):
        assert isinstance(layer, self.Layer)
        super().setLayer(layer.value)
        
    def setExclusiveZone(self, zone: int):
        assert isinstance(zone, int)
        super().setExclusiveZone(zone)
        
    def setExclusiveEdge(self, edge: Anchor):
        assert isinstance(edge, self.Anchor)
        super().setExclusiveEdge(edge.value)
        
    def setMargins(self, margins: QMargins):
        assert isinstance(margins, QMargins)
        super().setMargins(margins)