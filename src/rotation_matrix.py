import numpy as np


def calculate_rotation_matrix(omega: float, phi: float, kappa: float) -> np.ndarray:
    """
    Calculates rotation matrix from euler rotation angles.

    Parameters
    ----------
    omega : float
        Rotation around x-axis.
    phi : float
        Rotation around y-axis.
    kappa : float
        Rotation around z-axis.

    Returns
    -------
    _ : np.ndarray
        Rotation matrix.
    """
    r11 = np.cos(phi) * np.cos(kappa)
    r12 = -np.cos(phi) * np.sin(kappa)
    r13 = np.sin(phi)
    r21 = (np.cos(omega) * np.sin(kappa)) + (np.sin(omega) * np.sin(phi) * np.cos(kappa))
    r22 = (np.cos(omega) * np.cos(kappa)) - (np.sin(omega) * np.sin(phi) * np.sin(kappa))
    r23 = -np.sin(omega) * np.cos(phi)
    r31 = (np.sin(omega) * np.sin(kappa)) - (np.cos(omega) * np.sin(phi) * np.cos(kappa))
    r32 = (np.sin(omega) * np.cos(kappa)) + (np.cos(omega) * np.sin(phi) * np.sin(kappa))
    r33 = np.cos(omega) * np.cos(phi)

    return np.array([[r11, r12, r13], [r21, r22, r23], [r31, r32, r33]])