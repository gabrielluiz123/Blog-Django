from django import template

register = template.Library()


@register.filter(name='plural_comentario')
def plural_comentario(num_comentario):
    try:
        num_comentario = int(num_comentario)
        if num_comentario == 0:
            return 'Nenhum comentario'
        elif num_comentario == 1:
            return f'{num_comentario} Comentario'
        else:
            return f'{num_comentario} Comentarios'
    except:
        return f'{num_comentario} Comentario(s)'