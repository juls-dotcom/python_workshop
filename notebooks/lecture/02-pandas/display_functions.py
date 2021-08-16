import pandas as pd
from itertools import islice
from ipywidgets import HBox
from ipywidgets import HTML
from IPython.display import display

pd.set_option('max_colwidth', 20)


def df_HBox(objects, names=None, px=50):
    children = []
    space_html = HTML('<span style="padding-left:{}px">'.format(px))
    for i, obj in enumerate(objects):
        name = names[i] if names is not None else ''
        if isinstance(obj, pd.Series):
            info = (("Name: {}, ".format(obj.name) if obj.name else "") +
                    "dtype: {}".format(obj.dtype))
            html_str = (
                '<div class="rendered_html"><pre>{}</pre></div>'.format(obj.to_string())
            )
            obj_html = HTML(name+html_str+info)
        else:
            html_str = obj.to_html(classes='rendered_html')
            obj_html = HTML(name+html_str)

        children.append(obj_html)
        if i != (len(objects)-1):
            children.append(space_html)
    display(HBox(children=children))


def unpack_groups(grouped, prefix='group: '):
    names, groups = list(zip(*list(grouped)))
    names = ["{}{}".format(prefix, name) for name in names]
    return list(names), list(groups)


def head(path, n=5):
    """Read first lines of a file."""
    try:
        with open(path, 'r') as f:
            first_n = islice(f, n)
            for line in first_n:
                print(line, end="")
    except UnicodeDecodeError:
        # Pray it's in latin-1.
        with open(path, 'r', encoding='latin-1') as f:
            first_n = islice(f, n)
            for line in first_n:
                print(line, end="")


