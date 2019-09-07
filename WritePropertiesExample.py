import fileLibrary

test = fileLibrary.nueces_data()

print(test.get_config_value())
print(test.get_clasif_buenas_value())
print(test.get_clasif_malas_value())
print(test.get_subclasif_buenas_chicas_value())
print(test.get_subclasif_buenas_grandes_value())


test.set_config_value(1)
test.set_clasif_buenas_value(2)
test.set_clasif_malas_value(3)
test.set_subclasif_buenas_chicas_value(4)
test.set_subclasif_buenas_grandes_value(5)


print(test.get_config_value())
print(test.get_clasif_buenas_value())
print(test.get_clasif_malas_value())
print(test.get_subclasif_buenas_chicas_value())
print(test.get_subclasif_buenas_grandes_value())
