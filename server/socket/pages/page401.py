from .base import base_html


def unauthorized_access():
    html = '''
        <div class="col-md-6 text-center">
            <h1 class="display-1 primary-color" style="font-weight: 600">401</h1>
        </div>
        <div class="col-md-6 mt-2 text-center mb-4">
            <p class="fs-3">
            <span class="text-danger">Unauthorized Access</span>
            </p>
            <p class="lead">Aceess is denied due to invalid credentials.</p>
            <a
            href="http://127.0.0.1:5500/html/login.html"
            class="btn btn-primary-color mt-3"
            >
            Go Home
            </a>
        </div>

    '''
    context = {
        'html': html,
        'title': '401 Unauthorized Access',
        'extra_class': 'align-items-center'
    }
    complite_html = base_html(context)
    html_bytes = bytes(complite_html, "utf-8")
    return html_bytes
