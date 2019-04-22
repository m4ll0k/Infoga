FROM alpine:3.9

RUN apk update
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN apk add git
WORKDIR /tmp
RUN git clone https://github.com/m4ll0k/Infoga.git infoga
WORKDIR /tmp/infoga

RUN pip3 install recon
RUN pip3 install requests
RUN pip3 install --upgrade urllib3
RUN pip3 install colorama


ENTRYPOINT ["python3", "infoga.py"]
