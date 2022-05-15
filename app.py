from flask import Flask, request
import operasi

app = Flask(__name__)

@app.route("/api/calculator")
def main():
  op = request.args.get("op")
  x = request.args.get("x")
  y = request.args.get("y")
  try:
    if op == "tambah": return str(operasi.tambahkan(int(x),int(y)))
    return "No response!"
  except Exception as e:
    return str(e)
