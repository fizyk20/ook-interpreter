from .brainfuck import BrainfuckMachine
import re

class OokMachine(BrainfuckMachine):
	
	translation = {
		('Ook.', 'Ook?'): '>',
		('Ook?', 'Ook.'): '<',
		('Ook.', 'Ook.'): '+',
		('Ook!', 'Ook!'): '-',
		('Ook!', 'Ook.'): '.',
		('Ook.', 'Ook!'): ',',
		('Ook!', 'Ook?'): '[',
		('Ook?', 'Ook!'): ']'
	}
	
	def __init__(self):
		super().__init__()
		self.regex = re.compile(r'Ook[\.\?!]')
		
	def translate(self, program):
		result = self.regex.findall(program)
		result.reverse()
		resProgram = ''
		while result:
			ook1 = result.pop()
			ook2 = result.pop()
			resProgram += self.translation[(ook1, ook2)]
		return resProgram
		
	def setCode(self, program):
		super().setCode(self.translate(program))
		
