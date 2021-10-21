# musicboard
課題で作成した音楽スレ

## 必要なもの
### 環境
- pyenv 
- pipenv
### 詳細
- python 3.9.6
- django 3.8.2
- psycopg2-binary
- django-bootstrap-v5
### settings_local.py
- settings.pyの拡張
```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[ANY_NAME]',
        'USER': '[ANY_USER]',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 導入
### python設定
```
pyenv install 3.9.6
pyenv local 3.9.6
pipenv --python 3.9.6
pipenv shell
```
### 必要なライブラリ
```
pipenv install django psycopg2-binary django-bootstrap-v5
```