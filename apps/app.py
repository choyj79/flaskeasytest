from pathlib import Path
from flask import Flask, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#SQLAlchemy를 인스턴스화 하기
db = SQLAlchemy()

def create_app():
    # 플라스크 객체(인스턴스) 생성
    app = Flask(__name__)
    
    #앱의 config 설정
    print(Path(__file__).parent.parent)
    app.config.from_mapping(SECRET_KEY = b"\xfd_@E\x17\xd8'\xf6e-\xff\xe4\xa2MC2", SQLALCHEMY_DATABASE_URI =f"sqlite:///{Path(__file__).parent.parent/'local.sqlite'}", SQLALCHEMY_TRACK_MODIFICATIONS=False)
    db.init_app(app)
    Migrate(app, db)
    
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views
    
    #register_blueprint를 사용해 views 의 curd를 앱에 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")    
        
    return app