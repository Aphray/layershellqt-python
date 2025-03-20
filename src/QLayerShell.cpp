// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

#include "QLayerShell.h"

#include <QtGui/QFontMetrics>
#include <QtGui/QPainter>
#include <QtCore/QTimerEvent>


#define WINDOW_ANCHOR LayerShellQt::Window::Anchor


QLayerShell::QLayerShell(QWidget* widget, QObject* parent): 
    QObject(parent)
{
    // Hackish way of getting QWindow from QWidget: show() ... hide()
    // Might be better to subclass QWindow/QRasterWindow and handle events...
    widget->show();
    widget->hide();

    m_window = widget->windowHandle();
    m_layerShellWindow = LayerShellQt::Window::get(m_window);
}

void QLayerShell::setAnchors(Anchors anchor) {
    m_layerShellWindow->setAnchors((WINDOW_ANCHOR)(int)anchor);
}

QLayerShell::Anchors QLayerShell::anchors() const {
    return (Anchors)(int)m_layerShellWindow->anchors();
}

void QLayerShell::setExclusiveZone(int32_t zone) {
    m_layerShellWindow->setExclusiveZone(zone);
}

int32_t QLayerShell::exclusionZone() const {
    return m_layerShellWindow->exclusionZone();
}

void QLayerShell::setExclusiveEdge(Anchor edge) {
    m_layerShellWindow->setExclusiveEdge((WINDOW_ANCHOR)(int)edge);
}

QLayerShell::Anchor QLayerShell::exclusiveEdge() const {
    return (Anchor)(int)m_layerShellWindow->exclusiveEdge();
}

void QLayerShell::setMargins(const QMargins &margins) {
    m_layerShellWindow->setMargins(margins);
}

QMargins QLayerShell::margins() const {
    return m_layerShellWindow->margins();
}

void QLayerShell::setLayer(Layer layer) {
    m_layerShellWindow->setLayer(
        (LayerShellQt::Window::Layer)(int)layer
    );
}

QLayerShell::Layer QLayerShell::layer() const {
    return (Layer)(int)m_layerShellWindow->layer();
}

void QLayerShell::setScope(const QString& scope) {
    m_layerShellWindow->setScope(scope);
}

QString QLayerShell::scope() const {
    return m_layerShellWindow->scope();
}

void QLayerShell::setScreen(QScreen* screen) {
    m_window->setScreen(screen);
}

QScreen* QLayerShell::screen() const {
    return m_window->screen();
}
