import PySimpleGUI as sg
from Sequence import Sequence

sg.theme('DarkAmber')

layout = [
			[sg.Text('Interval Trainer')],
			# TODO: instead of text, show png of notes
			[sg.Text('						',key='KEY_SOLUTION_TEXT')],      
			[sg.B('New Sequence'), sg.B('Solution'),sg.B('Replay Sequence')]
		]

window = sg.Window('Interval Trainer', layout)      

sequence = None
while True:
	event, values = window.read() 
	print(event, values)       

	if event == sg.WIN_CLOSED or event == 'Exit':
		break

	elif event == 'New Sequence':
		window['KEY_SOLUTION_TEXT'].update(value='						')
		sequence = Sequence()
		sequence.play()

	elif event == 'Solution':
		if sequence is not None:
			solution = sequence.get_text()
			print(f'solution: {solution}')
			window['KEY_SOLUTION_TEXT'].update(value=solution)
		
	elif event == 'Replay Sequence':
		if sequence is not None:
			sequence.play()

window.close()