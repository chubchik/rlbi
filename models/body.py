from rlbig.models import BaseTree

class Body(BaseTree):

  def __init__(self, length=None, children=()):
      '''
      Initialization of Body class
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
      
  def __repr__(self):
      '''
      Self-representation
      '''
      if self.parent:
         return "Body of {0}".format(self.parent.name)
      else:
         return 'Ownerless Body'
         
  @property
  def name(self):
      return self.__repr__()