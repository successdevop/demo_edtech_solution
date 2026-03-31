def greet_pythons(items: list) -> None:
    greeting = "Hello"
    print(f"The ID of 'greeting' in 'greet_pythons' is {id(greeting)}")
    print(locals())
    print()

    def make_greetings(item: str) -> str:
        greeting = "Hi"
        print(f"The ID of 'greeting' in 'make_greetings' is {id(greeting)}")
        print(locals())
        return f"Hello {item}"

    for item in items:
        print(make_greetings(item))
        print()
    print(f"Inside greet_pythons, 'greeting' is {greeting}")
    print(f"The ID of 'greeting' in 'greet_pythons' is {id(greeting)}")


name = ["John", "Eric", "Graham", "Terry", "Terry", "Michael"]

greet_pythons(name)
