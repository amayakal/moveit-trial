# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from industrial_msgs/TriState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class TriState(genpy.Message):
  _md5sum = "deb03829f3c2d0f1b647fa38d7087952"
  _type = "industrial_msgs/TriState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# The tri-state captures boolean values with the additional state of unknown

int8 val

# enumerated values

# Unknown or unavailable 
int8 UNKNOWN=-1  

# High state                       
int8 TRUE=1
int8 ON=1
int8 ENABLED=1
int8 HIGH=1
int8 CLOSED=1

# Low state
int8 FALSE=0
int8 OFF=0
int8 DISABLED=0
int8 LOW=0
int8 OPEN=0


"""
  # Pseudo-constants
  UNKNOWN = -1
  TRUE = 1
  ON = 1
  ENABLED = 1
  HIGH = 1
  CLOSED = 1
  FALSE = 0
  OFF = 0
  DISABLED = 0
  LOW = 0
  OPEN = 0

  __slots__ = ['val']
  _slot_types = ['int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       val

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TriState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.val is None:
        self.val = 0
    else:
      self.val = 0

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
      buff.write(_struct_b.pack(self.val))
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
      end += 1
      (self.val,) = _struct_b.unpack(str[start:end])
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
      buff.write(_struct_b.pack(self.val))
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
      end += 1
      (self.val,) = _struct_b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_b = struct.Struct("<b")
