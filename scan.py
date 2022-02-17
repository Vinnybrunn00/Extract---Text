from rich import print
import pytesseract
import pyfiglet as pg
import sys
import cv2
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

banner = pg.figlet_format('Extract - T')
print(banner)

sys.platform = 'Linux'
system = sys.platform

if sys.platform == 'Linux':
	print(
		f'Sistema Operacional: [cyan]{system}[/]\n\n'
		'1 - START\n'
		'2 - DETALHES'
		)
	qq = int(input('Opção: '))
	msg = f'Você escolheu a opção: {qq}'
	desenvolvedor = 'Vinícius Bruno'

	if qq == '2':
		os.system(limpar)
		print(
			f'[red]{msg}[/]\n\n'
			'[green]-> [Este programa é capaz de extrair textos de uma imagem] <-\n\n[/]'
			f'[blue]DESENVOLVEDOR: {desenvolvedor}[/]')

	elif qq == '1':
		while True:
			try:
				os.system(limpar)
				print(banner)
				print(f'[red]{msg}[/]\n\n')
				arquivo = eval(input('Arraste a imagem aqui: '))
				img = cv2.imread(arquivo)
				txt = pytesseract.image_to_string(img)
				os.system(limpar)
				print(txt)

			except:
				print('error')

else:
	sys.platform = 'Windows'
	system = sys.platform

	if sys.platform == 'Windows':
			print(
				f'Sistema Operacional: [cyan]{system}[/]\n\n'
				'1 - START\n'
				'2 - DETALHES'
				)

			qq1 = int(input('Opcão: '))
			
			if qq1 == '2':
				print('xuxa')
