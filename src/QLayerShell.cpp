// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

#include <iostream>
#include "QLayerShell.h"

#include <QSurfaceFormat>

#define WINDOW_ANCHOR LayerShellQt::Window::Anchor


QLayerShell::QLayerShell(QWindow* window, QObject* parent): 
    QObject(parent)
{
    m_shellWindow = LayerShellQt::Window::get(window);
}

void QLayerShell::setAnchors(Anchors anchor) {
    m_shellWindow->setAnchors((WINDOW_ANCHOR)(int)anchor);
}

QLayerShell::Anchors QLayerShell::anchors() const {
    return (Anchors)(int)m_shellWindow->anchors();
}

void QLayerShell::setExclusiveZone(int32_t zone) {
    m_shellWindow->setExclusiveZone(zone);
}

int32_t QLayerShell::exclusionZone() const {
    return m_shellWindow->exclusionZone();
}

void QLayerShell::setExclusiveEdge(Anchor edge) {
    m_shellWindow->setExclusiveEdge((WINDOW_ANCHOR)(int)edge);
}

QLayerShell::Anchor QLayerShell::exclusiveEdge() const {
    return (Anchor)(int)m_shellWindow->exclusiveEdge();
}

void QLayerShell::setMargins(const QMargins &margins) {
    m_shellWindow->setMargins(margins);
}

QMargins QLayerShell::margins() const {
    return m_shellWindow->margins();
}

void QLayerShell::setLayer(Layer layer) {
    m_shellWindow->setLayer(
        (LayerShellQt::Window::Layer)(int)layer
    );
}

QLayerShell::Layer QLayerShell::layer() const {
    return (Layer)(int)m_shellWindow->layer();
}

void QLayerShell::setScope(const QString& scope) {
    m_shellWindow->setScope(scope);
}

QString QLayerShell::scope() const {
    return m_shellWindow->scope();
}

void QLayerShell::useLayerShell() {
    LayerShellQt::Shell::useLayerShell();
}