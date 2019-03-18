from functools import update_wrapper


# Django REST framework
@classmethod
def as_view(cls, **initkwargs):
    if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
        def force_evaluation():
            raise RuntimeError(
                'Do not evaluate the `.queryset` attribute directly, '
                'as the result will be cached and reused between requests. '
                'Use `.all()` or call `.get_queryset()` instead.'
            )

        cls.queryset._fetch_all = force_evaluation

    view = super(APIView, cls).as_view(**initkwargs)
    view.cls = cls
    view.initkwargs = initkwargs

    # Note: session based authentication is explicitly CSRF validated,
    # all other authentication is CSRF exempt.
    return csrf_exempt(view)


# Django
@classonlymethod
def as_view(cls, **initkwargs):
    for key in initkwargs:
        if key in cls.http_method_names:
            raise TypeError("You tried to pass in the %s method name as a "
                            "keyword argument to %s(). Don't do that."
                            % (key, cls.__name__))
        if not hasattr(cls, key):
            raise TypeError("%s() received an invalid keyword %r. as_view "
                            "only accepts arguments that are already "
                            "attributes of the class." % (cls.__name__, key))

    def view(request, *args, **kwargs):
        self = cls(**initkwargs)
        if hasattr(self, 'get') and not hasattr(self, 'head'):
            self.head = self.get
        self.request = request
        self.args = args
        self.kwargs = kwargs
        return self.dispatch(request, *args, **kwargs)

    view.view_class = cls
    view.view_initkwargs = initkwargs

    # take name and docstring from class
    update_wrapper(view, cls, updated=())

    # and possible attributes set by decorators
    # like csrf_exempt from dispatch
    update_wrapper(view, cls.dispatch, assigned=())
    return view


"""
所以这里的update_wrapper并不是实现功能所必须的，而是为了兼容。
django中的一些方法实现中通过内省动态的的处理。而通过decorator/partial对原函数进行处理会覆盖wrapped函数的内省状态。

django应该有一些地方对as_view，和dispatch的内省信有依赖。在django rest framework中会override 或者 overwrite， as_view和dispatch方法

view = super(APIView, cls).as_view(**initkwargs)
继续使用父类的构造方法
    # take name and docstring from class
    update_wrapper(view, cls, updated=())

    # and possible attributes set by decorators
    # like csrf_exempt from dispatch
    update_wrapper(view, cls.dispatch, assigned=())
在子类中重写了父类的方法，却使用父类的函数签名。
"""
