import warnings
# print(f"NAmeError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#
# try:
#     try:
#        print('start')
#        print(10/0)
#        print('No errors')
#     except SyntaxError:
#        print("Wrong Errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)

# except NameError:
#     print("We have an error")
# except ZeroDivisionError:
#     print("We have an ZeroDivisionError")
#
#
# try:
#     print('start')
#
# except NameError as error:
#     print(error)
# else:
#     print('no problems')
#
# finally:
#     print('Finally code')
# print("Next Code")

# def checker(a):
#     if type(a) != str:
#         raise TypeError(f"Sorry, we can't work with {type(a)}," f"we need class str")
#     else:
#         return a
#
#
# var = 10
# checker(var)


#
# class BuildingError(Exception):
#
#     def __str__(self):
#         return  F"With so much material the house cannot be built"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material >= limit_value:
#         return 'enough material'
#     else:
#         raise BuildingError(amount_of_material)
#
#
# materials = 1320
# print(check_material(materials, 300))



# warnings.simplefilter('ignore',SyntaxWarning)
# warnings.simplefilter('error',ImportWarning)
#
#
# warnings.warn('Warning, no ccode here', SyntaxWarning)
# try:
#    warnings.warn('Warning, module not import, SyntaxWarning)
# except:
#     print("warning processed")






