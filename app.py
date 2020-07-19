from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def calculate():
   # here we declare bmi globally
   bmi=float()
   if request.method=='POST' and 'weight' in request.form and 'height' in request.form:
      try:
         weight=float(request.form.get('weight'))
         height=float(request.form.get('height'))
         bmi=round(weight/(height**2),2)
      except Exception as e:
         print(e) 
   return render_template("index.html",bmi=bmi)


if __name__=='__main__':
    app.run(debug=True)