### Steps

- `virutalenv env`
- `cd env/scripts`
- `activate`
- change to core directory
- install DRF, pillow
- Make migrations & migrate
- `python manage.py runserver`

## URL Routes

Registering account
`http://127.0.0.1:8000/api/register/`

Loggin into account
`http://127.0.0.1:8000/api/login/`

Creating/Updating/Getting users (GET, POST, PATCH)
`http://127.0.0.1:8000/api/user/`

![Alt text](image-6.png)
![Alt text](image.png)
![Alt text](image-1.png)
![Alt text](image-2.png)
![Alt text](image-3.png)

### When not logged in

![Alt text](image-4.png)

### Authenticated using token

![Alt text](image-5.png)

### Runiing unit test cases

![Alt text](image-7.png)
