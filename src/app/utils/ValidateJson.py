import json

from schema import Schema, And, Use, Optional
import schema

def validate_preferences(perferences):
    """Validates dictionary Schema for preferences 
    Keyword arguments:
    prefernces -- dictionary (dict) of preferences loaded from .rsgs file 
    Returns : 
    bool -> True if the dictionary has all the necessary fields else False 

    """
    perferences_schema = Schema(
        {
            "type_of_flight": str,
            "receiver_port": str,
            "radiosonde_port": str,
            "export_path": str,
            "frequency": str,
        }
    )
    try:
        perferences_schema.validate(perferences)
    except schema.SchemaMissingKeyError as err:
        print(err)
        print("Input Json (preferences.json) schema is invalid")
        return False
    except Exception as e:
        print(e)
        return False 
    return perferences

def validate_surface_values(surface_values):
    """Validates dictionary Schema for suface_values  
    Keyword arguments:
    surface_values -- dictionary (dict) of surface_values loaded from preferences.json
    Returns : 
    bool -> True if the dictionary has all the necessary fields else False 

    """
    surface_values_schema = Schema({
        "data" : {
                "frequency": float, 
                "temperature": float, 
                "pressure": float, 
                "altitude": float, 
                "latitude": float, 
                "longitude":float, 
                "windspeed": float, 
                "humidity": float,
        },
        "time" : str 
    })

    try:
        surface_values_schema.validate(surface_values)
    except schema.SchemaMissingKeyError as err:
        print(err)
        print("Input Json expors params (params.json) schema is invalid")
        return False 
    return True 