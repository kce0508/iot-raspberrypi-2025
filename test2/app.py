from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
DB_FILE = "userFlie.txt"

# 아이디 중복확인
def id_exists(user_id):
        if not os.path.exists(DB_FILE):
                return False
        with open(DB_FILE, 'r') as f:
                for line in f:
                        saved_id, *_ = line.strip().split()
                        if saved_id == user_id:
                                return True
        return False

# 회원가입
@app.route('/signup', methods=['GET', 'POST'])
def signup():
        if request.method == 'POST':
                user_id = request.form['id']
                pw = request.form['pw']

                if id_exists(user_id):
                        return "이미 존재하는 아이디 입니다. <a href='/signup'> 다시 시도</a>"

                # 최초 가입자=관리자
                is_admin = 1 if not os.path.exists(DB_FILE) or os.path.getsize(DB_FILE) == 0 else 0

                with open(DB_FILE, 'a') as f:
                        f.write(f"{user_id} {pw} {is_admin}\n")

                return f"회원가입 완료! {'관리자' if is_admin else '일반회원'}로 등록되었습니다. <a href='/login'>로그인하러 가기</a>"
        return render_template("signup.html")

# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
        if request.method == 'POST':
                user_id = request.form['id']
                pw = request.form['pw']

                if not os.path.exists(DB_FILE):
                        return "등록된 사용자가 없습니다. <a href='/signup'>회원가입</a>"

                with open(DB_FILE, 'r') as f:
                        for line in f:
                                saved_id, saved_pw, is_admin = line.strip().split()
                                if saved_id == user_id and saved_pw == pw:
                                        if is_admin == '1':
                                                return redirect(url_for('admin_page', username=user_id))
                                        else:
                                                return redirect(url_for('user_page', username=user_id))

                return "로그인 실패. <a href='/login'>다시 시도</a>"
        return render_template("login.html")

# 일반 사용자 화면
@app.route('/user/<username>')
def user_page(username):
        return render_template("user_page.html", username=username)

# 관리자 화면
@app.route('/admin/<username>')
def admin_page(username):
        users = []
        with open(DB_FILE, 'r') as f:
                for line in f:
                        user_id, pw, is_admin = line.strip().split()
                        users.append({'id': user_id, 'pw': pw, 'is_admin': is_admin})
        return render_template("admin_page.html", username=username, users=users)

# 회원 삭제
@app.route('/delete_user', methods=['POST'])
def delete_user():
        target_id = request.form['target_id']
        admin_id = request.form['admin_id']

        with open(DB_FILE, 'r') as f:
                lines = f.readlines()
        with open(DB_FILE, 'w') as f:
                for line in lines:
                        user_id, pw, is_admin = line.strip().split()
                        if user_id != target_id:
                                f.write(line)
        return redirect(url_for('admin_page', username=admin_id))

# 관리자 권한 변경
@app.route('/toggle_admin', methods=['POST'])
def toggle_admin():
        target_id = request.form['target_id']
        admin_id = request.form['admin_id']

        new_lines = []
        with open(DB_FILE, 'r') as f:
                for line in f:
                        user_id, pw, is_admin = line.strip().split()
                        if user_id == target_id:
                                is_admin = '0' if is_admin == '1' else '1'
                        new_lines.append(f"{user_id} {pw} {is_admin}\n")

        with open(DB_FILE, 'w') as f:
                f.writelines(new_lines)

        return redirect(url_for('admin_page', username=admin_id))

# 홈
@app.route('/')
def home():
        return render_template("home.html")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)
