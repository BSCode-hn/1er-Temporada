#-*- coding:utf8 -*-
from Classes.Queue import *

Books = LinkedListQueue()

Books.add("El Principito")
Books.add("Hola Mundo")
Books.add("Adios Mundo")

Books.printLL()
Books.getFirst()

Books.delete()

Books.getLast()
Books.printLL()
