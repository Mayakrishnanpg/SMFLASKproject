from flask import*
from database import DB,CR
farmer=Blueprint("farmer",__name__)

@farmer.route("/")
def farmerhome():
  return render_template("farmerhome.html")

@farmer.route("/answerquestion",methods=["post","get"])
def AnswerQuestion():
  CR.execute("SELECT * FROM smdatabase")
  smdatabase=CR.fetchall()
  if 'submit' in request.form:
    answer = request.form['ans']
    id = request.form['submit']
    sql = "UPDATE smdatabase set answer=%s WHERE id=%s" 
    val = (answer,id)
    CR.execute(sql,val)
    DB.commit()
    flash("Answer Submited")
    return redirect(url_for("farmer.AnswerQuestion"))
  
  return render_template('answerquestion.html',smdatabase=smdatabase)

@farmer.route("/delete",methods=["post","get"])
def delete():
  CR.execute("SELECT * FROM smdatabase")
  res=CR.fetchall()
  if "submit" in request.form:
    id=request.form['submit']
    CR.execute("DELETE FROM smdatabase WHERE id=%s",(id,))
    DB.commit()
    flash("Item Delete")
    return redirect(url_for('farmer.delete'))
  return render_template('delete.html',res=res)