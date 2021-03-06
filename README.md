# WadThePlanet??
It's like Facebook, but with more planets.

### Setup
Requires Python 3.6+.
- Pull the repo.
- `cd planetWad; virtualenv venv; cd venv`
- `pip install -r requirements.txt`
- `python manage.py makemigrations planet`
- `python manage.py migrate`
- `python populate_planet.py`
- `python manage.py runserver`

The site can be accessed from `127.0.0.1:8000` (not `localhost:8000` due to security restrictions`).

* * * * *

### Server-side and middleware
- [Django 1.11](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Cleanup](https://github.com/un1t/django-cleanup)
- [Pillow](https://pillow.readthedocs.io/en/stable/)

### Hosting
- [PythonAnywhere](https://pythonanywhere.com)
- [CDN.js](https://cdnjs.com/) (hosts JS files)

### Client-side
- [Bootstrap](https://getbootstrap.com)
- [MDBootstrap](https://mdbootstrap.com/) (free version, CSS only)
- [jQuery](https://jquery.com)
- [Three.js](https://threejs.org)

### Images and other resources
- [CC0textures](https://cc0textures.com/view.php?tex=Ground14) (for planet base textures)
- [Font Awesome](https://fontawesome.com/font) (icon font)
- [Freepik](https://www.freepik.com/free-vector/classic-astronaut-character-with-flat-design_2868156.htm) (astronaut image)

### External programs
- [SpaceScape](http://alexcpeterson.com/spacescape/) (to generate the starfield skybox)

### Documentation
- [Tango With Django](https://www.tangowithdjango.com/)
- [Django documentation](https://docs.djangoproject.com/en/1.11/)
- [Three.js examples](https://threejs.org/examples/)


