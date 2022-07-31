#==============×==============#
#      Created by: Alfa-Ex
#=========× Dapsya ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b userbot https://github.com/dapsya/Daps-Userbot /home/userbot/ \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

COPY ./sample_config.env ./config.env* /home/userbot/

WORKDIR /home/userbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
