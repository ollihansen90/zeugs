import matplotlib.pyplot as plt

img = []
with open("image.txt", "r") as file:
    img.extend(file.readlines())
img = [list(i.strip()) for i in img]
img = [[int(i) for i in line] for line in img]

plt.figure()
plt.imshow(img)
plt.show()