another_string = "testing"

my_variable = '''
    <html>
        <head>
            <title>Look at this now</title>
        </head>
        <body>
        ''' + another_string + '''
            <h1>Hello World</h1>
        </body>
        </html>
'''

my_html_file = open("C:/Users/bl11749/Documents/My Projects/my_html_file2.html","w")

my_html_file.write(my_variable)

my_html_file.close()

animal = "cat"
print("%s ran over the hill" % animal)
