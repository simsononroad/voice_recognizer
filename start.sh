#/bin/bash
set -e

git clone https://github.com/simsononroad/voice_recognizer.git
cd voice_recognizer/
python3 -m venv myenv
source myenv/bin/activate
pip3 install speechrecognition
pip3 install pyttsx3
pip3 install requests
sudo apt update
sudo apt install portaudio19-dev python3-pyaudio
pip3 install pyaudio
read -p "A program létre fog hozni egy wledip.txt file-t. Miután belépett a szerkesztőbe nyomjon egy 'i' betűt utána csak és kizárólag az wled ip címét írja be. Miután megvan nyomja meg az 'esc' gombot majd írja be ezt: ':x' majd nyomjon egy entert? (I/N): " confirm && [[ $confirm == [iI] ]] || exit 1
vim wledip.txt
echo "=================================="
echo "   Python libary-k telepítve.     "
echo "   Created By: Gyuris Dániel      "