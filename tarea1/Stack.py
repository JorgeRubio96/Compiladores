#	Jorge Emilio Rubio Barboza 	A00368770
#	Tarea #1 	15/01/18
#	Clase Stack, clase que se basa en el ordenamiento
#	lifo enfocado, en este caso, a arreglos/listas

class Stack:
	#funcion inicial, con esta funcion siempre se va 
	#a iniciar cuando llamemos a un objeto de la clase
	#en este caso se crea un arreglo vacio
	def __init__(self):
		self.items = []

	#isEmpty es la funcion que revisa si mi arreglo/lista (que va a representar a nuestro stack)
	#esta vacia, y a partir de la respuesta puedo tomar accion
	#para agregar o sacar elementos
	def isEmpty(self):
		return self.items == []

	#push es el metodo que nos permite agregar elementos
	#a nuestro stack 
	def push(self, item):
		self.items.append(item)

	#pop es el metodo para eliminar elementos de nuestro stack
	#importante recordar la logica del stack (lifo), por lo cual
	#se utiliza pop, ya que no nos interesa la posición del ultimo
	#elemento, simplemente nos interesa que el ultimo elemento
	#desaparezca de la lista
	def pop(self):
		return self.items.pop()

	#last es el metodo que regresa el ultimo elemento del stack
	#o el elemento que esta en el tope del stack
	def last(self):
		return self.items.[len(self.items)-1]

	#size es el metodo que nos regresa el tamanio de
	#nuestro stack
	def size(self):
		return len(self.items)