#!/bin/bash

# author: j0ey1iu
# date: Jan 26, 2021
###############################
# Note that this script might #
# Not work for your mac       #
###############################

# install homebrew
which brew || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew updata && brew upgrade
# install dependencies for vapoursynth
brew install python3 libass zimg imagemagick wget git
# ffmpeg
wget https://evermeet.cx/ffmpeg/ffmpeg-4.3.1.zip
[ ! -d "/usr/local/bin" ] && sudo mkdir /usr/local/bin # need password here
sudo mv ffmpeg /usr/local/bin
rm -f ff*
sudo xattr -dr com.apple.quarantine /usr/local/bin/ff*
if (echo $PATH | grep "/usr/local/bin"); then
    echo "/usr/local/bin is in PATH"
else
    touch ~/.temp && echo "path+=/usr/local/bin" >~/.temp
    source ~/.temp
    rm ~/.temp
fi
# install vapoursynth via homebrew and pip3
brew install VapourSynth
pip3 install vapoursynth
# install python dependencies for compilation
pip3 intall cython meson ninja
# install fftw3f for vapoursynth-mvtools
wget http://www.fftw.org/fftw-3.3.9.tar.gz
tar -xvf fftw-3.3.9.tar.gz
rm fft2-3.3.9.tar.gz
cd fftw-3.3.9
./configure --enable-float --enable-threads
sudo make
sudo make install
cd .. && rm -rf ff*
# pull from github
git clone -r https://github.com/J0ey1iu/VapourSynth-Denoise-Script.git VS
cd VS/vapoursynth-mvtools/build/mac

