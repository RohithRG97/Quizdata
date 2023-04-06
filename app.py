from flask import Flask, request, render_template
import string
import re
import os

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("upload.html")
    
# @app.route('/upload', methods=['GET', 'POST'])
# def texteval():
#     try:
#         if request.method == 'POST':

    
#             entered_text = request.form.get("entertext")

#             textlength = len(entered_text)

#             upper_count = 0
#             digit_count = 0
#             for char in entered_text:
#                 if char.isupper():
#                     upper_count = upper_count + 1
#                 if char.isdigit():
#                     digit_count = digit_count + 1
            
#             space_count = entered_text.count(' ')
#             spch1_count = entered_text.count('.')
#             spch2_count = entered_text.count(',')
#             spch3_count = entered_text.count(':')
#             spch4_count = entered_text.count('?')
#             spch5_count = entered_text.count('$')
#             spch6_count = entered_text.count('(')
#             spch7_count = entered_text.count(')')
#             spch8_count = entered_text.count('-')
#             spch9_count = entered_text.count('&')

#             spch_count = spch1_count + spch2_count + spch3_count + spch4_count + spch5_count + spch6_count + spch7_count + spch8_count + spch9_count

#             translator = str.maketrans('', '', string.punctuation + string.digits)
#             converted_text = entered_text.translate(translator)

#             upper_converted_text = converted_text.upper()
#             textlength2 = len(upper_converted_text)

#             return render_template("display.html", textlength=textlength, space_count=space_count, spch_count=spch_count, upper_count = upper_count, digit_count=digit_count, upper_converted_text=upper_converted_text, textlength2=textlength2)    
    
#     except AttributeError:
#     # handle the AttributeError raised by accessing the "some_method" attribute
#         print("AttributeError: 'NoneType' object has no attribute 'some_method'")
#     except TypeError:
#     # handle the TypeError raised by passing None to a method that doesn't accept it
#         print("TypeError: 'NoneType' object is not callable")
#     except:
#         # handle any other exception that might be raised
#         print("An unknown error occurred")
    
@app.route('/upload', methods=['GET', 'POST'])
def texteval2():
    if request.method == 'POST':
        entered_text2 = request.form.get("entertext2")
        entered_text2 = entered_text2.lower()
        words = request.form.get("words")
        words = words.lower()
        words_list = words.split()
        counts = []

        for word in words_list:
            matches = re.findall(r"\b" + word + r"\b", entered_text2)
            #count = entered_text2.count(word) 
            count = len(matches)
            counts.append((word, count))

        return render_template('display2.html', counts=counts)

    
