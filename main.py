from flask import jsonify, send_file, render_template, Flask, request
import scraper, to_pdf

app = Flask(__name__)
host = "127.0.0.1"
port = 12345



@app.route("/", methods = ["GET"])
def index():
    return render_template("main.html")

@app.route("/search", methods = ["GET"])
def search():
    first_company_name = request.args.get("company1")
    second_comapany_name = request.args.get("company2")
    url = f"/get-data?company1={first_company_name}&company2={second_comapany_name}"
    return render_template("search.html", frame_src=url)

@app.route("/get-data", methods=['GET'])
def get_data():
    first_company_name = request.args.get("company1")
    second_comapany_name = request.args.get("company2")
    
    statistics_list = scraper.get_statistics(first_company_name, second_comapany_name)
    income_statement_list = scraper.get_income_statement(first_company_name, second_comapany_name)
    balance_sheet_list = scraper.get_balance_sheet(first_company_name, second_comapany_name)
    cash_flow_list = scraper.get_cash_flow(first_company_name, second_comapany_name)
    if not statistics_list or not income_statement_list or not balance_sheet_list or not cash_flow_list:
        return "Not Found", 404
    return render_template("data.html", first_company_name = first_company_name, second_company_name = second_comapany_name, statistics_list=statistics_list, income_statement_list=income_statement_list, balance_sheet_list=balance_sheet_list, cash_flow_list=cash_flow_list)

@app.route("/get-pdf", methods=['GET'])
def get_pdf():
    first_company_name = request.args.get("company1")
    second_comapany_name = request.args.get("company2")
    url = f"{host}:{port}/get-data?company1={first_company_name}&company2={second_comapany_name}"
    to_pdf.url_to_pdf(url)
    return send_file("out.pdf")
    
    



if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
