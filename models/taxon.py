#-*- coding: utf-8 -*-

class Taxon:
  name=''
  year=''
  author=''
  type=''
  children=()

  def __init__(self, name, type="", year="", author="", children=()):
      self.name=name
      self.type=type
      self.year=year
      self.author=author
      self.children=children
      
  def __repr__(self):
	  if self.type:
	     return "{0} {1} ({2})".format(self.name, self.year, self.type)
	  else:
	     return "{0} {1}".format(self.name, self.year)