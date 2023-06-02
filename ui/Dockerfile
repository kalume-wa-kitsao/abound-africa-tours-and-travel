FROM node:20.2-alpine3.17

WORKDIR /opt/ui/

COPY package*.json /opt/ui/

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
