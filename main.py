from tkinter import filedialog
import tkinter
from pygame import mixer
import taglib

mixer.init()

root=tkinter.Tk()
root.title('Lettore MP3 & OGG by pingumen96')

#variabili globali
global filename
filename=None
global mp3_pause
global volume_value
volume_value=tkinter.StringVar()
global mp3_tags
mp3_tags=None
global mp3_tags_dict
mp3_tags_dict={'titolo':tkinter.StringVar(),'artista':tkinter.StringVar(),'album':tkinter.StringVar()}

def open_file():
	try:
		global filename
		filename=tkinter.filedialog.askopenfilename(filetypes=[('MP3','.mp3'),('OGG','.ogg')])
		mixer.music.load(filename)
		loaded=True
		mp3_tags=taglib.File(filename)
		print(mp3_tags.tags) #prova funzionamento taglib
		mp3_tags_dict['titolo'].set(mp3_tags.tags['TITLE'][0])
		mp3_tags_dict['artista'].set(mp3_tags.tags['ARTIST'][0])
		mp3_tags_dict['album'].set(mp3_tags.tags['ALBUM'][0])
		print(mp3_tags_dict['titolo'].get())
		mixer.music.play()
	except FileNotFoundError:
		pass

def play(opened_file):
	if not opened_file:
		print("file non caricato")
	else:
		mixer.music.unpause()
		pass

def pause():
	mp3_pause=True
	mixer.music.pause()

def stop():
	mixer.music.stop()

def volume(command): #da usare solo passando comando come parametro
	volume_value_string=mixer.music.get_volume() #stringa che contiene valore del volume
	volume_value.set(volume_value_string)
	if command=='+':
		volume_value_string=str(round(float(mixer.music.get_volume()+0.1),1))
		volume_value.set(volume_value_string)
	elif command=='-':
		volume_value_string=str(round(float(mixer.music.get_volume()-0.1),1))
		volume_value.set(volume_value_string)
	mixer.music.set_volume(float(volume_value.get()))

def get_tags(tag):
	if tag=='titolo':
		if mp3_tags_dict:
			return mp3_tags_dict['titolo']
		else:
			return '-'
	if tag=='album':
		if mp3_tags_dict:
			return mp3_tags_dict['album']
		else:
			return '-'
	if tag=='artista':
		if mp3_tags_dict:
			return mp3_tags_dict['artista']
		else:
			return '-'

def gui(): #creazione dell'interfaccia grafica
	#operazioni in idle
	#idle=tkinter.Button(command=root.update())
	#idle.grid()
	open_button=tkinter.Button(text='Apri',command=lambda:open_file())
	open_button.grid(row=0,column=0)
	play_button=tkinter.Button(text='Play',command=lambda:play(filename))
	play_button.grid(row=1,column=0)
	pause_button=tkinter.Button(text='Pausa',command=lambda:pause())
	pause_button.grid(row=1,column=1)
	stop_button=tkinter.Button(text='Stop',command=lambda:stop())
	stop_button.grid(row=1,column=2)
	volume_label=tkinter.Label(text='  Volume: ')
	volume_label.grid(row=1,column=3)
	volume_increase=tkinter.Button(text='+',width=1,command=lambda:volume('+'))
	volume_increase.grid(row=1,column=4)
	volume_decrease=tkinter.Button(text='-',width=1,command=lambda:volume('-'))
	volume_decrease.grid(row=1,column=5)
	volume_value_label=tkinter.Label(textvariable=volume_value)
	volume_value_label.grid(row=1,column=6)

	#visualizzazione info media
	title=tkinter.Label(text='Titolo:')
	title.grid(row=2,column=0)
	song_title_label=tkinter.Label(textvariable=get_tags('titolo'))
	song_title_label.grid(row=2,column=1)
	artist=tkinter.Label(text='Artista:')
	artist.grid(row=3,column=0)
	song_artist_label=tkinter.Label(textvariable=get_tags('artista'))
	song_artist_label.grid(row=3,column=1)
	album=tkinter.Label(text='Album:')
	album.grid(row=4,column=0)
	song_album_label=tkinter.Label(textvariable=get_tags('album'))
	song_album_label.grid(row=4,column=1)


#open_file()
gui()
root.mainloop()