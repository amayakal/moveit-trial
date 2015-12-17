/****************************************************************************
** Meta object code from reading C++ file 'motion_planning_frame.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.6)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../../../../src/moveit_ros/visualization/motion_planning_rviz_plugin/include/moveit/motion_planning_rviz_plugin/motion_planning_frame.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'motion_planning_frame.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.6. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_moveit_rviz_plugin__MotionPlanningFrame[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
      52,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: signature, parameters, type, tag, flags
      41,   40,   40,   40, 0x05,

 // slots: signature, parameters, type, tag, flags
      60,   40,   40,   40, 0x08,
      91,   40,   40,   40, 0x08,
     125,  119,   40,   40, 0x08,
     160,   40,   40,   40, 0x08,
     189,  183,   40,   40, 0x08,
     215,   40,   40,   40, 0x08,
     235,   40,   40,   40, 0x08,
     258,   40,   40,   40, 0x08,
     296,  288,   40,   40, 0x08,
     325,  288,   40,   40, 0x08,
     358,  351,   40,   40, 0x08,
     398,  119,   40,   40, 0x08,
     431,   40,   40,   40, 0x08,
     460,   40,   40,   40, 0x08,
     488,   40,   40,   40, 0x08,
     512,   40,   40,   40, 0x08,
     538,   40,   40,   40, 0x08,
     563,   40,   40,   40, 0x08,
     595,  589,   40,   40, 0x08,
     618,   40,   40,   40, 0x08,
     642,   40,   40,   40, 0x08,
     664,   40,   40,   40, 0x08,
     692,   40,   40,   40, 0x08,
     725,  589,   40,   40, 0x08,
     761,  756,   40,   40, 0x08,
     811,  802,   40,   40, 0x08,
     877,   40,   40,   40, 0x08,
     907,   40,   40,   40, 0x08,
     935,   40,   40,   40, 0x08,
     965,   40,   40,   40, 0x08,
     990,   40,   40,   40, 0x08,
    1017,   40,   40,   40, 0x08,
    1042,   40,   40,   40, 0x08,
    1069,   40,   40,   40, 0x08,
    1096,   40,   40,   40, 0x08,
    1121,   40,   40,   40, 0x08,
    1158, 1146,   40,   40, 0x08,
    1205,   40,   40,   40, 0x08,
    1230,   40,   40,   40, 0x08,
    1260,   40,   40,   40, 0x08,
    1289,   40,   40,   40, 0x08,
    1316,   40,   40,   40, 0x08,
    1343,   40,   40,   40, 0x08,
    1374,   40,   40,   40, 0x08,
    1404,   40,   40,   40, 0x08,
    1433,   40,   40,   40, 0x08,
    1459,   40,   40,   40, 0x08,
    1486,   40,   40,   40, 0x08,
    1518,  756,   40,   40, 0x08,
    1558,   40,   40,   40, 0x08,
    1590,  119,   40,   40, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame[] = {
    "moveit_rviz_plugin::MotionPlanningFrame\0"
    "\0planningFinished()\0databaseConnectButtonClicked()\0"
    "publishSceneButtonClicked()\0index\0"
    "planningAlgorithmIndexChanged(int)\0"
    "resetDbButtonClicked()\0state\0"
    "approximateIKChanged(int)\0planButtonClicked()\0"
    "executeButtonClicked()\0"
    "planAndExecuteButtonClicked()\0checked\0"
    "allowReplanningToggled(bool)\0"
    "allowLookingToggled(bool)\0enable\0"
    "allowExternalProgramCommunication(bool)\0"
    "pathConstraintsIndexChanged(int)\0"
    "useStartStateButtonClicked()\0"
    "useGoalStateButtonClicked()\0"
    "onClearOctomapClicked()\0"
    "importFileButtonClicked()\0"
    "importUrlButtonClicked()\0"
    "clearSceneButtonClicked()\0value\0"
    "sceneScaleChanged(int)\0sceneScaleStartChange()\0"
    "sceneScaleEndChange()\0removeObjectButtonClicked()\0"
    "selectedCollisionObjectChanged()\0"
    "objectPoseValueChanged(double)\0item\0"
    "collisionObjectChanged(QListWidgetItem*)\0"
    "feedback\0"
    "imProcessFeedback(visualization_msgs::InteractiveMarkerFeedback&)\0"
    "copySelectedCollisionObject()\0"
    "exportAsTextButtonClicked()\0"
    "importFromTextButtonClicked()\0"
    "saveSceneButtonClicked()\0"
    "planningSceneItemClicked()\0"
    "saveQueryButtonClicked()\0"
    "deleteSceneButtonClicked()\0"
    "deleteQueryButtonClicked()\0"
    "loadSceneButtonClicked()\0"
    "loadQueryButtonClicked()\0item,column\0"
    "warehouseItemNameChanged(QTreeWidgetItem*,int)\0"
    "loadStateButtonClicked()\0"
    "saveStartStateButtonClicked()\0"
    "saveGoalStateButtonClicked()\0"
    "removeStateButtonClicked()\0"
    "clearStatesButtonClicked()\0"
    "setAsStartStateButtonClicked()\0"
    "setAsGoalStateButtonClicked()\0"
    "detectObjectsButtonClicked()\0"
    "pickObjectButtonClicked()\0"
    "placeObjectButtonClicked()\0"
    "selectedDetectedObjectChanged()\0"
    "detectedObjectChanged(QListWidgetItem*)\0"
    "selectedSupportSurfaceChanged()\0"
    "tabChanged(int)\0"
};

void moveit_rviz_plugin::MotionPlanningFrame::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        MotionPlanningFrame *_t = static_cast<MotionPlanningFrame *>(_o);
        switch (_id) {
        case 0: _t->planningFinished(); break;
        case 1: _t->databaseConnectButtonClicked(); break;
        case 2: _t->publishSceneButtonClicked(); break;
        case 3: _t->planningAlgorithmIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 4: _t->resetDbButtonClicked(); break;
        case 5: _t->approximateIKChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 6: _t->planButtonClicked(); break;
        case 7: _t->executeButtonClicked(); break;
        case 8: _t->planAndExecuteButtonClicked(); break;
        case 9: _t->allowReplanningToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 10: _t->allowLookingToggled((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 11: _t->allowExternalProgramCommunication((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 12: _t->pathConstraintsIndexChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 13: _t->useStartStateButtonClicked(); break;
        case 14: _t->useGoalStateButtonClicked(); break;
        case 15: _t->onClearOctomapClicked(); break;
        case 16: _t->importFileButtonClicked(); break;
        case 17: _t->importUrlButtonClicked(); break;
        case 18: _t->clearSceneButtonClicked(); break;
        case 19: _t->sceneScaleChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        case 20: _t->sceneScaleStartChange(); break;
        case 21: _t->sceneScaleEndChange(); break;
        case 22: _t->removeObjectButtonClicked(); break;
        case 23: _t->selectedCollisionObjectChanged(); break;
        case 24: _t->objectPoseValueChanged((*reinterpret_cast< double(*)>(_a[1]))); break;
        case 25: _t->collisionObjectChanged((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 26: _t->imProcessFeedback((*reinterpret_cast< visualization_msgs::InteractiveMarkerFeedback(*)>(_a[1]))); break;
        case 27: _t->copySelectedCollisionObject(); break;
        case 28: _t->exportAsTextButtonClicked(); break;
        case 29: _t->importFromTextButtonClicked(); break;
        case 30: _t->saveSceneButtonClicked(); break;
        case 31: _t->planningSceneItemClicked(); break;
        case 32: _t->saveQueryButtonClicked(); break;
        case 33: _t->deleteSceneButtonClicked(); break;
        case 34: _t->deleteQueryButtonClicked(); break;
        case 35: _t->loadSceneButtonClicked(); break;
        case 36: _t->loadQueryButtonClicked(); break;
        case 37: _t->warehouseItemNameChanged((*reinterpret_cast< QTreeWidgetItem*(*)>(_a[1])),(*reinterpret_cast< int(*)>(_a[2]))); break;
        case 38: _t->loadStateButtonClicked(); break;
        case 39: _t->saveStartStateButtonClicked(); break;
        case 40: _t->saveGoalStateButtonClicked(); break;
        case 41: _t->removeStateButtonClicked(); break;
        case 42: _t->clearStatesButtonClicked(); break;
        case 43: _t->setAsStartStateButtonClicked(); break;
        case 44: _t->setAsGoalStateButtonClicked(); break;
        case 45: _t->detectObjectsButtonClicked(); break;
        case 46: _t->pickObjectButtonClicked(); break;
        case 47: _t->placeObjectButtonClicked(); break;
        case 48: _t->selectedDetectedObjectChanged(); break;
        case 49: _t->detectedObjectChanged((*reinterpret_cast< QListWidgetItem*(*)>(_a[1]))); break;
        case 50: _t->selectedSupportSurfaceChanged(); break;
        case 51: _t->tabChanged((*reinterpret_cast< int(*)>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData moveit_rviz_plugin::MotionPlanningFrame::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject moveit_rviz_plugin::MotionPlanningFrame::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame,
      qt_meta_data_moveit_rviz_plugin__MotionPlanningFrame, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &moveit_rviz_plugin::MotionPlanningFrame::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *moveit_rviz_plugin::MotionPlanningFrame::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *moveit_rviz_plugin::MotionPlanningFrame::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_moveit_rviz_plugin__MotionPlanningFrame))
        return static_cast<void*>(const_cast< MotionPlanningFrame*>(this));
    return QWidget::qt_metacast(_clname);
}

int moveit_rviz_plugin::MotionPlanningFrame::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 52)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 52;
    }
    return _id;
}

// SIGNAL 0
void moveit_rviz_plugin::MotionPlanningFrame::planningFinished()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}
QT_END_MOC_NAMESPACE
