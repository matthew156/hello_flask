from flask import Flask  
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
  return "dojo"
    

@app.route('/say/michael')
def michael():
  return "Hi Michael!"
    
@app.route('/say/john')
def john():
  return "Hi John"
    
@app.route('/hello/<string:matt>/<int:num>')
def matt(matt, num):
  return f"Hello {matt * num}"
    

if __name__=="__main__":   # Ensure this file is being run directly and 
    app.run(debug=True)    # Run the app in debug mode.

