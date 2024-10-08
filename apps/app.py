from pathlib import Path
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect #CSRFProtect import하기
from apps.config import config
from flask_login import LoginManager

#LoginManager를 인스턴스화 한다.(객체화)
login_manager = LoginManager()
#login_view 속성에 미로그인시 리다이렉트하는 엔드포인트 지정하기
login_manager.login_view = "auth.signup"
#login_message 속성에 로그인 후에 표시할 메세지 지정하기
#여기서는 아무것도 표시하지 않도록 공백 지정하기
login_manager.login_message = ""

#SQLAlchemy를 인스턴스화 하기
db = SQLAlchemy()
csrf = CSRFProtect() #객체생성하기


    

def create_app(config_key):
    
    # 플라스크 객체(인스턴스) 생성
    app = Flask(__name__)
    
    #앱의 config 설정
    app.config.from_object(config[config_key])
    #앱과 연계하기
    csrf.init_app(app) 
    
    # SQLAlchemy와 앱을 연계한
    db.init_app(app)    
    
    # Migrate와 앱을 연계한다
    Migrate(app, db)
    
    #login_manager를 애플리케이션과 연계
    login_manager.init_app(app)
    
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views
    
    #register_blueprint를 사용해 views 의 curd를 앱에 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    
    # mycrud 패키지로부터 views를 import한다
    from apps.mycrud import views as mycrud_views
    
    #register_blueprint를 사용해 views 의 mycrud 앱에 등록
    app.register_blueprint(mycrud_views.mycrud, url_prefix="/mycrud")
    
    # auth 패키지로부터 views를 import한다
    from apps.auth import views as auth_views
    
    #register_blueprint를 사용해 views 의 auth 앱에 등록
    app.register_blueprint(auth_views.auth, url_prefix="/auth")
        
    return app
