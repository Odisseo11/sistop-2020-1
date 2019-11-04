""" boring.py -> classses needed to complete everything boring """
import sys
from random import randint
from proc import Process

class BoringHelper(object):
	"""
		Class that handles the UI menu and the generation of 'n' random process.
	"""

	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	            'Y', 'Z']

	def __init__(self, num_procs):
		self.num_procs = num_procs

	def generate_procs(self):
		"""
			Generates 'num_procs' number of processes
		"""
		procs = []
		for i in range(self.num_procs):
			if i > len(self.alphabet)-1:
				print("Maximun number of generated processes has been reached(%d)" % len(self.alphabet))
				sys.exit()

			units = randint(Process.MIN_UNITS, Process.MAX_UNITS)
			letter_id = self.alphabet[i]
			proc = Process(letter_id=letter_id, units=units)
			procs.append(proc)
		return procs

	def showmenu(self):
		"""
			Shows the user the multiple options
		"""
		return input("\nAsignar (0) Liberar (1) Salir (2): ")

	def nextkey(self, count):
		"""
			Returns the next key if the alphabet
		"""
		return self.alphabet[count]
