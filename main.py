from fasthtml.common import *
from flowbite import *
toc = Div(
    Div(
        Div(
            H4('On this page', cls='pl-2.5 mb-2 text-sm font-semibold tracking-wide text-gray-900 uppercase dark:text-white lg:text-xs'),
            Nav(
                Ul(
                    Li( A('Default popover', href='#default-popover', cls='!border-blue-700 !after:opacity-100 !text-blue-700 dark:!border-blue-500 dark:!text-blue-500')),
                    Li( A('User profile', href='#user-profile')),
                ),
                id='TableOfContents'),
            cls='mb-8'),
        cls='flex overflow-y-auto sticky top-28 flex-col justify-between pt-10 pb-6 h-[calc(100vh-5rem)]'),
    cls='flex-none hidden w-64 pl-8 mr-8 xl:text-sm xl:block')

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
