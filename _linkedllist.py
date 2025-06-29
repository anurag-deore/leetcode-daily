class Node:
		def __init__(self, data = None, next=None):
			self.data = data
			self.next = next
			
class LinkedList:
		def __init__(self):
			self.head = None

		def insert_beginning(self,data):
			node = Node(data,self.head)
			self.head = node

		def insert_end(self,data):
			if self.head is None:
				node = Node(data,self.head)
				self.head = node
				return

			itr = self.head
			while itr.next:
				itr = itr.next
			itr.next = Node(data,None)


		def insert_values_start(self,values):

			for v in values:
				self.insert_beginning(v)

		def insert_values_end(self,values):
			for v in values:
				self.insert_end(v)


		def get_length(self):
			count = 0
			itr = self.head
			while itr:
					pass
		def print_linkedlist(self):
					if self.head is None:
						print("EMPTY LinkedList")
						return
					
					itr = self.head
					st =''
					while itr:	
						st += "| "+str(itr.data)+" | --> "
						itr = itr.next
					st += "X"
					print(st)




if __name__ == "__main__":
	ll = LinkedList()
	ll.insert_values_end([5,20,32,12])
	ll.inse
	ll.print_linkedlist()