'''
    File name: 02_optimoCentroides.py
    Author: Juan Andres Corrochano
    Date created: 16/04/2019
    Date last modified: 17/04/2019
    Python Version: 3.6
    Description: En este programa se obtiene la gráfica de la inercia tras aplicar el K-means 
		 respecto al número de Clusters para sacar el número óptimo de clusters mediante el
	 	 Elbow Method. El fichero a pasar al script es aquel que tiene los valores de 
	 	 latitud y longitud de las 20 paradas con la media de tiempo de espera mas alta.
	 	 Este fichero esta basado en https://jarroba.com/seleccion-del-numero-optimo-clusters/
'''

# --------------------------------------------------------------------------------------------------
# IMPORTS
# --------------------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# --------------------------------------------------------------------------------------------------
# DEFINES
# --------------------------------------------------------------------------------------------------
DATASET1 = "top20Coordenadas.txt"
LOOPS = 20
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = 'k-means++'
CONVERGENCE_TOLERANCE = 0.001
NUM_THREADS = 8


# --------------------------------------------------------------------------------------------------
# FUNCIONES
# --------------------------------------------------------------------------------------------------
def dataset_to_list_points(dir_dataset):
    """
    Read a txt file with a set of points and return a list of objects Point
    :param dir_dataset:
    """
    points = list()
    with open(dir_dataset, 'rt') as reader:
        for point in reader:
            points.append(np.asarray([float(x) for x in point.split("::")]))
    return points


def plot_results(inertials):
    x, y = zip(*[inertia for inertia in inertials])
    plt.plot(x, y, 'ro-', markersize=8, lw=2)
    plt.grid(True)
    plt.xlabel('Num Clusters')
    plt.ylabel('Inertia')
    plt.show()


def select_clusters(dataset, loops, max_iterations, init_cluster, tolerance, num_threads):
    # Read data set
    points = dataset_to_list_points(dataset)

    inertia_clusters = list()

    for i in range(1, loops + 1, 1):
        # Object KMeans
        kmeans = KMeans(n_clusters=i, max_iter=max_iterations, init=init_cluster, tol=tolerance, n_jobs=num_threads)

        # Calculate Kmeans
        kmeans.fit(points)

        # Obtain inertia
        inertia_clusters.append([i, kmeans.inertia_])

    plot_results(inertia_clusters)


# --------------------------------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    select_clusters(DATASET1, LOOPS, MAX_ITERATIONS, INITIALIZE_CLUSTERS,CONVERGENCE_TOLERANCE, NUM_THREADS)
