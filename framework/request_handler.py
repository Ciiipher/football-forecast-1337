from webapp2 import RequestHandler
import os
import jinja2

class FFRequestHandler(RequestHandler):
    template_directory = os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)), 'templates'
    )

    jinja_environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory)
    )

    def render(self, template, **kwargs):

        jinja_template = self.jinja_environment.get_template(template)
        html_from_template = jinja_template.render(kwargs)

        self.response.out.write(html_from_template)

    def json_response(self, status_code=200, **kwargs):
        from json import dumps

        self.response.status = status_code
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(dumps(kwargs))