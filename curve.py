import numpy as np
import matplotlib.pyplot as plt

def	draw_EC(a: int, b: int) -> None:
	fig = plt.figure()
	y, x = np.ogrid[-5:5:100j, -5:5:100j]
	plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
	plt.show()
	fig.savefig("EC.pdf")

draw_EC(8, 5)