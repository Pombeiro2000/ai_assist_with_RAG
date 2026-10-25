FROM node:22-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# Local: ng serve with live reload (code is bind-mounted)
FROM deps AS dev
ENV NG_CLI_ANALYTICS=false
EXPOSE 4200
CMD ["npx", "ng", "serve", "--host", "0.0.0.0", "--port", "4200"]

FROM deps AS build
COPY . .
RUN npx ng build --configuration production

# Production: static files served by nginx, which also proxies /api
FROM nginx:1.27-alpine AS prod
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/frontend/browser /usr/share/nginx/html
EXPOSE 80
