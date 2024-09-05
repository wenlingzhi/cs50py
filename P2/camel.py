user_input = input("camelCase: ")
output = []
for char in user_input:
    if(char.isupper()):
        output.append("_")
        output.append(char.lower())
    else:
        output.append(char)
snake_case_output = "".join(output)
print(f"snake_case: {snake_case_output}")

'''
user = input("camelCase: ")
output = ""
for i in user:
    if (i.isupper()):
        i = i.replace(i,f"_{i.lower()}")
    output += i
print(f"snake_case: {output}")

改进：
变量名和格式化输出：变量名可以更具描述性，使代码更易读。
另外，在格式化输出时，可以在字符串中直接使用变量名，而不是通过逗号分隔的方式。

处理首字母大写的情况：你的代码对于首字母大写的情况并没有单独处理，
这会导致输出不符合标准的蛇形命名。例如，"camelCase" 输入为 "CamelCase" 时，
输出应为 "snake_case: _camel_case" 而非 "snake_case: Camel_Case"。

使用 join 函数：在构建输出字符串时，可以考虑使用列表和 join 函数，而不是直接用 += 操作符，这样会更高效。
'''

