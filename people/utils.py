menu = [
    "О сайте",
    "Добавить статью",
    "Обратная связь",
    "Войти",
]


class DataMixin:
    title_page = None
    category_selected = None
    extra_context = {}
    paginate_by = 5

    def __init__(self) -> None:
        if self.title_page:
            self.extra_context['title'] = self.title_page
        if self.category_selected is not None:
            self.extra_context['category_selected'] = self.category_selected
        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['category_selected'] = None
        context.update(kwargs)
        return context
