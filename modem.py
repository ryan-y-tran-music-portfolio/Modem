import os

import numpy as np
from scipy.io import wavfile

def sanity_check_tone_power() -> None:
    """Sanity check the tone_power function."""

def tone_power(samples: np.ndarray, target_frequency: int, sample_rate: int) -> float:
    """Get the power for a single target freuqnecy
    
    Args:
        samples: Numpy array of block of samples
        target_frequency: Candidate Frequency (2025 or 2225) in Hz
        sample_rate: Sample Rate

    Returns:
        Power for target frequency
    """

    N = len(samples)
    n = np.arrange(N) 

    angle = 2 * np.pi * target_frequency * n / sample_rate
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)

    I = np.dot(samples, cos_angle)
    Q = np.dot(samples, sin_angle)

    return I**2 + Q**2

def decode_wavfile(file_path: str) -> str:
    """Decode a WAV File via a simplified Bell 103 Modem Protocol
    
    Args:
        file_path: Path to WAV file to decode.

    Returns:
        A string of the decoded WAV file.
    """
    sample_rate, data = wavfile.read(file_path)
    if sample_rate != 48000 or data.ndim > 1:
        raise Exception(f"{file_path} should be a 48 kilosample per second 16-bit mono WAV file.")

    samples = data.astype(np.float32) / 32768.0 # Convert samples to floats
    
    return f"{file_path} message: TO BE ADDED HERE"

if __name__ == "__main__":
    try:
        print(decode_wavfile("message.wav"))
    except Exception as e:
        print (e)