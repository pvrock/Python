class TrieNode:
	def __init__(self):
		self.words={}
		self.last=False

class Trie:
	def __init__(self):
		self.root=TrieNode()
		self.sugges=[]

		
	def insert_node(self,val):
		for x in val:
			node=self.root
			for y in x:
				if not node.words.get(y):
					node.words[y]=TrieNode()
				node=node.words[y]
			node.last=True

	def getSuggestion(self,node,st):
		if node.last==True:
			self.sugges.append(st)
		#print(node.words,st,node.last)
		for k,n in node.words.items():
			self.getSuggestion(n,st+k)


	def autosuggestion(self,val):
		node=self.root
		st=""
		for x in val:
			if node.words.get(x):
				st+=x
				node=node.words[x]
			else:
				return -1
		self.getSuggestion(node,st)
		return self.sugges

if __name__ == '__main__':
	t=Trie()
	val=["hello","hey","how are you","what is the current time","current time","time","how is the weather","what is autocomplete"]
	t.insert_node(val)
	print(t.autosuggestion("wh"))


