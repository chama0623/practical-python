import types
from functools import wraps


def my_class_decorator(klass):
    klass.extra_param = "hello"
    return klass


# クラスデコレータ
@my_class_decorator
class MyClass:
    pass


def trace_func(func):
    if hasattr(func, "tracing"):
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            result = e
            raise
        finally:
            print(f"{func.__name__}({args!r}, {kwargs!r}) -> " f"{result!r}")

    wrapper.tracing = True
    return wrapper


trace_types = (
    types.MethodType,
    types.FunctionType,
    types.BuiltinFunctionType,
    types.BuiltinMethodType,
    types.MethodDescriptorType,
    types.ClassMethodDescriptorType,
)


def trace(klass):
    for key in dir(klass):
        value = getattr(klass, key)
        if isinstance(value, trace_types):
            wrapped = trace_func(value)
            setattr(klass, key, wrapped)
    return klass


@trace
class TraceDict(dict):
    pass


if __name__ == "__main__":
    print(MyClass)
    print(MyClass.extra_param)

    # クラスに含まれる全てのメソッドについて, 引数, 戻り値, 発声した例外をヘルパーする
    trace_dict = TraceDict([("hi", 1)])
    trace_dict["there"] = 2
    trace_dict["hi"]
    try:
        trace_dict["does not exist"]
    except KeyError:
        pass
