from app import app

# Vercel yêu cầu biến 'app' phải sẵn sàng ở cấp độ module
if __name__ == "__main__":
    app.run()