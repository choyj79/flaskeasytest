from email_validator import validate_email, EmailNotValidError
from flask import (Flask, render_template , url_for, current_app, 
                   g, request, redirect, flash, make_response, session) #모듈 import
import logging
import os #os모듈 추가히기
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message  #Mail 클래시 import하기

app = Flask(__name__)
# SECRET_KEY를 추가한다
# app.config["SECRET_KEY"] = b"\xfd_@E\x17\xd8'\xf6e-\xff\xe4\xa2MC2"
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"

#로그레벨을 설정한다.
app.logger.setLevel(logging.DEBUG)

#리다이렉트를 중단하지 않도록 한다.
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
#DebugToolbarExtension 에 애플리케이션을 설정
toolbar = DebugToolbarExtension(app)

# Mail 클래스의 컨피그를 추가한다
# print('=========////',os.environ.get("MAIL_SERVER"))
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'jojju486@gmail.com'
# app.config['MAIL_PASSWORD'] = 'stkm cgck saeq hlju'  # 앱 비밀번호 사용

# flask-mail 확장을 등록한다
mail = Mail(app)

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

def send_email(to, subject, template, **kwargs):    
    """메일을 송신하는 함수"""
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! : {template}")
    msg = Message(subject, sender='jojju486@gmail.com', recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)

with app.test_request_context("/users?updated=true"):
    # true가 출력된다
    print(request.args.get("updated"))
    
@app.route("/contact")
def contact():
    #응답 객체 취득
    response = make_response(render_template("contact.html"))
    #쿠키 설정
    response.set_cookie("flaskweb key","flaskweb vlaue")
    #세션 설정
    session["username"] = "cho"
    #응답 오브젝트 반환
    return response 

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

        # 메일을 보낸다              
        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail",
            username=username,
            description=description,
        )
    
        # 문의 완료 엔드포인트로 리다이렉트한다
        flash("문의 내용은 메일로 송신했습니다. 문의해 주셔서 감사합니다.")
   
        #contact 엔드포인트로 리다이렉트
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")

     
app.logger.critical("fatal error")
app.logger.error("error")
app.logger.warning("warning")
app.logger.info("info")
app.logger.debug("debug")
