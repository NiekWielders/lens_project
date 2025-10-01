from utils import cosmology
import numpy as np

fid_cosmo = {
 "H0": 70,
 "omega_m_0": 0.3,
 "omega_k_0": 0.0,
 "omega_lambda_0": 0.7,
 }
H_tolerance = 0.01
z_range = np.array([0.0, 0.5, 1.0])

print(cosmology.hubble(z_range, fid_cosmo))