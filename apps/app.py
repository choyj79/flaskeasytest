from flask import Flask

def create_app():
    # 플라스크 객체(인스턴스) 생성
    app = Flask(__name__)
    
    # crud 패키지로부터 views를 import한다
    from apps.crud import views as crud_views
    
    #register_blueprint를 사용해 views 의 curd를 앱에 등록
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    
    return app