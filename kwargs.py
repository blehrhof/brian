def my_keyword_argument_function(**kwargs):
    if kwargs["name"] == "dave":
        kwargs["name"] = "fred"

    print(kwargs)


my_keyword_argument_function(name="dave", size="large")