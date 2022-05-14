"""
This type stub file was generated by pyright.
"""

from .dom1core import dom1core
from .dom_tag import dom_tag

"""
HTML tag classes.
"""
__license__ = ...
underscored_classes = ...
_ATTR_GLOBAL = ...
_ATTR_EVENTS = ...
ERR_ATTRIBUTE = ...
ERR_CONTEXT = ...
ERR_CONTENT = ...

class html_tag(dom_tag, dom1core):
    def __init__(self, *args, **kwargs) -> None:
        """
        Creates a new html tag inst"""
        ...

class html(html_tag):
    """
    The html element represents t"""

    ...

class head(html_tag):
    """
    The head element represents a"""

    ...

class title(html_tag):
    """
    The title element represents"""

    text = ...

class base(html_tag):
    """
    The base element allows autho"""

    is_single = ...

class link(html_tag):
    """
    The link element allows autho"""

    is_single = ...

class meta(html_tag):
    """
    The meta element represents v"""

    is_single = ...

class style(html_tag):
    """
    The style element allows auth"""

    is_pretty = ...

class script(html_tag):
    """
    The script element allows aut"""

    is_pretty = ...

class noscript(html_tag):
    """
    The noscript element represen"""

    ...

class body(html_tag):
    """
    The body element represents t"""

    ...

class main(html_tag):
    """
    The main content area of a do"""

    ...

class section(html_tag):
    """
    The section element represent"""

    ...

class nav(html_tag):
    """
    The nav element represents a"""

    ...

class article(html_tag):
    """
    The article element represent"""

    ...

class aside(html_tag):
    """
    The aside element represents"""

    ...

class h1(html_tag):
    """
    Represents the highest rankin"""

    ...

class h2(html_tag):
    """
    Represents the second-highest"""

    ...

class h3(html_tag):
    """
    Represents the third-highest"""

    ...

class h4(html_tag):
    """
    Represents the fourth-highest"""

    ...

class h5(html_tag):
    """
    Represents the fifth-highest"""

    ...

class h6(html_tag):
    """
    Represents the sixth-highest"""

    ...

class hgroup(html_tag):
    """
    The hgroup element represents"""

    ...

class header(html_tag):
    """
    The header element represents"""

    ...

class footer(html_tag):
    """
    The footer element represents"""

    ...

class address(html_tag):
    """
    The address element represent"""

    ...

class p(html_tag):
    """
    The p element represents a pa"""

    ...

class hr(html_tag):
    """
    The hr element represents a p"""

    is_single = ...

class pre(html_tag):
    """
    The pre element represents a"""

    is_pretty = ...

class blockquote(html_tag):
    """
    The blockquote element repres"""

    ...

class ol(html_tag):
    """
    The ol element represents a l"""

    ...

class ul(html_tag):
    """
    The ul element represents a l"""

    ...

class li(html_tag):
    """
    The li element represents a l"""

    ...

class dl(html_tag):
    """
    The dl element represents an"""

    ...

class dt(html_tag):
    """
    The dt element represents the"""

    ...

class dd(html_tag):
    """
    The dd element represents the"""

    ...

class figure(html_tag):
    """
    The figure element represents"""

    ...

class figcaption(html_tag):
    """
    The figcaption element repres"""

    ...

class div(html_tag):
    """
    The div element has no specia"""

    ...

class a(html_tag):
    """
    If the a element has an href"""

    ...

class em(html_tag):
    """
    The em element represents str"""

    ...

class strong(html_tag):
    """
    The strong element represents"""

    ...

class small(html_tag):
    """
    The small element represents"""

    ...

class s(html_tag):
    """
    The s element represents cont"""

    ...

class cite(html_tag):
    """
    The cite element represents t"""

    ...

class q(html_tag):
    """
    The q element represents some"""

    ...

class dfn(html_tag):
    """
    The dfn element represents th"""

    ...

class abbr(html_tag):
    """
    The abbr element represents a"""

    ...

class time_(html_tag):
    """
    The time element represents e"""

    ...

_time = time_

class code(html_tag):
    """
    The code element represents a"""

    ...

class var(html_tag):
    """
    The var element represents a"""

    ...

class samp(html_tag):
    """
    The samp element represents ("""

    ...

class kbd(html_tag):
    """
    The kbd element represents us"""

    ...

class sub(html_tag):
    """
    The sub element represents a"""

    ...

class sup(html_tag):
    """
    The sup element represents a"""

    ...

class i(html_tag):
    """
    The i element represents a sp"""

    ...

class b(html_tag):
    """
    The b element represents a sp"""

    ...

class u(html_tag):
    """
    The u element represents a sp"""

    ...

class mark(html_tag):
    """
    The mark element represents a"""

    ...

class ruby(html_tag):
    """
    The ruby element allows one o"""

    ...

class rt(html_tag):
    """
    The rt element marks the ruby"""

    ...

class rp(html_tag):
    """
    The rp element can be used to"""

    ...

class bdi(html_tag):
    """
    The bdi element represents a"""

    ...

class bdo(html_tag):
    """
    The bdo element represents ex"""

    ...

class span(html_tag):
    """
    The span element doesn't mean"""

    ...

class br(html_tag):
    """
    The br element represents a l"""

    is_single = ...
    is_inline = ...

class wbr(html_tag):
    """
    The wbr element represents a"""

    is_single = ...
    is_inline = ...

class ins(html_tag):
    """
    The ins element represents an"""

    ...

class del_(html_tag):
    """
    The del element represents a"""

    ...

_del = del_

class img(html_tag):
    """
    An img element represents an"""

    is_single = ...

class iframe(html_tag):
    """
    The iframe element represents"""

    ...

class embed(html_tag):
    """
    The embed element represents"""

    is_single = ...

class object_(html_tag):
    """
    The object element can repres"""

    ...

_object = object_

class param(html_tag):
    """
    The param element defines par"""

    is_single = ...

class video(html_tag):
    """
    A video element is used for p"""

    ...

class audio(html_tag):
    """
    An audio element represents a"""

    ...

class source(html_tag):
    """
    The source element allows aut"""

    is_single = ...

class track(html_tag):
    """
    The track element allows auth"""

    is_single = ...

class canvas(html_tag):
    """
    The canvas element provides s"""

    ...

class map_(html_tag):
    """
    The map element, in conjuncti"""

    ...

_map = map_

class area(html_tag):
    """
    The area element represents e"""

    is_single = ...

class table(html_tag):
    """
    The table element represents"""

    ...

class caption(html_tag):
    """
    The caption element represent"""

    ...

class colgroup(html_tag):
    """
    The colgroup element represen"""

    ...

class col(html_tag):
    """
    If a col element has a parent"""

    is_single = ...

class tbody(html_tag):
    """
    The tbody element represents"""

    ...

class thead(html_tag):
    """
    The thead element represents"""

    ...

class tfoot(html_tag):
    """
    The tfoot element represents"""

    ...

class tr(html_tag):
    """
    The tr element represents a r"""

    ...

class td(html_tag):
    """
    The td element represents a d"""

    ...

class th(html_tag):
    """
    The th element represents a h"""

    ...

class form(html_tag):
    """
    The form element represents a"""

    ...

class fieldset(html_tag):
    """
    The fieldset element represen"""

    ...

class legend(html_tag):
    """
    The legend element represents"""

    ...

class label(html_tag):
    """
    The label represents a captio"""

    ...

class input_(html_tag):
    """
    The input element represents"""

    is_single = ...

_input = input_

class button(html_tag):
    """
    The button element represents"""

    ...

class select(html_tag):
    """
    The select element represents"""

    ...

class datalist(html_tag):
    """
    The datalist element represen"""

    ...

class optgroup(html_tag):
    """
    The optgroup element represen"""

    ...

class option(html_tag):
    """
    The option element represents"""

    ...

class textarea(html_tag):
    """
    The textarea element represen"""

    ...

class keygen(html_tag):
    """
    The keygen element represents"""

    is_single = ...

class output(html_tag):
    """
    The output element represents"""

    ...

class progress(html_tag):
    """
    The progress element represen"""

    ...

class meter(html_tag):
    """
    The meter element represents"""

    ...

class details(html_tag):
    """
    The details element represent"""

    ...

class summary(html_tag):
    """
    The summary element represent"""

    ...

class command(html_tag):
    """
    The command element represent"""

    is_single = ...

class menu(html_tag):
    """
    The menu element represents a"""

    ...

class font(html_tag):
    """
    The font element represents t"""

    ...

class comment(html_tag):
    """
    Normal, one-line comment:
    """

    ATTRIBUTE_CONDITION = ...
    ATTRIBUTE_DOWNLEVEL = ...
