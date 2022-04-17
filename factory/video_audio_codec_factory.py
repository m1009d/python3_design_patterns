#!/usr/bin/env python3

# pylint: disable=missing-class-docstring,missing-function-docstring

"""Factory pattern.

The factory pattern defines an interface for creating an object, but let's
subclasses decide which class to instantiate.
Factory methods let a class defer instantiation to subclasses.
"""

from abc import ABC, abstractmethod
from typing import Tuple


class AudioCodec(ABC):
    """Abstract class to encode audio stream."""

    @abstractmethod
    def encode(self):
        """Abstract method to enconde an audio stream."""


class VideoCodec(ABC):
    """Abstract class to encode video stream."""

    @abstractmethod
    def encode(self):
        """Abstract method to enconde an audio stream."""


class CodecFactory(ABC):
    """
    Factory class.

    This class doesn't create instances by itself, but rather provides
    an interface to subclasses which are responsible to instantiate objects.
    """

    @abstractmethod
    def make(self) -> Tuple[AudioCodec, VideoCodec]:
        """Abstract method to make the required media stream."""


class WAVAudioCodec(AudioCodec):
    """WAV Audio Codec class."""

    def encode(self):
        """Encode WAV audio."""
        print('Encoding audio to WAV')


class AACAudioCodec(AudioCodec):
    """AAC Audio Codec class."""

    def encode(self):
        """Encode AAC audio."""
        print('Encoding audio to AAC')


class MP4AudioCodec(VideoCodec):
    """MP4 Video Codec class."""

    def encode(self):
        """Encode MP4 video."""
        print('Encoding video to MP4')


class AVIAudioCodec(VideoCodec):
    """AVI Video Codec class."""

    def encode(self):
        """Encode AVI video."""
        print('Encoding video to AVI')


class LosslessCodecFactory(CodecFactory):
    """Factory subclass to create Lossless media."""

    def make(self) -> Tuple[AVIAudioCodec, WAVAudioCodec]:
        """Make lossless media."""
        return (AVIAudioCodec(), WAVAudioCodec())


class CompressedlessCodecFactory(CodecFactory):
    """Factory subclass to create Compressed media."""

    def make(self) -> Tuple[MP4AudioCodec, AACAudioCodec]:
        """Make compressed media."""
        return (MP4AudioCodec(), AACAudioCodec())


def ask_user() -> CodecFactory:
    """Ask user which type of media to create and return the factory subclass."""
    obj_map = {
        '1': LosslessCodecFactory(),
        '2': CompressedlessCodecFactory()
    }

    while True:
        answer = input('''
            Select pizza:
                1 - Lossless media
                2 - Compressed media

            : ''')
        if answer in obj_map:
            return obj_map[answer]
        print('{answer!r} is not a valid option!')


def main(media: CodecFactory) -> None:
    """Let's create the chosen media."""
    audio, video = media.make()
    audio.encode()
    video.encode()


if __name__ == "__main__":

    main(ask_user())
