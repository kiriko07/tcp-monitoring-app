# Dockerfile
# 构建阶段
# 使用官方的 Node.js 16 镜像作为构建环境
FROM node:16-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 生产阶段
# 使用官方的 Nginx 镜像作为 Web 服务器
FROM nginx:stable-alpine
# 从构建阶段复制构建好的静态文件到 Nginx 的默认目录
COPY --from=builder /app/build /usr/share/nginx/html
# 复制我们自定义的 nginx.conf 文件
COPY nginx.conf /etc/nginx/conf.d/default.conf
# 暴露 Nginx 的 80 端口
EXPOSE 80