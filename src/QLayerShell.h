// Copyright (C) 2016 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

#ifndef QLAYERSHELL_H
#define QLAYERSHELL_H

#include "macros.h"

#include <QObject>
#include <QWindow>
#include <QWidget>
#include <QScreen>
#include <QPainter>
#include <QRasterWindow>
#include <LayerShellQt/Shell>
#include <LayerShellQt/Window>


class BINDINGS_API QLayerShell : public QObject
{
    Q_OBJECT

public:

    enum Anchor {
        AnchorNone = 0,
        AnchorTop = 1, ///< The top edge of the anchor rectangle
        AnchorBottom = 2, ///< The bottom edge of the anchor rectangle
        AnchorLeft = 4, ///< The left edge of the anchor rectangle
        AnchorRight = 8, ///< The right edge of the anchor rectangle
    };
    Q_ENUM(Anchor)
    Q_DECLARE_FLAGS(Anchors, Anchor)

    enum Layer {
        LayerBackground = 0,
        LayerBottom = 1,
        LayerTop = 2,
        LayerOverlay = 3,
    };
    Q_ENUM(Layer)

    enum KeyboardInteractivity {
        KeyboardInteractivityNone = 0,
        KeyboardInteractivityExclusive = 1,
        KeyboardInteractivityOnDemand = 2,
    };
    Q_ENUM(KeyboardInteractivity)

    enum ScreenConfiguration {
        ScreenFromQWindow = 0,
        ScreenFromCompositor = 1,
    };
    Q_ENUM(ScreenConfiguration)

    explicit QLayerShell(QWindow* window, QObject* parent = nullptr);

    void setAnchors(Anchors anchor);
    Anchors anchors() const;

    void setExclusiveZone(int32_t zone);
    int32_t exclusionZone() const;

    void setExclusiveEdge(Anchor edge);
    Anchor exclusiveEdge() const;

    void setMargins(const QMargins& margins);
    QMargins margins() const;

    // void setKeyboardInteractivity(KeyboardInteractivity interactivity);
    // KeyboardInteractivity keyboardInteractivity() const;

    void setLayer(Layer layer);
    Layer layer() const;

    void setScope(const QString& scope);
    QString scope() const;

    static void useLayerShell();


private:
    LayerShellQt::Window* m_shellWindow;

};

#endif