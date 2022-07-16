from flask import Flask, render_template

from utils import *

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route('/')
    def page_with_candidates():
        """
        выводим список всех кандидатов
        :return:
        """
        candidates = load_candidates_from_json()
        return render_template('list.html', candidates=candidates)


    @app.route('/candidate/<int:pk>/')
    def page_candidate(pk):
        candidate = get_candidate(pk)
        return render_template('single.html', candidate=candidate)


    @app.route('/search/<name>/')
    def search_by_name(name):
        candidates = get_candidates_by_name(name)
        count_candidates = len(candidates)
        return render_template('search.html', candidates=candidates, count_candidates=count_candidates)


    @app.route('/skill/<skill>/')
    def search_by_skill(skill):
        candidates = get_candidates_by_skill(skill)
        count_candidates = len(candidates)
        return render_template('skill.html', candidates=candidates, count_candidates=count_candidates)


    app.run(debug=True)