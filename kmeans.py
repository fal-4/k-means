import numpy as np
class KMeans:
    def __init__(self,num_clusters,x,y):
        self.num_clusters = num_clusters
        self.x = x
        self.y = y
    def sel_center(self):
        self.clustercent = np.random.default_rng(12345).choice(self.x,self.num_clusters,replace = False)
    def assign_centroid(self):
        self.assigned_centroid = []
        for i in range (len(self.x)):
            dist = []
            for j in range (self.num_clusters):
                dist.append(np.linalg.norm(self.x[i] - self.clustercent[j]))
            self.assigned_centroid.append(np.argmin(dist))
    def recalc_centroid(self):
        mean = 0
        new_clustercenter = []
        center_changed_num = 0
        updated = True
        for i in range(self.num_clusters):
            sum = 0
            count = 0
            for j in range (len(self.x)):
                if self.assigned_centroid[j] == i:
                    sum += self.x[j]
                    count += 1
            mean = sum/count
            new_clustercenter.append(mean)
            if not np.array_equal(new_clustercenter[i], self.clustercent[i]):
                self.clustercent[i] = new_clustercenter[i]
                center_changed_num += 1
        if center_changed_num == 0:
            updated = False
            return updated
        else:
            updated = True
            return updated
    def run_kmeans(self):
        self.sel_center()
        for _ in range(100):
            self.assign_centroid()
            updated = self.recalc_centroid()
            if(updated == False):
                break
            

        





                
            



        
    