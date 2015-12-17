# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/RobotTrajectory.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import trajectory_msgs.msg
import geometry_msgs.msg
import genpy
import std_msgs.msg

class RobotTrajectory(genpy.Message):
  _md5sum = "dfa9556423d709a3729bcef664bddf67"
  _type = "moveit_msgs/RobotTrajectory"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """trajectory_msgs/JointTrajectory joint_trajectory
trajectory_msgs/MultiDOFJointTrajectory multi_dof_joint_trajectory

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start

================================================================================
MSG: trajectory_msgs/MultiDOFJointTrajectory
# The header is used to specify the coordinate frame and the reference time for the trajectory durations
Header header

# A representation of a multi-dof joint trajectory (each point is a transformation)
# Each point along the trajectory will include an array of positions/velocities/accelerations
# that has the same length as the array of joint names, and has the same order of joints as 
# the joint names array.

string[] joint_names
MultiDOFJointTrajectoryPoint[] points

================================================================================
MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint
# Each multi-dof joint can specify a transform (up to 6 DOF)
geometry_msgs/Transform[] transforms

# There can be a velocity specified for the origin of the joint 
geometry_msgs/Twist[] velocities

# There can be an acceleration specified for the origin of the joint 
geometry_msgs/Twist[] accelerations

duration time_from_start

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

"""
  __slots__ = ['joint_trajectory','multi_dof_joint_trajectory']
  _slot_types = ['trajectory_msgs/JointTrajectory','trajectory_msgs/MultiDOFJointTrajectory']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       joint_trajectory,multi_dof_joint_trajectory

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobotTrajectory, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.joint_trajectory is None:
        self.joint_trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.multi_dof_joint_trajectory is None:
        self.multi_dof_joint_trajectory = trajectory_msgs.msg.MultiDOFJointTrajectory()
    else:
      self.joint_trajectory = trajectory_msgs.msg.JointTrajectory()
      self.multi_dof_joint_trajectory = trajectory_msgs.msg.MultiDOFJointTrajectory()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.joint_trajectory.header.seq, _x.joint_trajectory.header.stamp.secs, _x.joint_trajectory.header.stamp.nsecs))
      _x = self.joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.joint_trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.positions))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.velocities))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.accelerations))
        length = len(val1.effort)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.effort))
        _v1 = val1.time_from_start
        _x = _v1
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_struct_3I.pack(_x.multi_dof_joint_trajectory.header.seq, _x.multi_dof_joint_trajectory.header.stamp.secs, _x.multi_dof_joint_trajectory.header.stamp.nsecs))
      _x = self.multi_dof_joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.multi_dof_joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.multi_dof_joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.multi_dof_joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.multi_dof_joint_trajectory.points:
        length = len(val1.transforms)
        buff.write(_struct_I.pack(length))
        for val2 in val1.transforms:
          _v2 = val2.translation
          _x = _v2
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v3 = val2.rotation
          _x = _v3
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.velocities:
          _v4 = val2.linear
          _x = _v4
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v5 = val2.angular
          _x = _v5
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        for val2 in val1.accelerations:
          _v6 = val2.linear
          _x = _v6
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v7 = val2.angular
          _x = _v7
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v8 = val1.time_from_start
        _x = _v8
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.joint_trajectory is None:
        self.joint_trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.multi_dof_joint_trajectory is None:
        self.multi_dof_joint_trajectory = trajectory_msgs.msg.MultiDOFJointTrajectory()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.joint_trajectory.header.seq, _x.joint_trajectory.header.stamp.secs, _x.joint_trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.effort = struct.unpack(pattern, str[start:end])
        _v9 = val1.time_from_start
        _x = _v9
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.joint_trajectory.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.multi_dof_joint_trajectory.header.seq, _x.multi_dof_joint_trajectory.header.stamp.secs, _x.multi_dof_joint_trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.multi_dof_joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.multi_dof_joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.multi_dof_joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.multi_dof_joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.multi_dof_joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.transforms = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Transform()
          _v10 = val2.translation
          _x = _v10
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v11 = val2.rotation
          _x = _v11
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.transforms.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.velocities = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v12 = val2.linear
          _x = _v12
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v13 = val2.angular
          _x = _v13
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.velocities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.accelerations = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v14 = val2.linear
          _x = _v14
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v15 = val2.angular
          _x = _v15
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.accelerations.append(val2)
        _v16 = val1.time_from_start
        _x = _v16
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.multi_dof_joint_trajectory.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.joint_trajectory.header.seq, _x.joint_trajectory.header.stamp.secs, _x.joint_trajectory.header.stamp.nsecs))
      _x = self.joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.joint_trajectory.points:
        length = len(val1.positions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.positions.tostring())
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.velocities.tostring())
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.accelerations.tostring())
        length = len(val1.effort)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.effort.tostring())
        _v17 = val1.time_from_start
        _x = _v17
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
      _x = self
      buff.write(_struct_3I.pack(_x.multi_dof_joint_trajectory.header.seq, _x.multi_dof_joint_trajectory.header.stamp.secs, _x.multi_dof_joint_trajectory.header.stamp.nsecs))
      _x = self.multi_dof_joint_trajectory.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.multi_dof_joint_trajectory.joint_names)
      buff.write(_struct_I.pack(length))
      for val1 in self.multi_dof_joint_trajectory.joint_names:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.multi_dof_joint_trajectory.points)
      buff.write(_struct_I.pack(length))
      for val1 in self.multi_dof_joint_trajectory.points:
        length = len(val1.transforms)
        buff.write(_struct_I.pack(length))
        for val2 in val1.transforms:
          _v18 = val2.translation
          _x = _v18
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v19 = val2.rotation
          _x = _v19
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        length = len(val1.velocities)
        buff.write(_struct_I.pack(length))
        for val2 in val1.velocities:
          _v20 = val2.linear
          _x = _v20
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v21 = val2.angular
          _x = _v21
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        length = len(val1.accelerations)
        buff.write(_struct_I.pack(length))
        for val2 in val1.accelerations:
          _v22 = val2.linear
          _x = _v22
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v23 = val2.angular
          _x = _v23
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v24 = val1.time_from_start
        _x = _v24
        buff.write(_struct_2i.pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.joint_trajectory is None:
        self.joint_trajectory = trajectory_msgs.msg.JointTrajectory()
      if self.multi_dof_joint_trajectory is None:
        self.multi_dof_joint_trajectory = trajectory_msgs.msg.MultiDOFJointTrajectory()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.joint_trajectory.header.seq, _x.joint_trajectory.header.stamp.secs, _x.joint_trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.JointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.positions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.velocities = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.accelerations = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _v25 = val1.time_from_start
        _x = _v25
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.joint_trajectory.points.append(val1)
      _x = self
      start = end
      end += 12
      (_x.multi_dof_joint_trajectory.header.seq, _x.multi_dof_joint_trajectory.header.stamp.secs, _x.multi_dof_joint_trajectory.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.multi_dof_joint_trajectory.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.multi_dof_joint_trajectory.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.multi_dof_joint_trajectory.joint_names = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.multi_dof_joint_trajectory.joint_names.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.multi_dof_joint_trajectory.points = []
      for i in range(0, length):
        val1 = trajectory_msgs.msg.MultiDOFJointTrajectoryPoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.transforms = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Transform()
          _v26 = val2.translation
          _x = _v26
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v27 = val2.rotation
          _x = _v27
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.transforms.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.velocities = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v28 = val2.linear
          _x = _v28
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v29 = val2.angular
          _x = _v29
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.velocities.append(val2)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.accelerations = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Twist()
          _v30 = val2.linear
          _x = _v30
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v31 = val2.angular
          _x = _v31
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          val1.accelerations.append(val2)
        _v32 = val1.time_from_start
        _x = _v32
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _struct_2i.unpack(str[start:end])
        self.multi_dof_joint_trajectory.points.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
_struct_3I = struct.Struct("<3I")
_struct_2i = struct.Struct("<2i")
_struct_3d = struct.Struct("<3d")
