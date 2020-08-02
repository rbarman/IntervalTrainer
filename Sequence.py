from music21 import *
import random
import pygame

class Sequence:
	def __init__(self,root='C', num_notes = 2, note_duration = 4):
		self.root = root
		self.num_notes = num_notes
		self.note_duration = note_duration
		self.sequence = self.generate()
		self.sequence_path = self.save()

	def generate(self):
		
		scale_pitches = scale.MajorScale(self.root).pitches
		
		root_pitch = scale_pitches[0]
		root_note = note.Note(root_pitch, quarterLength = self.note_duration)

		next_notes = []
		for _ in range(self.num_notes - 1):
			random_pitch = random.choice(scale_pitches)
			new_note = note.Note(random_pitch, quarterLength = self.note_duration)
			next_notes.append(new_note)
		
		sequence = stream.Stream()
		sequence.append(root_note)
		sequence.append(next_notes)
		return sequence

	def save(self):
		fp = self.sequence.write('midi')
		return fp

	def play(self):
		pygame.init()
		pygame.mixer.music.load(self.sequence_path)
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			# check if playback has finished
			pass

	def get_png(self):
		fp = self.sequence.write('lily.png')
		return fp

	def get_text(self):
		names = [note.name for note in self.sequence.notes]
		return ' '.join(names)

if __name__ == '__main__':

	pygame.init()
	seq = Sequence()
	seq.play()
