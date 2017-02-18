
def recursiveChildren(node,depth=0):
	#a = recursiveChildren(PS)
	results = [(node.type,node.name)]
	print "{0}{1}".format(' ' * depth, node.name)
	if len(node.children) > 0:
		for child in node.children:
			results.extend(recursiveChildren(child,(depth+1)))
	return results

