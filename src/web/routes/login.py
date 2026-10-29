from typing import Annotated

from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["login_pages"], include_in_schema=False)


@router.get("/login", response_class=HTMLResponse)
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}


# def login(request: Request) -> HTMLResponse:
#     return HTMLResponse("coucou")
# return templates.TemplateResponse(request, "index.html")
# @app.post("/login/")


# class SignupView(FormView):
#     template_name = "registration/signup.html"
#     form_class = SignupForm
#     success_url = reverse_lazy("signup_done")
#
#     def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
#         if request.user.is_authenticated:
#             return redirect("home")
#         return super().dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form: SignupForm) -> HttpResponse:
#         user = form.save()
#         # Saved before sending, so the "Resend" button works even if sending fails.
#         self.request.session["signup_email"] = user.email
#         send_activation_email(self.request, user)
#         return super().form_valid(form)
#
