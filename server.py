from flask import Flask, render_template, url_for,request, redirect, send_from_directory
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('webserver/database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["Message"]
		print(f'\n{email},{subject},{message}')
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('webserver/database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["Message"]
		csv_writer=csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

		

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	print(data)
    	write_to_csv(data)
    	return redirect('/contacts.html')
    else:
    	return 'Something went wrong !'





