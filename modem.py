import os

import numpy as np
from scipy.io import wavfile

def sanity_check_tone_power() -> None:
    """Sanity check the tone_power function."""

    sample_rate = 48000
    N = 160 # Larger N, larger Ratio
    t = np.arange(N) / sample_rate

    space_block = 0.5 * np.sin(2 * np.pi * 2025 * t) # Amplitude of 0.5 (in the middle)
    mark_block = 0.5 * np.sin(2 * np.pi * 2225 * t)
    
    print("SPACE BLOCK TEST\n" + "=" * 20)
    power_2025_space = tone_power(space_block, 2025, sample_rate)
    power_2225_space = tone_power(space_block, 2225, sample_rate)
    print(f"Power at 2025 HZ: {power_2025_space}\nPower at 2225 HZ: {power_2225_space}")
    print(f"{'PASS\n' if power_2025_space > power_2225_space else 'FAIL\n'}")

    print("MARK BLOCK TEST\n" + "=" * 20)
    mark_2025_space = tone_power(mark_block, 2025, sample_rate)
    mark_2225_space = tone_power(mark_block, 2225, sample_rate)
    print(f"Power at 2025 HZ: {mark_2025_space}\nPower at 2225 HZ: {mark_2225_space}")
    print(f"{'PASS\n' if mark_2025_space < mark_2225_space else 'FAIL\n'}")

def tone_power(samples: np.ndarray, target_frequency: int, sample_rate: int) -> float:
    """Get the power for a single target freuqnecy
    
    Args:
        samples (np.ndarray): Numpy array of block of samples
        target_frequency (int): Candidate Frequency (2025 or 2225) in Hz
        sample_rate (int): Sample Rate

    Returns:
        Power for target frequency
    """

    N = len(samples)
    n = np.arange(N) 

    angle = 2 * np.pi * target_frequency * n / sample_rate
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)

    I = np.dot(samples, cos_angle)
    Q = np.dot(samples, sin_angle)

    return I**2 + Q**2

def samples_to_bits(samples: np.ndarray, samples_per_bit: int, sample_rate: int) -> list[int]:
    """Convert samples into blocks, calculate powers from those blocks, and determine bit value.
    
    Args:
        samples (np.ndarray): Numpy array of samples
        samples_per_bit (int): Numerical amount of samples per bit
        sample_rate (int): Sample Rate
    """
    bits = []

    for i in range(0, len(samples) - samples_per_bit + 1, samples_per_bit):
        block_to_check = samples[i: i + samples_per_bit]

        power_space = tone_power(block_to_check, 2025, sample_rate)
        mark_space = tone_power(block_to_check, 2225, sample_rate)
        bit = 0 if power_space > mark_space else 1

        print(f"Power Space: {power_space} | Mark Space: {mark_space} | Bit: {bit}") # Debug
        bits.append(bit)
    
    return bits

def modem_byte_framing(bits: list[int]) -> bytearray:
    """Convert bits into message bytes
    Args:
        bits (list[int]): Array of Bits
    
        Returns:
            Message Byte Array

    """

def decode_wavfile(file_path: str) -> str:
    """Decode a WAV File via a simplified Bell 103 Modem Protocol
    
    Args:
        file_path (str): Path to WAV file to decode.

    Returns:
        A string of the decoded WAV file.
    """
    sample_rate, data = wavfile.read(file_path)
    if sample_rate != 48000 or data.ndim > 1:
        raise Exception(f"{file_path} should be a 48 kilosample per second 16-bit mono WAV file.")

    samples = data.astype(np.float32) / 32768.0 # Convert samples to floats
    bits = samples_to_bits(samples, 160, sample_rate)
    
    return f"{file_path} message: TO BE ADDED HERE"

if __name__ == "__main__":
    decode_wavfile("message.wav")