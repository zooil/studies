FROM node:12-alpine
WORKDIR /app
COPY $PWD/package*.json /app
RUN npm install
COPY $PWD/. /app
CMD [ "npm", "start" ]
EXPOSE 3000
