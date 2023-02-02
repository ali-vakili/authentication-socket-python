def base_html(context):
    html = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
            crossorigin="anonymous"
            />
            <link rel="stylesheet" href="../static/css/index.css" />
            <link
            rel="apple-touch-icon"
            sizes="180x180"
            href="../static/image/apple-touch-icon.png"
            />
            <link
            rel="icon"
            type="image/png"
            sizes="32x32"
            href="../static/image/favicon-32x32.png"
            />
            <link
            rel="icon"
            type="image/png"
            sizes="16x16"
            href="../static/image/favicon-16x16.png"
            />
            <!-- <link rel="manifest" href="../static/image/site.webmanifest" /> -->
            <link
            rel="mask-icon"
            href="../static/image/safari-pinned-tab.svg"
            color="#bf94e5"
            />
            <meta name="msapplication-TileColor" content="#bf94e5" />
            <meta name="theme-color" content="#ffffff" />
            <title>{context['title']}</title>
        </head>
        <body style="height: 100vh; background-color: #fafafa">
            <div
            class="container d-flex {context['extra_class']} justify-content-center flex-column h-100">
                {context['html']}
            </div>

            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
            crossorigin="anonymous"
            ></script>
            <script
            src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
            integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3"
            crossorigin="anonymous"
            ></script>
            <script
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"
            integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD"
            crossorigin="anonymous"
            ></script>
        </body>
        </html>


    '''
    return html
