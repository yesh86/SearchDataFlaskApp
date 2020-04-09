import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)

initial_df = pd.read_excel("SearchData.xlsx", sheet_name="Details")

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        result = request.form['searchattribute']
        selection = request.form['searchcriteria']
        if selection == 'reqid':
            row_list = []
            for index, rows in initial_df.iterrows():
                mylist = [rows.CoreProcessArea, rows.FunctionalArea, rows.FunctionalSubArea, rows.ScreenName, rows.RequirementDescription]
                print(mylist)
                if mylist[4] == result:
                    row_list.append(mylist)
            list = pd.DataFrame(row_list, columns = ["CoreProcessArea", "FunctionalArea", "FunctionalSubArea", "ScreenName","RequirementDescription"])
            print(list)
            list.reset_index(drop=True, inplace=True)
            list.fillna(' ', inplace=True)
            return render_template('result.html', tables = [list.to_html(classes ='')], titles = ['na'], result = result)
            return render_template('search.html, result = result')
        elif selection == 'screenname':
            row_list = []
            for index, rows in initial_df.iterrows():
                mylist = [rows.CoreProcessArea, rows.FunctionalArea, rows.FunctionalSubArea, rows.ScreenName, rows.RequirementDescription]
                if mylist[3] == result:
                    row_list.append(mylist)
            list = pd.DataFrame(row_list, columns = ["CoreProcessArea", "FunctionalArea", "FunctionalSubArea", "ScreenName","RequirementDescription"])
            print(list)
            list.reset_index(drop=True, inplace=True)
            list.fillna(' ', inplace=True)
            return render_template('result.html', tables = [list.to_html(classes ='')], titles = ['na'], result = result)
            return render_template('search.html, result = result')

@app.route('/search', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return render_template('search.html')


if __name__ == '__main__':
    app.run(debug=True)