from typing import TypedDict

from .Box import Box


class KeypointData(TypedDict):
    'Data format for each fram of the AlphaPose output'
    image_id: str
    category_id: int
    keypoints: list[float]
    score: float
    box: list[float]
    idx: list[float]

class SignerData(TypedDict):
    'Data format for generated signer data file'
    scores: list[float]
    roi: Box
    keypoints: list[KeypointData]

class CutData(TypedDict):
    '''type of the cuts json data file'''
    label: str
    start: float
    end: float
    video: str
    playlist: str
