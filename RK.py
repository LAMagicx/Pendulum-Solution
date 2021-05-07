"""
Méthodes de RUNGE-KUTTA d'ordre 1 et 2
"""

import numpy as np

def RK(step_fun, fun, t_span, y0, t_eval = None) :
	"""
	Applique une méthode itérative pour évaluer la solution de l'équation différentielle :
	     | y = `fun`(t, y)
             | y(`t_span[0]`) = `y0`
	
	Parameters
	----------
	step_fun : fonction
		Fonction définissant le calcul d'une itération. Elle doit avoir la signature
		 step_fun(fun, t, y, t_next, args) avec :
		* fun : second membre de l'équation différentielle
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
		* t_next : l'instant suivant
	fun : fonction
		Second membre de l'équation différentielle. Elle doit avoir la signature
		 fun(t, y, args) avec :
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
	t_span : couple de flottants
		Intervalle de résolution [t_0, t_f]
		La résolution démarre à l'instant t_0 et termine à l'instant t_f.
	y0 : ndarray NumPy, dimension (n, )
		Condition initiale
	t_eval : ndarray NumPy, dimension (n, n_points) ou `None`, optionnel
		Subdivision utilisée pour la résolution
		Les valeurs doivent être triées, commencer par `t_span[0]` et terminer par `t_span[-1]`.
		Si `t_eval` vaut `None`, alors la subdivision est simplement `t_span`.
	
	Returns
	-------
	ndarray NumPy, dimension (n, n_points)
		Estimation des valeurs de la solution aux instants de `t_eval` ou `t_span` si `t_eval` vaut `None`
	"""
	(t0, tf) = t_span
	if t_eval is None :
		t, y = np.array(t_span), np.zeros((y0.size, 2))
		y[:, 0] = y0
		y[:, 1] = step_fun(fun, t0, y0, tf)
	else :
		n = y0.size
		n_points = t_eval.size
		t = t_eval
		y = np.zeros((n, n_points))
		y[:, 0] = y0
		for i in range(1, n_points) :
			y[:, i] = step_fun(fun, t[i - 1], y[:, i - 1], t[i])
	return y

def RK1_step(fun, t, y, t_next) :
	return y + (t_next - t) * fun(t, y)
def RK1(fun, t_span, y0, t_eval = None) :
	"""
	Applique une méthode de RUNGE-KUTTA d'ordre 1 (a.k.a. méthode d'EULER)
	     | y = `fun`(t, y)
             | y(`t_span[0]`) = `y0`
	
	Parameters
	----------
	step_fun : fonction
		Fonction définissant le calcul d'une itération. Elle doit avoir la signature
		 step_fun(fun, t, y, t_next, args) avec :
		* fun : second membre de l'équation différentielle
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
		* t_next : l'instant suivant
	fun : fonction
		Second membre de l'équation différentielle. Elle doit avoir la signature
		 fun(t, y, args) avec :
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
	t_span : couple de flottants
		Intervalle de résolution [t_0, t_f]
		La résolution démarre à l'instant t_0 et termine à l'instant t_f.
	y0 : ndarray NumPy, dimension (n, )
		Condition initiale
	t_eval : ndarray NumPy, dimension (n, n_points) ou `None`, optionnel
		Subdivision utilisée pour la résolution
		Les valeurs doivent être triées, commencer par `t_span[0]` et terminer par `t_span[-1]`.
		Si `t_eval` vaut `None`, alors la subdivision est simplement `t_span`.
	
	Returns
	-------
	ndarray NumPy, dimension (n, n_points)
		Estimation des valeurs de la solution aux instants de `t_eval` ou `t_span` si `t_eval` vaut `None`
	"""
	return RK(RK1_step, fun, t_span, y0, t_eval)

def RK2_step(fun, t, y, t_next) :
	h = t_next - t
	t_mid = 0.5 * (t + t_next)
	y_mid = y + 0.5 * h * fun(t, y)
	return y + h * fun(t_mid, y_mid)
def RK2(fun, t_span, y0, t_eval = None) :
	"""
	Applique une méthode de RUNGE-KUTTA d'ordre 2
	pour évaluer la solution de l'équation différentielle :
	     | y = `fun`(t, y)
             | y(`t_span[0]`) = `y0`
	
	Parameters
	----------
	step_fun : fonction
		Fonction définissant le calcul d'une itération. Elle doit avoir la signature
		 step_fun(fun, t, y, t_next, args) avec :
		* fun : second membre de l'équation différentielle
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
		* t_next : l'instant suivant
	fun : fonction
		Second membre de l'équation différentielle. Elle doit avoir la signature
		 fun(t, y, args) avec :
		* t : l'instant courant
		* y : l'estimation de la solution à l'instant `t`
	t_span : couple de flottants
		Intervalle de résolution [t_0, t_f]
		La résolution démarre à l'instant t_0 et termine à l'instant t_f.
	y0 : ndarray NumPy, dimension (n, )
		Condition initiale
	t_eval : ndarray NumPy, dimension (n, n_points) ou `None`, optionnel
		Subdivision utilisée pour la résolution
		Les valeurs doivent être triées, commencer par `t_span[0]` et terminer par `t_span[-1]`.
		Si `t_eval` vaut `None`, alors la subdivision est simplement `t_span`.
	
	Returns
	-------
	ndarray NumPy, dimension (n, n_points)
		Estimation des valeurs de la solution aux instants de `t_eval` ou `t_span` si `t_eval` vaut `None`
	"""
	return RK(RK2_step, fun, t_span, y0, t_eval)
