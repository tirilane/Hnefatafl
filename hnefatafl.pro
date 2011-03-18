TEMPLATE = app
QT = gui core
CONFIG += qt debug warn_on console
DESTDIR = bin
OBJECTS_DIR = build
MOC_DIR = build
UI_DIR = build
FORMS = ui/mainwindow.ui
HEADERS = src/mainwindowimpl.h \
 src/player.h \
 src/piece.h \
 src/board.h \
 src/square.h \
 src/pieceimg.h
SOURCES = src/mainwindowimpl.cpp \
 src/main.cpp \
 src/player.cpp \
 src/piece.cpp \
 src/board.cpp \
 src/square.cpp \
 src/pieceimg.cpp
