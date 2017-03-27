FROM sitespeedio/webbrowsers:firefox-52.0.1-chrome-57.0

ENV SITESPEED_IO_BROWSERTIME__XVFB true
ENV SITESPEED_IO_BROWSERTIME__CONNECTIVITY__ENGINE tc
ENV SITESPEED_IO_BROWSERTIME__CHROME__ARGS no-sandbox

RUN mkdir -p /usr/src/app && \
    wget -qO- https://github.com/sitespeedio/sitespeed.io/tarball/graphite-1.0 | tar xvz --strip-components=1 -C /usr/src/app
WORKDIR /usr/src/app
RUN npm install --production

COPY start.sh /start.sh

ENTRYPOINT ["/start.sh"]
VOLUME /sitespeed.io
WORKDIR /sitespeed.io

ADD send-annotation.js /usr/src/app/lib/plugins/graphite/send-annotation.js