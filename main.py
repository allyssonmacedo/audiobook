import pyttsx3
import pyPDF2

caminho_livro = 'carminho'

livro = open(caminho_livro, 'rb')

pdf = pyPDF2.PdfFileReader(livro)

paginas = pdf.numPages

voz = pyttsx3.init(driverName='sapi5')
voz.setProperty('rate', 200)

escolher_pagina = 8

pagina = pdf.getPage(escolher_pagina +1)

texto = pagina.extractText(paginas)

voz.say(texto)

#salvando arquivo em mp3
#voz.save_to_file(texto, 'audiobook.mp3')

voz.runAndWait()