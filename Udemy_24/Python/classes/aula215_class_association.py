class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool
    

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WritingTool:
    def __init__(self, tool_name):
        self.tool_name = tool_name

    def write(self):
        return f' is writing with {self.tool_name}'


writer = Writer('Ludwig')
blue_pen = WritingTool('blue pen')
type_machine = WritingTool('type machine')

print(blue_pen.write())
print(writer.name, blue_pen.write())
