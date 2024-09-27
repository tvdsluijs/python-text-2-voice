import os
import subprocess
from pydub import AudioSegment
from pydub.utils import which
from pydub.playback import play
import re
import json
import sys
import warnings

# Suppress SyntaxWarning from pydub
warnings.filterwarnings("ignore", category=SyntaxWarning, module='pydub')

AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

CONFIG_FILE = 'config.json'
AUDIO_FOLDER = 'audio-files'

# Function to create a slug from a string
def create_slug(text):
    text = re.sub(r'\W+', '-', text).lower()
    return re.sub(r'-$', '', text)

# Function to play audio
def play_audio(filename):
    try:
        audio = AudioSegment.from_wav(filename)
        play(audio)
    except Exception as e:
        print(f"Error playing audio: {e}")

# Function to list available voices
def list_voices():
    try:
        result = subprocess.run(['say', '-v', '?'], capture_output=True, text=True)
        voices = result.stdout.splitlines()
        return voices
    except Exception as e:
        print(f"Error listing voices: {e}")
        return []

# Function to convert text to speech
def text_to_speech(text, voice, output_folder):
    try:
        # Create slug for filename
        slug = create_slug(voice + '-' + text)
        output_filename = os.path.join(output_folder, slug)

        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Generate speech using macOS 'say' command
        subprocess.run(['say', '-v', voice, text, '-o', output_filename + '.aiff'])

        # Convert AIFF to WAV with specific parameters
        audio = AudioSegment.from_file(output_filename + '.aiff', format='aiff')
        audio.set_frame_rate(48000).set_sample_width(4).export(output_filename + '.wav', format='wav', parameters=["-acodec", "pcm_f32le"])

        # Clean up AIFF file
        os.remove(output_filename + '.aiff')
        outpufile = f"{output_filename}.wav"
        play_audio(outpufile)
        print(f"Speech saved as {outpufile}")
    except Exception as e:
        print(f"Error during text-to-speech: {e}")

# Function to save the chosen voice to config file
def save_voice_to_config(voice):
    try:
        with open(CONFIG_FILE, 'w') as config_file:
            json.dump({"voice": voice}, config_file)
        print(f"Voice '{voice}' saved to config file.")
    except Exception as e:
        print(f"Error saving voice to config: {e}")

# Function to load the chosen voice from config file
def load_voice_from_config():
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as config_file:
                config = json.load(config_file)
                return config.get("voice", None)
        else:
            return None
    except Exception as e:
        print(f"Error loading voice from config: {e}")
        return None

# Main function
def main():
    # Ensure audio-files folder exists
    if not os.path.exists(AUDIO_FOLDER):
        os.makedirs(AUDIO_FOLDER)

    print("Choose an option:")
    print("1: Choose and save a voice")
    print("2: Enter text to be spoken (requires saved voice)")

    option = input("Enter option (1 or 2): ")

    if option == "1":
        # List available voices and let the user choose one
        voices = list_voices()
        if not voices:
            print("No voices available.")
            return

        for i, voice in enumerate(voices):
            print(f"{i + 1}: {voice}")

        chosen_voice_index = int(input("Enter the number of the chosen voice: ")) - 1
        if 0 <= chosen_voice_index < len(voices):
            chosen_voice = voices[chosen_voice_index].split()[0]  # Use only the voice name
            save_voice_to_config(chosen_voice)
        else:
            print("Invalid voice selection.")

    elif option == "2":
        # Load voice from config file
        chosen_voice = load_voice_from_config()
        if not chosen_voice:
            print("No voice is saved in the config file. Please choose a voice first (Option 1).")
            return

        # Enter text to be spoken
        text = input("Enter the text to be spoken: ")
        if text:
            text_to_speech(text, chosen_voice, AUDIO_FOLDER)
        else:
            print("No text entered.")
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
