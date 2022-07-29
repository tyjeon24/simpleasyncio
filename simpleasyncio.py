import asyncio

loop = asyncio.get_event_loop()
async def async_call(function, *args):
    kwargs = {}
    args_without_kwargs = []
    for arg in args:
        if type(arg) is dict:
            kwargs = dict(kwargs, **arg)
        else:
            args_without_kwargs.append(arg)

    returned_values = await loop.run_in_executor(None, lambda: function(*args_without_kwargs, **kwargs))
    return returned_values

def call(function, parameters):
    parameters = [param if type(param) == list else [param] for param in parameters]

    futures = [async_call(function, *param) for param in parameters]
    results = loop.run_until_complete(asyncio.gather(*futures))
    loop.close
    return results