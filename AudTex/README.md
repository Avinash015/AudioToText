# Audio-to-Text Transcription

This Python script provides a simple yet powerful solution for transcribing large audio files into text format. It utilizes speech recognition techniques along with audio processing to achieve accurate transcription.

## Features

- **Speech Recognition**: Utilizes the `speech_recognition` library to convert audio input into text.
- **Audio Processing**: Employs the `pydub` library for splitting large audio files into manageable chunks based on silence intervals.
- **Output Formats**: Saves the transcribed text in a `.txt` file and also generates a corresponding `.pdf` document for easy readability.
- **Ease of Use**: Straightforward usage with minimal dependencies, making it accessible for various transcription needs.

## Requirements

Ensure you have Python installed along with the following libraries:

- `speech_recognition`
- `pyaudio`
- `pydub`
- `fpdf`

You can install these dependencies using the provided `requirements.txt` file.

## Usage

1. Place your audio file (in `.wav` format) in the same directory as the script.
2. Run the script providing the path to your audio file as an argument.
    ```
    python transcribe_audio.py path_to_audio_file.wav
    ```
3. The script will transcribe the audio and save the output in both text and PDF formats.

## Example

For demonstration purposes, a sample audio file (`sample_audio.wav`) has been provided. You can run the script using the following command:
```
python transcribe_audio.py sample_audio.wav
```
