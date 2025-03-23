import enum
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QMargins, QPoint, Qt
from PySide6.QtGui import QScreen, QRasterWindow, QPaintEvent, QPainter, QRegion, QSurfaceFormat

from .QtLayerShell import QLayerShell as QLayerShell_CPP


class QLayerShell(QRasterWindow):
    
    __shell_init = False
    
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
        container: QWidget | None = None,
        scope: str | None = None,
        screen: QScreen | None = None,
        layer: Layer | None = None,
        margins: QMargins | None = None,
        exclusiveZone: int | None = None,
        exclusiveEdge: Anchor | None = None,
    ):
        
        assert isinstance(container, QWidget) or issubclass(container, QWidget)
        
        super().__init__()
        
        format = QSurfaceFormat()
        format.setAlphaBufferSize(32)
        format.setBlueBufferSize(32)
        format.setRedBufferSize(32)
        format.setGreenBufferSize(32)
        format.setDepthBufferSize(32)
        format.setRenderableType(QSurfaceFormat.RenderableType.OpenGL)
        self.setFormat(format)
        
        self.__layerShell = QLayerShell_CPP(self)
        
        self.__widget = QWidget()
        self.__widget.setAttribute(Qt.WA_TranslucentBackground)
        self.__container = container if container else QWidget()
        self.__container.setParent(self.__widget)
        
        if not self.__shell_init:
            self.__shell_init = True
            QLayerShell_CPP.useLayerShell()
        
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
        
    # def setScreen(self, screen: QScreen):
    #     assert isinstance(screen, QScreen)
    #     self.__layerShell.setScreen(screen)
        
    def setScope(self, scope: str):
        assert isinstance(scope, str)
        self.__layerShell.setScope(scope)
        
    def setLayer(self, layer: Layer):
        assert isinstance(layer, self.Layer)
        self.__layerShell.setLayer(layer.value)
        
    def setExclusiveZone(self, zone: int):
        assert isinstance(zone, int)
        self.__layerShell.setExclusiveZone(zone)
        
    def setExclusiveEdge(self, edge: Anchor):
        assert isinstance(edge, self.Anchor)
        self.__layerShell.setExclusiveEdge(edge.value)
        
    def setMargins(self, margins: QMargins):
        assert isinstance(margins, QMargins)
        self.__layerShell.setMargins(margins)
        
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        
        self.__widget.resize(self.size())
        self.__widget.render(painter, QPoint(0, 0), QRegion(), 
                             QWidget.RenderFlag.DrawChildren)
        
        painter.end()