import imageio.v3 as iio

filenames = ['image1.jpeg', 'image2.jpeg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('cats.gif', images, duration = 500, loop = 0)
