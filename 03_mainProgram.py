'''
    File name: 03_mainProgram.py
    Author: Juan Andres Corrochano
    Date created: 16/04/2019
    Date last modified: 17/04/2019
    Python Version: 3.6
    Description: En este programa se calculan los centroides y se grupan los puntos reales a los 
		 mismos, pintando una grafica con diferentes colores y creando un fichero con las 
	 	 coordenadas de los centroides para pintarlos en un mapa posteriormente.
	 	 Basado en: https://jarroba.com/k-means-python-scikit-learn-ejemplos/
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
NUM_CLUSTERS = 5
MAX_ITERATIONS = 10
INITIALIZE_CLUSTERS = ['k-means++', 'random']
CONVERGENCE_TOLERANCE = 0.001
NUM_THREADS = 8
COLORS = ['red', 'blue', 'green', 'yellow', 'gray', 'pink', 'violet', 'brown', 'cyan', 'magenta']


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
            

def print_results(centroids, num_cluster_points):
    print ('\n\nFINAL RESULT:')
    with open("centroides.txt","w") as f:
        for i, c in enumerate(centroids):
            print ('\tCluster %d' % (i + 1))
            print ('\t\tNumber Points in Cluster %d' % num_cluster_points.count(i))
            print ('\t\tCentroid: %s' % str(centroids[i]))
            f.write(str(centroids[i]) + '\n')


def plot_results(centroids, num_cluster_points, points):
    plt.plot()
    for nc in range(len(centroids)):
        # plot points
        points_in_cluster = [boolP == nc for boolP in num_cluster_points]
        for i, p in enumerate(points_in_cluster):
            if bool(p):
                plt.plot(points[i][1], points[i][0], linestyle='None',
                         color=COLORS[nc], marker='.')
        # plot centroids
        centroid = centroids[nc]
        plt.plot(centroid[1], centroid[0], 'o', markerfacecolor=COLORS[nc],
                 markeredgecolor='k', markersize=10)
    plt.show()


def k_means(dataset, num_clusters, max_iterations, init_cluster, tolerance,
            num_threads):
    # Read data set
    points = dataset_to_list_points(dataset)

    # Object KMeans
    kmeans = KMeans(n_clusters=num_clusters, max_iter=max_iterations,
                    init=init_cluster, tol=tolerance, n_jobs=num_threads)

    # Calculate Kmeans
    kmeans.fit(points)

    # Obtain centroids and number Cluster of each point
    centroids = kmeans.cluster_centers_
    num_cluster_points = kmeans.labels_.tolist()

    # Print final result
    print_results(centroids, num_cluster_points)

    # Plot Final results
    plot_results(centroids, num_cluster_points, points)


if __name__ == '__main__':
    k_means(DATASET1, NUM_CLUSTERS, MAX_ITERATIONS, INITIALIZE_CLUSTERS[0],
            CONVERGENCE_TOLERANCE, NUM_THREADS)
