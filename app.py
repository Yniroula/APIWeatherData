from flask import Flask, render_template, request
import requests
import config

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
	error_msg = None
	if request.method == 'POST':
		city = request.form['city']
		api_key = (config.api_key)
		url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
		response = requests.get(url)
		if response.status_code == 200:
			data = response.json()
			temp = data['main']['temp']
			return render_template('index.html', city=city, temp=temp)
		else:
			error_msg = ('Failed to get data. Please enter a city name.')
	return render_template('index.html', error_msg=error_msg)


if __name__ == '__main__':
	app.run()
   