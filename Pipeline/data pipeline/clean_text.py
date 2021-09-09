from cleantext import clean

text = ""

clean_text = clean(s8,
        fix_unicode=True,
        to_ascii=True
        lower=True,
        no_line_breaks=True,
        no_urls=True,
        no_numbers=True,
        no_digits=True,
        no_currency_symbols=True,
        no_punct=True,
        replace_with_punct="",
        replace_with_punct="",
        replace_with_url="<URL>",
        replace_with_number="<NUMBER>"
        replace_with_digit="",
        replace_with_currency_symbol="<CUR>",
        lang= 'eng')


print(clean_text)
