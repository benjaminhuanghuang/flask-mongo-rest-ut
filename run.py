from app import create_app

env = 'dev'
app = create_app('app.settings.DevConfig', env=env)
app.run(debug=True, port=9527)
