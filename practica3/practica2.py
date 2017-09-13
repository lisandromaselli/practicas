# PRACTICA 2

class DisjointSets:
	def __init__(self, n):
		self.DS = [-1] * n
		
	def find(self, x):
		if( self.DS[x] == -1 ): return x
		self.DS[x] = self.find(self.DS[x])
		return self.DS[x]
	
	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if( x != y ): self.DS[x] = y


def partition(G):
	(V,E) = G
	etiq = {}
	for i, v in enumerate(V): etiq[v] = i
	S = DisjointSets(len(V))
	for (x,y) in E: S.union(etiq[x],etiq[y])
	dicc = {}
	for v in V: dicc.setdefault(S.find(etiq[v]), []).append(v)
	return dicc

def main():
	G = (list("EBCDAFGHIJ"), [tuple(e) for e in "EB EJ JB BF JF AH CD CI DI".split()])
	print( list(partition(G).values()) )
	
if __name__ == '__main__':
	main()	
