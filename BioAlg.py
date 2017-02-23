from rlbig.BioTools import memoize


@memoize
def flattenTree(node,depth=0,printout=False):
    '''
    Flatten a given tree. Additionally if printout is True print it out as tree while going thru it's structure.
    '''
    searchIndex = [value.upper() for attr, value in node.__dict__.iteritems() if attr not in ('parent','children','type','is_root') and value!='']
    results = [(node, node.type, node.name, "/".join(searchIndex))]

    if printout:
       print "{0}{1}".format(' ' * depth, node.name)

    if len(node.children) > 0:
       for child in node.children:
           results.extend(flattenTree(child,(depth+1),printout))
    return results


@memoize
def sortedflattednTree(node,sort_on=3,depth=0,printout=False):
    '''
    Flatten a given tree and sort it on given parameter. Additionally if printout is True print it out as tree while going thru it's structure.
    '''
    return sorted(flattenTree(node,depth,printout), key=lambda x: x[sort_on])


@memoize
def flattenDictTree(node,depth=0,printout=False):
    '''
    Flatten a given tree. Additionally if printout is True print it out as tree while going thru it's structure.
    '''
    searchIndex = [value.upper() for attr, value in node.__dict__.iteritems() if attr not in ('parent','children','type','is_root') and value!='']
    results = [{'node':node, 'type': node.type, 'name': node.name, 'index':"/".join(searchIndex)}]

    if printout:
       print "{0}{1}".format(' ' * depth, node.name)

    if len(node.children) > 0:
       for child in node.children:
           results.extend(flattenDictTree(child,(depth+1),printout))
    return results


def flattenSearch(node, text='',type='',raw=False):
    '''
    Python filter search algorithm in a given tree. Additionally look after type attribute and do exact match for it.
    '''
    flatten = flattenDictTree(node)
    if not type:
       result = filter(lambda x: text.upper() in x['index'], flatten)
    else:
       result = filter(lambda x: text.upper() in x['index'] and x['type']==type, flatten)

    return result if raw else [o['node'] for o in result]


def flattenOSearch(node, text='',type='',raw=False):
    '''
    Python filter search algorithm in a given tree. Additionally look after type attribute and do exact match for it.
    '''
    flatten = flattenTree(node)
    if not type:
       result = filter(lambda x: text.upper() in x[3], flatten)
    else:
       result = filter(lambda x: text.upper() in x[3] and x[1]==type, flatten)

    return result if raw else [o[0] for o in result]


def flattenLSearch(node, text='',type='',raw=False):
    '''
    Linear search algorithm in a given tree. Additionally look after type attribute and do exact match for it.
    '''
    flatten = flattenTree(node)
    result = []
    for x in flatten:
        if text.upper() in x[3]:
           if not type or type==x[1]:
              result.append(x)
    return result if raw else [o[0] for o in result]


def flattenDSearch(node, text='',type='',raw=False):
    '''
    Linear search algorithm in a given tree. Additionally look after type attribute and do exact match for it.
    '''
    flatten = flattenDictTree(node)
    result = []
    for x in flatten:
        if text.upper() in x['index']:
           if not type or type==x['type']:
              result.append(x)
    return result if raw else [o['node'] for o in result]


