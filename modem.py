import os

from scipy.io import wavfile

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
    
    return f"{file_path} message: TO BE ADDED HERE"

if __name__ == "__main__":
    try:
        print(decode_wavfile("message.wav"))
    except Exception as e:
        print (e)