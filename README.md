## Installation and setup instructions

### Update and install required packages
sudo apt-get update  
sudo apt build-essential git python-dev python3-dev python-pip python-distutils-extra tesseract-ocr tesseract-ocr-eng libopencv-dev libtesseract-dev libleptonica-dev python-all-dev swig libcv-dev python-opencv python-numpy python-setuptools build-essential subversion autoconf automake libtool libpng12-dev libjpeg62-dev libtiff4-dev zlib1g-dev install libicu-dev libpango1.0-dev libcairo2-dev  

### Clone the repository
git clone https://github.com/vikramriyer/ttsdaisy_v4.git  

### Install leptonica (required by tesseract ocr)
wget http://www.leptonica.com/source/leptonica-1.74.4.tar.gz  
tar xvf leptonica-1.74.tar.gz  
cd leptonica-1.74  
./configure  
make  
sudo make install  

### install anaconda from conda.io, create environment and install requirements.txt packages
bash <downloaded_filename>.sh  
conda create -n <whatever_env_name>  
pip install -r requirements.txt (make sure to be in the ttsdaisy_v4 directory before running the command)  


## References:
https://medium.com/@lucas63/installing-tesseract-3-04-in-ubuntu-14-04-1dae8b748a32  
https://gist.github.com/rajmani1995/cae8a16056e44bd901a6d17d8f1a7fbf  
https://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet  
https://www.anaconda.com/download/#linux  
