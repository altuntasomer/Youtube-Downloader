FROM nginx:1.17.4-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY fullchain.pem /etc/nginx/conf.d/fullchain.pem
COPY options-ssl-nginx.conf /etc/nginx/conf.d/options-ssl-nginx.conf
COPY ssl-dhparams.pem /etc/nginx/conf.d/ssl-dhparams.pem
COPY privkey.pem /etc/nginx/conf.d/privkey.pem

EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]