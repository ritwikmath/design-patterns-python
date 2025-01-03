class Application:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


app1 = Application()
app1.data = True
app2 = Application()
print(app2.data)
