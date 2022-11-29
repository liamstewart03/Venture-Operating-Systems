class Car:
    def __init__(self, subclass, model, base_price):
        self.subclass = subclass
        self.model = model
        self.price = base_price

    def __str__(self):
        return f"""
        Subclass: {self.subclass}
        Model: {self.model}
        Price: {self.price}
        """


# GLA_SUV = Car("SUV", "GLA SUV", 37500)
# GLB_SUV = Car("SUV", "GLB SUV", 38600)
# GLC_SUV = Car("SUV", "GLC SUV", 43850)
# GLC_COUPE = Car("SUV", "GLC Coupe", 52500)
# GLE_SUV = Car("SUV", "GLE SUV", 56150)
# GLE_COUPE = Car("SUV", "GLE COUPE", 78450)
# GLS_SUV = Car("SUV", "GLS SUV", 77850)
# G_CLASS_SUV = Car("SUV", "G-CLASS SUV", 139900)
# MERCEDES_MAYBACH_GLS_SUV = Car("SUV", "Mercedes-Maybach GLS SUV", 165100)
# SUVs = [GLA_SUV, GLB_SUV, GLC_SUV, GLC_COUPE, GLE_SUV,
#         GLE_COUPE, GLS_SUV, G_CLASS_SUV, MERCEDES_MAYBACH_GLS_SUV]


# A_CLASS_SEDAN = Car("Sedan", "A-Class Sedan", 33950)
# C_CLASS_SEDAN = Car("Sedan", "C-Class Sedan", 43550)
# E_CLASS_SEDAN = Car("Sedan", "E-Class Sedan", 54950)
# S_CLASS_SEDAN = Car("Sedan", "S-Class Sedan", 111100)
# MERCEDES_MAYBACH_S_CLASS = Car("Sedan", "Mercedes-Maybach S-Class", 184900)
# E_CLASS_WAGON = Car("Wagon", "E-Class Wagon", 68400)
# self.Sedans_Wagons = [A_CLASS_SEDAN, C_CLASS_SEDAN, E_CLASS_SEDAN,
#                  S_CLASS_SEDAN, MERCEDES_MAYBACH_S_CLASS, E_CLASS_WAGON]


# CLA_COUPE = Car("Coupe", "CLA Coupe", 39350)
# C_CLASS_COUPE = Car("Coupe", "C-Class Coupe", 47850)
# E_CLASS_COUPE = Car("Coupe", "E-Class Coupe", 66100)
# CLS_COUPE = Car("Coupe", "CLS Coupe", 72950)
# MERCEDES_AMG_GT_4_DOOR_COUPE = Car("Coupe", "Mercedes-AMG GT 4-door Coupe", 92500)
# MERCEDES_AMG_GT = Car("Coupe", "Mercedes-AMG GT", 118600)
# Coupes = [CLA_COUPE, C_CLASS_COUPE, E_CLASS_COUPE,
#           CLS_COUPE, MERCEDES_AMG_GT_4_DOOR_COUPE, MERCEDES_AMG_GT]


# C_CLASS_CABRIOLET = Car("Convertible", "C-Class Cabriolet", 55400)
# E_CLASS_CABRIOLET = Car("Convertible", "E-Class Cabriolet", 73250)
# SL_ROADSTER = Car("Roadster", "SL Roadster", 137400)
# Convertibles_Roadsters = [C_CLASS_CABRIOLET, E_CLASS_CABRIOLET, SL_ROADSTER]


# EQB_SUV = Car("Electric", "EQB SUV", 54500)
# EQS_SEDAN = Car("Electric", "EQS Sedan", 102310)
# EQS_SUV = Car("Electric", "EQS SUV", 104400)
# Electric = [EQB_SUV, EQS_SEDAN, EQS_SUV]
