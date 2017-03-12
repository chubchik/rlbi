from rlbig.models import BaseTree

class Tail(BaseTree):
  
  def __init__(self, length=None, color=(0,0,0), children=()):
      '''
      Initialization of Tail class, color is RGB
      '''
      self.type=self.__class__.__name__
      self.children=children
      self.is_root = False
      self.parent = self
      
      self.is_physical = True
 
      '''
      Species specific attributes
      '''
      self.length=length
      if type(color)==tuple:
         self.color='#%02x%02x%02x'%color
      else:
         self.color=color
      
  def __repr__(self):
      '''
      Self-representation
      '''
      if self.parent:
         return "Tail of {0}".format(self.parent.name)
      else:
         return 'Ownerless Tail'
         
  @property
  def rgb_color(self):
      if self.color:
         value = self.color.lstrip('#')
         lv = len(value)
         return tuple(int(value[i:i+2], 16) for i in (0, 2 ,4))
      return None
      
  @property
  def name(self):
      return self.__repr__()