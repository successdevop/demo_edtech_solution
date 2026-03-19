def banner(text: str = " ", screen_width: int = 80) -> None:
    if len(text) > screen_width - 4:
        print("EEKS!!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED SCREEN WIDTH")

    if text == "*":
        print(text * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner(text="*")
banner("the fox jumps over the lazy dog hello everyone")
banner()
banner("Your idea is the basis for your future business.")
banner("A business plan template can be useful")
banner("Be realistic and honest.")
banner("*")