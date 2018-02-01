#	Jorge Emilio Rubio Barboza 	A00368770
#	Tarea #1 	15/01/18
#	Clase Hash, clase que se basa en replicar la estructura
#   de datos de Hashmap/HashTable/Table/Dictionary la cual se basa
#  	en un par de llave/identificador y valor.
#	Python ya cuenta con la estructura dict (referencia a dictionary)
#	Pero decidi realizarla para practicar el lenguaje que voy a estar
#	utilizando durante el curso

class Hash:
	#funcion inicial, con esta funcion siempre se va 
	#a iniciar cuando llamemos a un objeto de la clase
	#en este caso se inicia un arreglo vacio con un tamanio fijo
	#para caso practico el tamanio sera de 5
	def __init__(self):
		self.size = 5
		self.map = [None] * self.size

	# _get_pos, es el metodo con el cual conocemos la ubicacion ideal
	# para nuestro elemento, esto basado en un calculo para omitir duplicar
	# o empalmar elementos, de ese modo tener un elemento en cada ubicacion y 
	# evitar choques. Para eso utilizaremos el valor ASCII de cada letra de nuestro
	# indice y sacarle el % size(tamanio de la tabla/diccionario) para lograr una mejor ubicacion
	def _get_pos(self, key):
		hash = 0
		for char in str(key) : #ciclo que recorre caracter por caracter nuestro indice en caso de que sea una palabra
			hash += ord(char) #sumar el valor del caracter
					#ord(ch) es una funcion de python que regresa el valor ASCII del caracter dado
		return hash % self.size #se regresa la ubicacion ideal
	
	# add, es el metodo que agrega a la tabla el valor segun el indice
	# almacena el valor en nuestro direcotrio
	def add(self, key, value):
		key_hash = self._get_pos(key) #obtenemos la posicion en la cual vamos a insertar el valor
									  #utilizando el metodo anterior
		key_value = [key, value] #creamos una variable que va a ser el "valor" que vamos a insertar en nuestra
								#tabla, este valor se forma por la tupla key y value
		if self.map[key_hash] is None: #revisamos si la ubicacion/index esta disponible
			self.map[key_hash] = list([key_value]) #si esta disponible, insertamos el valor
			return True #regresamos true para informar que ya se guardo el valor
		else:
			for pair in self.map[key_hash]: #si encontramos que ya esta ocupada, vamos a iterar por todo nuestro diccionario
				if pair[0] == key: #ya que encontramos el indice
					pair[1] = value #agregamos el valor a la pareja
					return True #regresamos true para informar que ya se guardo el valor
			self.map[key_hash].append(key_value) #si no encontramos el indice, creamos uno
			return True

	#delete, es el metodo que elimina
	# elementos del diccionario
	def delete(self, key):
	 	key_hash = self._get_pos(key) #primero obtenemos la posicion del indice deseado a eliminar	
	 	if self.map[key_hash] is None: #revisar si el indice existe
	 	 	return False #si no exise el indice, regresamos false
	 	for i in range(0, len(self.map[key_hash])): #iteramos por todo el diccionario para buscar la posicion
	 		if self.map[key_hash][i][0] == key: #ya que encontremos el elemento dentro del mapa
	 			self.map[key_hash].pop(i) # lo eliminamos del diccionario
	 			return True

	#print, es la funcion que simplemente imprime todo lo que esta en el diccionario
	def print(self):
		for item in self.map:
			if item is not None: #si el elemento no esta vacio entonces lo imprimimos
				print(str(item))