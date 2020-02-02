from app import app
from db_setup import init_db, db_session
from forms import MovieSearchForm, MovieForm
from flask import flash, render_template, request, redirect
from models import Movie, Actor
from tables import Results

init_db()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = MovieSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Actor':
            qry = db_session.query(Movie, Actor).filter(
                Actor.id==Movie.actor_id).filter(
                    Actor.name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Movie':
            qry = db_session.query(Movie).filter(
                Movie.title.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Rating':
            qry = db_session.query(Movie).filter(
                Movie.publisher.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Movie)
            results = qry.all()
    else:
        qry = db_session.query(Movie)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


@app.route('/new_movie', methods=['GET', 'POST'])
def new_movie():

    form = MovieForm(request.form)

    if request.method == 'POST' and form.validate():
        movie = Movie()
        save_changes(movie, form, new=True)
        flash('Movie added successfully!')
        return redirect('/')

    return render_template('new_movie.html', form=form)


def save_changes(movie, form, new=False):

    actor = Actor()
    actor.name = form.actor.data

    movie.actor = actor
    movie.title = form.title.data
    movie.release_date = form.release_date.data
    movie.rating = form.rating.data
    movie.genre_type = form.genre_type.data

    if new:
        db_session.add(movie)
    db_session.commit()


@app.route('/item/<int:id>', methods=['GET', 'POST'])
def edit(id):
    qry = db_session.query(Movie).filter(
                Movie.id==id)
    movie = qry.first()

    if movie:
        form = MovieForm(formdata=request.form, obj=movie)
        if request.method == 'POST' and form.validate():
            save_changes(movie, form)
            flash('Movie updated successfully!')
            return redirect('/')
        return render_template('edit_movie.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    qry = db_session.query(Movie).filter(
        Movie.id==id)
    movie = qry.first()

    if movie:
        form = MovieForm(formdata=request.form, obj=movie)
        if request.method == 'POST' and form.validate():
            db_session.delete(movie)
            db_session.commit()

            flash('Movie deleted successfully!')
            return redirect('/')
        return render_template('delete_movie.html', form=form)
    else:
        return 'Error deleting #{id}'.format(id=id)


if __name__ == '__main__':
    import os
    if 'WINGDB_ACTIVE' in os.environ:
        app.debug = False
    app.run(port=5001)