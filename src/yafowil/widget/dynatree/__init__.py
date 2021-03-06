from yafowil.base import factory
from yafowil.utils import entry_point
import os


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'yafowil.widget.dynatree.dependencies',
    'resource': 'jquery.dynatree/jquery.dynatree.min.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.dynatree.common',
    'resource': 'widget.js',
    'order': 21,
}]
default_css = [{
    'group': 'yafowil.widget.dynatree.dependencies',
    'resource': 'jquery.dynatree/skin/ui.dynatree.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.dynatree.common',
    'resource': 'widget.css',
    'order': 21,
}]
bootstrap_css = [{
    'group': 'yafowil.widget.dynatree.dependencies',
    'resource': 'jquery.dynatree/skin-bootstrap/ui.dynatree.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.dynatree.common',
    'resource': 'widget.css',
    'order': 21,
}]


@entry_point(order=10)
def register():
    from yafowil.widget.dynatree import widget  # noqa
    factory.register_theme('default', 'yafowil.widget.dynatree',
                           resourcedir, js=js, css=default_css)
    factory.register_theme('bootstrap', 'yafowil.widget.dynatree',
                           resourcedir, js=js, css=bootstrap_css)
