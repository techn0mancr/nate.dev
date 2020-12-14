def apology(message, code=400):
    return "Something went wrong"

def md2html(file_path):
    """ Reads a Markdown file and renders it to marked-safe HTML. """
    from flask import Markup
    import markdown

    # Read file
    with open(file_path, 'r', encoding="utf-8") as input_file:
        text = input_file.read()
    
    # Convert Markdown syntax to HTML
    html = markdown.markdown(
               text,
               extensions=[
                   "md_in_html",
                   "nl2br",
                   "sane_lists"
               ],
               output_format="html5"
           )
    
    # Mark HTML as safe and return it
    return Markup(html)

