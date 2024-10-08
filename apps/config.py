from pathlib import Path

basedir = Path(__file__).parent.parent

#BaseConfig 클래스 작성하기
class BaseConfig:
    SECRET_KEY = "2AZSMss3p5QPbcY2hBsJ"
    WTF_CSRF_SECRET_KEY = "AuwzyszU5sugKN7KZs6f"

# BaseConfig 클래스를 상속하여 LocalConfig 클래스를 작성한다
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


# BaseConfig 클래스를 상속하여 TestingConfig 클래스를 작성한다
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    # 이미지 업로드처에 tests/detector/images를 지정한다
    UPLOAD_FOLDER = str(Path(basedir, "tests", "detector", "images"))


# config 사전에 매핑한다
config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
    