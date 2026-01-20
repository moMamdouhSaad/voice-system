import numpy as np

def silence(duration_sec: float, sample_rate: int):
    length = int(duration_sec * sample_rate)
    return np.zeros(length, dtype=np.float32)


def concat_audios(audios):
    return np.concatenate(audios)
