FROM python:3.7

# RUN mkdir /WebAPI.CTCESimulation
RUN mkdir /seminario-ziu
WORKDIR /seminario-ziu

RUN pip install flask==1.1.2
RUN pip install werkzeug==0.16.0
RUN pip install flask_restplus==0.13.0
RUN pip install Pillow
RUN pip install qrcode
RUN pip install Image

EXPOSE 5000
CMD ["python", "./app.py","--host", "0.0.0.0"]