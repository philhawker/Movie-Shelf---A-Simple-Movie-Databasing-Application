from wtforms import Form, StringField, SelectField, validators

class MovieSearchForm(Form):
    choices = [('Movie', 'Movie'),
               ('Actor', 'Actor'),
               ('Genre', 'Genre'),
               ('Release Year', 'Release Year'),
               ('Rating', 'Rating')]
    select = SelectField('Browse Your Movie Shelf:', choices=choices)
    search = StringField('')


class MovieForm(Form):
    genre_types = [('Action', 'Action'),
                   ('Comedy', 'Comedy'),
                   ('Horror', 'Horror'),
                   ('Sci-Fi', 'Sci-Fi'),
                   ('Drama', 'Drama'),
                   ('Suspense', 'Suspense'),
                   ('Documentary', 'Documentary'),
                   ('Kids and Family', 'Kids and Family'),
                   ('Romance', 'Romance')
                   ]
    title = StringField('Title')
    actor = StringField('Starring Actors')
    release_date = StringField('Year Released')
    rating = StringField('Rating')
    genre_type = SelectField('Genre', choices=genre_types)
