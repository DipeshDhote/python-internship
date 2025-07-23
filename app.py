from flask import Flask, request, jsonify
from db_config import connect_to_db


app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "This is a home page"})


@app.route('/employees',methods=['GET'])
def get_employee():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM Employees")
    all_data = cur.fetchall()
    
    employee = []
    
    for row in all_data:
        employee.append([{'id': row[0], 'name': row[1], 'email': row[2], 'age': row[3]}])

    con.close()
    return jsonify(employee)

@app.route('/employee',methods=["POST"])
def add_employee(quary:str):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(quary)
    con.commit()
    con.close()

    return jsonify({"message": "Employee added successfully"})

@app.route('/employees/<int:id>',methods=["PUT"])
def update_employee(id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(f"UPDATE Employees SET age = 30 WHERE id = {id}")
    con.commit()
    con.close()

    return jsonify({"message": "Employee updated successfully"})

@app.route('/employees/<int:id>',methods=['DELETE'])
def delete_employee(id):
    con = connect_to_db()
    cur = con.cursor()
    cur.execute(f"DELETE FROM Employees WHERE id = {id}")
    con.commit()
    con.close()

    return jsonify({"message": "Employee deleted successfully"})


if __name__=="__main__":
    app.run(debug=True)



