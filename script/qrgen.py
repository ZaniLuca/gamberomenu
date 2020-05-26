import qrcode

qrc = qrcode.QRCode(
	version=1,
	box_size=5,
	border=5
)

data = 'https://gambero.netlify.app/Menu1.pdf'
qrc.add_data(data)
qrc.make(fit=True)
img = qrc.make_image(fill='black', back_color='white')
img.save('prova.png')