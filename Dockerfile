FROM promethee/pimoroni.inky
WORKDIR /usr/src/app
COPY ./CODE2000.TTF ./main.py ./
CMD python3 main.py
