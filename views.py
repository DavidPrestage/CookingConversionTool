from datetime import datetime
from flask import Flask, render_template, request
from . import app, db
from decimal import *


# A Python function that removes trailing zeros to avoid 4 decimal places being shown when they don't contain useful info. 
# Usually named 'def remove_exponent(d):' from python decimal documentation. https://docs.python.org/3/library/decimal.html#decimal-faq
def remove_zero_trail(d):
    return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()
 

@app.route("/", methods=["GET", "POST"])
def cooking():
    session = db.session()

    cursor = session.execute("SELECT unit, ml FROM liquid;").cursor
    liquiddb = cursor.fetchall()

    cursor = session.execute("SELECT unit, g FROM flour;").cursor
    flourdb = cursor.fetchall()

    cursor = session.execute("SELECT unit, g FROM butter;").cursor
    butterdb = cursor.fetchall()

    cursor = session.execute("SELECT unit, c FROM temp;").cursor
    tempdb = cursor.fetchall()

    if request.method == "POST":
        
        # Give variables that will be passed to HTML default values, to avoid passing non existent values
        substance = "default"
        fq = "default"
        fu = "default"
        tu = "default"
        tq = "default"
        clicked = "default"

        #Checks which substance has been selected by the user
        if request.form.get("liquid"):
            measure = "ml"
            substance = "liquid"

        elif request.form.get("flour"):
            measure = "g"
            substance = "flour"
        
        elif request.form.get("butter"):
            measure = "g"
            substance = "butter"

        elif request.form.get("temp"):
            measure = "c"
            substance = "temp"

        # Check that the submission made is not a conversion, to avoid running the code for this when using buttons
        if substance == "default":

            # Check if buttons have been clicked and pass this data to the HTML 
            if request.form.get("liquidbutton"):
                clicked = "liquidbutton"

            elif request.form.get("flourbutton"):
                clicked = "flourbutton"

            elif request.form.get("butterbutton"):
                clicked = "butterbutton"

            elif request.form.get("tempbutton"):
                clicked = "tempbutton"

            elif request.form.get("measurementinfo"):
                clicked = "measurementinfo"

        else:
            # Pull the value for 'liquidfromqty', 'flourfromqty', or 'butterfromqty' from HTML. Uses the variable 'substance' to decide which one
            fq = request.form.get(f"{substance}fromqty")

            fu = request.form.get(f"{substance}fromunit")

            tu = request.form.get(f"{substance}tounit")


            # Get the value of the unit you are converting from in g/ml from the database. Python string formatting '{}' has been used to have variable table and column names.
            cursor = session.execute("SELECT {} FROM {} WHERE unit = '{}'".format(measure, substance, fu)).cursor

            fromunit_in_measure = cursor.fetchall()
            # Take the value out of the tuple that the SQL query has generated
            fromunit_in_measure = fromunit_in_measure[0][0]

            # Get the value of the unit you are converting to in g/ml from the database
            cursor = session.execute("SELECT {} FROM {} WHERE unit = '{}'".format(measure, substance, tu)).cursor

            tounit_in_measure = cursor.fetchall()
            # Take the value out of the tuple that the SQL query has generated
            tounit_in_measure = tounit_in_measure[0][0]

            # If the substance isn't temperature, complete the math required to get the converted figure and save it as tq. This figure will be the result of the conversion.
            if substance != "temp" or fu == tu:
                tq = (Decimal(fromunit_in_measure) * Decimal(fq)) / Decimal(tounit_in_measure)

            # If converting from Celsius to Fahrenheit the below math gives the converted figure
            elif fu == "Celsius" and tu == "Fahrenheit":
                tq = Decimal(fq) * Decimal(9 / 5) + Decimal(32) 

            # If converting from Fahrenheit to Celsius the below math gives the converted figure
            elif fu == "Fahrenheit" and tu == "Celsius":
                tq = (Decimal(fq) - Decimal(32)) * Decimal(5 / 9)
            
            # Round the converted figure to 4 decimal points and remove trailing zeros where not needed
            tq = round(tq, 4)
            tq = remove_zero_trail(tq)


        return render_template("cooking.html", liquiddb=liquiddb, flourdb=flourdb, butterdb=butterdb, tempdb=tempdb, substance = substance, fq = fq, fu = fu, tu = tu, tq = tq, clicked = clicked)
    
    #If the user is on the homepage then render the template without running the above code. 
    else:
        home = "yes"
        return render_template("cooking.html", liquiddb=liquiddb, flourdb=flourdb, butterdb=butterdb, tempdb=tempdb, home = home)
