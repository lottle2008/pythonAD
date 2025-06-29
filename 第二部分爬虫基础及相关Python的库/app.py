from flask import Flask, render_template_string, request

app = Flask(__name__)

# 登录页面 HTML 模板
login_page_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登录页面</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .message {
            margin-top: 20px;
            font-size: 1.2em;
            color: green;
        }
        .hidden {
            display: none;
        }
        .big-message {
            font-size: 2em;
            color: #28a745;
        }
    </style>
</head>
<body>

    <div class="login-container" id="login-container">
        <h2>登录</h2>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="用户名">
            <input type="password" name="password" placeholder="密码">
            <button type="submit">登录</button>
        </form>
    </div>

    <div class="message hidden" id="message"></div>

</body>
</html>
'''

# 登录成功后的页面 HTML
welcome_page_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>欢迎页面</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .big-message {
            font-size: 2em;
            color: #28a745;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="big-message">
        欢迎加入 郑州大学商务分析与数据智能<br>
        这里你能学到强大的爬虫技术 和数据分析技术
    </div>
</body>
</html>
'''

# 登录失败页面 HTML
error_page_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登录失败</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .message {
            font-size: 2em;
            color: red;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="message">
        用户名或密码错误！
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(login_page_html)


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 检查用户名和密码是否正确
    if username == 'zzu' and password == '123456':
        return render_template_string(welcome_page_html)
    else:
        return render_template_string(error_page_html)


if __name__ == '__main__':
    app.run(debug=True)
