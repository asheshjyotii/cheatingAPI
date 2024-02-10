from flask import Flask, send_file, abort
import os
from ai import prompt

app = Flask(__name__)

# folder = r"/home/asheshjyoti/house/asheshjyoti/workspace/web_dev/cmdAPI/files/"

@app.route('/<query>', methods=['GET'])
def get_code(query):
    # file = os.path.join(folder, filename)
    # print(file)
    # if os.path.exists(file):
    #     return send_file(file, as_attachment=True)
    # else:
    #     abort(404)
    prompt_ = prompt(query)
    fp = open('files/ashesh.txt', 'w')
    fp.write(prompt_)
    fp.close()
    return send_file('files/ashesh.txt', as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



