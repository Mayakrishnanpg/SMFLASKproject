from flask import*
from database import DB,CR
from datetime import datetime
merchant=Blueprint("merchant",__name__)
@merchant.route("/")
def merchanthome():
  CR.execute("SELECT * FROM smdatabase")
  res = CR.fetchall()
  return render_template("merchanthome.html",res = res)

@merchant.route("/askquestion",methods=["post","get"])
def askquestion():
    if "submit" in request.form:
        question = request.form['question']
        date = datetime.now()
        sql ='INSERT INTO smdatabase (question,date)VALUES(%s,%s)'
        val=(question,date)
        CR.execute(sql,val)
        DB.commit()
        flash("Question submitted")
        return redirect(url_for('merchant.merchanthome'))
    return render_template('askquestion.html')