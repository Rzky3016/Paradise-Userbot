# Feri Ganteng
FROM biansepang/weebproject:buster
#
# Feri
#
RUN git clone -b Linux-Userbot https://github.com/ferikunn/Linux-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ferikunn/Linux-Userbot/Linux-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
