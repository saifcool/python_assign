from flask import Flask, render_template, request
def grade(x,y):
    percent=(int(x)*100)/int(y)
    if(percent>95):
        return "S"
    elif(percent>90):
        return "A+"
    elif(percent>85):
        return "A"
    elif(percent>80):
        return "B+"
    elif(percent>75):
        return "B"
    elif(percent>70):
        return "C+"
    elif(percent>65):
        return "C"
    elif(percent>60):
        return "D+"
    elif(percent>55):
        return "D"
    elif(percent>=50):
        return "E"
    else:
        return "FAIL"
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('marksheetinput.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if(request.method=='POST'):
        name=request.form['name']
        reg=request.form['reg']
        sem=request.form['sem']
        college=request.form['clg']
        sub1_name=request.form['sub1']
        sub1_mark=request.form['sub1m']
        sub1_total=request.form['sub1tm']
        sub1_grade=grade(sub1_ark,sub1_total)
        sub2_name=request.form['sub2']
        sub2_mark=request.form['sub2m']
        sub2_total=request.form['sub2tm']
        sub2_grade=grade(sub2_mark,sub2_total)
        sub3_name=request.form['sub3']
        sub3_mark=request.form['sub3m']
        sub3_total=request.form['sub3tm']
        sub3_grade=grade(sub3_mark,sub3_total)
        sub4_name=request.form['sub4']
        sub4_mark=request.form['sub4m']
        sub4_total=request.form['sub4tm']
        sub4_grade=grade(sub4_mark,sub4_total)
        if(sub1_grade=="FAIL" or sub2_grade=="FAIL" or sub3_grade=="FAIL" or sub4_grade=="FAIL"):
            status="FAILED"
        else:
            status="PASSED"
        return render_template('marksheet.html',name=name,reg=reg,sem=sem,college=college,sub1_name=sub1_name,sub1_mark=sub1_mark,sub1_total=sub1_total,sub2_name=sub2_name,sub2_mark=sub2_mark,sub2_total=sub2_total,sub3_name=sub3_name,sub3_mark=sub3_mark,sub3_total=sub3_total,sub4_name=sub4_name,sub4_mark=sub4_mark,sub4_total=sub4_total,sub1_grade=sub1_grade,sub2_grade=sub2_grade,sub3_grade=sub3_grade,sub4_grade=sub4_grade,status=status)
if(__name__=='__main__'):
    app.run()    