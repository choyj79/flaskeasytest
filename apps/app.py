from pathlib import Path
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect #CSRFProtect import하기

#SQLAlchemy를 인스턴스화 하기
db = SQLAlchemy()
csrf = CSRFProtect() #객체생성하기

def create_app():
    
    # 플라스크 객체(인스턴스) 생성
    app = Flask(__name__)
    
    #앱의 config 설정
    app.config.from_mapping(
            SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ",
            SQLALCHEMY_DATABASE_URI =f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}", 
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SQLALCHEMY_ECHO = True, #SQL을 콘솔 로그에 출력하는 설정
            WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7Ks6f", #키 랜덤한 값 생성
            ) 
    #앱과 연계하기
    csrf.init_app(app) 
    
    # SQLAlchemy와 앱을 연계한
    db.init_app(app)    
    
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views
    
    #register_blueprint를 사용해 views 의 curd를 앱에 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")     
        
    return app
