from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html> <html> 
<head> <style> form {{ background-color: #eee; padding: 20px; 
margin: 0 auto; width: 540px; font: 16px sans-serif; 
border-radius: 10px;}} textarea{{margin: 10px 0; width: 540px; 
height: 120px;}} 
</style> </head> 
<body> 
<form method='post'><label for='rot'>Rotate by: </label><input id='rot' type='text' name='rot'/> 
<textarea name='mess'> {0} </textarea> 
<button type='submit'>Submit</button></form>  
</body>
<script type='text/javascript' src='static/main.js'></script> 
</html>"""

@app.route("/")
def index():
    return form.format("Type your message here.")

@app.route("/", methods=["GET", "POST"])
def encryption():
    rot = 0
    mess = ""
    if request.method == 'POST':
        rot = request.form['rot']
        mess = request.form['mess']
        encrypted = encrypt(mess, int(rot))
        return form.format(encrypted)
    
        
    
   






app.run()