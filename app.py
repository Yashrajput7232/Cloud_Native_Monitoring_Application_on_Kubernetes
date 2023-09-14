import psutil
from flask import Flask ,render_template
 
app=Flask(__name__)
@app.route('/')
def index():
    cpu_percent=psutil.cpu_percent()
    memeory_usage=psutil.virtual_memory().percent
    message=None
    if cpu_percent>80 or memeory_usage>80 :
        message="high usage if detected so scale up" 
    return render_template("index.html",cpu_metric=cpu_percent,mem_metric=memeory_usage)


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')