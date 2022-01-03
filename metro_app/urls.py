from django.urls import path
from .views import (create_project, delete_nodes, delete_roads_types,
                    create_network, create_roadtype,
                    project_details, update_network, update_project,
                    delete_project, network_details, index,
                    delete_network, visualization, edges_point_geojson,
                    edges_table, nodes_table, road_type_table,
                    create_zoneset, zoneset_details, update_zoneset,
                    delete_zoneset, zones_table,
                    create_od_matrix, od_matrix_details, update_od_matrix,
                    delete_od_matrix, od_pair_table,
                    fetch_task,
                    )

from .networks import (upload_edge, upload_node, upload_road_type, upload_zone,
                       upoload_od_pair,)
from .metrosim import upload_edges_results

urlpatterns = [
    path('', index, name='home'),
    path('network/<str:pk>/delete/nodes', delete_nodes, name='delete_nodes'),
    path('network/<str:pk>/delete/road_types', delete_roads_types,
         name='delete_roads_types'),
    path('project/', create_project, name='create_project'),
    path('project/<str:pk>/', project_details, name='project_details'),
    path('update_project/<str:pk>/', update_project, name='update_project'),
    path('delete_project/<str:pk>/', delete_project, name='delete_project'),
    path('network/project/<str:pk>/', create_network, name='create_network'),
    path('update_network/<str:pk>/', update_network, name='update_network'),
    path('delete_network/<str:pk>/', delete_network, name='delete_network'),
    path('network/<str:pk>/roadtype/', create_roadtype, name='roadtype'),
    path('network/<str:pk>/details/', network_details, name='network_details'),
    path('network/<str:pk>/upload_node/', upload_node, name='upload_node'),
    path('network/<str:pk>/upload_edge/', upload_edge, name='upload_edge'),
    path('visualization/network/<str:pk>/', visualization,
         name='network_visualization'),
    path('network/<str:pk>/upload_road/', upload_road_type, name='upload_road'
         ),
    path('network/<str:pk>/edges.geojson/', edges_point_geojson),
    path('metrosim/run/<str:pk>/upload_edges_results/', upload_edges_results),
    path('table/network/<str:pk>/edges/', edges_table, name='edges'),
    path('table/network/<str:pk>/nodes/', nodes_table, name='nodes'),
    path('table/network/<str:pk>/roadtype/', road_type_table,
         name='roadtable'),
    path('zoneset/project/<str:pk>/', create_zoneset, name='create_zoneset'),
    path('zoneset/<str:pk>/details/', zoneset_details, name='zoneset_details'),
    path('update_zoneset/<str:pk>/', update_zoneset, name='update_zoneset'),
    path('delete_zoneset/<str:pk>/', delete_zoneset, name='delete_zoneset'),
    path('zone/<str:pk>/upload_zone/', upload_zone, name='upload_zone'),
    path('table/zoneset/<str:pk>/zones/', zones_table, name='zones'),
    path('odmatrix/project/<str:pk>/', create_od_matrix,
         name='create_od_matrix'),
    path('odmatrix/<str:pk>/details/', od_matrix_details,
         name='od_matrix_details'),
    path('update_odmatrix/<str:pk>/', update_od_matrix,
         name='update_od_matrix'),
    path('delete_od_matrix/<str:pk>/', delete_od_matrix,
         name='delete_od_matrix'),
    path('odpair/<str:pk>/upoload_od_pair/', upoload_od_pair,
         name='upoload_od_pair'),
    path('table/odmatrix/<str:pk>/odpair/', od_pair_table,
         name='od_pair'),
    path('task/<uuid:task_id>/', fetch_task, name='fetch_task'),
]
