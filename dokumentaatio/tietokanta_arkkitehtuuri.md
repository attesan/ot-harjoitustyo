```mermaid
classDiagram
    Devices <-- DevicePoints: Devices.id = DevicePoints.device_id
    Devices <-- DeviceData: Devices.id = DeviceData.device_id
    
class Devices{
    id, integer
    model, text
    manufacturer, text
}

class DevicePoints{
    id, integer
    device_id, integer
    point_name, text
    point_type, text
}

class DeviceData{
    id, integer
    device_id, integer
    data_value, real
    data_information, text
}
