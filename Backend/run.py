from app import create_app

app = create_app()

if __name__ == "__main__":
    # Em um ambiente de desenvolvimento, debug=True é útil.
    # Para produção, use um servidor WSGI como Gunicorn ou uWSGI.
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000, debug=True)

