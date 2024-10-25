from typing import List

from pydantic import BaseModel


class AudioTranscription(BaseModel):
    text: str


class Word(BaseModel):
    word: str
    start: float
    end: float


class Segment(BaseModel):
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: List[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float


class AudioTranscriptionVerbose(BaseModel):
    language: str
    duration: float
    text: str
    words: List[Word]
    segments: List[Segment]