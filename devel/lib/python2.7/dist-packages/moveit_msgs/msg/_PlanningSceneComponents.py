# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from moveit_msgs/PlanningSceneComponents.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PlanningSceneComponents(genpy.Message):
  _md5sum = "bc993e784476960b918b6e7ad5bb58ce"
  _type = "moveit_msgs/PlanningSceneComponents"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message defines the components that make up the PlanningScene message.
# The values can be used as a bitfield to specify which parts of the PlanningScene message
# are of interest

# Scene name, model name, model root
uint32 SCENE_SETTINGS=1

# Joint values of the robot state
uint32 ROBOT_STATE=2

# Attached objects (including geometry) for the robot state
uint32 ROBOT_STATE_ATTACHED_OBJECTS=4

# The names of the world objects
uint32 WORLD_OBJECT_NAMES=8

# The geometry of the world objects
uint32 WORLD_OBJECT_GEOMETRY=16

# The maintained octomap 
uint32 OCTOMAP=32

# The maintained list of transforms
uint32 TRANSFORMS=64

# The allowed collision matrix
uint32 ALLOWED_COLLISION_MATRIX=128

# The default link padding and link scaling
uint32 LINK_PADDING_AND_SCALING=256

# The stored object colors
uint32 OBJECT_COLORS=512

# Bitfield combining options indicated above
uint32 components

"""
  # Pseudo-constants
  SCENE_SETTINGS = 1
  ROBOT_STATE = 2
  ROBOT_STATE_ATTACHED_OBJECTS = 4
  WORLD_OBJECT_NAMES = 8
  WORLD_OBJECT_GEOMETRY = 16
  OCTOMAP = 32
  TRANSFORMS = 64
  ALLOWED_COLLISION_MATRIX = 128
  LINK_PADDING_AND_SCALING = 256
  OBJECT_COLORS = 512

  __slots__ = ['components']
  _slot_types = ['uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       components

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PlanningSceneComponents, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.components is None:
        self.components = 0
    else:
      self.components = 0

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
      buff.write(_struct_I.pack(self.components))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 4
      (self.components,) = _struct_I.unpack(str[start:end])
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
      buff.write(_struct_I.pack(self.components))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(_x))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(_x))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 4
      (self.components,) = _struct_I.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
