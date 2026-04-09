from flask import Flask,render_template,request
import string
app=Flask(__name__)
en_letter=string.ascii_letters
ar_letters = "ابتثجحخدذرزسشصضطظعغفقكلمنهويأإآؤئبة " 
punctuation= string.punctuation
arqam= string.digits
@app.route("/",methods=["GET", "POST"])
def home():
    return render_template("index.html")
@app.route("/t" ,methods=["GET", "POST"])
def tshfir():
    if request.method=="POST":
        mess_moushfr=[]
        mess=request.form.get("dinp",0)
        armz=int(request.form.get("rmz")or 0)
        for i in (mess):
            
            if i in (en_letter):
                mess_moushfr.append(en_letter[(en_letter.index(i) - armz) % len(en_letter)])
            elif i in (ar_letters):
                mess_moushfr.append(ar_letters[(ar_letters.index(i) - armz) % len(ar_letters)])
            elif i in (punctuation):
                mess_moushfr.append(punctuation[(punctuation.index(i) - armz) % len(punctuation)])
            elif i in (arqam):
                mess_moushfr.append(arqam[(arqam.index(i) - armz) % len(arqam)])
        return render_template("tshfir.html", mess="".join(mess_moushfr) ,butt="تشفير",pla="ستظهر رسالتك المشفرة هنا")
    else:
        return render_template("tshfir.html", mess="" ,butt="تشفير",pla="ستظهر رسالتك المشفرة هنا")
@app.route("/f",methods=["POST","GET"])
def  fktshfir():
    if request.method=="POST":
        mess_moushfr=[]
        mess=request.form.get("dinp",0)
        armz=int(request.form.get("rmz")or 0)
        for i in (mess):
            
            if i in (en_letter):
                mess_moushfr.append(en_letter[(en_letter.index(i) + armz) % len(en_letter)])                         
            elif i in (ar_letters):
                mess_moushfr.append(ar_letters[(ar_letters.index(i) + armz) % len(ar_letters)])
            elif i in (punctuation):
                mess_moushfr.append(punctuation[(punctuation.index(i) + armz) % len(punctuation)])
            elif i in (arqam):
                mess_moushfr.append(arqam[(arqam.index(i) + armz) % len(arqam)])
        return render_template("fktshfir.html", mess="".join(mess_moushfr) ,butt="فك التشفير" )
    else:
        return render_template("fktshfir.html", mess="" ,butt="فك التشفير" )
if __name__=="__main__":
    app.run(debug=True)
