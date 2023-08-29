from pyshacl import validate

shapes_file_format = 'turtle'
shapes_file_name = 'spotter_buoy.schema.ttl'
with open(shapes_file_name, encoding="utf-8") as f:
    shapes_spotter_buoy = f.read()

data_file_format = 'json-ld'
data_file_name = 'spotter_buoy.schema.json'
with open(data_file_name, encoding="utf-8") as f:
    data_spotter_buoy = f.read()

conforms, v_graph, v_text = validate(data_spotter_buoy, 
                                     shacl_graph=shapes_spotter_buoy,
                                     data_graph_format=data_file_format,
                                     shacl_graph_format=shapes_file_format,
                                     inference='rdfs', 
                                     debug=True,
                                     serialize_report_graph=True)
print(conforms)
print('-------')
print(v_graph.decode('utf-8'))
print('-------')
print(v_text)
