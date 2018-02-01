#	Jorge Emilio Rubio Barboza 	A00368770
#	Tarea #1 	15/01/18
#	Clase Queue, clase que se basa en el ordenamiento
#	fifo enfocado, en este caso, a arreglos/listas

class Queue:
	#funcion inicial, con esta funcion siempre se va 
	#a iniciar cuando llamemos a un objeto de la clase
	#en este caso se crea un arreglo vacio
	def __init__(self):
		self.items = []

	#isEmpty es la funcion que revisa si mi arreglo/lista (que va a representar a nuestro queue)
	#esta vacia, y a partir de la respuesta puedo tomar accion
	#para agregar o sacar elementos
	def isEmpty(self):
		return self.items == []

	#push es el metodo que nos permite agregar elementos
	#a nuestro queue, a diferencia del stack, al momento de agregar
	#elementos buscamos agregarlos al principio de la lista y no al final
	#de ahi el uso del insert en lugar de un append
	def push(self, item):
		self.items.insert(0, item)

	#pop es el metodo para eliminar elementos de nuestro queue
	#importante recordar la logica del queue (fifo), por lo cual
	#se utiliza pop, ya que no nos interesa la posición del ultimo
	#elemento, simplemente nos interesa que el ultimo elemento
	#desaparezca de la lista
	def pop(self):
		return self.items.pop()

	#size es el metodo que regresa el tamanio de nuestro queue
	def size(self)
		return len(self.items)