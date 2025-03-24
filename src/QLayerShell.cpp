// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

#include <iostream>
#include "QLayerShell.h"

#include <QSurfaceFormat>

#define WINDOW_ANCHOR LayerShellQt::Window::Anchor


bool QLayerShell::m_shellInit = false;


QLayerShell::QLayerShell(QWindow* window): 
    QRasterWindow(window)
{

    if (!m_shellInit) {
        m_shellInit = true;
        LayerShellQt::Shell::useLayerShell();
    }

    // Root widget with translucent background
    m_root = new QWidget();
    m_root->setAttribute(Qt::WA_TranslucentBackground);

    QSurfaceFormat format;
    format.setAlphaBufferSize(32);
    format.setBlueBufferSize(32);
    format.setRedBufferSize(32);
    format.setGreenBufferSize(32);
    format.setDepthBufferSize(32);
    format.setRenderableType(QSurfaceFormat::RenderableType::OpenGL);
    setFormat(format);

    m_shellWindow = LayerShellQt::Window::get(this);
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

void QLayerShell::setWidget(QWidget* widget) {
    if (widget) {
        if (m_container) {
            m_container->setParent(nullptr);
        }
        m_container = widget;
        m_container->setParent(m_root);
    }
}

QWidget* QLayerShell::widget() {
    return m_container;
}

void QLayerShell::paintEvent(QPaintEvent* event) {
    QPainter painter(this);
    painter.setRenderHint(QPainter::RenderHint::Antialiasing, true);

    m_root->resize(size());
    m_root->render(&painter, QPoint(0, 0), QRegion(), 
                    QWidget::RenderFlag::DrawChildren);
                    
    painter.end();

    QRasterWindow::paintEvent(event);
}