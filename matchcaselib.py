from typing import List, Tuple, Union

class match:

  def __init__(self, *attrs):
    self._attrs = attrs
    self._default = True

  def __enter__(self):
    return self

  def __exit__(self, typ, val, tb):
    return self

  def case(self, *_objects):
    if len(_objects) != len(self._attrs):
      raise ValueError(f"The amount of objects passed in ({len(_objects)}) does not match the amount of objects used to initialize the match in context ({len(self._attrs)}).")

    if _objects == self._attrs:
      self._default = False
      return True

  @property
  def default(self):
    return self._default

  def exit(self):
    return self.__exit__(None, None, None)
