# LORD USERBOT
FROM koala21/kampangbot:buster

#
# LORD
#
RUN git clone -b SAYA-USERBOT https://github.com/ferikunn/Saya-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ferikunn/Saya-Userbot/Saya-Userbot/requirements.txt

CMD ["python3","-m","userbot"]
