from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    actor = Col('Actors')
    release_date = Col('Release Year')
    rating = Col('Rating')
    genre_type = Col('Genre')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(id='id'))