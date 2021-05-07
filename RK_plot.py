import numpy as np
import matplotlib.pyplot as plt

def plot_solution(titre, t, exact, *sols) :
	"""
	Affiche plusieurs courbes de résolution pour comparaison
	
	Parameters
	----------
	titre : str
		Titre du graphe
	t : ndarray NumPy, dimension (n,)
		Instants où sont calculées les estimations
	exact : fonction ou `None`
		Fonction vectorisée à appliquer à `t` pour calculer la solution exacte
		Si `exact` vaut `None`, le calcul ne sera pas effectué et la courbe ne sera pas tracée.
		(Par exemple, dans le cas, où on ne connaît pas la solution exacte.)
	sols : séquence de triplets (ndarray NumPy dimension (n,), str, str)
		Chaque triplet contient, dans l'ordre :
		* les estimations de la solution
		* l'étiquette correspondante qui sera placée dans la légende
		* le style de la courbe correspondante dans le graphe
	
	Returns
	-------
	Figure, Axes
		Couple figure/sous-figure contenant le graphe final
	"""
	fig, ax = plt.subplots()
	if exact is not None :
		ax.plot(t, exact(t), 'k-', label = "Solution exacte")
	for sol in sols :
		ax.plot(t, sol[0][0,:], sol[2], label = sol[1])
	if titre is not None :
		ax.set_title(titre)
	ax.set_xlabel("$t$")
	ax.set_ylabel("$y(t)$")
	ax.legend()
	return fig, ax
