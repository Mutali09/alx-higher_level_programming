#include <python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	int length = pyList_size(p);
	int q;
	pyListobject *obj = (pListobject *)p;

	printf("[*] Size of python List = %li\n", size);
	printf("[*] Allocated = %lin\n". obj->allocated);
	for (q = 0; q < size; q++)
		printf("Element %q: %s\n", q, py_TYPE(obj->ob_item[q])->typ_name);
}
