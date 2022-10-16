from fastapi import FastAPI, Response
from .auth.router import router as auth_router
from .users.router import router as users_router
from .recipes.router import router as recipe_routes


# init application and include routers.
app = FastAPI()

app.include_router(auth_router, prefix='/auth')
app.include_router(users_router, prefix='/users')
app.include_router(recipe_routes, prefix='/recipes')


@app.route('/test/')
def test_route(request):
    return Response('Hello world!!')
