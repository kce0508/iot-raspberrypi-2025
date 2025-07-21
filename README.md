# iot-raspberrypi-2025

## 1일차
- LED
    <img src="./image/ras0003.png" width="300">
    
- 스위치

## 2일차
- 온습도 센서

## 3일차
- 부저

## 4일차

- 릴레이 모듈 : 저전압 제어 신호로 고전압 회로를 ON/OFF할 수 있게 해주는 전자 스위치 모듈

    <img src="./image/ras0002.png" width="400">

    |이름|상태|기능| 
    |:--|:--|:--|
    |COM(Common)|공통 단자|기준 전원 또는 GND|
    |NO(Normally Open)|평소에는 OFF(열림)|릴레이 ON시 닫혀서 회로 연결|
    |NC(Normally Closed)|평소에는 ON(닫힘)|릴레이 ON시 열려서 회로 끊김|

- 릴레이모듈 사용해서 led제어
    - GPIO에서 VCC신호를 릴레이의 IN핀으로 보내면, 릴레이 내부의 전자석이 작동 -> 접점이 붙음 -> 회로가 연결된다.
    - 연결
    <img src="./image/ras0001.jpg" width="400">

    - 동작

    https://github.com/user-attachments/assets/b6044752-a866-4639-91b0-49174165eec7

## 5일차

## 6일차

#### Flask 
- 웹 서버와 웹 애플리케이션을 빠르게 만들 수 있게 해주는 파이썬 마이크로 프레임워크

- 기본 구조

    ``` python
        from flask import Flask
        app = Flask(__name__)       # 서버 객체 생성

        @app.route('/')             # 루트 URL에 대한 응답 정의
        def hello():
            return "Hello World"

        if __name__ == "__main__":
            app.run(host='0.0.0.0') # 모든 아이피 처리 가능
    ```

## 7일차

#### Flask

##### render_template
- Flask에서 HTML파일을 웹페이지로 표시할 때 사용하는 함수, HTML안에 동적인 값을 넣어서 브라우저에 보여줄 수 있게 해준다.

- 사용 방법

    ```python 
        from flask import Flask, render_temp

        app = Flask(__name__)

        @app.route('/')
        def home():
            return rendeer_template('index.html', name="user", age=25)
    ```
    - templates/index.html 파일안에서
    ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title>홈페이지</title>
        </head>
        <body>
            <h1>안녕하세요 {{name}} 님</h1>
            <h1>당신의 나이는 {{age}}세 입니다. </h1>
        </body>
        </html>
    ```
    - 주의 : render_template에서 사용하는 HTML 파일은 반드시 templates 폴더 안에 있어야 한다.
