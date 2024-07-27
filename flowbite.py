from fasthtml.common import *
from fasthtml.svg import *

from mistletoe import markdown

def Markdown(s, **kw): return Div(NotStr(markdown(s)), **kw)

svgd = dict(aria_hidden='true', xmlns='http://www.w3.org/2000/svg', fill='none')
SvgAccordian = Svg(
    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M9 5 5 1 1 5'),
    viewbox='0 0 10 6', cls='w-3 h-3 rotate-180 shrink-0', **svgd)

def AccordionItem(id, title, c):
    heading_id,body_id = f"{id}-heading", f"{id}-body"
    if isinstance(c, FT): c = (c,)
    return (H2(
        Button(
            Span(title),
            SvgAccordian, type='button', data_accordion_target=f'#{body_id}', aria_expanded='true', aria_controls=body_id,
            cls='flex items-center justify-between w-full p-5 font-medium rtl:text-right text-gray-500 border border-gray-200 rounded-t-xl focus:ring-4 focus:ring-gray-200 dark:focus:ring-gray-800 dark:border-gray-700 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 gap-3'
        ), id=heading_id),
    Div(
        Div(*c, cls='p-5 border border-gray-200 dark:border-gray-700 dark:bg-gray-900'),
        id=body_id, aria_labelledby=heading_id, cls='hidden'))

def Accordion(*items, id="accordion-collapse", collapse=False, cls=''):
    return Div(*[AccordionItem(f'{id}-{i}', title, c) for i,(title,c) in enumerate(items)],
        id=id, data_accordion='collapse' if collapse else 'open', cls=cls)

SvgNav = Svg(
    Path(stroke='currentColor', stroke_linecap='round', stroke_linejoin='round', stroke_width='2', d='M1 1h15M1 7h15M1 13h15'),
    viewbox='0 0 17 14', cls='w-5 h-5', **svgd)

def NavItem(txt, href, sel):
    basecls = 'block py-2 px-3 rounded'
    currcls = f'{basecls} text-white bg-blue-700 md:bg-transparent md:text-blue-700 md:p-0 dark:text-white md:dark:text-blue-500'
    regcls  = f'{basecls} text-gray-900 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-700 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent'
    kw = {'aria_current':'page'} if sel else {}
    return Li(A(txt, href=href, cls=currcls if sel else regcls, **kw))

def Navbar(id, selidx, logo, href, items, sticky=False):
    sid = f'{id}-nav'
    items = [NavItem(txt, href, i==selidx) for i,(txt,href) in enumerate(items)]
    itemcls = 'font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700'
    stickycls = 'fixed w-full z-20 top-0 start-0' if sticky else ''
    return Nav(
        Div(
            A(logo, href=href, cls='flex items-center space-x-3 rtl:space-x-reverse'),
            Button(
                Span('Open menu', cls='sr-only'), SvgNav,
                data_collapse_toggle=sid, type='button', aria_controls=sid, aria_expanded='false',
                cls='inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600'),
            Div(
                Ul(*items, cls=itemcls),
                id=sid, cls='hidden w-full md:block md:w-auto'),
            cls='max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4'
        ), id=id, cls=f'bg-white border-gray-200 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-600 {stickycls}')

# TODO: create toc component. Rough sketch here:
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

