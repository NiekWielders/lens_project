import numpy as np

def hubble(redshift: float, cosmo_dict: dict[float]) -> float:
    """Hubble Parameter.
    Calculate the Hubble parameter at a given redshift using the cosmological parameter values
    provided.
    Parameters
    ----------
    redshift : float or numpy.ndarray
     Redshift(s) at which the Hubble parameter should be calculated
    cosmo_dict : dict
     Dictionary of cosmological constants. Must contain the following keys:
     * ``H0``: The Hubble parameter value at redshift zero.
     * ``omega_m_0``: The matter density at redshift zero.
     * ``omega_k_0``: The curvature density at redshift zero.
     * ``omega_lambda_0``: The dark energy density at redshift zero.
    Returns
    -------
    float or numpy.ndarray
     Value of the Hubble parameter (km/s/Mpc) at the specified redshift(s) for a given cosmology.
    Notes
    -----
    This function implements the calculation of the Hubble parameter as follows:
    .. math::
     H(z) = \sqrt{H_0^2 (\Omega_{m,0}(1+z)^3 + \Omega_{k,0}(1+z)^2 +
     \Omega_{\Lambda,0})}
    """

    hubble_const = cosmo_dict["H0"]
    matter = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    curvature = cosmo_dict["omega_k_0"] * (1 + redshift) ** 2
    dark_energy = cosmo_dict["omega_lambda_0"]

    return np.sqrt(
        hubble_const**2 * (matter + curvature + dark_energy)
    )