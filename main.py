from fasthtml.common import *
from flowbite import *

flowurl = 'https://cdn.jsdelivr.net/npm/flowbite@2.4.1/dist'
hdrs = (
    Meta(name="theme-color", content="#ffffff"),
    Link(href=f"{flowurl}/flowbite.min.css", rel="stylesheet"),
)
app,rt = fast_app(pico=False, hdrs=hdrs)

@rt('/')
def get():
    navitems = [('Home', '#'), ('About', '#'), ('Services', '#'), ('Pricing', '#'), ('Contact', '#')]
    logo = Img(src='logo.svg', cls='h-8', alt='Logo')
    nb = Navbar(id='navbar-default', selidx=0, logo=logo, href='https://fasthtml.answer.ai/', items=navitems, sticky=True)
    pcls = 'mb-2 text-gray-500 dark:text-gray-400'
    acc = Accordion(
        ('First thing?', P('First thing.', cls=pcls)),
        ('Second thing?', P('Second thing.', cls=pcls)),
        cls='pb-5'
    )
    paras = [Markdown(f'**This** is *paragraph {i}*.', cls=pcls) for i in range(1, 21)]
    cts = Div(acc, *paras, cls="p-5 max-w-screen-xl mx-auto pt-24")

    return (
        Title('Flowbite FastHTML demo'),
        Div(
            Main(nb, cts,
                 cls="flex-auto w-full min-w-0 mx-auto max-w-4xl"),
            toc, cls="flex w-full"),
        Script(src=f"{flowurl}/flowbite.min.js")
    )

run_uv()
