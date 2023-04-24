```mermaid
classDiagram
    devices_db -- database_connection
    device_repository --> database_connection
    index <-- initialize_database
    initialize_database <-- "1" devices_db
    index <-- ui
    main_window <-- new_device
    main_window <-- edit_device
    main_window --> ui
    main_window <-- add_project_device
    device_repository --> new_device
    device_repository --> edit_device
    device_repository --> add_project_device
