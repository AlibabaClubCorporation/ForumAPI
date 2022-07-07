from django.utils.text import slugify



rus_en = {
    'й':'y',
    'ц':'c',
    'у':'u',
    'к':'k',
    'е':'e',
    'н':'n',
    'г':'g',
    'ш':'sh',
    'щ':'sh',
    'з':'z',
    'х':'h',
    'ъ':'',
    'ф':'ph',
    'ы':'i',
    'в':'v',
    'а':'a',
    'п':'p',
    'р':'r',
    'о':'o',
    'л':'l',
    'д':'d',
    'ж':'zh',
    'э':'e',
    'я':'ya',
    'ч':'ch',
    'с':'s',
    'м':'m',
    'и':'i',
    'т':'t',
    'ь':'',
    'б':'b',
    'ю':'yu',
}



def _rus_to_en( text : str ) -> str:
    """ Функция, которая превращает кириллические символы в латиницу """

    new_text = ''

    for symbol in text.lower():
        if symbol in rus_en:
            new_text += rus_en[symbol]
        else:
            new_text += symbol
    
    return new_text



def text_to_slug( text : str ) -> str:
    """ Функция, которая делает text пригодным для использования в качестве slug """

    slug = _rus_to_en( text )
    slug = slugify( slug )

    return slug