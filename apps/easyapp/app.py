from email_validator import validate_email, EmailNotValidError
from flask import (Flask, render_template , url_for, current_app, 
                   g, request, redirect, flash) #모듈 import

app = Flask(__name__)

# SECRET_KEY를 추가한다
app.config["SECRET_KEY"] = b"\xfd_@E\x17\xd8'\xf6e-\xff\xe4\xa2MC2"

# URL과 실행하는 함수를 매핑한다
@app.route("/")
def index():
    return "Hello, Flaskbook!"

# @app.route("/hello")
# def hello():
#     return "hello, world!!"

# @app.route("/hello", methods=["GET","POST"], endpoint="hello-endpoint")
# def hello():
#     return "Hello, world!!"

@app.route("/hello/<name>", methods=["GET","POST"], endpoint="hello-endpoint")
def hello1(name):
    return f"Hello, {name}"

#show_name엔드포인트 작성
@app.route("/name/<name>")
def show_name(name):
    #변수를 템플릿 엔진에게 건넨다
    return render_template("index.html",name=name)

with app.test_request_context():
    #/
    print(url_for("index"))
    #/hello/world
    print(url_for("hello-endpoint",name="world"))
    #/name/easy?page=1
    print(url_for("show_name", name="easy", page="1"))

# 여기에서 호출하면 오류가 된다
# print(current_app)

# 애플리케이션 컨텍스트를 취득하여 스택에 push한다
ctx = app.app_context()
ctx.push()

# current_app에 접근이 가능해진다
print(current_app.name)
# >> apps.minimalapp.app

# 전역 임시 영역에 값을 설정한다
g.connection = "connection"
print(g.connection)
# >> connection

with app.test_request_context("/users?updated=true"):
    # true가 출력된다
    print(request.args.get("updated"))
    
@app.route("/contact")
def contact():
    return render_template("contact.html") #html파일 렌더링

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        #form속성을 사용해서 폼의 값을 취득
        username = request.form["username"]
        email = request.form["email"]        
        description = request.form["description"]
        
        is_valid = True
        if not username:
            flash("사용자명은 필수입니다")
            is_valid = False

        if not email:
            flash("메일 주소는 필수입니다")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False
        
        if not description:
            flash("문의 내용은 필수입니다")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))

        flash("문의해 주셔서 감사합니다.")
        #이메일보내기(차후 구현)
        
        #contact 엔드포인트로 리다이렉트
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
        