


pybind11_add_module(pcl_python cserv_pybind.cpp)
set_target_properties(pcl_python
        PROPERTIES PREFIX ""
               SUFFIX ".so"
        )
target_link_libraries(pcl_python PRIVATE cserv_core )

