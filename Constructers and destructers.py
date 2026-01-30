class Employee:

      #initializing (constructor)
      def __init__(self) :
            print('Employee Created. ')

       # deleting (destructor)
      def __del__(self):
            print('Destructor called, Employee')

obj = Employee()
del obj               