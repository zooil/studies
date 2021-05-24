FROM node

COPY run.sh /

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
