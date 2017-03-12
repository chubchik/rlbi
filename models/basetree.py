class BaseTree:
  '''
  Base Class for building trees
  '''
  def __init__(self, type=None, children=(), is_root=False, is_physical=True):
      '''
      Initialization of Tree class
      '''
      self.is_physical = is_physical
      self.type=type
      self.children=children
      self.is_root = is_root
      self.parent = self


  def hasSameSiblings(self, name, parent):
      '''
      There is more than one Instance of the same Class
      '''
      if [c.__class__.__name__ for c in self.children].count(name) > 1:
         return True
      return False
  

  def setParents(self, parent):
      '''
      Sets recursively parent node for each children node
      '''
      self.parent = parent
      
      for c in self.children:
          '''
          Convert physical children to attributes of self object
          '''
          if c.is_physical:
             '''
             If more than one child, then create property list instead of blank property.
             '''
             if len(self.children) > 1 and self.hasSameSiblings(c.__class__.__name__, self):
                if getattr(self,"%ss"%c.__class__.__name__.lower(), None) is None:
                   setattr(self, "%ss"%c.__class__.__name__.lower(), [])
                else:
                   tmp = getattr(self,"%ss"%c.__class__.__name__.lower(), [])
                   tmp.append(c)
             else:
                setattr(self, c.__class__.__name__.lower(), c)
          c.setParents(self)
