# 使用一个基础镜像，例如 Python 3.10
FROM python:3.10-slim

# 安装必要的系统依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
ENV TZ=Asia/Shanghai
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

# 设置工作目录
WORKDIR /app
ENV PYTHONUNBUFFERED=1
# 复制 requirements.txt 文件到工作目录
COPY requirements.txt /app/

# 安装 Python 依赖
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 复制项目代码（依赖安装完成后，代码变动不会触发重新安装依赖）
COPY . /app
# 设置环境变量（如果需要）
# ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
# ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

# 运行应用程序
CMD ["python", "App.py"]