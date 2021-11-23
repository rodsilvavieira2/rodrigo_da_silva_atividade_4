def parse_null_values(args) -> str:
    di_args = dict(args)

    values = {
        k: v for k,
        v in di_args.items() if v is not None
    }

    str_data = ''

    for k, v in values.items():
        str_data += f"{k} = '{v}', "

    return str_data.rstrip(", ")


def parse_args_to_tuple(args: dict, seq: list) -> tuple:
    result = [args[v] for v in seq]

    return tuple(result)
