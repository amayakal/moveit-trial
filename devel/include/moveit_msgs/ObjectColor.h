// Generated by gencpp from file moveit_msgs/ObjectColor.msg
// DO NOT EDIT!


#ifndef MOVEIT_MSGS_MESSAGE_OBJECTCOLOR_H
#define MOVEIT_MSGS_MESSAGE_OBJECTCOLOR_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/ColorRGBA.h>

namespace moveit_msgs
{
template <class ContainerAllocator>
struct ObjectColor_
{
  typedef ObjectColor_<ContainerAllocator> Type;

  ObjectColor_()
    : id()
    , color()  {
    }
  ObjectColor_(const ContainerAllocator& _alloc)
    : id(_alloc)
    , color(_alloc)  {
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _id_type;
  _id_type id;

   typedef  ::std_msgs::ColorRGBA_<ContainerAllocator>  _color_type;
  _color_type color;




  typedef boost::shared_ptr< ::moveit_msgs::ObjectColor_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::moveit_msgs::ObjectColor_<ContainerAllocator> const> ConstPtr;

}; // struct ObjectColor_

typedef ::moveit_msgs::ObjectColor_<std::allocator<void> > ObjectColor;

typedef boost::shared_ptr< ::moveit_msgs::ObjectColor > ObjectColorPtr;
typedef boost::shared_ptr< ::moveit_msgs::ObjectColor const> ObjectColorConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::moveit_msgs::ObjectColor_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::moveit_msgs::ObjectColor_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace moveit_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'shape_msgs': ['/opt/ros/indigo/share/shape_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'moveit_msgs': ['/home/aniket/moveit/devel/share/moveit_msgs/msg', '/home/aniket/moveit/src/moveit_msgs/msg'], 'trajectory_msgs': ['/opt/ros/indigo/share/trajectory_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'object_recognition_msgs': ['/opt/ros/indigo/share/object_recognition_msgs/cmake/../msg'], 'octomap_msgs': ['/opt/ros/indigo/share/octomap_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::moveit_msgs::ObjectColor_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::moveit_msgs::ObjectColor_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::moveit_msgs::ObjectColor_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ec3bd6f103430e64b2ae706a67d8488e";
  }

  static const char* value(const ::moveit_msgs::ObjectColor_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xec3bd6f103430e64ULL;
  static const uint64_t static_value2 = 0xb2ae706a67d8488eULL;
};

template<class ContainerAllocator>
struct DataType< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "moveit_msgs/ObjectColor";
  }

  static const char* value(const ::moveit_msgs::ObjectColor_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# The object id for which we specify color\n\
string id\n\
\n\
# The value of the color\n\
std_msgs/ColorRGBA color\n\
\n\
================================================================================\n\
MSG: std_msgs/ColorRGBA\n\
float32 r\n\
float32 g\n\
float32 b\n\
float32 a\n\
";
  }

  static const char* value(const ::moveit_msgs::ObjectColor_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.color);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct ObjectColor_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::moveit_msgs::ObjectColor_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::moveit_msgs::ObjectColor_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.id);
    s << indent << "color: ";
    s << std::endl;
    Printer< ::std_msgs::ColorRGBA_<ContainerAllocator> >::stream(s, indent + "  ", v.color);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOVEIT_MSGS_MESSAGE_OBJECTCOLOR_H
