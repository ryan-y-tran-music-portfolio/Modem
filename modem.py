from scipy.io import wavfile

def decode_wavfile(file_path: str) -> str:
    """Decode a WAV File via a simplified Bell 103 Modem Protocol
    
    Args:
        file_path: Path to WAV file to decode.

    Returns:
        A string of the decoded WAV file.
    """
    
    return f"When we're done, we will decode {file_path}."

if __name__ == "__main__":
    print(decode_wavfile("message.wav"))