import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from kmeans import KMeans

def gen_data():
    x,y = make_blobs(centers = 4, cluster_std= 0.7, random_state = 0)
    return x,y
def main():
    x,y = gen_data()
    km = KMeans(4,x,y)
    km.run_kmeans()
    print('hi!')
    plt.scatter(x[:, 0], x[:, 1], c=km.assigned_centroid, cmap='viridis')
    plt.scatter(km.clustercent[:, 0], km.clustercent[:, 1], c='red', marker='X', s=200)
    plt.show()
if __name__ == "__main__":
    main()
