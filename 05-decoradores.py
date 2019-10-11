def protected (func):
    def wrapper(password):
        if password == 'Contraseña':
            return func()
        else:
            print('La contraseña es incorrecta.')

    return wrapper

@protected
def protected_func():
    print('La contraseña es correcta.')




if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))
    protected_func(password)
    #plugin_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    #rint(plugin_path)