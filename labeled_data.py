import numpy as np

def import_labeled_data():
	csv = np.genfromtxt('data/train.csv', delimiter=",")
	label = csv[1:, 0]
	fotos_sin_bias = csv[1:, 1:]
	fotos_sin_bias /= 783
	M = len(fotos_sin_bias)  # dimension de data
	bias = np.ones((M, 1))
	fotos = np.append(fotos_sin_bias, bias, axis=1)
	v = 10 * [0]
	for k in range(M):
		v[int(label[k])] += 1

	A = np.empty((10,),dtype=object)
	for i in range(10):
		A[i] = np.empty((v[i], 785))

	cont = 10 * [0]
	for k in range(M):
		i = int(label[k])
		A[i][cont[i]] = fotos[k]
		cont[i] += 1

	del fotos  # libero memoria de las fotos (ya no se usaran)

	return A, v