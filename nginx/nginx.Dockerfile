# Nginx environment

# Use Nginx image as base
FROM nginx

# Remove default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
