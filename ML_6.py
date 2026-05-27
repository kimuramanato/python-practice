from sklearn.utils import resample
import numpy as np
data=np.array([1,2,3,4,5])
n_bootstrap_samples=3
x=[resample(data,replace=True, n_samples=len(data),random_state=i) for i in range(n_bootstrap_samples)]

sorted_bootstrap_samples = [np.sort(sample) for sample in x]

print(sorted_bootstrap_samples)