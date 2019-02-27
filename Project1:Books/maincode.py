import psycopg2 #convert python variable to sql variable
import os
import requests #for requesting Api
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgres://tzxyempokotnfe:e38e00f7e54ef1b0665e895ada1146fc4624b158aee42845243e91490426d38f@ec2-54-163-246-159.compute-1.amazonaws.com:5432/d444jseosr52v2')
   # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))


@app.route('/',methods=["GET","POST"])
def sigin():
        return render_template('sigin.html')

#decorator to fetch the value of user signup and insert it into database
@app.route('/sigin.html',methods=["GET","POST"])
def insertfunc():
    uid = request.form.get("id")      #request data from the form filled on sigin.html with attribut name="id"
    uname = request.form.get("uname")
    upass = request.form.get("pass")
    email = request.form.get("email")
    db.execute("INSERT INTO \"user\" (id,name,password,email) VALUES (:id,:name,:password,:email)",{"id":uid, "name":uname, "password":upass,"email":email})
    db.commit()
    return render_template('sigin.html')

#decorate to show the # REVIEW:  of the user entered for isbn and it's rating
@app.route('/bookpage.html',methods=["GET","POST"])
def finalreview():
   revw = db.execute("select * from review").fetchall()
   #number = revw.rowcount
   #print(number)
   #if number > 0:
   #else:
       #form1 = request.get_json()
    #   return render_template("error.html",message="Sorry to say but no record found try something else :)")
   return render_template("bookpage.html", revw = revw)

#intermediate api for fetching the information entered by user about rating of book.
@app.route('/savedrating',methods=["GET","POST"])
def reviewfunc():
#    print("HEllo")
    #print(form1)
#    print(request.method)
    #if request.method == 'POST'
    isbn1 = request.form.get("isbn1")
    rating1 = request.form.get("rating1")

    #print(isbn1)
    db.execute("INSERT INTO \"review\" (rating,isbn) VALUES (:rating,:isbn)",{"rating":rating1,"isbn":isbn1})
    #print("HEllo again")
    db.commit()
    #print("HEllo aaga")
    return render_template("bookpage.html")

#decoratar for welcome.html page:
@app.route('/welcome.html',methods=["POST","GET"])
def welcome():
    upass = request.form.get("pass")
    try:
        name = request.form.get("name")
    except ValueError:
        return render_template("error.html",message="Invalid username")

    if db.execute(("select name,password from \"user\" where name = '{0}' and password = '{1}'").format(name,upass)).rowcount > 0:
        return render_template("welcome.html",name=name)
    else:
        return render_template("error.html",message="Wrong username or password try again :)")

#decoratar for signup.html page:
@app.route('/signup.html',methods=["POST","GET"])
def signup():
      return render_template("signup.html")

#decoratar for search.html page for book by author or it's title:
@app.route('/search.html',methods=["POST","GET"])
def search():
    return render_template("search.html")

#decoratar for seeing # REVIEW: :
@app.route('/seereview.html',methods=["POST","GET"])
def showreview():
    bauthor = request.form.get("byauthor")
    btitle = request.form.get("title")
    bisbn = request.form.get("byisbn")
    #if bisbn is None:
    #    book = db.execute(("select * from \"book\" where  title  = '{0}'  or author = '{1}' ;").format(btitle,bauthor))
    #elif bauthor is None:
    #    book = db.execute(("select * from \"book\" where  title  = '{0}'  or isbn = '{1}' ;").format(btitle,bisbn))
    #else:
    #    book = db.execute(("select * from \"book\" where  isbn  = '{0}'  or author = '{1}' ;").format(bisbn,bauthor))

    book = db.execute(("select * from \"book\" where isbn = '{0}' or title  = '{1}'  or author = '{2}' ;").format(bisbn,btitle,bauthor))
    number = book.rowcount
    #print(number)
    if number > 0:
        return render_template("seereview.html", book = book)
    else:
        return render_template("error.html",message="Sorry to say but no record found try something else :)")


#@app.route("/bookpage/<int:book_id>",methods=["GET","POST"])
#def bookpage(book_id):
#      book = db.execute("SELECT * FROM book WHERE id = :id", {"id": book_id}).fetchone()
#      if book is None:
#          return render_template("error.html", message="No such book.")

      # Get all book
#      book= db.execute("SELECT title FROM book WHERE book_id = :id",{"id": book_id}).fetchall()
#      return render_template("seereview.html", book=book)


#decoratar for display.html page to display data of the book:
@app.route("/display.html")
def display():
    books = db.execute("select * from book").fetchall()
    return render_template("display.html",books = books)

#decoratar for review.html page it call itsef only and do nothing :
@app.route('/review.html',methods=["GET"])
def review():
    return render_template("review.html")
#decoratar for reading googlereadapi by passing integer to it:
#it is the dynamic route example
@app.route("/apiaccess/<string:isbn>",methods=["GET","POST"])
def apiaccess(isbn):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "tM06fwn9rIgrIG6NwK8CcA", "isbns":isbn})
    if res.status_code != 200:
       return render_template("error.html",message = "404 Page not found")
    else:
        res = res.json()
        res = res['books'][0]
        ct = res['average_rating']
        cr = res['reviews_count']
        return render_template("apisuccess.html",res =res, ct = ct, cr = cr);

if __name__ == "__main__":
    app.run(debug=True)


# psql postgres://tzxyempokotnfe:e38e00f7e54ef1b0665e895ada1146fc4624b158aee42845243e91490426d38f@ec2-54-163-246-159.compute-1.amazonaws.com:5432/d444jseosr52v2
