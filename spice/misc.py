from PIL import Image
import io
import random
import string
import os
import imghdr

def thumb(image, size):
	output = io.BytesIO()
	img = Image.open(image)
	img.thumbnail(size)
	img.save(output,format="png")
	return output

def random_string(N):
	return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

def random_name(ext, length=12, dir = ""):
	no_file = False
	home = os.getcwd()
	os.chdir(dir)
	while not no_file:
		filename = random_string(length) + "." + ext
		if not os.path.exists(filename):
			no_file = True
	os.chdir(home)
	return filename

def check_for_jpeg(buf, file):
	signatures = [b'\xff\xd8\xff\xdb',b'\xff\xd8\xff\xe2']
	if file:
		str = file.read(4)
	else:
		str = buf[:4]
	if str in signatures :
		return "jpeg"
	else:
		return None

imghdr.tests.append(check_for_jpeg)