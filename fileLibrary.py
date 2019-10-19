from configparser import ConfigParser


class nueces_data():

    props = ConfigParser()
    config = None
    clasificacion = None
    subClasificacion = None

    debug = None

    def __init__(self):
        self.props.read('Database.properties')
        self.config = self.props['CONFIGURACION']
        self.clasificacion = self.props['CLASIFICACION']
        self.subClasificacion = self.props['SUBCLASIFICACION']
        self.debug = self.props['DEBUG']

    def get_config_value(self):
        return self.config['Umbral']

    def get_clasif_buenas_value(self):
        return self.clasificacion['Nueces_Buenas']

    def get_clasif_malas_value(self):
        return self.clasificacion['Nueces_Malas']

    def get_subclasif_buenas_chicas_value(self):
        return self.subClasificacion['Nueces_Buenas_Chicas']

    def get_subclasif_buenas_grandes_value(self):
        return self.subClasificacion['Nueces_Buenas_Grandes']

    def set_config_value(self, value):
        self.props.set('CONFIGURACION', 'Umbral', str(value))
        self.write_property_file()

    def set_clasif_buenas_value(self, value):
        self.props.set('CLASIFICACION', 'Nueces_Buenas', str(value))
        self.write_property_file()

    def set_clasif_malas_value(self, value):
        self.props.set('CLASIFICACION', 'Nueces_Malas', str(value))
        self.write_property_file()

    def set_subclasif_buenas_chicas_value(self, value):
        self.props.set('SUBCLASIFICACION', 'Nueces_Buenas_Chicas', str(value))
        self.write_property_file()

    def set_subclasif_buenas_grandes_value(self, value):
        self.props.set('SUBCLASIFICACION', 'Nueces_Buenas_Grandes', str(value))
        self.write_property_file()

    """"Debug"""
    def get_diametro_actual(self):
        return self.debug['Diametro_Actual']

    def set_diametro_actual(self, value):
        self.props.set('DEBUG', 'Diametro_Actual', str(value))
        self.write_property_file()

    """General"""
    def write_property_file(self):
        with open('Database.properties', 'w') as configfile:
            self.props.write(configfile)

        #self.props.write('Database.properties')

    def read_values(self):
        self.props.read('Database.properties')

