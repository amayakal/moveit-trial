/****************************************************************************
** Meta object code from reading C++ file 'start_screen_widget.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../src/moveit_setup_assistant/src/widgets/start_screen_widget.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'start_screen_widget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_moveit_setup_assistant__StartScreenWidget[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      43,   42,   42,   42, 0x05,
      61,   42,   42,   42, 0x05,

 // slots: signature, parameters, type, tag, flags
      72,   42,   42,   42, 0x08,
      89,   42,   42,   42, 0x08,
     111,   42,   42,   42, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_moveit_setup_assistant__StartScreenWidget[] = {
    "moveit_setup_assistant::StartScreenWidget\0"
    "\0readyToProgress()\0loadRviz()\0"
    "showNewOptions()\0showExistingOptions()\0"
    "loadFilesClick()\0"
};

void moveit_setup_assistant::StartScreenWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        StartScreenWidget *_t = static_cast<StartScreenWidget *>(_o);
        switch (_id) {
        case 0: _t->readyToProgress(); break;
        case 1: _t->loadRviz(); break;
        case 2: _t->showNewOptions(); break;
        case 3: _t->showExistingOptions(); break;
        case 4: _t->loadFilesClick(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData moveit_setup_assistant::StartScreenWidget::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject moveit_setup_assistant::StartScreenWidget::staticMetaObject = {
    { &SetupScreenWidget::staticMetaObject, qt_meta_stringdata_moveit_setup_assistant__StartScreenWidget,
      qt_meta_data_moveit_setup_assistant__StartScreenWidget, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &moveit_setup_assistant::StartScreenWidget::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *moveit_setup_assistant::StartScreenWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *moveit_setup_assistant::StartScreenWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_moveit_setup_assistant__StartScreenWidget))
        return static_cast<void*>(const_cast< StartScreenWidget*>(this));
    return SetupScreenWidget::qt_metacast(_clname);
}

int moveit_setup_assistant::StartScreenWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = SetupScreenWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void moveit_setup_assistant::StartScreenWidget::readyToProgress()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void moveit_setup_assistant::StartScreenWidget::loadRviz()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}
static const uint qt_meta_data_moveit_setup_assistant__SelectModeWidget[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       0,    0, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

       0        // eod
};

static const char qt_meta_stringdata_moveit_setup_assistant__SelectModeWidget[] = {
    "moveit_setup_assistant::SelectModeWidget\0"
};

void moveit_setup_assistant::SelectModeWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    Q_UNUSED(_o);
    Q_UNUSED(_id);
    Q_UNUSED(_c);
    Q_UNUSED(_a);
}

const QMetaObjectExtraData moveit_setup_assistant::SelectModeWidget::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject moveit_setup_assistant::SelectModeWidget::staticMetaObject = {
    { &QFrame::staticMetaObject, qt_meta_stringdata_moveit_setup_assistant__SelectModeWidget,
      qt_meta_data_moveit_setup_assistant__SelectModeWidget, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &moveit_setup_assistant::SelectModeWidget::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *moveit_setup_assistant::SelectModeWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *moveit_setup_assistant::SelectModeWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_moveit_setup_assistant__SelectModeWidget))
        return static_cast<void*>(const_cast< SelectModeWidget*>(this));
    return QFrame::qt_metacast(_clname);
}

int moveit_setup_assistant::SelectModeWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QFrame::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    return _id;
}
QT_END_MOC_NAMESPACE
