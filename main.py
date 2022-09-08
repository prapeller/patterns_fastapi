from app import create_app


if __name__ == '__main__':
    flask = create_app()

    @flask.route('/')
    def allocate_endpoint():
        return '<h1>wohoo!</h1>'

    flask.run(debug=True)