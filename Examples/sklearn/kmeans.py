# -*- encoding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans

data = np.random.rand(100, 3) #生成一个随机数据，样本大小为100, 特征数为3
print("data:\n", data)
#假如我要构造一个聚类数为3的聚类器
estimator = KMeans(n_clusters=3)#构造聚类器
estimator.fit(data)#聚类
label_pred = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和
print("result:")
print("label:\n", label_pred)
print("centroids:\n", centroids)  
print("inertia:\n", inertia)