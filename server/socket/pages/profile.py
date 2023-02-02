from .base import base_html


def generate_html(user):

    html = '''
        <div class="row">
            <div class="col-lg-6 align-self-center mx-auto mb-3">
                <div class="card login-shadow no-border" style="margin-bottom: 10px">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between">
                            <div>
                                <h5 class="card-title d-inline ps-4">Welcome back</h5>
                                <h4 class="card-title d-inline primary-color">@'''+user["username"] + '''</h4>
                            </div>

                            <span class="pe-4">
                                <svg
                                    width="36"
                                    height="36"
                                    viewBox="0 0 36 36"
                                    fill="none"
                                    xmlns="http://www.w3.org/2000/svg"
                                >
                                    <circle cx="18" cy="18" r="18" fill="#B26DEE" />
                                    <path
                                    d="M11.3333 24.25C11.3333 23.6975 11.5528 23.1676 11.9435 22.7769C12.3342 22.3861 12.8641 22.1667 13.4166 22.1667H24.6666"
                                    stroke="white"
                                    stroke-width="2"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    />
                                    <path
                                    d="M13.4166 9.66666H24.6666V26.3333H13.4166C12.8641 26.3333 12.3342 26.1138 11.9435 25.7231C11.5528 25.3324 11.3333 24.8025 11.3333 24.25V11.75C11.3333 11.1975 11.5528 10.6676 11.9435 10.2769C12.3342 9.88615 12.8641 9.66666 13.4166 9.66666Z"
                                    stroke="white"
                                    stroke-width="2"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    />
                                </svg>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-6 align-self-center mx-auto mb-4">
            <div class="card card-shadow no-border" style="margin-bottom: 40px">
                <div class="card-body">
                <div
                    class="d-flex align-items-center justify-content-between mb-4"
                >
                    <div>
                    <h5 class="card-title d-inline ps-4">Student information</h5>
                    </div>

                    <span
                    class="pe-4"
                    data-bs-toggle="tooltip"
                    data-bs-placement="left"
                    data-bs-title="@ali"
                    >
                    <svg
                        width="36"
                        height="36"
                        viewBox="0 0 36 36"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <circle cx="18" cy="18" r="18" fill="#B26DEE" />
                        <path
                        d="M24.6666 25.5V23.8333C24.6666 22.9493 24.3155 22.1014 23.6903 21.4763C23.0652 20.8512 22.2174 20.5 21.3333 20.5H14.6666C13.7826 20.5 12.9347 20.8512 12.3096 21.4763C11.6845 22.1014 11.3333 22.9493 11.3333 23.8333V25.5"
                        stroke="white"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        />
                        <path
                        d="M18 17.1667C19.841 17.1667 21.3334 15.6743 21.3334 13.8333C21.3334 11.9924 19.841 10.5 18 10.5C16.1591 10.5 14.6667 11.9924 14.6667 13.8333C14.6667 15.6743 16.1591 17.1667 18 17.1667Z"
                        stroke="white"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        />
                    </svg>
                    </span>
                </div>

                <div class="col-12 px-4" style="margin-top: 32px">
                    <div class="d-flex justify-content-between w-100">
                    <div class="d-flex col-6">
                        <p class="lead">First Name: <span>'''+user["first_name"] + '''</span></p>
                    </div>
                    <div class="d-flex col-6">
                        <p class="lead">Last Name: <span>'''+user["last_name"] + '''</span></p>
                    </div>
                    </div>
                    <div class="d-flex justify-content-between w-100">
                    <div class="d-flex col-6">
                        <p class="lead">Student Code: <span>''' + user["student_code"] + '''</span></p>
                    </div>
                    <div class="d-flex col-6">
                        <p class="lead">
                        Field of Study: <span>''' + user["field_of_study"] + '''</span>
                        </p>
                    </div>
                    </div>
                    <div class="d-flex justify-content-between w-100">
                    <div class="d-flex col-6">
                        <p class="lead">
                        Grade: <span class="primary-color">''' + user["grade"] + '''</span>
                        </p>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
    '''

    context = {
        'html': html,
        'title': f"{user['username']}\'s Profile",
        'extra_class': ''
    }
    complite_html = base_html(context)
    html_bytes = bytes(complite_html, "utf-8")
    return html_bytes
