from rlbig.models import Taxon

class Species(Taxon):

  def __init__(self, name, year=None, author=None, length=None, weight=None, children=()):
      '''
      Initialization of Species class
      '''
      self.name=name
      self.type=self.__class__.__name__
      self.year=year
      self.author=author
      self.children=children
      self.is_root = False
      self.parent = self
      
      self.is_physical = False
      
      '''
      Species specific attributes
      '''
      self.length=length
      self.weight=weight