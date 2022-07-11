import printing_functions_15 as print_func


def main():
    unprinted_designs = ['iphone', 'xbox', 'ps5']
    completed_models = []

    print_func.print_models(unprinted_designs, completed_models)
    print_func.show_completed_models(completed_models)


if __name__ == "__main__":
    main()
