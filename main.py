# Required installations
# pip install flask
# pip install flask-login
# pip install sqlalchemy

from Website import create_app

app = create_app()

def main():

    app.run(debug=True) # debug=True should be False in production

if __name__ == "__main__":
    main()