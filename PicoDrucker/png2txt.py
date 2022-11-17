import matplotlib.pyplot as plt

img = 1-plt.imread("image.png")[::4,::4,0]
img[img<0.5] = 0
img[img>=0.5] = 1

plt.figure()
plt.imshow(img)
plt.show()
with open("image.txt", "w") as file:
    for line in img:
        for pixel in line:
            file.write(str(int(pixel)))
        file.write("\n")
    