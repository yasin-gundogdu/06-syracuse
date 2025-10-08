# imports

from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER

def syr_plot(lsyr):
	title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
	fig = Figure({
		'layout': {
			'title': {'text': title},
			'xaxis': {'title': {'text': "x"}},
			'yaxis': {'title': {'text': "y"}},
		}
	})
	x = [i for i in range(len(lsyr))]
	t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
	fig.add_trace(t)
	fig.show()
	# fig.write_html('fig.html', include_plotlyjs='cdn')
	return None

#######################

def syracuse_l(n):
	"""retourne la suite de Syracuse de source n

	Args:
		n (int): la source de la suite

	Returns:
		list: la suite de Syracuse de source n
	"""
	l = [n]
	while n != 1:
		if n % 2 == 0:
			n = n // 2
		else:
			n = 3 * n + 1
		l.append(n)
	return l


def temps_de_vol(l):
	"""Retourne le temps de vol d'une suite de Syracuse

	Args:
		l (list): la suite de Syracuse

	Returns:
		int: le temps de vol
	"""
	return len(l) - 1

def temps_de_vol_en_altitude(l):
	"""Retourne le temps de vol en altitude d'une suite de Syracuse

	Args:
		l (list): la suite de Syracuse

	Returns:
		int: le temps de vol en altitude
	"""
	n0 = l[0]
	for i in range(1, len(l)):
		if l[i] < n0:
			# on renvoie le nombre d'itérations complètes avant redescente
			return i - 1
	return len(l) - 1  # si jamais on ne redescend pas

def altitude_maximale(l):
	"""retourne l'altitude maximale d'une suite de Syracuse

	Args:
		l (list): la suite de Syracuse

	Returns:
		int: l'altitude maximale
	"""
	return max(l)

def main():
	lsyr = syracuse_l(15)
	syr_plot(lsyr)
	print("Temps de vol :", temps_de_vol(lsyr))
	print("Temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
	print("Altitude maximale :", altitude_maximale(lsyr))

if __name__ == "__main__":
	main()
