# Dockerfile
# 使用官方的 Python 3.9 运行时作为基础镜像
FROM python:3.9-slim

# 设置工作目录在容器内的 /app
WORKDIR /app

# 将当前目录下的 requirements.txt 复制到容器的 /app 目录
COPY requirements.txt .

# 运行 pip install 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 将当前目录下的所有文件（除了 requirements.txt）复制到容器的 /app 目录
COPY . .

# 暴露 FastAPI 默认的 8000 端口
EXPOSE 8000

# 定义环境变量，告诉 uvicorn 运行 app.main 模块中的 app 对象
ENV PYTHONPATH=/app

# 使用 uvicorn 运行 FastAPI 应用
# --host 0.0.0.0 表示服务器监听所有网络接口，这对于在 Docker 容器中运行至关重要
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]