""" Flask-related imports """
from flask import render_template

def apology(message, code=400):
    """ Renders a message as an apology to the user. """
    
    def escape_special_chars(string : str) -> str:
        """
        Escape special characters.
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            string : str = string.replace(old, new)
        
        return string

    return render_template("apology.html", top=code, bottom=escape_special_chars(message)), code


def md2html(file_path) -> str:
    """ Reads a Markdown file and renders it to marked-safe HTML. """
    from flask import Markup
    import markdown

    # Read file
    with open(file_path, 'r', encoding="utf-8") as input_file:
        text : str = input_file.read()
    
    # Convert Markdown syntax to HTML
    html : str = markdown.markdown(
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

