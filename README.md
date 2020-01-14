##### Django搭建后台服务
#### 在setting.py中设置解决404问题
```
'DIRS': [
            #os.path.join(BASE_DIR,'django-vue/dist')
            'django-vue/dist'
        ],
		STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "django-vue/dist/static"),
]
```